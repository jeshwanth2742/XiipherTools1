import streamlit as st

def user_inputs():
    """
    Streamlit input form for the user to enter X handle,
    select sub-project, and choose timeframe.
    
    Returns:
        tuple: (username, sub_project, timeframe)
    """
    st.sidebar.header("User Inputs")
    
    # Input X handle (without @)
    username = st.sidebar.text_input("Enter X handle (without @)", "Jeswanth")
    
    # Select sub-project
    sub_project = st.sidebar.selectbox(
        "Select Sub-project",
        ["@Anoma", "@Monad", "@Ethereum"]
    )
    
    # Select timeframe
    timeframe = st.sidebar.selectbox(
        "Select Timeframe",
        ["24h", "7d", "30d", "90d"]
    )
    
    return username.strip(), sub_project, timeframe
