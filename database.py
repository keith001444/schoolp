import sqlite3
import document_functions


#---------------------------------Create Table--------------------------------------------------#

#---Create Admin Logins
def add_admin_login():
    with sqlite3.connect('admin.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS logins(
            position TEXT,
            password TEXT
        )
        ''')
        conn.commit()

#----------------current fees table
def current_fees():
    with sqlite3.connect('fees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS current_fees(
            term NUMBER,
            amount REAL
        )
        ''')
        conn.commit()

#===Create manager logins table
def add_manager_login():
    with sqlite3.connect('manager.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS logins(
            username TEXT,
            password TEXT
        )
        ''')
        conn.commit()

def add_manager(username, password):
    with sqlite3.connect('manager.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO logins (
               username,
               password
                ) VALUES (?, ?)
            ''', (username, password))
        conn.commit()


#---Create Admin Details ----------
def add_admin_data():
    with sqlite3.connect('admin.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS data_admin(
            admin_id TEXT PRIMARY KEY,
            position TEXT,
            f_name TEXT,
            m_name TEXT,
            l_name TEXT,
            gender NUMBER,
            age NUMBER
        )
        ''')
        conn.commit()


#create table students

def init_student_add_name():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students(
             admission_no TEXT PRIMARY KEY, 
             first_name TEXT,
             middle_name TEXT,
             last_name TEXT,
             gender TEXT,
             AGE INTEGER
        )
        ''')
        conn.commit()


#create rest table that contains the rest of the student data
def init_student_add_level():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS rest(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admission_no TEXT,
            Grade TEXT,
            FOREIGN KEY (admission_no) REFERENCES students (admission_no)
        )
        ''')
        conn.commit()


#Add subjects per student
subject = ['Mathematics', 'Biology', 'Chemistry', 'Physics', 'Geography', 'Business',
           'English', 'Kiswahili', 'CRE', 'French']


#Add Logins Table
def init_logins():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS logins(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admission_no TEXT,
            password TEXT,
            FOREIGN KEY (admission_no) REFERENCES students (admission_no)
        )
        ''')
        conn.commit()


#-------------------------------Get Details From The DataBase-----------------------------------#
#get First name
def get_first_name(admission_no):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT first_name
            FROM students
            WHERE admission_no = ?
        ''', (admission_no,))

        result = cursor.fetchone()
    if result:
        return result[0]  # Return the first name
    else:
        return None


def get_middle_name(admission_no):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT middle_name
            FROM students
            WHERE admission_no = ?
        ''', (admission_no,))

        result = cursor.fetchone()
    if result:
        return result[0]  # Return the middle name
    else:
        return None


def get_last_name(admission_no):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT last_name
            FROM students
            WHERE admission_no = ?
        ''', (admission_no,))

        result = cursor.fetchone()
    if result:
        return result[0]  # Return the last name
    else:
        return None

def get_email(admission_no):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT email
            FROM students
            WHERE admission_no = ?
        ''',(admission_no,))
        result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def get_phone(admission_no):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT email
            FROM students
            WHERE admission_no = ?
        ''',(admission_no,))
        result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

def get_gender(admission_no):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT gender
            FROM students
            WHERE admission_no = ?
        ''',(admission_no,))
        result = cursor.fetchone()
    if result:
        return result[0]
    else:
        return None

import sqlite3
import base64

def get_profile(admission_no: str) -> str:
    try:
        conn = sqlite3.connect('student.db')
        cursor = conn.cursor()
        cursor.execute("SELECT profile_pic FROM students WHERE admission_no = ?", (admission_no,))
        result = cursor.fetchone()
        
        if result and result[0]:
            # Convert binary data to base64
            base64_image = base64.b64encode(result[0]).decode('utf-8')
            return f"data:image/png;base64,{base64_image}"
        else:
            print("No image found for the given admission number.")
            return None
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()





#---------Get
def view_students():
    # Connect to the SQLite database
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    # Fetch all students
    cursor.execute("SELECT admission_no, first_name, last_name FROM students")
    students = cursor.fetchall()
    processed_students = [
        (document_functions.replace_slash_with_dot(student[0]), student[1].capitalize(), student[2].capitalize())
        for student in students
    ]
    # Close the connection
    conn.close()
    return processed_students


#-----------Get Students and Their Marks

def get_students_and_subjects():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()

        # Query to select first_name, last_name, and all subjects for each student
        query = '''
        SELECT s.first_name, s.last_name, sub.*
        FROM students s
        INNER JOIN subjects sub ON s.admission_no = sub.admission_no 
        ORDER BY sub.average
        '''

        cursor.execute(query)
        result = cursor.fetchall()

    return result


#-------------------------------Put Data To Database-------------------------------------------#
#Enter data To Students table
def add_someone(admission_no, f_name, m_name, l_name, gender, age, email):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO students (
            admission_no,
            first_name,
            middle_name,
            last_name,
            gender,
            AGE,
            email
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (admission_no, f_name, m_name, l_name, gender, age, email))
        conn.commit()


#-----Add details to logins table Admin
def add_admin_login1(position, password):
    with sqlite3.connect('admin.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO logins(position,password
        )VALUES (?,?)
        ''', (position, password))
        conn.commit()


#-------------add full admin details
def add_admin_data1(position, f_name, m_name, l_name, gender, age):
    with sqlite3.connect('admin.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO admin_data(
            position,
             f_name,
             m_name,
             l_name,
             gender,
             age
                ) VALUES (?, ?,?,?,?,?)
            ''', (position.capitalize(), f_name.capitalize(), m_name.capitalize(), l_name.capitalize(), gender.capitalize(), age))
        conn.commit()


def add_login(admission_no, password):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO logins (
            admission_no,
            password
                ) VALUES (?, ?)
            ''', (admission_no, password))
        conn.commit()


#add details rest table Contains the Class of the student
def add_level(admission_no, grade, phone):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO rest(
            admission_no,
            Grade,
            phone_number
                ) VALUES (?, ?, ?)
            ''', (admission_no, grade, phone))
        conn.commit()


#=================insert Marks of Each Student

def insert_marks(year,time,exam_type,admission_no, marks_list):
    if len(marks_list) != len(subject):
        raise ValueError("Marks list length must match the number of subjects.")

    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()

        # Build the SQL query dynamically based on the subjects
        query =  f'''
            UPDATE Examinations
            SET {', '.join([f"{subj} = ?" for subj in subject])}
            WHERE admission_no = ? AND year = ? AND term = ? AND type = ?
        '''
        # Execute the query with admission_no followed by marks list
        cursor.execute(query, ( *marks_list,admission_no,year,time,exam_type))
        conn.commit()
def insert_time(admission_no,year, term, exam_type):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        query = '''
                INSERT INTO Examinations (admission_no,year,term,type) 
                VALUES ( ?, ?, ?, ?)
                '''
        cursor.execute(query, (admission_no,year,term,exam_type))
        conn.commit()
#remove data from the database


def remove_student_login(admission_no):
    # Connect to the SQLite database
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()

        # Define the SQL query with a parameter placeholder
        query = '''
            DELETE FROM logins WHERE admission_no = ?
        '''

        # Execute the query with the admission number as the parameter
        cursor.execute(query, (admission_no,))

        # Commit the transaction to make sure the deletion is saved
        conn.commit()


def remove_student_details(admission_no):
    """
    Removes a student login record from the 'logins' table in the database
    based on the given admission number.

    Parameters:
        admission_no (str): The admission number of the student whose login record should be removed.
    """
    # Connect to the SQLite database
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()

        # Define the SQL query with a parameter placeholder
        query = '''
            DELETE FROM students WHERE admission_no = ?
        '''

        # Execute the query with the admission number as the parameter
        cursor.execute(query, (admission_no,))

        # Commit the transaction to make sure the deletion is saved
        conn.commit()


def remove_student_subjects(admission_no):
    """
    Removes a student login record from the 'logins' table in the database
    based on the given admission number.

    Parameters:
        admission_no (str): The admission number of the student whose login record should be removed.
    """
    # Connect to the SQLite database
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()

        # Define the SQL query with a parameter placeholder
        query = '''
            DELETE FROM subjects WHERE admission_no = ?
        '''

        # Execute the query with the admission number as the parameter
        cursor.execute(query, (admission_no,))

        # Commit the transaction to make sure the deletion is saved
        conn.commit()


#--------------Remove all data from a student----------------------------
def delete_student(admission_no):
    remove_student_details(admission_no)
    remove_student_subjects(admission_no)
    remove_student_login(admission_no)


#==============================Exams Table=================================================#

def init_exams_table():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        create_table_query = '''
                CREATE TABLE IF NOT EXISTS Examinations(
            admission_no TEXT,
            year number,
            term number,
            type TEXT,
            
        '''
        for i in range(len(subject)):
            create_table_query += f'{subject[i]} REAL, '

        create_table_query += '''
            FOREIGN KEY (admission_no) REFERENCES students (admission_no)
        )
        '''

        # Execute the final query
        cursor.execute(create_table_query)
        conn.commit()


#===================Student Fees Table
def fee_table():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS fees_student(
            admission_no TEXT,
            pay REAL,
            payday DATETIME,
            balance REAL,
            FOREIGN KEY (admission_no) REFERENCES students (admission_no)
        )
        ''')
        conn.commit()


def default_fee():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS fees(
            term NUMBER,
            amount REAL
        )
        ''')
        conn.commit()

def set_fee(admission_no,pay,payday,balance):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO fees_student (
            admission_no,
            pay,
            payday,
            balance
                ) VALUES (?, ?, ?, ?)
            ''', (admission_no, pay,payday,balance))
        conn.commit()


#==============Non Compliant Students
def add_non_compliant_students():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS non_compliant(
            admission_no TEXT,
            send_date TIMESTAMP,
            return_date TIMESTAMP,
            duration TEXT,
            reason TEXT,
            status TEXT,
            FOREIGN KEY (admission_no) REFERENCES students (admission_no)
        )
        ''')
        conn.commit()

def insert_non_compliant_students(admission_no, send_date,return_date,duration,reason,status):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
                INSERT INTO non_compliant(
                    admission_no ,
                    send_date,
                    return_date,
                    duration,
                    reason,
                    status
                    
                   
                )  VALUES (?, ?, ?, ?,?,?)
            ''', (admission_no, send_date,return_date,duration,reason.capitalize(),status))
        conn.commit()


#=============View All Non Compliant Students
def non_compliant_students():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT students.admission_no, students.first_name, students.last_name, non_compliant.reason,non_compliant.duration,non_compliant.send_date,non_compliant.return_date,non_compliant.status
            FROM students
            INNER JOIN non_compliant ON students.admission_no = non_compliant.admission_no 
        ''')
        result = cursor.fetchall()
        # Process the result to replace slashes with dots
        processed_results = [
            (document_functions.replace_slash_with_dot(res[0]), res[1].capitalize(), res[2].capitalize(), res[3].capitalize(), res[4], res[5], res[6], res[7])
            for res in result
        ]
        # Close the connection
        return processed_results

def add_ill_students():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ill_students(
            admission_no TEXT,
            sick TEXT,
            description TEXT
        )
        ''')
        conn.commit()

def put_ill_students(admission_no,sick,description):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        if sick:
            cursor.execute('''
            INSERT INTO ill_students(
                admission_no,sick,description
            )VALUES (?, ?, ?)
            ''', (admission_no,sick.capitalize(),description.capitalize()))
            conn.commit()

def get_ill_students():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT students.admission_no, students.first_name, students.last_name, ill_students.sick, ill_students.description
        FROM students
        INNER JOIN ill_students ON students.admission_no = ill_students.admission_no
        ''')
        result = cursor.fetchall()
        # Process the result to replace slashes with dots
        processed_results = [
            (document_functions.replace_slash_with_dot(res[0]), res[1].capitalize(), res[2].capitalize(), res[3].capitalize(), res[4])
            for res in result
        ]
        # Close the connection
        return processed_results
#======================Manager Database=======================
def add_Manager_details():
    with sqlite3.connect('manager.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS manager(
            manager_id TEXT PRIMARY KEY,
            f_name TEXT,
            m_name TEXT,
            l_name TEXT,
            position TEXT
        )
        ''')
        conn.commit()

#====================
def get_students_with_balance():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute("ATTACH DATABASE 'fees.db' AS feesdb")

        # Query to fetch students with balance > 0
        query = """
            SELECT s.admission_no, s.first_name, s.middle_name, s.last_name, f.remaining_balance
            FROM students s
            JOIN feesdb.students f ON s.admission_no = f.admission_number
            WHERE f.remaining_balance > 0
            ORDER BY f.remaining_balance DESC
        """

        cursor.execute(query)
        students_with_balance = cursor.fetchall()
        return students_with_balance

# check if admission exists
def student_exist(admission_no):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE admission_no = ?", (admission_no,))
        existing_student = cursor.fetchone()
        return existing_student

#============average Table
def average_table():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS average(
            admission_no TEXT,
            average REAL,
            FOREIGN KEY (admission_no) REFERENCES students (admission_no)
        ) 
        ''')
        conn.commit()

def add_column_average():
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
        ALTER TABLE Examinations
        ADD COLUMN average DECIMAL(5,2);
        """)
        conn.commit()

def get_all_students_exams():
    query_template = '''
            SELECT students.admission_no, students.first_name, {subjects}, Examinations.average
    
        FROM students
        JOIN Examinations ON students.admission_no = Examinations.admission_no
        ORDER BY Examinations.average
    '''

    subject_columns = ', '.join([f'Examinations.{subj}' for subj in subject])
    query = query_template.format(subjects=subject_columns)

    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()

    return result


def set_average(admission_no,term,year,exam_type):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()

        query = """
            SELECT ROUND(
                (Mathematics + Biology + Chemistry + Physics + Geography + Business +
                English + Kiswahili + CRE + French) / 10.0, 2) AS avg_marks
            FROM Examinations
            WHERE admission_no = ? AND term = ? AND year = ? AND type = ?
        """

        # Execute the query with the admission_no parameter correctly passed as a tuple
        cursor.execute(query, (admission_no,term,year,exam_type))

        # Fetch the result if you need to do something with the calculated average
        avg_marks = cursor.fetchone()[0]  # Fetch the average from the result

        query2 = '''
        UPDATE Examinations SET average = ? WHERE admission_no = ? AND term = ? AND year = ? AND type = ? 
        '''
        cursor.execute(query2,(avg_marks,admission_no,term,year,exam_type))

        conn.commit()

        # No need to call conn.commit() since no changes are made to the database


# Example usage:
# set_average('EB3/57373/21')
def get_students_marks_filtered(year,term,exam_type,grade):
    query_template = '''
            SELECT students.admission_no, students.first_name, {subjects}, Examinations.average
            FROM students
            JOIN Examinations ON students.admission_no = Examinations.admission_no
            JOIN rest ON Examinations.admission_no = rest.admission_no
            WHERE Examinations.year = ? AND Examinations.term = ? AND Examinations.type = ? AND rest.grade = ?
            
        '''

    subject_columns = ', '.join([f'Examinations.{subj}' for subj in subject])
    query = query_template.format(subjects=subject_columns)

    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query,(year,term,exam_type,grade))
        result = cursor.fetchall()
    return result
def setup_database():
    conn = sqlite3.connect('fees.db')
    cursor = conn.cursor()

    # Create students table (if it doesn't exist)

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS students (
            admission_number TEXT PRIMARY KEY,
            total_paid REAL DEFAULT 0,
            remaining_balance REAL DEFAULT {document_functions.current_fee()}
        )
    ''')

    # Create payment history table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payment_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admission_number TEXT,
            amount_paid REAL,
            remaining_balance REAL,
            date_time TEXT,
            FOREIGN KEY (admission_number) REFERENCES students(admission_number)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fees (
            admission_no TEXT,
            total_fee REAL,
            paid_amount REAL DEFAULT 0,
            balance_amount REAL DEFAULT 0,
            last_payment_date TEXT,
            FOREIGN KEY (admission_no) REFERENCES students(admission_no)
        )
    ''')



    conn.commit()
    conn.close()

#==============Fee Processing
def current_fee():
    with sqlite3.connect('fees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
         SELECT term, amount FROM current_fee
        )
        ''')
        data = cursor.fetchone()
        return data

#======================================================================
def fee_data():
    with sqlite3.connect('fees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM fee
        ''')
        fee_details = cursor.fetchall()
    return fee_details
#====================================================================
def get_admission_number(first_name, last_name):
    with sqlite3.connect('student.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT admission_no FROM students
        WHERE first_name = ? 
        AND last_name = ?
        ''',(first_name.upper(), last_name.upper()))
        admission_number = cursor.fetchone()[0]
    return admission_number
def teachers():
    conn = sqlite3.connect('admin.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            phone TEXT,
            grade TEXT,
            subject TEXT,
            date TEXT
        )
    ''')
    conn.commit()
    conn.close()





def add_all_tables():
    current_fees()
    add_admin_login()
    add_admin_data()
    init_logins()
    init_student_add_level()
    init_student_add_name()
    init_exams_table()
    fee_table()
    default_fee()
    add_ill_students()
    add_Manager_details()
    add_admin_data()
    add_non_compliant_students()
    setup_database()
    teachers()
