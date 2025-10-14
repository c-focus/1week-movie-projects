"""Data models for IMDb scraper."""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from datetime import datetime


@dataclass
class Movie:
    """Movie data model with validation."""
    title: str
    year: Optional[int] = None
    rating: Optional[float] = None
    runtime: Optional[str] = None
    genres: List[str] = field(default_factory=list)
    director: Optional[str] = None
    cast: List[str] = field(default_factory=list)
    plot: Optional[str] = None
    imdb_id: Optional[str] = None
    url: Optional[str] = None
    scraped_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate data after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Movie title cannot be empty")

        if len(self.title) > 200:
            raise ValueError("Movie title too long")

        if self.rating is not None and not (0.0 <= self.rating <= 10.0):
            raise ValueError(f"Invalid rating: {self.rating}")

        if self.year is not None and not (1900 <= self.year <= 2030):
            raise ValueError(f"Invalid year: {self.year}")

        if self.plot and len(self.plot) > 1000:
            self.plot = self.plot[:997] + "..."

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return {
            "title": self.title,
            "year": self.year,
            "rating": self.rating,
            "runtime": self.runtime,
            "genres": self.genres,
            "director": self.director,
            "cast": self.cast,
            "plot": self.plot,
            "imdb_id": self.imdb_id,
            "url": self.url,
            "scraped_at": self.scraped_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Movie':
        """Create Movie from dictionary."""
        # Convert scraped_at back to datetime if present
        if 'scraped_at' in data and isinstance(data['scraped_at'], str):
            data['scraped_at'] = datetime.fromisoformat(data['scraped_at'])

        return cls(**data)


@dataclass
class SearchResult:
    """Search result data model."""
    title: str
    year: Optional[int] = None
    imdb_id: Optional[str] = None
    url: Optional[str] = None
    relevance_score: float = 0.0  # 0.0 to 1.0

    def __post_init__(self):
        """Validate data after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Search result title cannot be empty")

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "title": self.title,
            "year": self.year,
            "imdb_id": self.imdb_id,
            "url": self.url,
            "relevance_score": self.relevance_score,
        }


@dataclass
class ScraperError:
    """Error information for scraper operations."""
    error_type: str
    message: str
    url: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.now)
    retry_count: int = 0

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "error_type": self.error_type,
            "message": self.message,
            "url": self.url,
            "timestamp": self.timestamp.isoformat(),
            "retry_count": self.retry_count,
        }