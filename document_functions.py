import sqlite3
from datetime import datetime
import pytz



# Define the timezone for Nairobi
nairobi_tz = pytz.timezone('Africa/Nairobi')

# Get the current time in Nairobi
nairobi_time = datetime.now()

def greet_based_on_time():
    current_hour = nairobi_time.hour + 3

    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"

def greet():
    pass
def copyright_updater():
    current_year = nairobi_time.year
    return current_year


# Example usage
def replace_slash_with_dot(input_string):
    return input_string.replace('/', '.')
def replace_slash_with_slash(input_string):
    return input_string.replace('.', '/')
def current_fee():
    with sqlite3.connect('fees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT amount FROM current_fees
        ''')
        fee=cursor.fetchone()
    return fee[0]


def c_fee():
    with sqlite3.connect('fees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT amount FROM fee
        ''')
        data = cursor.fetchall()
    with sqlite3.connect('fees.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT term FROM fee
        ''')
        terms = cursor.fetchall()
        # ===Determine the current time
        current_month = datetime.now().month

        # Determine the fee based on the month
        if current_month in [1, 2, 3, 4]:
            current_fee = data[0][0]
            term = terms[0][0]
        elif current_month in [5, 6, 7, 8]:
            current_fee = data[1][0]
            term = terms[1][0]
        elif current_month in [9, 10, 11, 12]:
            current_fee = data[2][0]
            term = terms[2][0]
        else:
            raise ValueError("Invalid month encountered.")

        # Connect to the SQLite database
        with sqlite3.connect('fees.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE current_fees SET term = ? , amount = ?
            ''', (term, current_fee))
            print('Data set sucessfuly')
            conn.commit()

    with sqlite3.connect('fees.db') as conn:
        cursor = conn.cursor()

        # Get the fee for the current term
        cursor.execute('SELECT amount FROM current_fees')
        fees = cursor.fetchone()
    return fees[0]