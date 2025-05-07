code ![494687592_1002167008351690_1184954181489037296_n](https://github.com/user-attachments/assets/bff1690e-cf41-45e5-a2e3-6e2c49b3bab0)
output ![494688379_1461038501944492_6567327078522748328_n](https://github.com/user-attachments/assets/4ef4ca5e-34f5-4698-865e-96d3e1cb11cc)
explanation
Database Connection using SQLAlchemy:
get_db_engine() function sets up the database connection string using SQLAlchemy.

The create_engine() function creates a connection to the MySQL database. You'll need to replace the credentials (username, password, host, and database name) with your actual MySQL server details.

2. Fetching Data from MySQL:
The fetch_data_from_db() function executes a raw SQL query to fetch data from the database and loads it into a pandas DataFrame.

The query is customizable. You can change it to suit your specific needs (e.g., filtering, sorting).

3. Inserting New Data into the Database:
The insert_data_to_db() function takes user input (name and age) and inserts it into the MySQL database using a basic INSERT INTO SQL query.

It’s important to sanitize inputs (avoid SQL injection). In a production app, consider using prepared statements instead.

4. User Authentication (Bonus):
The authenticate_user() function uses Streamlit's session state (st.session_state) to manage user authentication.

Simple hardcoded credentials (admin / password) are used in this example, but you should integrate a proper authentication system (e.g., OAuth, or a database of user credentials) for production use.

5. Streamlit Interface:
The app displays a data table of records from the database and allows form input to insert new rows into the database.

Users must log in before accessing the data.

