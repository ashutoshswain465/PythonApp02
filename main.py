import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ashutosh Swain")
    content = """Hi, I’m Ashutosh Swain, a motivated Test Analyst at TCS with expertise in SQL, JavaScript, Python, and testing. Currently pursuing an OPGDM in Data Science and Analytics from Great Lakes, I aim to transition into cybersecurity to tackle complex challenges.
With a B.Tech in EEE from ITER, I combine technical skills with a drive for continuous learning. In my free time, I enjoy reading books like Atomic Habits. This portfolio reflects my journey, skills, and passion for growth."""
    st.info(content)

content2 = """
Below you can find some of the apps I have built in python. Feel free to check it out!
"""
st.write(content2)
