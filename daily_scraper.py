from jobspy import scrape_jobs
from dotenv import load_dotenv
import os

# --- Load personal config ---
load_dotenv("your_cv_config/file_config.env")
jobs = scrape_jobs(
    site_name= os.getenv("site_name"), 
    search_term= os.getenv("search_term"),
    google_search_term= os.getenv("google_search_term"),
    location= os.getenv("location"),
    results_wanted= int(os.getenv("results_wanted")),
    hours_old= int(os.getenv("hours_old")),
    country_indeed= os.getenv("country_indeed"),
    linkedin_fetch_description= os.getenv("linkedin_fetch_description"), # gets more info such as description, direct job url (slower)
    proxies= os.getenv("proxies").split(",") if os.getenv("proxies") else None,
)