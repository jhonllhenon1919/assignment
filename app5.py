import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
from sqlalchemy import text

# Database connection setup (SQLAlchemy)
def get_db_engine():
    # Replace these values with your own database credentials
    username = 'your_username'
    password = 'your_password'
    host = 'localhost'  # or the IP address of your MySQL server
    database = 'your_database'

    connection_string = f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"
    engine = create_engine(connection_string)
    return engine

# Fetch data from the database
def fetch_data_from_db(query):
    engine = get_db_engine()
    with engine.connect() as connection:
        result = connection.execute(text(query))
        data = result.fetchall()
        columns = result.keys()
        df = pd.DataFrame(data, columns=columns)
    return df

# Insert new data into the database
def insert_data_to_db(name, age):
    engine = get_db_engine()
    with engine.connect() as connection:
        insert_query = f"""
        INSERT INTO your_table (name, age) 
        VALUES ('{name}', {age});
        """
        connection.execute(text(insert_query))

# Title and description
st.title("Streamlit with MySQL Integration")
st.write("""
This app connects to a MySQL database, fetches data, displays it, and allows users to insert new data.
""")

# Fetch and filter data section
st.header("View Data from Database")

# SQL query to fetch data
query = "SELECT * FROM your_table LIMIT 100;"  # Customize the query to match your table structure
data = fetch_data_from_db(query)

# Show the data in a table
st.dataframe(data)

# Form to insert new rows into the database
st.header("Insert New Data")

with st.form(key='data_form'):
    name = st.text_input("Enter Name")
    age = st.number_input("Enter Age", min_value=0, max_value=150)
    
    submit_button = st.form_submit_button(label='Submit')
    
    if submit_button:
        insert_data_to_db(name, age)
        st.success("Data inserted successfully!")

# Bonus: User Authentication (Simple version using Streamlit session state)
st.sidebar.header("User Authentication")

def authenticate_user():
    if "user_authenticated" not in st.session_state:
        st.session_state["user_authenticated"] = False

    if not st.session_state["user_authenticated"]:
        username = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        
        if st.button("Login"):
            if username == "admin" and password == "password":  # Use actual authentication methods here
                st.session_state["user_authenticated"] = True
                st.sidebar.success("Logged in successfully")
            else:
                st.sidebar.error("Invalid credentials")
    else:
        st.sidebar.write(f"Hello, {username}")

# Authenticate user before showing the app
authenticate_user()

if st.session_state["user_authenticated"]:
    st.write("Welcome to the secure section of the app!")
    # You can put more secure content here for authenticated users.
else:
    st.warning("Please log in to access the data.")

