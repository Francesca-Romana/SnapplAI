import pandas as pd
from groq import Groq
from schedule import jobs
from dotenv import load_dotenv
import os

def agentic_summarize(jobs):
    load_dotenv("your_cv_config/file_config.env")
    
    groq_client = Groq(os.getenv("LLM_KEY"))
    
    for index, row in jobs.iterrows():
        system_prompt = "summarize the job description max 100 words,return only the summary without any other text or explanation, important include if is remote or hydrid work, and the link for apply"
        messages = [{"role": "system", "content": system_prompt}] + [{"role": "user", "content": f"job description: {row['description']}"}]
        result = response.choices[0].message.content
        jobs.at[index, "summary"] = result
    
    return jobs
