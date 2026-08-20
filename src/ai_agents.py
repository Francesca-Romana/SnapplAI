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
        f"Match this job against the candidate CV: {cv}. "
        "Score fit from 1-10 based on skills and experience. "
        "Extract remote/hybrid status from the description. "
        "apply_link must be the original LinkedIn URL (https://www.linkedin.com/jobs/view/...), never modify it. "
        "Respond ONLY with valid JSON, no other text: "
        '{"score": 8, "company": "", "role": "", "summary": "max 75 chars", "is_remote": , "apply_link": "https://www.linkedin.com/jobs/view/..."}'
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



        