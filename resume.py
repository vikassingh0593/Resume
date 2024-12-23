import streamlit as st
from PIL import Image

# Setting up the page configuration
st.set_page_config(page_title="Vikas Singh - Portfolio", layout="wide")

# Remove any unnecessary margin or padding and set body padding to 0
st.markdown(
    """
    <style>
    body {
        margin: 0;
        padding: 0;
    }
    .css-1y4e0bo {
        padding-top: 0;  /* Remove any padding from the top */
    }
    .stImage > img {
        margin-top: 0;  /* Remove any margin from the image */
    }
    .stApp {
        padding-top: 0 !important;  /* Ensure no padding in the main app container */
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
    col1, col2, col3 = st.columns([1, 1.1, 1])  # Adjust the ratio as needed

    with col2:
        # Display the image with a fixed width (in normal aspect ratio)
        img = Image.open("vikaspic.jpeg")
        st.image(img, use_container_width=True)
                #  use_container_width=False, width=2000)  # Adjust width as needed

    col1, col2, col3 = st.columns([1, 2.3, 1])  # Adjust the ratio as needed

    with col2:
        # Display a motivational quote
        st.markdown(
            """
            ### Turning Data into Stories | A Glimpse into My Work
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
    if st.button("📈 Discover The World 📈"):
        st.session_state.page = "resume"  # Update session state to the next page
        st.rerun()  # Trigger a rerun to show the new content


# Resume Page
elif st.session_state.page == "resume":
    st.title("Turning Data into Insights, and Insights into Impact")


    # Navigation button with a hover effect
    if st.button("📈 Work Experience 📈"):
        st.session_state.page = "experience"  # Update session state to the next page
        st.rerun()  # Trigger a rerun to show the new content

    if st.button("📈 Skills 📈"):
        st.session_state.page = "skill"  # Update session state to the next page
        st.rerun()  # Trigger a rerun to show the new content

    if st.button("📈 Education 📈"):
        st.session_state.page = "edu"  # Update session state to the next page
        st.rerun()  # Trigger a rerun to show the new content   

    if st.button("📈 Certifications 📈"):
        st.session_state.page = "cert"  # Update session state to the next page
        st.rerun()  # Trigger a rerun to show the new content

    # Back to Home navigation button
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun() 



# Resume Page
elif st.session_state.page == "experience":
    st.title("Career Highlights 🚀")

    # Work Experience Section
    with st.expander("**Tredence Inc.**", expanded=True):

        st.subheader("Senior Software Engineer - Data Analytics & Engineering")
        st.write("**Feb'22 - Present**")
        st.markdown("### Data Analytics & Solutions 📊")
        st.write("**Developed a supply chain simulation & analytics tool for a global CPG client**")
        st.write(
            """
            - Enabled analysis of scenarios like demand, supply fluctuations, capacity bottlenecks, and changes to drive data-informed decisions.
            - Designed an architecture integrating ADLS, Databricks, Power BI & Power Apps for seamless data flow.
            - Improved user experience and system efficiency through smooth data movement and platform integration.
            - **Outcome:** ~$1 million in anticipated cost savings over the course of a year.
            """
        )

        st.markdown("### Data Engineering & Solutions ⚙️")
        st.write("**Developed an integrated solution for a CPG client on Databricks and ADLS**")
        st.write(
            """
            - Unified multiple recommendation models into a single platform for the command center.
            - Implemented a modularized code structure, ensuring synchronization across recommendation models to deliver consistent and relevant information.
            - **Outcome:** Achieved ~5% reduction in order diversion recommendations and STOs, while improving outbound-inbound forecast accuracy.
            """
        )

        st.write("**Awards:** Pat on the Back Award 🎉")
        st.write("---")


    with st.expander("**EXL**"):

        st.subheader("Consultant - Analytics")
        st.write("**Feb'22 - Jan'24**")

        st.markdown("### Data Engineering & Solutions ⚙️")
        st.write("**Designed and implemented a composite data source for an automobile client using HiveQL and PySpark**")
        st.write(
            """
            - Linked dealership repair order transactions, survey responses, services, and status flags.
            - Enabled business teams to track Net Promoter Score (NPS) and dealer performance.
            - **Outcome:** Empowered better decision-making for tracking performance and customer satisfaction.
            """
        )

        st.write("**Engineered an interactive real-time monitoring solution for telecommunication clients using Teradata SQL and PySpark**")
        st.write(
            """
            - Provided live tracking for ETL processes, including KPI evaluation for completion percentage, time estimates, and reliability.
            - Addressed top management's challenges with data asset oversight and SLA mitigation strategies.
            - **Outcome:** Streamlined real-time monitoring for improved data reliability and management.
            """
        )

        st.write("**Developed a composite data source for an automobile client to track customer satisfaction (CSAT) using HiveQL**")
        st.write(
            """
            - Enabled granular tracking of customer journeys for electric vehicles.
            - Provided insights into customer behavior and satisfaction to improve experience management.
            - **Outcome:** Enabled quick identification of customer experience issues and improved satisfaction scores.
            """
        )

        st.markdown("### Data Analytics & Visualization 📊")
        st.write("**Developed a Quartile Distribution table to analyze dealers' performance and suggest improvements**")
        st.write(
            """
            - Analyzed dealer performance and suggested best practices to improve service quality and brand score.
            - **Outcome:** Delivered actionable insights for improving service delivery across dealerships.
            """
        )

        st.write("**Developed a summary dataset and Power BI dashboard for tracking dealer performance**")
        st.write(
            """
            - Created a dataset in Hive to track key performance indicators (KPIs) like NPS change by various categories.
            - Delivered an interactive Power BI dashboard for real-time dealer performance monitoring.
            - **Outcome:** Enabled better tracking and comparison of dealer performance across multiple dimensions.
            """
        )

        st.markdown("### Stakeholder Management & Initiatives 👥")
        st.write("**Up-skilled the team on new technologies, including Azure Databricks and Azure DevOps**")
        st.write(
            """
            - Delivered knowledge transfer sessions on continuous integration/continuous deployment (CI/CD) pipelines.
            - **Outcome:** Improved team efficiency in adopting new technologies and methodologies.
            """
        )

        st.write("**Facilitated the adoption of new inbuilt technology for scheduling workflows**")
        st.write(
            """
            - Assisted internal and external teams with transitioning to a new workflow scheduling technology.
            - Streamlined SQL workflows in PySpark scripts for smoother execution.
            - **Outcome:** Reduced deployment time and enhanced workflow visibility.
            """
        )

        st.write("**Awards:** Stellar Performance Award 🌟")

        st.write("---")

    with st.expander("**Edlabz Innovation**"):
        st.subheader("Program Associate – Data Analytics")
        st.write("**Sep'19 - Feb'22**")

        st.markdown("### Data Analytics & Visualization 📈")
        st.write("**Applied Python models, including K-Means Clustering, to enhance marketing campaigns**")
        st.write(
            """
            - Gained deeper insights into customer behavior to inform targeted marketing strategies.
            - **Outcome:** Improved marketing campaigns with data-driven customer segmentation.
            """
        )

        st.write("**Conducted comprehensive Exploratory Data Analysis (EDA) to analyze market trends**")
        st.write(
            """
            - Analyzed customer requirements to recommend targeted promotions and offers for Instagram and Facebook campaigns.
            - **Outcome:** Enabled more impactful and relevant marketing initiatives.
            """
        )

        st.write("**Utilized RFM techniques to improve campaign personalization and engagement**")
        st.write(
            """
            - Precisely targeted customers to boost personalization and engagement.
            - **Outcome:** Increased customer response rates and campaign success.
            """
        )

        st.write("**Used Tableau to create interactive dashboards for effective communication**")
        st.write(
            """
            - Delivered weekly and monthly insights to senior management with interactive Tableau dashboards.
            - **Outcome:** Enhanced decision-making through clear and actionable visual insights.
            """
        )

        st.markdown("### Stakeholder Management & Initiatives 🤝")
        st.write("**Collaborated closely with developers to prioritize and integrate initiatives**")
        st.write(
            """
            - Worked to ensure smooth integration of initiatives into the product roadmap, tracking implementation timelines.
            - **Outcome:** Successful execution of key initiatives with clear communication and alignment.
            """
        )

        st.write("**Devised and implemented systems to optimize lead utilization and feedback capture**")
        st.write(
            """
            - Improved decision-making and strategic refinement by streamlining lead management and feedback processes.
            - **Outcome:** Enhanced operational efficiency and actionable insights for future campaigns.
            """
        )

        st.write("---")


    # Back to Home navigation button
    if st.button("Back"):
        st.session_state.page = "resume"
        st.rerun() 

elif st.session_state.page == "skill":
    st.title("My Toolbox 🧰")

    # Define markdown content for the skills, tools, and platforms
    programming_languages_markdown = """
    - 🐍 Python
    - 📊 SQL
    - 📝 HiveQL
    - ⚙️ Teradata SQL
    - 🔥 PySpark
    """

    scripting_tools_markdown = """
    - 💾 BTEQ scripting
    - 🖥️ Linux commands
    - 🚀 Streamlit
    - 🧪 Flask
    """

    data_platforms_tools_markdown = """
    - ⚡ Databricks
    - ❄️ Snowflake
    - ☁️ Azure
    - 🔄 Airflow
    - 🛠️ Oozie
    - 🌈 Hue
    - 🔧 Alteryx
    - 🖥️ DBeaver
    - 📝 Jupyter
    - ☁️ Azure DevOps
    - 🐙 GitHub
    - 🖥️ VS Code
    """

    bi_analytics_tools_markdown = """
    - 📊 Power BI
    - 🎨 Tableau
    - 🧮 Excel
    - 🎤 PowerPoint
    """

    # Create the columns for the layout
    col1, col2 = st.columns([2, 1]) 

    # Column 1: Programming Languages & Scripting
    with col1:
        st.subheader("💻 Programming Languages & Scripting")
        st.markdown(programming_languages_markdown)
        st.markdown(scripting_tools_markdown)

    # Column 2: Data Platforms & Tools
    with col2:
        st.subheader("⚙️ Data Platforms & Tools")
        st.markdown(data_platforms_tools_markdown)

    # Create a centered column for the third section
    col3 = st.columns([1, 2, 0.5])[1]  # Center the third column (middle one)

    # Column 3: Business Intelligence & Analytics Tools
    with col3:
        st.subheader("📊 Business Intelligence & Analytics Tools")
        st.markdown(bi_analytics_tools_markdown)

    # Back to Home navigation button
    if st.button("Back"):
        st.session_state.page = "resume"
        st.rerun()


elif st.session_state.page == "edu":
    st.title("My Academic Journey 🎓") # My Academic Journey / The Scholar’s Path

    # st.write("---")
    st.header("🎓 [Bachelor of Technology](https://www.dcrustm.ac.in/)")
    # st.header("🎓 Bachelor of Technology")
    st.write("🗓 **Jul'15 - Jun'19**")
    st.write("---")

    st.markdown("""
        <style>
        a {
            color: grey !important;  /* Force color to black */
            text-decoration: none !important;  /* Remove underline */
        }
        </style>
        """, unsafe_allow_html=True)

    st.subheader("🏫 [**Deenbandhu Chhotu Ram University of Science and Technology**](https://www.dcrustm.ac.in/)")
    # st.subheader("🏫 **Deenbandhu Chhotu Ram University of Science and Technology (DCRUST)**")
    
    st.write("🔍 **Key Projects & Training**")
    st.write("- 🌱 Investigated cost-effective strategies for optimizing Biogas plant operations.")
    
    # st.write("---")
    st.write("💼 **Internship Experience**")

    st.write("- 🔋 Exide Industries Ltd., Bawal | Research Intern")
    # st.write("- 🔍 Assessed awareness of Exide's emergency and online services among 20+ dealers and 400+ customers in Rewari district.")
    # st.write("- 📊 Exide's market share was strong (~70%), but awareness of emergency & online services was low.")
    # st.write("- 📱 Utilized social media targeting (25-35 age group) to bridge the communication gap and raise awareness.")
    # st.write("- 🛠 Used warranty space to advertise services, conducted quarterly dealer training for new products and offerings.")

    st.write("- 🎨 Nerolac Pvt. Ltd., Bawal | Student Intern")
    # st.write("- 🔧 Optimized paint solvent usage by analyzing data variance between SAP ERP and On-Floor Books.")
    # st.write("- 🔄 Analyzed the lifecycle of solvent and paint manufacturing processes to identify causes of variance.")
    # st.write("- 📉 Achieved 87% reduction in variance by suggesting changes in the floor measurement methodology.")
    # st.write("- 💸 Reduced solvent wastage by 24%, minimizing transportation and handling losses.")

    st.write("---")
    st.write("🏅 **Extra-Curricular Activities & Achievements**")

    st.write("- 🌍 Volunteer at N.S.S Camp & Net Impact Event")
    st.write("- 💻 Coached 100+ people on how to use the UPI interface with or without the app.")
    st.write("- 🏆 Ranked #1 in Haryana and #13 in India in 🧮 National Mathematics Olympiad 2009 (50,000+ participants).")
    st.write("- 🏢 Elected President of B. Tech Hostel & Managed a student community 👥 of 450+ members.")
    st.write("- 🎉 Coordinator| 🚨 Managed a team of 25+ students to ensure the smooth execution of the cultural event.")


    st.write("---")

    # Back to Home navigation button
    if st.button("Back"):
        st.session_state.page = "resume"
        st.rerun() 

elif st.session_state.page == "cert":
    st.title("🏆 Professional Certifications")

    st.markdown("""
        ### Unlocking skills with industry-recognized certifications:
    """)
    
    st.write("🌟 [SnowPro Core Certification](https://achieve.snowflake.com/28c5d1ba-3e6f-4663-9c18-dff6f228e04f#acc.T9U3DcjH)")
    st.image("snowflake.png", width=100) 
    
    st.write("🌟 [Databricks Certified Data Engineer Associate](https://credentials.databricks.com/fee07c14-42f8-4fd0-895f-aa8a9bce315b#acc.1aISCKcw)")
    st.image("databricks.png", width=100)  # Upload the Databricks logo
    
    st.write("🌟 [Microsoft Azure Data Fundamentals](https://www.credly.com/badges/19b2fcf6-d864-447b-ac18-b5af7defeb98)")
    # st.image("azure_logo.png", width=40)  # Upload the Azure logo
    
    st.write("🌟 [Data Warehouse with BigQuery](https://www.credly.com/badges/100a7552-326d-4fdb-9f2a-627f36066477/linked_in_profile)")
    # st.image("bigquery_logo.png", width=40)  # Upload the BigQuery logo
    
    st.write("🌟 [Scrum Fundamentals Certified](https://www.scrumstudy.com/certification/verify?type=SFC&number=1016849)")
    # st.image("scrum_logo.png", width=40)  # Upload the Scrum logo
    
    st.write("🌟 [SQL (Advanced) - HackerRank](https://www.hackerrank.com/certificates/310efed0a7ae)")
    st.image("sql.png", width=100)  # Upload the HackerRank logo


    # Back to Home navigation button
    if st.button("Back"):
        st.session_state.page = "resume"
        st.rerun() 











# [theme]
# base="light"
# backgroundColor="#cbc6c6"

