import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Self_photo.jpg")

with col2:
    st.title("Ashutosh Swain")
    content = """
    Hi there! I’m Ashutosh Swain, a tech enthusiast and motivated Test Analyst at TCS, with expertise in 
    SQL, JavaScript, Python, and software testing. My passion lies in leveraging technology to solve problems and create 
    impactful solutions.
    
    Currently pursuing an OPGDM in Data Science and Analytics at Great Lakes Institute of Management, I’m gearing up to 
    transition into the exciting world of cybersecurity, combining analytical prowess with cutting-edge innovation. With 
    a B.Tech in Electrical and Electronics Engineering from ITER, S'O'A University, I’ve built a strong technical 
    foundation that I’m eager to expand.
    
    Beyond work, you’ll often find me immersed in self-development books like Atomic Habits, fueling my commitment to 
    growth and excellence. My calm demeanor and drive to improve continuously define who I am, both personally and 
    professionally.
    
    This portfolio showcases my journey, skills, and projects that speak to my dedication and ambition. Whether it’s 
    securing systems or creating value through technology, I’m ready to make an impact.
    Thanks for stopping by—I’d love to connect and collaborate!"""
    st.info(content)

content2 = """
Below you can find some of the apps I have built in python. Feel free to check it out!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
