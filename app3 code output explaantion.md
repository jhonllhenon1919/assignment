code ![image](https://github.com/user-attachments/assets/24c4bcd4-e992-47f8-9e8d-c25945a8bc94)
output ![image](https://github.com/user-attachments/assets/671a3d94-5e65-4fb3-8295-ed0c670d7500)
explanation
General Setup
import streamlit as st
→ Imports the Streamlit library so you can build interactive web apps.

st.title("Data Warehousing & Enterprise Data Management")
→ Adds a main title to the app.

Sidebar and Topic Selection
st.sidebar.title("Data Management Topics")
→ Adds a title to the sidebar.

topic_option = st.sidebar.selectbox(...)
→ Creates a dropdown in the sidebar to let the user pick one of four topics:

Introduction

ETL Process

Data Models

Data Governance

Section 1: Introduction
If the user selects "Introduction", it shows:

Header: "What is Data Warehousing?"

Two explanatory text blocks:

What a Data Warehouse is.

What Enterprise Data Management (EDM) means.

Section 2: ETL Process
If "ETL Process" is selected:

A header and paragraph explain the ETL steps: Extract, Transform, Load.

A bulleted list outlines the benefits of ETL.

st.columns(2)
→ Splits the layout into two columns:

Left: Explains Data Extraction

Right: Explains Data Transformation

st.expander("Data Loading Explanation")
→ A collapsible section explaining how transformed data is loaded into a data warehouse or data lake.

Section 3: Data Models
If "Data Models" is selected:

A header and paragraph explain the three major schema types used in data warehousing:

Star Schema

Snowflake Schema

Galaxy Schema

st.tabs([...])
→ Creates three tabs where each schema is explained separately using st.subheader and st.write.

Section 4: Data Governance
If "Data Governance" is selected:

A header and a paragraph describe what Data Governance is — managing data integrity, security, and accessibility in an organization.

