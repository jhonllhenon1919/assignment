code ![494688198_968653935340342_4698691562953419876_n](https://github.com/user-attachments/assets/1032e301-a837-497b-b899-949838cd7d26)
      ![494687592_1002167008351690_1184954181489037296_n](https://github.com/user-attachments/assets/d876fc0e-188e-4711-8864-939d69ddbc50)


output ![494688379_1461038501944492_6567327078522748328_n](https://github.com/user-attachments/assets/284376bb-6a76-4729-9ad0-c07b5a9a4af4)

explanation
Database Connection using SQLAlchemy:
get_db_engine() function sets up the database connection string using SQLAlchemy.

The create_engine() function creates a connection to the MySQL database. You'll need to replace the credentials (username, password, host, and database name) with your actual MySQL server details.

 Fetching Data from MySQL:
The fetch_data_from_db() function executes a raw SQL query to fetch data from the database and loads it into a pandas DataFrame.

The query is customizable. You can change it to suit your specific needs (e.g., filtering, sorting).

 Inserting New Data into the Database:
The insert_data_to_db() function takes user input (name and age) and inserts it into the MySQL database using a basic INSERT INTO SQL query.

It’s important to sanitize inputs (avoid SQL injection). In a production app, consider using prepared statements instead.

 User Authentication (Bonus):
The authenticate_user() function uses Streamlit's session state (st.session_state) to manage user authentication.

Simple hardcoded credentials (admin / password) are used in this example, but you should integrate a proper authentication system (e.g., OAuth, or a database of user credentials) for production use.

 Streamlit Interface:
The app displays a data table of records from the database and allows form input to insert new rows into the database.

Users must log in before accessing the data.

