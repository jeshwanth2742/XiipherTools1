import streamlit as st
from src.api.x_client import get_user_id, fetch_tweets
from src.api.metrics import calculate_metrics
from src.utils.time_utils import get_time_range
from src.frontend.components.inputs import user_inputs
from src.frontend.components.dashboard import display_metrics


def main():
    st.set_page_config(page_title="XiipherTools - Contribution Tracker", layout="centered")
    st.title("XiipherTools 🛠️")
    st.markdown("Track X (Twitter) user contributions toward sub-projects under a main project.")

    # Get user inputs
    username, sub_project, timeframe = user_inputs()

    # Fetch metrics on button click
    if st.button("Fetch Metrics"):
        if not username.strip():
            st.error("Please enter a valid X handle.")
            return
        try:
            with st.spinner("Fetching data..."):
                user_id = get_user_id(username)
                start, end = get_time_range(timeframe)
                tweets = fetch_tweets(user_id, start, end, sub_project)
                metrics = calculate_metrics(tweets)
                display_metrics(metrics)
        except Exception as e:
            st.error(f"Error fetching metrics: {e}")


if __name__ == "__main__":
    main()
