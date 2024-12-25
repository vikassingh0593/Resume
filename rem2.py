import streamlit as st

# Set up the page config
st.set_page_config(page_title="Data Chronicles by Vikas Singh", layout="wide")

# List of pages with radio buttons (only one option can be selected at a time)
page = st.sidebar.radio("Select Page", ["Home", "Experience", "Skills", "Education", "Certifications"])

# Show content based on selected page
if page == "Home":
    st.title("Welcome to Data Chronicles!")
    st.write("This is the homepage of Data Chronicles by Vikas Singh.")
elif page == "Experience":
    st.title("Work Experience")
    st.write("Details about my work experience, projects, and achievements...")
elif page == "Skills":
    st.title("Skills")
    st.write("Skills in data analytics, programming languages, and machine learning...")
elif page == "Education":
    st.title("Education")
    st.write("My educational background, degrees, and relevant coursework...")
elif page == "Certifications":
    st.title("Certifications")
    st.write("Certifications I've obtained in various data science and analytics fields.")
