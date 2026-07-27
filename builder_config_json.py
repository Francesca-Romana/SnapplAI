import os
import json
from dotenv import load_dotenv

# --- Load personal config ---
load_dotenv("personal_data/file_config.env")


def _list(key):
    val = os.getenv(key, "")
    return [v.strip() for v in val.split(",") if v.strip()]

def _int(key):
    val = os.getenv(key)
    return int(val) if val else None

def _bool(key):
    val = os.getenv(key, "")
    return val.lower() == "true" if val else False


# --- Build JSON ---
config = {
    "apify": {
        "max_items": _int("APIFY_MAX_ITEMS") or 15,
        "scrape_company": _bool("APIFY_SCRAPE_COMPANY")
    },
    "job_queries": _list("JOB_QUERIES"),
    "filters": {
        "title": {
            "include": _list("FILTER_TITLE_INCLUDE"),
            "exclude": _list("FILTER_TITLE_EXCLUDE")
        },
        "location": {
            "include": _list("FILTER_LOCATION_INCLUDE"),
            "exclude": _list("FILTER_LOCATION_EXCLUDE")
        },
        "seniority_level": {
            "include": _list("FILTER_SENIORITY_INCLUDE"),
            "exclude": _list("FILTER_SENIORITY_EXCLUDE")
        },
        "employment_type": {
            "include": _list("FILTER_EMPLOYMENT_TYPE_INCLUDE"),
            "exclude": _list("FILTER_EMPLOYMENT_TYPE_EXCLUDE")
        },
        "salary": {
            "min": _int("FILTER_SALARY_MIN"),
            "currency": os.getenv("FILTER_SALARY_CURRENCY", "EUR")
        },
        "company": {
            "exclude_names": _list("FILTER_COMPANY_EXCLUDE_NAMES"),
            "min_employees": _int("FILTER_COMPANY_MIN_EMPLOYEES"),
            "max_employees": _int("FILTER_COMPANY_MAX_EMPLOYEES")
        },
        "experience": {
            "max_years_required": _int("FILTER_MAX_YEARS_REQUIRED") or 5
        },
        "applicants": {
            "max_count": _int("FILTER_MAX_APPLICANTS")
        },
        "posted_within_hours": _int("FILTER_POSTED_WITHIN_HOURS") or 3
    },
    "scoring": {
        "keywords": _list("SCORING_KEYWORDS"),
        "keyword_boost": _int("SCORING_KEYWORD_BOOST") or 10,
        "fresh_grad_boost": _int("SCORING_FRESH_GRAD_BOOST") or 5,
        "top_results": _int("SCORING_TOP_RESULTS") or 5
    },
    "email": {
        "subject_prefix": os.getenv("EMAIL_SUBJECT_PREFIX", "[Job Alert]")
    },
    "resume_path": os.getenv("RESUME_PATH", "resume.pdf")
}

# --- Write JSON ---
with open("filter_config.json", "w") as f:
    json.dump(config, f, indent=2)

print("filter_config.json generated")
