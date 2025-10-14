"""Configuration constants for IMDb scraper."""


# Request configuration
REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
}

REQUEST_TIMEOUT = 10  # seconds
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds, will be multiplied by attempt number

# IMDb URLs
IMDB_BASE_URL = "https://www.imdb.com"
IMDB_SEARCH_URL = f"{IMDB_BASE_URL}/find/"
IMDB_TITLE_URL = f"{IMDB_BASE_URL}/title/"

# CSS Selectors for movie details (may need updates if IMDb changes layout)
MOVIE_SELECTORS = {
    "title": "h1[data-testid='hero__pageTitle'] span.hero__primary-text",
    "year": "a[href*='/releaseinfo'] span",
    "rating": "div[data-testid='hero-rating-bar__aggregate-rating'] span",
    "runtime": "li[data-testid='title-techspec_runtime'] div",
    "genres": "div[data-testid='genres'] a span",
    "director": "div[data-testid='title-pc-principal-credit'] li a[href*='/name/']",
    "cast": "div[data-testid='title-cast-item'] a[data-testid='title-cast-item__actor']",
    "plot": "p[data-testid='plot'] span[data-testid='plot-xl']",
}

# Search result selectors
SEARCH_SELECTORS = {
    "results": "section[data-testid='find-results-section'] ul li",
    "title_link": "a[href*='/title/']",
    "title_text": "a[href*='/title/']",
    "year": "span[data-testid='find-result-year']",
}

# Rate limiting
MIN_REQUEST_DELAY = 0.5  # seconds between requests
MAX_REQUEST_DELAY = 2.0  # maximum delay

# Data validation
MAX_TITLE_LENGTH = 200
MAX_PLOT_LENGTH = 1000
VALID_RATING_RANGE = (0.0, 10.0)
VALID_YEAR_RANGE = (1900, 2030)