# 🧠 1 Week Project — Shared Context & Coordination Document

## Purpose
This project simulates a **professional developer workflow** under a **1-week deadline**.  
The goal is to **learn core tools** (Docker, GitHub, automation, documentation) and **build working prototypes**.

---

## 🗓️ Project Duration
**Timeline:** 7 days  started on Oct 13, 2025
**Objective:** Complete, test, and document all modules within the week.

---

## 🎯 Learning Goals
- Learn to use **Docker** for reproducible environments.
- Learn **GitHub** for version control, branching, and collaboration workflow.
- Learn to maintain **documentation and issue tracking** like professionals.
- Learn to structure projects for growth and clarity.

---

## 📦 Current Projects
### 1. IMDb Scraper
**Status:** Active  
**Purpose:** Build a data scraper for IMDb movie information (titles, ratings, years).  
**Skills Focus:** Requests, BeautifulSoup, data structuring, Docker containerization, GitHub workflow.

**Next Steps**
- Set up GitHub repo with README, .gitignore, and issue templates.  
- Write scraper base script.  
- Add Dockerfile for containerized execution.  
- Push, commit, and test GitHub workflow.

---

### 2. Speech Cleanup AI
**Status:** Deferred (end of day)  
**Purpose:** Clean text from speech-to-text input (grammar, punctuation, tone).  
**Next Steps**
- Collect raw data samples.  
- Build cleanup pipeline (LanguageTool or Hugging Face).  
- Integrate basic UI or CLI for input/output.

---

## ⚙️ Environment
- **Docker:** Python 3.11-slim (main base)
- **GitHub Repo:** [To be created]
- **Editor:** [to be decided]
- **OS:** macOS
- **Optional Tools:** n8n, Apple Calendar integration (later automation task)

---

## 🧩 Workflow Rules
1. **Branching**
   - `main` = stable release  
   - `dev` = ongoing development  
   - `feature/*` = per-feature branches

2. **Commit Format**
    - feat: add imdb top 250 scraper
    - fix: correct url parser bug
    - docs: update readme with setup instructions
3. **Daily Log Format**
    Add a short section in `/docs/daily_log.md` each day:
        Day 3
	    • Implemented IMDb scraper base
	    • Tested parsing and pagination
	    • Next: containerize and push to GitHub
4. **AI Use**
- Use this document at the start of every chat to sync context.
- Add “Updated” date after each edit.

---

## 📈 Professional Simulation
| Area | Tool | Purpose |
|------|------|----------|
| Codebase | GitHub | Source control |
| Documentation | Markdown files | Team reference |
| Issue Tracking | GitHub Issues | Task management |
| Automation | GitHub Actions | Continuous testing/build |
| Containerization | Docker | Environment isolation |

---

## 🚧 Pending / Open Items
- [ ] Create GitHub repo for IMDb Scraper  
- [ ] Create Dockerfile for IMDb Scraper  
- [ ] Set up basic `README.md`  
- [ ] Collect sample data for Speech Cleanup AI  
- [ ] Create LanguageTool test script  
- [ ] Write `docs/daily_log.md` template  

---

## 🧾 Notes
- Focus on **end-to-end workflow**, not feature depth.  
- Prefer small, working deliverables every day.  
- Document each problem and its fix (this is as valuable as code).

---

_Last updated: [Oct 14, 2025]_