from jobspy import scrape_jobs
from dotenv import load_dotenv
import os
import pandas as pd
from google import genai
from google.genai import types
import json
import time
import smtplib
from email.message import EmailMessage
import os
from datetime import date,datetime
from pypdf import PdfReader
import time
from schedule import jobs


import sys
sys.path.append("..")

from src.daily_scraper import job_scraper
from src.ai_agents import agentic_summarize,agentic_analyze
from src.smtp import send_email

def main():
    jobs= job_scraper()

    jobs= agentic_summarize(jobs)

    jobs= agentic_analyze(jobs)

    send_email(jobs)



main()
