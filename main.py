from jobspy import scrape_jobs
import os
from dotenv import load_dotenv
import pandas as pd
from groq import Groq
import json

import sys
sys.path.append("..")

from src.daily_scraper import job_scraper
from src.ai_agents import agentic_summarize,agentic_analyzent
from src.smtp import send_email
