import pandas as pd
from groq import Groq
from schedule import jobs
from dotenv import load_dotenv
import os

def agentic_summirize(jobs):
    load_dotenv("your_cv_config/file_config.env")
    
    groq_client = Groq(os.getenv("LLM_KEY"))
    
    for index, row in jobs.iterrows():
        istruzioni = "summarize the job description max 100 words,return only the summary without any other text or explanation"
        messages = [{"role": "system", "content": istruzioni}] + [{"role": "user", "content": f"job description: {row['description']}"}]
        response = groq_client.chat.completions.create(model="llama-3.1-8b-instant", messages=messages, temperature=0)
        result = response.choices[0].message.content
        jobs.at[index, "summary"] = result
    
    return jobs
