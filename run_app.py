#!/usr/bin/env python3
"""Streamlit app for IMDb movie scraper."""

import streamlit as st
from imdb_scraper.scraper import IMDbScraper
from imdb_scraper.models import Movie
from imdb_scraper.history import SearchHistory


def display_movie(movie: Movie):
    """Display movie information in a nice format."""
    st.header(f"🎬 {movie.title}")

    col1, col2 = st.columns([2, 1])

    with col1:
        # Basic info
        if movie.year:
            st.write(f"**📅 Year:** {movie.year}")
        if movie.rating:
            st.write(f"**⭐ Rating:** {movie.rating}/10")
        if movie.runtime:
            st.write(f"**⏱️ Runtime:** {movie.runtime}")
        if movie.genres:
            st.write(f"**🎭 Genres:** {', '.join(movie.genres)}")
        if movie.director:
            st.write(f"**🎬 Director:** {movie.director}")
        if movie.cast:
            st.write(f"**🎭 Cast:** {', '.join(movie.cast)}")

        # Plot
        if movie.plot:
            with st.expander("📖 Plot Summary"):
                st.write(movie.plot)

    with col2:
        # IMDb link
        if movie.url:
            st.markdown(f"[🔗 View on IMDb]({movie.url})")
        if movie.imdb_id:
            st.write(f"**IMDb ID:** {movie.imdb_id}")


def main():
    """Main Streamlit app."""
    st.set_page_config(
        page_title="IMDb Movie Search",
        page_icon="🎬",
        layout="wide"
    )

    st.title("🎬 IMDb Movie Search")
    st.markdown("Search for movies and get detailed information from IMDb.")

    # Initialize scraper and history
    if 'scraper' not in st.session_state:
        # Check for test mode (can be set via environment or UI)
        test_mode = st.session_state.get('test_mode', False)
        st.session_state.scraper = IMDbScraper(test_mode=test_mode)
    if 'history' not in st.session_state:
        st.session_state.history = SearchHistory()

    # Sidebar with search history
    with st.sidebar:
        # Test mode toggle
        test_mode = st.checkbox("🧪 Test Mode (use fake data)", value=st.session_state.get('test_mode', False))
        if test_mode != st.session_state.get('test_mode', False):
            st.session_state.test_mode = test_mode
            # Reinitialize scraper with new mode
            st.session_state.scraper = IMDbScraper(test_mode=test_mode)
            st.rerun()

        st.header("🔍 Search History")

        # Popular searches
        popular = [item for item in st.session_state.history.get_popular_searches(5) if item['last_result'] == 'success']
        if popular:
            st.subheader("Popular Searches")
            for item in popular:
                if st.button(f"📊 {item['query']} ({item['count']}x)",
                           key=f"popular_{item['query']}",
                           help=f"Last searched: {item['last_searched'] or 'Never'}"):
                    st.session_state.search_input = item['query']
                    st.rerun()

        # Recent searches
        recent = [item for item in st.session_state.history.get_recent_searches(5) if item['last_result'] == 'success']
        if recent:
            st.subheader("Recent Searches")
            for item in recent:
                if st.button(f"🕒 {item['query']}",
                           key=f"recent_{item['query']}",
                           help=f"Searched {item['count']} times"):
                    st.session_state.search_input = item['query']
                    st.rerun()

        # Stats
        total_searches = st.session_state.history.get_total_searches()
        unique_queries = st.session_state.history.get_unique_queries()
        st.markdown("---")
        st.markdown(f"**Total searches:** {total_searches}")
        st.markdown(f"**Unique movies:** {unique_queries}")

    # Search input
    if 'search_input' not in st.session_state:
        st.session_state.search_input = ""

    movie_query = st.text_input(
        "Enter a movie title:",
        value=st.session_state.search_input,
        placeholder="e.g., The Shawshank Redemption",
        help="Type the name of any movie to search"
    )

    # Clear the search input after use
    if st.session_state.search_input and movie_query != st.session_state.search_input:
        st.session_state.search_input = ""

    col1, col2 = st.columns([3, 1])
    with col1:
        search_clicked = st.button("🔍 Search Movie", type="primary", use_container_width=True)
    with col2:
        if st.button("🗑️ Clear History", help="Clear all search history"):
            st.session_state.history.clear_history()
            st.success("Search history cleared!")
            st.rerun()

    if search_clicked and movie_query:
        # Check if this search exists in history
        search_stats = st.session_state.history.get_search_stats(movie_query)

        if search_stats:
            st.info(f"📊 This movie has been searched {search_stats['count']} times before. "
                   f"Last searched: {search_stats['last_searched'] or 'Unknown'}")

        with st.spinner("Searching IMDb..."):
            try:
                movie = st.session_state.scraper.search_and_get_movie(movie_query)

                if movie:
                    # Show success with search count
                    search_count = st.session_state.history.get_search_stats(movie_query)
                    if search_count and search_count['count'] > 1:
                        st.success(f"✅ Found '{movie.title}'! (Searched {search_count['count']} times total)")
                    else:
                        st.success(f"✅ Found '{movie.title}'!")

                    display_movie(movie)
                    st.rerun()  # Refresh to update search history sidebar
                else:
                    st.error(f"❌ No movie found for '{movie_query}'. Try a different title or check the spelling.")

            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("💡 Try again in a few moments. If the problem persists, the movie might not exist in IMDb.")

    # Footer
    st.markdown("---")
    st.markdown("*Built with IMDb data and anti-bot protection*")


if __name__ == "__main__":
    main()