# LinkedIn Job Alerts
 
A modular job alert pipeline that scrapes LinkedIn postings every 30 minutes, scores them against your profile, and emails you the best matches with a direct apply link — so you're always among the first to know.
 
## About this fork
 
This project is a fork of [danyijia/LinkedIn-Job-Scrape](https://github.com/danyijia/LinkedIn-Job-Scrape), rebuilt with a modular architecture and a faster check cycle.
 
**What changed from the original:**
 
- Refactored from 2 scripts into a 3-module pipeline: `scraper.py` → `matcher.py` → `sender.py`
- Check frequency raised from once daily to every 30 minutes via GitHub Actions
- Duplicate detection to avoid re-sending jobs already notified
## Features
 
- **Smart Filtering**: Automatically removes jobs requiring more years of experience than your threshold (customizable).
- **Keyword Scoring**: Boosts jobs that match your skills (Python, SQL, etc.) and prioritizes relevant roles.
- **Context Aware**: Distinguishes between "2 years experience" (filtered out) vs "within 2 years" (kept).
- **30-Minute Alerts**: Runs every 30 minutes on GitHub Actions — you get an email as soon as a new matching job appears.
- **No Duplicates**: Tracks already-notified jobs so you only receive new ones.
  
## Architecture
 
```
scraper.py      Fetches job postings from LinkedIn via Apify
    ↓
matcher.py      Scores and filters jobs against your resume, keywords and experience level
    ↓
sender.py       Sends an email with the top matches (title, company, details, direct apply link)
```
 
## Apify Setup
 
This project uses **Apify** to scrape data from LinkedIn.
 
1. **Create an Account**: Go to [Apify](https://apify.com/) and sign up.
2. **Get API Token**: Go to Settings > Integrations and copy your Personal API Token.
3. **Choose an Actor**:
   - By default, this project uses the actor **`curious_coder/linkedin-jobs-scraper`**.
   - You need to "Rent" or "Start" this actor in your Apify console at least once to ensure it's active (or just rely on the API call).
   - **Note**: You can swap this for any other LinkedIn scraper actor on Apify. If you do, update the Actor ID in `scraper.py`.
     
## Setup
 
1. **Install Dependencies**
```bash
   pip install -r requirements.txt
```
 
2. **Environment Variables**
   Create a `.env` file in the root directory:
```env
   APIFY_TOKEN=your_apify_token_here
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
```
 
3. **Resume**
   Place your resume PDF in the project folder and update `config.json` with its filename.
## Customization
 
All settings are managed in `config.json`.
 
- **`settings`**:
  - `max_experience_years`: Filter out jobs requiring more than this (e.g., set to 3 to keep 1–3 year roles).
  - `top_results_limit`: How many jobs to include in each email (e.g., 10, 20).
  - `fresh_grad_boost_score`: Bonus points for "fresh grad" / "junior" roles.
  - `resume_path`: Path to your PDF resume.
- **`apify`**:
  - `max_items`: How many jobs to fetch from LinkedIn per run (e.g., 100).
- **`job_queries`**: Add or remove LinkedIn search URLs.
  - **Tip**: In the URL, `f_TPR=r86400` means "Past 24 Hours", `f_TPR=r604800` means "Past Week", `f_TPR=r2592000` means "Past Month".
- **`keywords`**: Add skills you want to match (e.g., "Python", "SQL", "Power BI", "Data Engineer").

## Usage
 
Run the pipeline manually:
 
```bash
python3 scraper.py
```
 
## Cloud Automation (Recommended)
 
To run this without keeping your laptop on, use **GitHub Actions**.
 
1. **Push the code** to your GitHub repository.
2. **Add Secrets**: Go to your Repo **Settings** > **Secrets and variables** > **Actions**.
   - Click **New repository secret** (do NOT use "Variables" or "Environment secrets").
   - Add `APIFY_TOKEN`
   - Add `EMAIL_USER`
   - Add `EMAIL_PASSWORD`
3. **Done!** The workflow (in `.github/workflows/job_alert.yml`) is pre-configured to run **every 30 minutes**. Adjust the cron schedule in the YAML file if you want a different frequency.
   
## Local Automation (Cron)
 
If you prefer to run it on your own computer:
 
1. Run `crontab -e`.
2. Add:
```bash
   */30 * * * * cd "/path/to/project" && /usr/bin/python3 scraper.py >> cron_log.txt 2>&1
```
 
## Planned Improvements
 
- [ ] Replace keyword scoring with AI-powered matching (Ollama / Claude API)
- [ ] Add support for multiple job sources beyond LinkedIn
- [ ] Telegram / webhook notifications as alternative to email
- [ ] Configurable scoring weights per skill category
- [ ] Dashboard to review and track notified jobs
   
## Credits

Original project by [danyijia](https://github.com/danyijia/LinkedIn-Job-Scrape).


 
Original project by [danyijia](https://github.com/danyijia/LinkedIn-Job-Scrape).
 
