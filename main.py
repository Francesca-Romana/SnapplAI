from jobspy import scrape_jobs
from dotenv import load_dotenv
import os
import pandas as pd
from google import genai
from google.genai import types
import json


import sys
sys.path.append("..")

from src.daily_scraper import job_scraper
from src.ai_agents import agentic_summarize,agentic_analyzent
from src.smtp import send_email
