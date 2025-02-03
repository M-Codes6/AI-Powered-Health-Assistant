import streamlit as st

st.set_page_config(page_title="AI-Powered Health Assistant", page_icon="🧳")

st.title("🧳Welcome to AI-Powered Health Assistant")
st.markdown("## Learn more about health, fitness, and personalized advice!")

if st.button("Get Started"):
    st.experimental_set_query_params(page="pages/main.py")
