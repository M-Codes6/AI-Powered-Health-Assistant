import streamlit as st

st.title("Welcome to Your Health Assistant App")
st.image("welcome_image.jpg", caption="Your trusted AI health companion")  # Optional image
st.markdown("## Learn more about health, fitness, and personalized advice!")

if st.button("Get Started"):
    st.experimental_set_query_params(page="pages/main.py")
