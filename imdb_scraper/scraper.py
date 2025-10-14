"""Core IMDb scraper with anti-bot protection and robust error handling."""

import time
import re
import logging
from typing import List, Optional
from urllib.parse import quote, urljoin

import requests
from bs4 import BeautifulSoup

from .config import (
    REQUEST_HEADERS, REQUEST_TIMEOUT, MAX_RETRIES, RETRY_DELAY,
    IMDB_BASE_URL, IMDB_SEARCH_URL, IMDB_TITLE_URL,
    MOVIE_SELECTORS, SEARCH_SELECTORS, MIN_REQUEST_DELAY
)
from .models import Movie, SearchResult
from .history import SearchHistory

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class IMDbScraper:
    """IMDb scraper with anti-bot protection and error handling."""

    def __init__(self):
        """Initialize scraper with session management."""
        self.session = requests.Session()
        self.session.headers.update(REQUEST_HEADERS)
        self.last_request_time = 0
        self.history = SearchHistory()

    def _rate_limit(self):
        """Implement rate limiting between requests."""
        elapsed = time.time() - self.last_request_time
        if elapsed < MIN_REQUEST_DELAY:
            delay = MIN_REQUEST_DELAY - elapsed
            time.sleep(delay)
        self.last_request_time = time.time()

    def _make_request(self, url: str, max_retries: int = MAX_RETRIES) -> Optional[BeautifulSoup]:
        """Make HTTP request with retry logic and error handling."""
        for attempt in range(max_retries):
            try:
                self._rate_limit()
                logger.info(f"Making request to: {url} (attempt {attempt + 1})")

                response = self.session.get(url, timeout=REQUEST_TIMEOUT)
                response.raise_for_status()

                # Check if we got a valid HTML response
                if 'text/html' not in response.headers.get('content-type', ''):
                    logger.warning(f"Non-HTML response from {url}")
                    return None

                return BeautifulSoup(response.content, 'html.parser')

            except requests.exceptions.RequestException as e:
                logger.warning(f"Request failed (attempt {attempt + 1}): {e}")
                if attempt < max_retries - 1:
                    delay = RETRY_DELAY * (attempt + 1)  # Exponential backoff
                    time.sleep(delay)
                else:
                    logger.error(f"Failed to fetch {url} after {max_retries} attempts")
                    return None
            except Exception as e:
                logger.error(f"Unexpected error fetching {url}: {e}")
                return None

        return None

    def _extract_text_safe(self, soup: BeautifulSoup, selector: str) -> Optional[str]:
        """Safely extract text from a CSS selector."""
        try:
            element = soup.select_one(selector)
            return element.get_text(strip=True) if element else None
        except Exception as e:
            logger.warning(f"Failed to extract text with selector '{selector}': {e}")
            return None

    def _extract_multiple_text(self, soup: BeautifulSoup, selector: str, limit: int = 5) -> List[str]:
        """Extract text from multiple elements matching a selector."""
        try:
            elements = soup.select(selector)[:limit]
            return [elem.get_text(strip=True) for elem in elements if elem.get_text(strip=True)]
        except Exception as e:
            logger.warning(f"Failed to extract multiple text with selector '{selector}': {e}")
            return []

    def search_movies(self, query: str, max_results: int = 5) -> List[SearchResult]:
        """Search for movies by title and return search results."""
        if not query or not query.strip():
            return []

        # URL encode the query
        encoded_query = quote(query.strip())
        search_url = f"{IMDB_SEARCH_URL}?q={encoded_query}&s=tt&ttype=ft&ref_=fn_ft"

        soup = self._make_request(search_url)
        if not soup:
            return []

        results = []

        try:
            # IMDb now uses React/JSON embedded in script tags
            # Look for script tags containing JSON data
            script_tags = soup.find_all('script', type='application/json')

            for script in script_tags:
                try:
                    import json
                    script_content = script.string
                    if not script_content:
                        continue
                    data = json.loads(script_content)

                    # Navigate to the title results
                    title_results = data.get('props', {}).get('pageProps', {}).get('titleResults', {}).get('results', [])

                    for item in title_results[:max_results]:
                        title = item.get('titleNameText', '').strip()
                        if not title:
                            continue

                        # Extract year from titleReleaseText
                        year = None
                        release_text = item.get('titleReleaseText', '')
                        if release_text:
                            year_match = re.search(r'\b(19|20)\d{2}\b', release_text)
                            if year_match:
                                year = int(year_match.group())

                        # Build full URL
                        imdb_id = item.get('id', '')
                        url = f"{IMDB_TITLE_URL}{imdb_id}/" if imdb_id else None

                        # Calculate relevance score
                        query_lower = query.lower()
                        title_lower = title.lower()
                        score = 1.0 if query_lower in title_lower else 0.5

                        result = SearchResult(
                            title=title,
                            year=year,
                            imdb_id=imdb_id,
                            url=url,
                            relevance_score=score
                        )
                        results.append(result)

                except (json.JSONDecodeError, KeyError, AttributeError):
                    # Not the right script tag, continue
                    continue

            # Fallback: try to parse traditional HTML if JSON parsing failed
            if not results:
                logger.info("JSON parsing failed, trying HTML fallback")
                result_elements = soup.select(SEARCH_SELECTORS["results"])

                for element in result_elements[:max_results]:
                    try:
                        title_link = element.select_one(SEARCH_SELECTORS["title_link"])
                        if not title_link:
                            continue

                        title = title_link.get_text(strip=True)
                        href = title_link.get('href', '')
                        if isinstance(href, list):
                            href = href[0] if href else ''
                        url = urljoin(IMDB_BASE_URL, href)

                        imdb_id_match = re.search(r'/title/(tt\d+)/', str(url))
                        imdb_id = imdb_id_match.group(1) if imdb_id_match else None

                        year_elem = element.select_one(SEARCH_SELECTORS["year"])
                        year = None
                        if year_elem:
                            year_text = year_elem.get_text(strip=True)
                            year_match = re.search(r'\b(19|20)\d{2}\b', year_text)
                            if year_match:
                                year = int(year_match.group())

                        query_lower = query.lower()
                        title_lower = title.lower()
                        score = 1.0 if query_lower in title_lower else 0.5

                        result = SearchResult(
                            title=title,
                            year=year,
                            imdb_id=imdb_id,
                            url=url,
                            relevance_score=score
                        )
                        results.append(result)

                    except Exception as e:
                        logger.warning(f"Failed to parse search result: {e}")
                        continue

        except Exception as e:
            logger.error(f"Failed to parse search results: {e}")

        # Sort by relevance score
        results.sort(key=lambda x: x.relevance_score, reverse=True)
        return results

    def get_movie_details(self, imdb_id: str) -> Optional[Movie]:
        """Get detailed movie information by IMDb ID."""
        if not imdb_id or not imdb_id.startswith('tt'):
            return None

        movie_url = f"{IMDB_TITLE_URL}{imdb_id}/"
        soup = self._make_request(movie_url)
        if not soup:
            return None

        try:
            # IMDb now uses JSON data embedded in script tags
            script_tags = soup.find_all('script', type='application/json')

            movie_data = None
            for script in script_tags:
                try:
                    import json
                    script_content = script.string
                    if not script_content:
                        continue
                    data = json.loads(script_content)

                    # Extract data from pageProps
                    page_props = data.get('props', {}).get('pageProps', {})
                    if page_props:
                        movie_data = page_props
                        break

                except (json.JSONDecodeError, KeyError, AttributeError):
                    continue

            if not movie_data:
                # Fallback to HTML parsing if JSON fails
                logger.warning(f"JSON parsing failed for {imdb_id}, using HTML fallback")
                return self._get_movie_details_html(soup, imdb_id, movie_url)

            # Extract data from aboveTheFoldData
            above_fold = movie_data.get('aboveTheFoldData', {})

            title = above_fold.get('titleText', {}).get('text', '').strip()
            if not title:
                return None

            # Extract year
            year = above_fold.get('releaseYear', {}).get('year')

            # Extract rating
            rating = above_fold.get('ratingsSummary', {}).get('aggregateRating')

            # Extract runtime
            runtime = None
            runtime_data = above_fold.get('runtime', {})
            if runtime_data:
                display_prop = runtime_data.get('displayableProperty', {}).get('value', {}).get('plainText')
                if display_prop:
                    runtime = display_prop

            # Extract genres
            genres = []
            genres_data = above_fold.get('genres', {}).get('genres', [])
            genres = [genre.get('text', '') for genre in genres_data if genre.get('text')]

            # Extract director - try different sources
            director = None

            # Try mainColumnData crew first
            main_column = movie_data.get('mainColumnData', {})
            crew_data = main_column.get('crewV2', [])
            for crew_item in crew_data:
                grouping = crew_item.get('grouping', {})
                category = grouping.get('text', '')
                if category == 'Director':
                    credits = crew_item.get('credits', [])
                    if credits:
                        director = credits[0].get('name', {}).get('nameText', {}).get('text', '')
                        break

            # Fallback: try principalCredits
            if not director:
                principal_credits = above_fold.get('principalCredits', [])
                for credit in principal_credits:
                    if credit.get('category', {}).get('text') == 'Director':
                        directors = credit.get('credits', [])
                        if directors:
                            director = directors[0].get('name', {}).get('nameText', {}).get('text', '')
                            break

            # Final fallback: directorsPageTitle
            if not director:
                directors_page = above_fold.get('directorsPageTitle', [])
                if directors_page and len(directors_page) > 0:
                    director = directors_page[0].get('name', {}).get('nameText', {}).get('text', '')

            # Extract cast
            cast = []
            cast_data = above_fold.get('castPageTitle', {}).get('edges', [])
            cast = [edge.get('node', {}).get('name', {}).get('nameText', {}).get('text', '')
                   for edge in cast_data[:5] if edge.get('node', {}).get('name')]

            # Extract plot
            plot = None
            plot_data = above_fold.get('plot', {}).get('plotText', {}).get('plainText')
            if plot_data:
                plot = plot_data.strip()

            movie = Movie(
                title=title,
                year=year,
                rating=rating,
                runtime=runtime,
                genres=genres,
                director=director,
                cast=cast,
                plot=plot,
                imdb_id=imdb_id,
                url=movie_url
            )

            return movie

        except Exception as e:
            logger.error(f"Failed to parse movie details for {imdb_id}: {e}")
            return None

    def _get_movie_details_html(self, soup: BeautifulSoup, imdb_id: str, movie_url: str) -> Optional[Movie]:
        """Fallback HTML parsing for movie details."""
        try:
            # Extract basic information using old selectors
            title = self._extract_text_safe(soup, MOVIE_SELECTORS["title"])
            if not title:
                return None

            # Extract year
            year = None
            year_text = self._extract_text_safe(soup, MOVIE_SELECTORS["year"])
            if year_text:
                year_match = re.search(r'\b(19|20)\d{2}\b', year_text)
                if year_match:
                    year = int(year_match.group())

            # Extract rating
            rating = None
            rating_text = self._extract_text_safe(soup, MOVIE_SELECTORS["rating"])
            if rating_text:
                try:
                    rating = float(rating_text.split('/')[0])
                except (ValueError, IndexError):
                    pass

            # Extract other details
            runtime = self._extract_text_safe(soup, MOVIE_SELECTORS["runtime"])
            genres = self._extract_multiple_text(soup, MOVIE_SELECTORS["genres"])
            director = self._extract_text_safe(soup, MOVIE_SELECTORS["director"])
            cast = self._extract_multiple_text(soup, MOVIE_SELECTORS["cast"], limit=5)
            plot = self._extract_text_safe(soup, MOVIE_SELECTORS["plot"])

            movie = Movie(
                title=title,
                year=year,
                rating=rating,
                runtime=runtime,
                genres=genres,
                director=director,
                cast=cast,
                plot=plot,
                imdb_id=imdb_id,
                url=movie_url
            )

            return movie

        except Exception as e:
            logger.error(f"HTML fallback failed for {imdb_id}: {e}")
            return None

    def search_and_get_movie(self, query: str) -> Optional[Movie]:
        """Search for a movie and return the best match with full details."""
        results = self.search_movies(query, max_results=1)
        if not results:
            self.history.record_search(query, success=False)
            return None

        best_result = results[0]
        if not best_result.imdb_id:
            self.history.record_search(query, success=False)
            return None

        movie = self.get_movie_details(best_result.imdb_id)
        self.history.record_search(query, success=movie is not None)
        return movie