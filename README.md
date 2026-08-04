
# THE CONCEPT
 
<div align="center">
<img src="https://media.giphy.com/media/qgQUggAC3Pfv687qPC/giphy.gif" width="400" alt="Coding GIF">

 
</div>

**Work in progress: Automated job hunting pipeline — scrape, match, apply. Be first in line.**

# 🔎 LinkedIn AI Job Alerts

 
## 🧠 How It Works
 
```
  .env                filter_config.json           LinkedIn
   │                        │                         │
   ▼                        ▼                         ▼
┌──────────────┐    ┌──────────────┐    ┌───────────────────┐
│ builder_     │───▶│  daily_bot   │───▶│ daily_job_matcher  │───▶ 📧 Email
│ config_json  │    │  (JobSpy)    │    │ (Groq AI + CV)     │
└──────────────┘    └──────────────┘    └───────────────────┘
 
 You set your         Scrapes jobs         AI reads your CV,
 preferences          from LinkedIn        matches it against
                                           each listing, and
                                           emails you the results
 
                      🔁 Every 2-4 hours
```
 
1. **Config** — You fill in a `.env` with your job preferences. `builder_config_json.py` converts it into `filter_config.json`.
2. **Scrape** — `daily_bot.py` uses [JobSpy](https://github.com/Bunsly/JobSpy) to scrape LinkedIn listings based on your filters.
3. **Match** — `daily_job_matcher.py` is an AI agent powered by **Groq**. It reads your CV, synthesizes it, and scores each job against your profile.
4. **Notify** — The agent generates a summary of the best matches and sends it to your inbox, ready to apply.
The whole pipeline runs every 2-4 hours so you're always first in line.
 
---
 
## 🛠️ Built With
 
- [JobSpy](https://github.com/Bunsly/JobSpy) — Job scraping
- [Groq](https://groq.com/) — LLM inference for CV-job matching
- Python
---
 
<div align="center">
*Stop refreshing LinkedIn. Let the bot do it for you.* 🤖
 
</div>
 
