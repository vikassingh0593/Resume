import streamlit as st
from PIL import Image

# Setting up the page configuration
st.set_page_config(page_title="Vikas Singh - Portfolio", layout="wide")

# Remove any unnecessary margin or padding
st.markdown(
    """
    <style>
    body {
        margin: 0;
        padding: 0;
    }
    .css-1y4e0bo {
        padding-top: 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation control
if "page" not in st.session_state:
    st.session_state.page = "home"  # Set default page to 'home' if it's not already set

# Homepage
if st.session_state.page == "home":
    # Create columns to center the image
    col1, col2, col3 = st.columns([1, 1.9, 1])  # Adjust the ratio as needed

    with col2:
        # Display the image with a fixed width (in normal aspect ratio)
        img = Image.open("vikaspic.jpeg")
        st.image(img, use_container_width=False, width=400)  # Adjust width as needed

    col1, col2, col3 = st.columns([1, 2.3, 1])  # Adjust the ratio as needed

    with col2:
        # Display a motivational quote
        st.markdown(
            """
            ### "Turning Data into Stories | A Glimpse into My Work"
            """
        )

    # Add CSS styling for button
    st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #B0B0B0;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 12px;
            padding: 10px 24px;
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #808080;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Navigation button with a hover effect
    if st.button("🌟 Discover The World 🌟"):
        st.session_state.page = "resume"  # Update session state to the next page
        st.rerun()  # Trigger a rerun to show the new content


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
