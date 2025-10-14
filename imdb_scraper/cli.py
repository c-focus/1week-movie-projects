#!/usr/bin/env python3
"""Command-line interface for IMDb scraper."""

import argparse
import json
import sys

from .scraper import IMDbScraper


def print_movie(movie):
    """Pretty print movie information."""
    print(f"\n🎬 {movie.title}")
    print("=" * (len(movie.title) + 2))

    if movie.year:
        print(f"📅 Year: {movie.year}")
    if movie.rating:
        print(f"⭐ Rating: {movie.rating}/10")
    if movie.runtime:
        print(f"⏱️  Runtime: {movie.runtime}")
    if movie.genres:
        print(f"🎭 Genres: {', '.join(movie.genres)}")
    if movie.director:
        print(f"🎬 Director: {movie.director}")
    if movie.cast:
        print(f"🎭 Cast: {', '.join(movie.cast[:3])}{'...' if len(movie.cast) > 3 else ''}")
    if movie.plot:
        # Truncate plot if too long
        plot = movie.plot[:200] + "..." if len(movie.plot) > 200 else movie.plot
        print(f"📖 Plot: {plot}")
    if movie.imdb_id:
        print(f"🔗 IMDb ID: {movie.imdb_id}")
    if movie.url:
        print(f"🌐 URL: {movie.url}")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="IMDb Movie Scraper")
    parser.add_argument("movie", help="Movie title to search for")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON instead of formatted text"
    )
    parser.add_argument(
        "--search-only",
        action="store_true",
        help="Only show search results, don't fetch full movie details"
    )

    args = parser.parse_args()

    if not args.movie or not args.movie.strip():
        print("Error: Please provide a movie title to search for.")
        sys.exit(1)

    scraper = IMDbScraper()

    try:
        if args.search_only:
            # Only show search results
            results = scraper.search_movies(args.movie)
            if not results:
                print(f"No search results found for: {args.movie}")
                sys.exit(1)

            if args.json:
                output = [result.to_dict() for result in results]
                print(json.dumps(output, indent=2))
            else:
                print(f"🔍 Search results for: {args.movie}")
                print(f"Found {len(results)} results:")
                for i, result in enumerate(results, 1):
                    print(f"\n{i}. {result.title}")
                    if result.year:
                        print(f"   Year: {result.year}")
                    if result.imdb_id:
                        print(f"   IMDb ID: {result.imdb_id}")
                    print(f"   Relevance: {result.relevance_score:.1f}")

        else:
            # Get full movie details
            movie = scraper.search_and_get_movie(args.movie)
            if not movie:
                print(f"No movie found for: {args.movie}")
                print("Try using --search-only to see available search results.")
                sys.exit(1)

            if args.json:
                print(json.dumps(movie.to_dict(), indent=2))
            else:
                print_movie(movie)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()