code ![image](https://github.com/user-attachments/assets/de182e9e-4726-41ff-b20e-7e7a5eae861f)
output ![image](https://github.com/user-attachments/assets/2426aa54-7d89-46bd-bc71-11443483e98b)
explanation
import streamlit as st
→ Loads Streamlit for building the interactive web app.

import pandas as pd
→ Loads pandas for working with tabular data (like CSVs).

import matplotlib.pyplot as plt
→ Imports matplotlib for static plotting.

import seaborn as sns
→ Imports seaborn for statistical data visualization.

import plotly.express as px
→ Imports Plotly Express for interactive plots.

import requests
→ Allows making HTTP requests (used here to load external data indirectly).

🧾 Title and Sidebar Input
st.title("COVID-19 Stats Visualization")
→ Adds a big title at the top of the app.

st.sidebar.header("Filter Options")
→ Adds a sidebar header for input filters.

country = st.sidebar.text_input(...)
→ Lets users type in a country name (defaults to "United States").

📊 Loading COVID-19 Data
@st.cache_data
→ Caches the result of the data loading function for performance.

def load_data():
→ Defines a function to load COVID-19 data.

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
→ Points to the online dataset from Our World in Data.

df = pd.read_csv(url, parse_dates=["date"])
→ Downloads and reads the CSV, parsing dates automatically.

Error handling:
If the data can't be loaded, it shows an error using st.error() and returns None.

🗂 Filtering and Displaying Country Data
df_country = data[data['location'].str.lower() == country.lower()]
→ Filters the dataset to only rows matching the selected country.

if not df_country.empty:
→ If the filtered DataFrame has data, proceed to display.

df_country.set_index('date', inplace=True)
→ Sets the index to the date column for time-based plotting.

st.write(...)
→ Shows the last few rows of total and new case counts for the selected country.

📈 Visualizations
st.subheader("Confirmed COVID-19 Cases Over Time")
→ Displays a header and a line chart of total cases using st.line_chart().

st.subheader("Daily New Cases")
→ Shows a bar chart of new daily cases with st.bar_chart().

st.subheader("Plotly Line Chart")
→ Displays an interactive Plotly line chart for total cases over time.

st.subheader("Seaborn Heatmap: New Cases")
→ Resamples new case data monthly and shows a heatmap using seaborn for trends.

⚠️ No Data or Load Failure
else: st.warning(...)
→ If no country data found, prompts the user to check the input.

else: st.stop()
→ If data didn’t load at all, stops the app and avoids further errors.

