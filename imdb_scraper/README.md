# IMDb Movie Scraper

A Python application that searches IMDb for movies and extracts detailed information including ratings, cast, director, plot, and more.

## Features

- 🔍 **Movie Search**: Search for movies by title
- 📊 **Detailed Information**: Extract comprehensive movie data
- 🛡️ **Anti-Bot Protection**: Built-in rate limiting and browser-like headers
- 🔄 **Error Handling**: Robust retry logic and graceful failure handling
- 🎨 **Web Interface**: Streamlit-based UI for easy movie searching
- 📋 **CLI Support**: Command-line interface for programmatic use

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Search for a movie:
```bash
python -m imdb_scraper.cli "The Shawshank Redemption"
```

Search only (show results without details):
```bash
python -m imdb_scraper.cli "Inception" --search-only
```

Get JSON output:
```bash
python -m imdb_scraper.cli "Pulp Fiction" --json
```

### Streamlit Web Interface

Run the web app:
```bash
# From the project root directory
python3 -m streamlit run run_app.py
```

Or if streamlit is in your PATH:
```bash
streamlit run run_app.py
```

Then open your browser to the displayed URL (usually http://localhost:8501) and start searching for movies!

## Extracted Movie Information

- Title and release year
- IMDb rating
- Runtime and genres
- Director and main cast
- Plot summary
- IMDb ID and direct link

## Technical Details

- **Web Scraping**: Uses requests + BeautifulSoup with anti-bot measures
- **Data Parsing**: Handles IMDb's modern JSON-based frontend
- **Rate Limiting**: Built-in delays to respect IMDb's servers
- **Error Recovery**: Automatic retries and fallback parsing methods

## Architecture

```
imdb_scraper/
├── scraper.py      # Core scraping logic with anti-bot protection
├── models.py       # Data models and validation
├── config.py       # Configuration and selectors
├── cli.py         # Command-line interface
├── app.py         # Streamlit web interface
└── tests/         # Unit tests (future)
```

## Anti-Bot Protection

The scraper includes several measures to avoid detection:
- Browser-like User-Agent headers
- Rate limiting between requests
- Session management
- Retry logic with exponential backoff
- Graceful handling of CAPTCHAs or blocks

## Development

Run linting:
```bash
ruff check .
ruff check --fix .  # Auto-fix issues
```

Run type checking:
```bash
mypy .
```

## License

This project is for educational purposes. Please respect IMDb's Terms of Service and use responsibly.