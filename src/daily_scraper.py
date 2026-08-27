from jobspy import scrape_jobs
from dotenv import load_dotenv
import os

def job_scraper():
    load_dotenv("your_cv_config/file_config.env")
    jobs = scrape_jobs(
        site_name= os.getenv("site_name"), 
        search_term= os.getenv("search_term"),
        location= os.getenv("location"),
        results_wanted= int(os.getenv("results_wanted")),
        hours_old= int(os.getenv("hours_old")),
        linkedin_fetch_description= os.getenv("linkedin_fetch_description") == "True", 
        proxies= os.getenv("proxies").split(",") if os.getenv("proxies") else None,
    )

    return jobs