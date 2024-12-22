import streamlit as st
from PIL import Image

# Setting up the page configuration
st.set_page_config(page_title="Vikas Singh - Portfolio", layout="wide")

# Navigation control
if "page" not in st.session_state:
    st.session_state.page = "home"
    # st.title("Vikas Singh - Portfolio")

# Homepage
elif st.session_state.page == "home":
    # st.title("Vikas Singh - Portfolio")
    # Create columns to center the image
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust the ratio as needed

    with col2:
        # Display the image with a fixed width (in normal aspect ratio)
        img = Image.open("vikaspic.jpeg")
        st.image(img, use_container_width=False, width=500)  # Adjust width as needed

    col1, col2, col3 = st.columns([1, 2.77, 1])  # Adjust the ratio as needed

    with col2:
    # Display a motivational quote
        st.markdown(
            """
            ### "Turning Data into Stories | A Glimpse into My Work"
            """
        )
    
    # Navigation button
    if st.button("Discover"):
        st.session_state.page = "resume"
        st.rerun()  # Correct way to force a rerun



# Resume Page
elif st.session_state.page == "resume":
    st.title("Turning Data into Insights, and Insights into Impact.")

    # Work Experience Section
    with st.expander("Work Experience"):
        st.subheader("Tredence Inc., Gurugram | Senior Software Engineer - Data")
        st.write("**Feb'22 - Present**")
        st.write(
            "- Developed an integrated solution on Databricks and ADLS for CPG client.\n"
            "- Achieved ~5% reduction in order diversion recommendations."
        )
        st.write("**Awards:** Pat on the Back Award")
        st.write("---")

        st.subheader("EXL Inductis (India) Pvt. Ltd., Gurugram | Consultant – Analytics")
        st.write("**Feb'22 - Present**")
        st.write(
            "- Designed and implemented composite data sources for multiple clients.\n"
            "- Engineered solutions using Teradata SQL, PySpark, and HiveQL."
        )
        st.write("**Awards:** Stellar Performance Award")

    # Skills Section
    with st.expander("Skills"):
        st.write("- Python, SQL, HiveQL, Teradata SQL, PySpark")
        st.write("- Databricks, Snowflake, Power BI, Tableau")

    # Education Section
    with st.expander("Education"):
        st.write("**Deenbandhu Chhotu Ram University of Science and Technology (DCRUST)**")
        st.write("Bachelor of Technology | July'15 - May'19")
        st.write("- Researched cost optimization strategies for Biogas plant operations.")

    # Certifications Section
    with st.expander("Certifications"):
        st.write("- SnowPro Core Certification")
        st.write("- Databricks Certified Data Engineer Associate")
        st.write("- Microsoft Azure Data Fundamentals")

    # Back to Home navigation button
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun() 
