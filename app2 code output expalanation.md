 code ![image](https://github.com/user-attachments/assets/25f913e1-1ac5-420a-9eea-d254eec3646c)
output ![image](https://github.com/user-attachments/assets/766b0806-8959-4180-8561-6fbbae6c3622)
expalantion
import streamlit as st
→ Imports the Streamlit library so you can use its app-building tools.

import pandas as pd
→ Imports Pandas, a library for working with tabular data like CSV files.

st.title("Load and Display Data")
→ Adds a large title at the top of the app that says "Load and Display Data".

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
→ Creates a file upload button that accepts CSV files. The uploaded file is stored in uploaded_file.

if uploaded_file is not None:
→ Checks if a file has been uploaded before proceeding with loading and displaying it.

df = pd.read_csv(uploaded_file)
→ Reads the uploaded CSV file into a Pandas DataFrame called df.

st.write("### Dataframe Preview")
→ Displays a subheading "Dataframe Preview" using markdown-style formatting (###).

st.dataframe(df)
→ Shows the loaded DataFrame (df) in a scrollable, interactive table.

if st.checkbox("Show raw data"):
→ Displays a checkbox labeled "Show raw data". If the user checks it, the next line runs.

st.write(df)
→ Outputs the full DataFrame as plain text-style output (less formatted than st.dataframe()).

columns = df.columns.tolist()
→ Gets a list of column names from the DataFrame and stores it in the columns variable.

selected_column = st.selectbox("Select a column to filter by", columns)
→ Creates a dropdown list (selectbox) where the user can choose which column to use for filtering.

unique_values = df[selected_column].unique()
→ Finds all unique values in the selected column.

selected_value = st.selectbox(f"Select a value from {selected_column}", unique_values)
→ Displays a second dropdown so the user can choose a specific value from the selected column.

filtered_df = df[df[selected_column] == selected_value]
→ Filters the DataFrame to include only rows where the selected column matches the selected value.

st.write(f"### Filtered Data by {selected_column} = {selected_value}")
→ Displays a subheading showing which column and value were used for filtering.

st.dataframe(filtered_df)
→ Shows the filtered data as an interactive table.

