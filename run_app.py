#!/usr/bin/env python3
"""Streamlit app for IMDb movie scraper."""

import streamlit as st
from imdb_scraper.scraper import IMDbScraper
from imdb_scraper.models import Movie


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

    # Initialize scraper
    if 'scraper' not in st.session_state:
        st.session_state.scraper = IMDbScraper()

    # Search input
    movie_query = st.text_input(
        "Enter a movie title:",
        placeholder="e.g., The Shawshank Redemption",
        help="Type the name of any movie to search"
    )

    if st.button("🔍 Search Movie", type="primary") and movie_query:
        with st.spinner("Searching IMDb..."):
            try:
                movie = st.session_state.scraper.search_and_get_movie(movie_query)

                if movie:
                    display_movie(movie)
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