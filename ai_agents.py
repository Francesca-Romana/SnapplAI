import pandas as pd
from groq import Groq
from schedule import jobs
from pypdf import PdfReader
from dotenv import load_dotenv
import os
import json

def agentic_summarize(jobs):
    load_dotenv("your_cv_config/file_config.env")
    
    groq_client = Groq(os.getenv("LLM_KEY"))
    
    for index, row in jobs.iterrows():
        system_prompt = "summarize the job description max 100 words,return only the summary without any other text or explanation, important include if is remote or hydrid work, and the link for apply"
        messages = [{"role": "system", "content": system_prompt}] + [{"role": "user", "content": f"job description: {row['description']}"}]
        response = groq_client.chat.completions.create(model="llama-3.1-8b-instant", messages=messages, temperature=0)
        result = response.choices[0].message.content
        jobs.at[index, "summary"] = result
    
    return jobs

def agentic_analyze(jobs):
    load_dotenv("your_cv_config/file_config.env")
    
    groq_client = Groq(os.getenv("LLM_KEY"))
    reader = PdfReader(os.getenv("dir_cv"))
    cv = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            cv += text
    system_prompt = (
            f"use only english"
            f"you goal is to analyze the row of the job summireze the description and match with the {cv} of the candidate and return the score of fitting and the summireze description and the link for apply"
            f"return the result in json format with the following keys: 'score from 1 to 10','name of campany', 'summary of the description max 50 characters', 'is_remote (take from the job description)', 'apply_link the url'"
            f"return only the json object without any other text or explanation only json object(result should format like this: {{'score': 8, 'name of campany':,'role':, 'company name', 'summary':, 'is_remote':, 'apply_link':'}})'"
        )
    response_list = []

    for index, row in jobs.iterrows():
        messages = [{"role": "system", "content": system_prompt}] + [{"role": "user", "content": f"company name: {row['company']},role: {row['title']}: {row['company']},job description: {row['summary']}, job url: {row['job_url']}"}]
        response = groq_client.chat.completions.create(model="llama-3.1-8b-instant", messages=messages,temperature=0,)
        response_list.append(response)
    
    
    json_jobs= []

    for x in response_list:
        try:
            result = x.choices[0].message.content
            result = result.replace("```json", "").replace("```", "")
            result_json = json.loads(result)
            json_jobs.append(result_json)
        except Exception as e:
            continue
    
    return json_jobs



        