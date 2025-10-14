"""Search history management for IMDb scraper."""

import json
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from pathlib import Path


class SearchHistory:
    """Manages search history and basic caching functionality."""

    def __init__(self, history_file: str = "search_history.json"):
        """Initialize search history manager.

        Args:
            history_file: Path to the history file (relative to project root)
        """
        self.history_file = Path(__file__).parent.parent / history_file
        self.history: Dict[str, Dict[str, Any]] = {}
        self._load_history()

    def _load_history(self) -> None:
        """Load search history from file."""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.history = data
            except (json.JSONDecodeError, FileNotFoundError):
                self.history = {}
        else:
            self.history = {}

    def _save_history(self) -> None:
        """Save search history to file."""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save search history: {e}")

    def record_search(self, query: str, success: bool = True) -> None:
        """Record a search query.

        Args:
            query: The search query
            success: Whether the search was successful
        """
        query = query.strip().lower()  # Normalize for better matching

        if query not in self.history:
            self.history[query] = {
                "count": 0,
                "last_searched": None,
                "last_result": None
            }

        entry = self.history[query]
        entry["count"] += 1
        entry["last_searched"] = datetime.now().isoformat()
        entry["last_result"] = "success" if success else "failed"

        self._save_history()

    def get_popular_searches(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get most popular searches.

        Args:
            limit: Maximum number of results to return

        Returns:
            List of search entries sorted by popularity
        """
        # Sort by count (descending), then by last searched (descending)
        sorted_searches = sorted(
            self.history.items(),
            key=lambda x: (x[1]["count"], x[1]["last_searched"] or ""),
            reverse=True
        )

        results = []
        for query, data in sorted_searches[:limit]:
            results.append({
                "query": query,
                "count": data["count"],
                "last_searched": data["last_searched"],
                "last_result": data["last_result"]
            })

        return results

    def get_recent_searches(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Get most recent searches.

        Args:
            limit: Maximum number of results to return

        Returns:
            List of recent search entries
        """
        # Sort by last searched timestamp (descending)
        sorted_searches = sorted(
            self.history.items(),
            key=lambda x: x[1]["last_searched"] or "",
            reverse=True
        )

        results = []
        for query, data in sorted_searches[:limit]:
            if data["last_searched"]:  # Only include searches that have been made
                results.append({
                    "query": query,
                    "count": data["count"],
                    "last_searched": data["last_searched"],
                    "last_result": data["last_result"]
                })

        return results

    def search_exists(self, query: str) -> bool:
        """Check if a search query exists in history.

        Args:
            query: The search query to check

        Returns:
            True if the query exists in history
        """
        return query.strip().lower() in self.history

    def get_search_stats(self, query: str) -> Optional[Dict[str, Any]]:
        """Get statistics for a specific search query.

        Args:
            query: The search query

        Returns:
            Search statistics or None if not found
        """
        query = query.strip().lower()
        if query in self.history:
            return self.history[query].copy()
        return None

    def cleanup_old_entries(self, days: int = 30) -> int:
        """Remove entries older than specified days.

        Args:
            days: Remove entries not searched in this many days

        Returns:
            Number of entries removed
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        entries_to_remove = []

        for query, data in self.history.items():
            if data["last_searched"]:
                last_searched = datetime.fromisoformat(data["last_searched"])
                if last_searched < cutoff_date:
                    entries_to_remove.append(query)

        for query in entries_to_remove:
            del self.history[query]

        if entries_to_remove:
            self._save_history()

        return len(entries_to_remove)

    def get_total_searches(self) -> int:
        """Get total number of searches recorded.

        Returns:
            Total search count across all queries
        """
        return sum(data["count"] for data in self.history.values())

    def get_unique_queries(self) -> int:
        """Get number of unique search queries.

        Returns:
            Number of unique queries in history
        """
        return len(self.history)

    def clear_history(self) -> None:
        """Clear all search history."""
        self.history = {}
        if self.history_file.exists():
            self.history_file.unlink()  # Delete the file