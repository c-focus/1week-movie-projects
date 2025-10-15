# 🎬 1-Week Movie Data Projects

A comprehensive 1-week project demonstrating professional software development practices with two movie-related applications: an IMDb web scraper and a speech-to-text cleanup AI.

## 📋 Project Overview

This repository contains two interconnected projects built during a 1-week development sprint:

### 🎯 **IMDb Movie Scraper**
A robust web scraper that searches IMDb and extracts detailed movie information with anti-bot protection and professional error handling.

**Features:**
- 🔍 Movie search by title
- 📊 Comprehensive data extraction (ratings, cast, plot, etc.)
- 🛡️ Anti-bot protection with rate limiting
- 🎨 Web interface (Streamlit) and CLI
- 🔄 Error handling and retry logic
- 🧪 Test mode with fake data for development
- 📈 Search history and caching

### 🎤 **Speech Cleanup AI** (Coming Soon)
AI-powered text cleanup for speech-to-text transcripts with grammar correction and tone adjustment.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- GitHub CLI (optional, for development workflow)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/c-focus/1week-movie-projects.git
cd 1week-movie-projects
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

### Usage

**Web Interface:**
```bash
python3 -m streamlit run run_app.py
```
Open http://localhost:8501 in your browser

**Test Mode:**
Enable test mode in the sidebar for development with fake movie data.

**Command Line:**
```bash
# Search for a movie
python3 -m imdb_scraper.cli "The Shawshank Redemption"

# JSON output
python3 -m imdb_scraper.cli "Inception" --json

# Search only (show results without details)
python3 -m imdb_scraper.cli "The Matrix" --search-only
```

## 🏗️ Project Structure

```
1week-movie-projects/
├── imdb_scraper/              # IMDb scraper package
│   ├── __init__.py           # Package initialization
│   ├── scraper.py            # Core scraping engine
│   ├── models.py             # Data models & validation
│   ├── config.py             # Configuration & selectors
│   ├── cli.py                # Command-line interface
│   ├── app.py                # Streamlit web interface
│   └── README.md             # Scraper documentation
├── speech_cleanup_ai/        # Speech cleanup AI (future)
├── docs/                     # Additional documentation
├── tests/                    # Test suite
├── run_app.py               # Streamlit launcher
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container configuration
├── AGENTS.md                # Agent development guidelines
└── README.md                # This file
```

## 🛡️ Anti-Bot Protection

The IMDb scraper includes comprehensive anti-bot measures:

- **Browser-like headers** with realistic User-Agent strings
- **Rate limiting** with configurable delays between requests
- **Session management** for connection reuse
- **Exponential backoff** retry logic
- **Request timeouts** to prevent hanging
- **Graceful error handling** with partial data recovery

## 🔧 Development

### Code Quality
```bash
# Linting
ruff check .
ruff check --fix .

# Type checking
mypy .

# Testing (future)
pytest
```

### Git Workflow

**Branching Strategy:**
- `main` - Production-ready code
- `dev` - Development integration branch
- `feature/*` - Feature branches
- `fix/*` - Bug fix branches

**Commit Convention:**
```
feat: add new feature
fix: bug fix
docs: documentation
style: formatting
refactor: code restructuring
test: testing
chore: maintenance
```

### Docker Support

Build and run with Docker:
```bash
docker build -t movie-projects .
docker run -p 8501:8501 movie-projects
```
The app will be accessible at http://localhost:8501

## 📊 Current Status

### ✅ **Completed**
- IMDb scraper with full functionality
- Anti-bot protection and rate limiting
- Web and CLI interfaces
- Professional code structure and documentation
- GitHub repository with proper branching
- UI improvements (test mode, search history, enhanced UX)
- Docker containerization

### 🔄 **In Progress**
- Enhanced search features
- Better error handling display

### 🚀 **Planned**
- Speech Cleanup AI implementation
- Advanced search filters
- Batch processing capabilities
- API endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Issues

Current UI improvement issues:
- [#1](https://github.com/c-focus/1week-movie-projects/issues/1) - Enter key should trigger movie search
- [#2](https://github.com/c-focus/1week-movie-projects/issues/2) - Display multiple search results with matching info
- [#3](https://github.com/c-focus/1week-movie-projects/issues/3) - Add rate limiting status indicators

## 📄 License

This project is for educational purposes. Please respect IMDb's Terms of Service and use responsibly.

## 🙏 Acknowledgments

- IMDb for providing movie data
- BeautifulSoup4, requests, and other open-source libraries
- Streamlit for the web interface framework

---

**Built during a 1-week professional development sprint** 🚀