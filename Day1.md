# Day 1 – Setup & Planning

## Completed
- Created project structure:
  - `/speech_cleanup_ai`
  - `/imdb_auto_scraper`
- Built a working Docker image using `python:3.11-slim`.
- Installed core libraries:
  - `streamlit`
  - `requests`
  - `beautifulsoup4`
- Verified installation and container operation.

## Notes
- `pyarrow` failed on `python:3.14-slim` but works on `3.11-slim` because 3.14 has no prebuilt wheels yet.
- Docker container runs successfully and mounts local folders correctly.
- `ca-certificates` kept for HTTPS.

## To-Do
- [ ] Define outputs for:
  - `speech_cleanup_ai` (e.g., cleaned text)
  - `imdb_auto_scraper` (e.g., movie list)
- [ ] Create 2–3 sample inputs for each.
- [x] Prepare Day 2 plan (basic Streamlit or scraping setup).

---

**Next step:** Begin Day 2 – Basic app skeletons inside the container.
