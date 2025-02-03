import streamlit as st

st.title("🧳Welcome to AI-Powered Health Assistant")
st.image("", caption="Your trusted AI health companion")  
st.markdown("## Learn more about health, fitness, and personalized advice!")

if st.button("Get Started"):
    st.experimental_set_query_params(page="pages/main.py")
