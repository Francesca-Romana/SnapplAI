from jobspy import scrape_jobs
from dotenv import load_dotenv
import os

def job_scraper():
    load_dotenv("your_cv_config/file_config.env")
    jobs = scrape_jobs(
        site_name= os.getenv("site_name"), 
        search_term= os.getenv("search_term"),
        google_search_term= os.getenv("google_search_term"),
        location= os.getenv("location"),
        results_wanted= int(os.getenv("results_wanted")),
        hours_old= int(os.getenv("hours_old")),
        linkedin_fetch_description= os.getenv("linkedin_fetch_description") == "True", # gets more info such as description, direct job url (slower)
        proxies= os.getenv("proxies").split(",") if os.getenv("proxies") else None,
    )
    keywords = os.getenv("keyword_filter_remote_job", "").split(",")

    keywords = [kw.strip().lower() for kw in keywords if kw.strip()]

    def find_keyword(text):
        if pd.isna(text):
            return None
        text = text.lower()
        for kw in keywords:
            if kw in text:
                return kw
        return None

    jobs["work_mode"] = jobs["description"].apply(find_keyword)
    if os.getenv("work_from_home") == "True":
        df_filtered = jobs[jobs["work_mode"].notna()]
    else:
        df_filtered = jobs
    return df_filtered