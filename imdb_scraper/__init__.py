"""IMDb Scraper Package."""

from .scraper import IMDbScraper
from .models import Movie, SearchResult, ScraperError

__version__ = "0.1.0"
__all__ = ["IMDbScraper", "Movie", "SearchResult", "ScraperError"]