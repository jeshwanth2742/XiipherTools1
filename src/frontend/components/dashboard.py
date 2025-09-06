import streamlit as st

def display_metrics(metrics: dict):
    """
    Display contribution metrics in a Streamlit dashboard.
    
    Args:
        metrics (dict): Dictionary returned by calculate_metrics()
    """
    st.subheader("Contribution Metrics")
    
    if not metrics or metrics.get("tweets", 0) == 0:
        st.info("No tweets found for the selected timeframe and sub-project.")
        return
    
    # Display metrics in columns
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Tweets", metrics.get("tweets", 0))
    col2.metric("Likes", metrics.get("likes", 0))
    col3.metric("Replies", metrics.get("replies", 0))
    
    col1, col2 = st.columns(2)
    col1.metric("Retweets", metrics.get("retweets", 0))
    col2.metric("Quotes", metrics.get("quotes", 0))
    
    st.markdown("---")
    st.success("Metrics fetched successfully!")
