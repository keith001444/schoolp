import database
import sqlite3
# database.add_someone("EB3/57373/21","KEITH","RICHARD","MUMO","MALE",22)
# database.delete_student('EB3/56373/21')
# # # database.add_logins()
# #
# # database.add_someone("EB3/57222/21","KASYOKI","MULE","KYULE","MALE",23)
# #
# # database.add_someone("EB3/55555/21","NATALIE","REBECA","MUIRO","FEMALE",21)
#
# data = database.get_students_and_subjects()
# print(data)
# import sqlite3
# def add_average_column():
#     with sqlite3.connect('student.db') as conn:
#         cursor = conn.cursor()
#
#         # Adding the 'average' column to the 'subjects' table
#         cursor.execute('''
#             ALTER TABLE subjects
#             ADD COLUMN average REAL
#         ''')
#         conn.commit()
#
# add_average_column()
#
#
# def calculate_and_store_averages():
#     with sqlite3.connect('student.db') as conn:
#         cursor = conn.cursor()
#
#         # Fetch all students and their marks
#         cursor.execute('''
#             SELECT admission_no, Mathematics, Biology, Chemistry, Physics, Geography,
#                    Business, English, Kiswahili, CRE, French
#             FROM subjects
#         ''')
#         students = cursor.fetchall()
#
#         # Calculate the average for each student and update the 'average' column
#         for student in students:
#             admission_no = student[0]
#             marks = student[1:]  # Exclude admission_no
#             valid_marks = [mark for mark in marks if mark is not None]  # Remove None values
#             if valid_marks:
#                 average = sum(valid_marks) / len(valid_marks)
#             else:
#                 average = None
#
#             # Update the 'average' column in the database
#             cursor.execute('''
#                 UPDATE subjects
#                 SET average = ?
#                 WHERE admission_no = ?
#             ''', (average, admission_no))
#
#         conn.commit()
#
# # Call the function to calculate and store the averages
# calculate_and_store_averages()
#database.add_login("EB3/57373/21","Keith99!!")
#database.add_all_tables()
#database.add_admin_data1("Lecturer","Mutina","WuWu","Magigi","Male",45)
#database.add_admin_login1("Lecturer","Keith99!!")
#database.add_all_tables()
# database.set_fee('EB3/57373/21',20000,'2024-04-01',6000)
# check=database.student_exist('EB3/5373/21')
# if check:
#     print('found')
# database.insert_non_compliant_students('EB3/57373/21','2023-09-03','2023-09-20','2 weeks','Eating alot','reported')
# database.insert_non_compliant_students('EB3/59843/21','2024-06-02','','3 weeks','walking Here and There','absent')
#data = database.get_all_students_exams()
# print(data)
# #database.set_average('EB3/57373/21')
# data = database.get_students_marks_filtered(2024,2,'mid-term','form4')
# print(data)
#database.add_level('EB3/21702688/21',grade='form4')
# database.insert_marks('EB3/57373/21',[23,45,66,78,89,90,99,87,96,10])
#database.set_average('EB3/55555/21')
# from intasend import APIService
#
# publishable_key = "INTASEND_PUBLISHABLE_KEY"
#
# service = APIService(token=token,publishable_key=publishable_key)
#
# response = service.collect.mpesa_stk_push(phone_number=254759843995,
#                                   email="joe@doe.com", amount=10, narrative="Purchase")
# print(response)
# import requests
# from requests.auth import HTTPBasicAuth
#
# # Replace these with your actual credentials
# consumer_key = ' sTFmEBfTSz6jg0AOFuB2GoSvy3sFMSIPXBRIcDYdZGu3KfzH'
# consumer_secret = ' iiT9sSspIQHp8Po4Gvv7zIl5k1yfeGqSNZrF50IiZ7GGeDHt5R0JWlBG1mA59V4Z'
#
# api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
#
#
# response = requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
#
# if response.status_code == 200:
#     access_token = response.json()['access_token']
#     print(f"Access Token: {access_token}")
# else:
#     print(f"Failed to get access token: {response.status_code}")
#     print(f"Response Text: {response.text}")
# def truncate_table(db_path, table_name):
#     try:
#         # Connect to the SQLite database
#         conn = sqlite3.connect(db_path)
#         cursor = conn.cursor()
#
#         # Execute the DELETE statement to remove all rows
#         cursor.execute(f"DELETE FROM {table_name};")
#
#         # Optionally, reset the auto-increment counter (if applicable)
#         cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}';")
#
#         # Commit the transaction
#         conn.commit()
#
#         print(f"Table {table_name} has been truncated.")
#
#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")
#
#     finally:
#         # Close the connection
#         if conn:
#             conn.close()
#
# # Example usage
# truncate_table('student.db', 'Examinations')
# database.add_manager('kay','1234')
# database.setup_database()
# Function to insert student data and set the initial fee balance

# Add a student


# with sqlite3.connect('fees.db') as conn:
#     cursor = conn.cursor()
#     def insert_student(admission_no, first_name, last_name, total_fee):
#         cursor.execute('''
#             INSERT INTO fees (admission_no, total_fee, balance_amount)
#             VALUES (?, ?, ?)
#         ''', (admission_no, total_fee, total_fee))
#
#         conn.commit()
#         print(f"Student {first_name} {last_name} added with a fee balance of {total_fee}.")
#
# insert_student('EB3/55555/21', 'John',  'Doe', 50000)
# data = database.get_students_with_balance()
# print(data)
# database.insert_marks('EB3/57373/21',[30,50,77,99,22,66,72,99,23,50])
# database.insert_time('EB3/57373/21',2024,2,'mid-term')
# database.insert_marks('EB3/55555/21',[60,34,67,90,45,67,98,66,5,59])
# database.insert_time('EB3/55555/21',2024,2,'mid-term')
#
# database.insert_marks('EB3/57222/21',[30,50,77,99,22,66,72,99,23,50])
# database.insert_time('EB3/57222/21',2024,2,'mid-term')

# database.add_level('EB3/59843/21','form2')
# import sqlite3
#
# def add_phone_number_column(db_path, table_name):
#     # Connect to the SQLite database
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#
#     # SQL command to add a new column "phone_number"
#     alter_table_query = f'''
#     ALTER TABLE {table_name}
#     ADD COLUMN phone_number TEXT;
#     '''
#
#     try:
#         # Execute the query to add the column
#         cursor.execute(alter_table_query)
#         conn.commit()
#         print(f"'phone_number' column added successfully to the {table_name} table.")
#     except sqlite3.OperationalError as e:
#         # If the column already exists or another error occurs, catch the exception
#         print(f"An error occurred: {e}")
#     finally:
#         # Close the connection
#         conn.close()
#
# # Example usage:
# db_path = 'student.db'  # Path to your SQLite database file
# table_name = 'rest'       # Name of the table to add the column to
# add_phone_number_column(db_path, table_name)
import app2
# import sqlite3
# data=app2.view_student_marks('EB3/57373/21')
# data2 = app2.get_students()
# print(data2)
# print(data2)
# def delete_exam_records(admission_no, year, term):
#     with sqlite3.connect('student.db') as conn:
#         cursor = conn.cursor()
#
#         # SQL query to delete records based on admission_no, year, and term
#         query = '''
#             DELETE FROM Examinations
#             WHERE admission_no = ? AND year = ? AND term = ?
#         '''
#
#         # Execute the query
#         cursor.execute(query, (admission_no, year, term))
#         conn.commit()
#
#         if cursor.rowcount > 0:
#             print(f"Records for admission_no {admission_no}, year {year}, term {term} deleted successfully.")
#         else:
#             print(f"No records found for admission_no {admission_no}, year {year}, term {term}.")
# delete_exam_records('EB3/57373/21',2024,2)
# import sqlite3
# def change(admission,password):
#     with sqlite3.connect('admin.db') as conn:
#         cursor = conn.cursor()
#         cursor.execute("UPDATE logins SET position = ? WHERE password = ?", (admission, password))
#
#         conn.commit()
#
# change('Teacher','Teacher99!!')
# def create_fee():
#     with sqlite3.connect('fees.db') as conn:
#         cursor = conn.cursor()
#
#         # Create students table (if it doesn't exist)
#         cursor.execute('''
#                CREATE TABLE IF NOT EXISTS fee (
#                    term NUMBER,
#                    amount REAL DEFAULT 0
#                )
#            ''')
#         conn.commit()
#         print('fee table created successfully')
#
# create_fee()
# conn = sqlite3.connect('fees.db')
# cursor = conn.cursor()
#
# # SQL commands to add columns month1, month2, month3, month4
# columns_to_add = ['month1', 'month2', 'month3', 'month4']
# for column in columns_to_add:
#     cursor.execute(f"ALTER TABLE fee ADD COLUMN {column} TEXT")
#
# # Commit the changes and close the connection
# conn.commit()
# conn.close()
#
# print("Columns month1, month2, month3, and month4 added to table 'fee'.")
# import sqlite3

# Connect to the SQLite database
# conn = sqlite3.connect("fees.db")
# cursor = conn.cursor()
#
# # Create a new table without the specified columns
# cursor.execute('''
#     CREATE TABLE fee_new AS
#     SELECT term, amount
#     FROM fee
# ''')
#
# # Drop the original table
# cursor.execute("DROP TABLE fee")
#
# # Rename the new table to the original name
# cursor.execute("ALTER TABLE fee_new RENAME TO fee")
#
# # Commit the changes and close the connection
# conn.commit()
# conn.close()
#
# print("Columns month1, month2, month3, and month4 removed successfully.")
# with sqlite3.connect('fees.db') as conn:
#     cursor = conn.cursor()
#     def fee(term, amount, month1,month2, month3, month4):
#         cursor.execute('''
#             INSERT INTO fee (term, amount, month1,month2, month3, month4 )
#             VALUES (?, ?, ?,?, ?, ?)
#         ''', (term, amount, month1,month2, month3, month4))
#
#         conn.commit()
#         print(f"Student term, amount, month1,month2, month3, month4 added successfully.")
#
# fee (1, 0,  'January', 'February', 'March', 'April')
# fee (2, 0,  'May', 'June', 'July', 'August')
# fee (3, 0,  'September', 'October', 'November', 'December')

# import sqlite3
# from datetime import datetime

# def upsert_fee_based_on_month(db_path='fees.db'):
#     # Determine the current month
#     current_month = datetime.now().month

#     # Determine the fee based on the month
#     if current_month in [1, 2, 3, 4]:
#         current_fee = 5000
#         term = 1
#     elif current_month in [5, 6, 7, 8]:
#         current_fee = 8000
#         term = 2
#     elif current_month in [9, 10, 11, 12]:
#         current_fee = 6000
#         term = 3
#     else:
#         raise ValueError("Invalid month encountered.")

#     # Connect to the SQLite database
#     with sqlite3.connect('fees.db') as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             UPDATE current_fees SET term = ? , amount = ?
#         ''',(term, current_fee))
#         print('Data set sucessfuly')
#         conn.commit()


    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()
    #
    #
    # try:
    #     # Insert or update the record in the current_fee table
    #     cursor.execute('''
    #         INSERT INTO current_fees (term, amount) VALUES (?, ?)
    #         ON CONFLICT(term) DO UPDATE SET amount = excluded.amount
    #     ''', (term, current_fee))
    #
    #     conn.commit()
    #     print(f"Current fee for {term} set to {current_fee} based on the month.")
    # except sqlite3.Error as e:
    #     print("An error occurred:", e)
    # finally:
    #     # Close the connection
    #     conn.close()

# Run the function
# upsert_fee_based_on_month()
#database.add_all_tables()
# with sqlite3.connect('fees.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('''
#     INSERT INTO current_fees(term, amount)
#     VALUES ( 1 ,2000)
#     ''')
#     conn.commit()
# print(database.get_admission_number("KEITH","MUMO"))


# name = "keith"
# name.capitalize()
# import sqlite3

# DATABASE = 'student.db'

# def add_image_column_to_table(column_name='profile_pic', table_name='students'):
#     conn = sqlite3.connect(DATABASE)
#     cursor = conn.cursor()

#     # Add a BLOB column to store images
#     alter_table_query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} BLOB;"
#     try:
#         cursor.execute(alter_table_query)
#         print(f"Column '{column_name}' added to table '{table_name}' successfully.")
#     except sqlite3.OperationalError as e:
#         print(f"Error: {e}")
    
#     conn.commit()
#     conn.close()

# # Add an image column to the student table
# add_image_column_to_table()
# from flask import Flask, render_template, request, jsonify
# import sqlite3

# app = Flask(__name__)

# # Fetch data for a specific admission number
# def get_payment_data(admission_no):
#     conn = sqlite3.connect('fees.db')
#     cursor = conn.cursor()
#     query = '''
#         SELECT date_time, amount_paid, remaining_balance 
#         FROM payment_history
#         WHERE admission_number = ?
#         ORDER BY date_time
#     '''
#     cursor.execute(query, (admission_no,))
#     data = cursor.fetchall()
#     conn.close()

#     # Prepare data for Chart.js
#     result = {
#         "dates": [row[0] for row in data],
#         "amount_paid": [row[1] for row in data],
#         "remaining_balance": [row[2] for row in data]
#     }
#     return result

# @app.route('/')
# def index():
#     return render_template('graph.html')

# @app.route('/get_data', methods=['POST'])
# def get_data():
#     admission_no = request.json.get('admission_no')
#     data = get_payment_data(admission_no)
#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)
# import sqlite3

# def add_email_column(db_path: str, table_name: str = 'students'):
#     """Add an 'email' column to the specified table in the SQLite database."""
#     try:
#         # Connect to the database
#         conn = sqlite3.connect(db_path)
#         cursor = conn.cursor()

#         # Check if the column already exists
#         cursor.execute(f"PRAGMA table_info({table_name})")
#         columns = [column[1] for column in cursor.fetchall()]
        
#         if 'email' not in columns:
#             # Add the 'email' column to the table
#             cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN email TEXT")
#             conn.commit()
#             print("Column 'email' added successfully.")
#         else:
#             print("Column 'email' already exists.")

#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")

#     finally:
#         conn.close()

# # Example usage
# add_email_column('student.db', 'students')
# import sqlite3

# def insert_email(db_path: str, phone: str, admission_no: str):
#     try:
#         conn = sqlite3.connect(db_path)
#         cursor = conn.cursor()
        
#         # Insert or update the email where admission_no matches
#         cursor.execute("UPDATE rest SET phone_number = ? WHERE admission_no = ?", (phone, admission_no))
        
#         if cursor.rowcount == 0:
#             print("No matching admission number found.")
#         else:
#             print("Phone updated successfully.")
        
#         conn.commit()
#     except sqlite3.Error as e:
#         print(f"Database error: {e}")
#     finally:
#         conn.close()

# # Example usage:
# insert_email('student.db', '0759843995', 'EB3/57373/21')
# def insert_image(db_path: str, admission_no: str, image_path: str):
#     try:
#         conn = sqlite3.connect(db_path)
#         cursor = conn.cursor()
        
#         # Read the image file as binary
#         with open(image_path, 'rb') as file:
#             image_data = file.read()
        
#         # Update the image where admission_no matches
#         cursor.execute("UPDATE students SET profile_pic = ? WHERE admission_no = ?", (image_data, admission_no))
        
#         if cursor.rowcount == 0:
#             print("No matching admission number found.")
#         else:
#             print("Image inserted successfully.")
        
#         conn.commit()
#     except sqlite3.Error as e:
#         print(f"Database error: {e}")
#     except FileNotFoundError:
#         print("Image file not found.")
#     finally:
#         conn.close()

# # Example usage:
# insert_image('student.db', 'EB3/57373/21', 'cartoon.jpg')
# with sqlite3.connect('fees.db') as conn:
#     cursor = conn.cursor()

#     # Check if column 'id_number' already exists
#     cursor.execute("PRAGMA table_info(admin_data);")
#     columns = [column[1] for column in cursor.fetchall()]

#     if "method_id" not in columns:
#         cursor.execute('ALTER TABLE payment_history ADD COLUMN method_of_payment TEXT')
#         cursor.execute('ALTER TABLE payment_history ADD COLUMN method_id TEXT')
#         conn.commit()
#         print('Method of payment added successfully.')
#     else:
#         print('Column "id_number" already exists.')
# import sqlite3

# # Connect to the database
# db_path = "admin.db"  # Ensure this is the correct path
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()

# # Enable Foreign Key Support
# cursor.execute("PRAGMA foreign_keys = ON;")

# # Create teachers table if not exists
# cursor.execute("DROP TABLE IF EXISTS logins")
# cursor.execute("DROP TABLE IF EXISTS admin_data_new")

# # Create new admin_data table with foreign key constraint
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS logins(
#     position TEXT ,
#     password TEXT,
#     FOREIGN KEY (position) REFERENCES teachers (username) ON DELETE CASCADE
# );
# """)

# # Copy data from old table if it exists


# # Drop old table and rename the new one



# # Commit and close connection
# conn.commit()
# conn.close()

# print("Foreign key added successfully!")
# import sqlite3

# conn = sqlite3.connect('payments.db')
# cursor = conn.cursor()
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS transactions (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     phone TEXT,
#     amount REAL,
#     mpesa_receipt TEXT,
#     transaction_date TEXT,
#     status TEXT
# )

# ''')
# conn.commit()
# conn.close()

# import sqlite3

# # Connect to the SQLite database
# conn = sqlite3.connect("student.db")  # Replace with your actual database name
# cursor = conn.cursor()

# # Query to fetch all emails from the students table
# cursor.execute("SELECT email FROM students")

# # Fetch all results and extract emails as a list
# emails = [row[0] for row in cursor.fetchall()]



# # Print or use the email list
# print(emails)

# # Close the connection
# conn.close()
# import sqlite3

# def get_student_emails(db_name, tableName, colName):
#     try:
#         # Connect to the database
#         conn = sqlite3.connect(db_name)
#         cursor = conn.cursor()

#         # Execute query to fetch all emails
#         cursor.execute(f"SELECT {colName} FROM {tableName}")
#         emails = [row[0] for row in cursor.fetchall()]

#         # Close the connection
#         conn.close()

#         return emails
#     except sqlite3.Error as e:
#         print(f"Database error: {e}")
#         return []

# # Example usage
# emails_list = get_student_emails('student.db','students','email')

# if 'richardkeith233@gmail.com' in emails_list:
#     print("wow found")
# else:
#     print("not found")

# with sqlite3.connect('manager.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('ALTER TABLE manager ADD COLUMN email TEXT')
#     conn.commit()
#     print("email column added successfully")

# import sqlite3

# def get_password(db_name, email):
#     try:
#         # Connect to the SQLite database
#         conn = sqlite3.connect(db_name)
#         cursor = conn.cursor()

#         # Query to fetch the password for the given username
#         cursor.execute('''SELECT logins.password 
#         FROM logins
#         JOIN teachers ON  students.admission_no = logins.position
#         WHERE students.email = ?''', (email,))
#         result = cursor.fetchone()

#         # Close the connection
#         conn.close()

#         # Return the password if found, otherwise return None
#         return result[0] if result else None
#     except sqlite3.Error as e:
#         print(f"Database error: {e}")
#         return None

# # Example usage
# username = "student.db"  # Replace with the actual username
# email = "richardkeith233@gmail.com"
# password = get_password('student.db',email)
# print(f"Password for {username}: {password}" if password else "User not found")
# import sqlite3

# def add_profile_picture_column(db_name="student.db"):
#     """Adds a profile_picture column to the users table if it does not exist."""
#     try:
#         # Connect to the database
#         conn = sqlite3.connect(db_name)
#         cursor = conn.cursor()

#         # Add the column if it does not already exist
        
#         cursor.execute("ALTER TABLE rest ADD COLUMN admission_date TEXT")
#         conn.commit()
#         print("Column 'admission_date' added successfully.")
       
#         # Close the connection
#         conn.close()
#     except sqlite3.Error as e:
#         print(f"Database error: {e}")
# add_profile_picture_column()

# import sqlite3

# def insert_profile_picture(user_id, image_path, db_name="admin.db"):
#     """Inserts an image as a profile picture for a user in the SQLite database."""
#     try:
#         # Read the image file as binary
#         with open(image_path, "rb") as file:
#             image_data = file.read()
        
#         # Connect to the database
#         conn = sqlite3.connect(db_name)
#         cursor = conn.cursor()

#         # Update the profile_picture column for the given user_id
#         cursor.execute("UPDATE admin_data SET profile_picture = ? WHERE position = ?", (image_data, user_id))
#         conn.commit()
#         print("Profile picture updated successfully.")

#         # Close the connection
#         conn.close()
#     except sqlite3.Error as e:
#         print(f"Database error: {e}")
#     except FileNotFoundError:
#         print("Image file not found.")

# # Example usage
# insert_profile_picture('kay', 'cartoon.jpg')  # Replace 1 with the actual user ID and "profile.jpg" with the image path
# {% extends "admin_dashboard.html" %}
# {% block content %}
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

#         /* General Styling */
#         body {
#             font-family: 'Poppins', sans-serif;
#             background-color: #eef1f7;
#             text-align: center;
#             padding: 20px;
#         }

#         h1 {
#             color: #333;
#             font-size: 28px;
#             margin-bottom: 20px;
#         }

#         /* Form Container */
#         .form-container {
#             background: white;
#             padding: 30px;
#             max-width: 750px;
#             margin: auto;
#             border-radius: 10px;
#             box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.15);
#         }

#         /* Table Styling */
#         table {
#             width: 100%;
#             border-collapse: collapse;
#             margin-top: 20px;
#         }

#         th, td {
#             padding: 14px;
#             text-align: left;
#             border-bottom: 1px solid #ddd;
#         }

#         th {
#             background-color: #007bff;
#             color: white;
#             text-transform: uppercase;
#         }

#         td {
#             background-color: #f9f9f9;
#         }

#         /* Select Dropdown Styling */
#         select {
#             width: 100%;
#             padding: 12px;
#             font-size: 16px;
#             border: 1px solid #ccc;
#             border-radius: 6px;
#             outline: none;
#             transition: all 0.3s ease-in-out;
#             background: white;
#         }

#         select:focus {
#             border-color: #007bff;
#             box-shadow: 0 0 10px rgba(0, 123, 255, 0.25);
#         }

#         /* Submit Button */
#         .submit-container {
#             text-align: center;
#             margin-top: 25px;
#         }

#         .submit-container input[type="submit"] {
#             padding: 14px 30px;
#             background: linear-gradient(to right, #007bff, #0056b3);
#             border: none;
#             border-radius: 6px;
#             color: white;
#             font-size: 18px;
#             font-weight: bold;
#             cursor: pointer;
#             transition: all 0.3s ease-in-out;
#         }

#         .submit-container input[type="submit"]:hover {
#             background: linear-gradient(to right, #0056b3, #003f7f);
#             transform: scale(1.05);
#         }

#         /* Responsive Design */
#         @media screen and (max-width: 600px) {
#             .form-container {
#                 width: 90%;
#                 padding: 20px;
#             }
#             select {
#                 font-size: 14px;
#             }
#         }
#     </style>

#     <div class="form-container">
#         <h1>Select Student Details</h1>

#         <form action="/students" method="post">
#             <table>
#                 <tr>
#                     <th>Year</th>
#                     <th>Term</th>
#                     <th>Type</th>
#                     <th>Class</th>
#                 </tr>
#                 <tr>
#                     <td>
#                         <select name="year" required id="yearDropdown">
#                             <option value="">Select Year</option>
#                         </select>
#                     </td>
#                     <td>
#                         <select name="term" required>
#                             <option value="">Select Term</option>
#                             <option value="1">Term 1</option>
#                             <option value="2">Term 2</option>
#                             <option value="3">Term 3</option>
#                         </select>
#                     </td>
#                     <td>
#                         <select name="type" required>
#                             <option value="">Select Type</option>
#                             <option value="opener">Opener</option>
#                             <option value="mid-term">Mid-Term</option>
#                             <option value="end-term">End-Term</option>
#                             <option value="mock">Mock</option>
#                             <option value="trial1">Trial 1</option>
#                             <option value="trial2">Trial 2</option>
#                             <option value="trial">Trial</option>
#                             <option value="other">Other</option>
#                         </select>
#                     </td>
#                     <td>
#                         <select name="class" required>
#                             <option value="">Select Class</option>
#                             <option value="play_group1">PP1</option>
#                             <option value="play_group2">PP2</option>
#                             <option value="grade1">Grade 1</option>
#                             <option value="grade2">Grade 2</option>
#                             <option value="grade3">Grade 3</option>
#                             <option value="grade4">Grade 4</option>
#                             <option value="grade5">Grade 5</option>
#                             <option value="grade6">Grade 6</option>
#                             <option value="form1">Form 1</option>
#                             <option value="form2">Form 2</option>
#                             <option value="form3">Form 3</option>
#                             <option value="form4">Form 4</option>
#                             <option value="form5">Form 5</option>
#                             <option value="form6">Form 6</option>
#                         </select>
#                     </td>
#                 </tr>
#             </table>

#             <div class="submit-container">
#                 <input type="submit" value="Submit">
#             </div>
#         </form>
#     </div>

#     <script>
#         // Function to populate year dropdown dynamically
#         function populateYearDropdown() {
#             let yearDropdown = document.getElementById("yearDropdown");
#             let currentYear = new Date().getFullYear();

#             for (let year = currentYear - 5; year <= currentYear + 10; year++) {
#                 let option = document.createElement("option");
#                 option.value = year;
#                 option.textContent = year;
#                 yearDropdown.appendChild(option);
#             }
#         }

#         // Call function on page load
#         document.addEventListener("DOMContentLoaded", populateYearDropdown);
#     </script>
# {% endblock %}
    # <!-- <script>
    #     // Student scores data from the server
    #     const studentScores = {{ exam_scores | safe }};

    #     // X-axis labels
    #     const terms = ['Term 1 Exam 1', 'Term 1 Exam 2', 'Term 1 Exam 3',
    #                    'Term 2 Exam 1', 'Term 2 Exam 2', 'Term 2 Exam 3',
    #                    'Term 3 Exam 1', 'Term 3 Exam 2', 'Term 3 Exam 3'];

    #     // Create datasets for each year with data
    #     const datasets = Object.keys(studentScores).map(year => ({
    #         label: `Year ${year}`,
    #         data: studentScores[year] || Array(9).fill(null),  // Fill with null if no data for that term
    #         fill: false,
    #         borderColor: getRandomColor(),
    #         tension: 0.1
    #     }));

    #     // Function to generate random colors for the lines
    #     function getRandomColor() {
    #         const letters = '0123456789ABCDEF';
    #         let color = '#';
    #         for (let i = 0; i < 6; i++) {
    #             color += letters[Math.floor(Math.random() * 16)];
    #         }
    #         return color;
    #     }

    #     // Create the chart
    #     const ctx = document.getElementById('studentScoresChart').getContext('2d');
    #     const studentScoresChart = new Chart(ctx, {
    #         type: 'line',
    #         data: {
    #             labels: terms,
    #             datasets: datasets
    #         },
    #         options: {
    #             responsive: true,
    #             plugins: {
    #                 legend: {
    #                     position: 'top',
    #                 },
    #                 title: {
    #                     display: true,
    #                     text: '{{ student_id }} Scores Over the Years'
    #                 }
    #             },
    #             scales: {
    #                 x: {
    #                     title: {
    #                         display: true,
    #                         text: 'Examinations'
    #                     },
    #                     ticks: {
    #                         maxRotation: 45,
    #                         minRotation: 45
    #                     }
    #                 },
    #                 y: {
    #                     title: {
    #                         display: true,
    #                         text: 'Scores'
    #                     },
    #                     beginAtZero: false
    #                 }
    #             }
    #         }
    #     });
    # </script> -->
# import database
# print(database.get_exam_type("EB3/57373/21"))