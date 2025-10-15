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

## 🔄 Workflow Preferences
- **Parallel Development**: Multiple branches and PRs simultaneously (don't wait for completion)
- **Self-Review Process**: Fast iteration as repository owner with self-review and merge
- **Proactive AI Guidance**: Need suggestions for next steps and workflow optimization
- **Learning-Focused**: Balance building features with understanding tools and processes

---

## 📦 Current Projects
### 1. IMDb Scraper
**Status:** Advanced Development (PR #6 Ready)
**Purpose:** Build a data scraper for IMDb movie information (titles, ratings, years).
**Skills Focus:** Requests, BeautifulSoup, data structuring, Docker containerization, GitHub workflow.

**Current Progress**
- ✅ Core scraper implemented with search and movie detail extraction
- ✅ Streamlit web interface with movie display
- ✅ Test mode with fake movie data
- ✅ Search validation and history tracking
- ✅ GitHub repo setup with professional workflow
- 🔄 PR #6 pending review (UI improvements, test mode, validation)

**Next Steps**
- Review and merge PR #6
- Add Dockerfile for containerized execution
- Set up CI/CD pipeline with GitHub Actions
- Add comprehensive test coverage

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
- **GitHub Repo:** ✅ https://github.com/c-focus/1week-movie-projects
- **Current Branch:** feature/ui-improvements (PR #6)
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
- Add "Updated" date after each edit.

5. **AI Context Maintenance**
- Reference PROJECT_CONTEXT.md for workflow preferences and learning goals
- Update document after major decisions or process changes
- Include current blockers and parallel development streams
- Maintain continuity across sessions to avoid repetition

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
- [ ] Review and merge PR #6 (IMDb scraper UI improvements)
- [ ] Create Dockerfile for IMDb Scraper containerization
- [ ] Set up GitHub Actions CI/CD pipeline
- [ ] Add comprehensive test coverage (pytest)
- [ ] Create issue templates and PR templates
- [ ] Collect sample data for Speech Cleanup AI
- [ ] Create LanguageTool test script
- [ ] Write `docs/daily_log.md` template  

---

## 🧾 Notes
- Focus on **end-to-end workflow**, not feature depth.  
- Prefer small, working deliverables every day.  
- Document each problem and its fix (this is as valuable as code).

---

_Last updated: [Oct 14, 2025] - Updated with current progress, workflow preferences, and AI context guidelines_