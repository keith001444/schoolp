import sqlite3
from flask import request
def profile(admission_no):
      # Get admission number from query parameter

    conn = sqlite3.connect("fees.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM payment_history LIMIT 1")
    student = cursor.fetchone()

    if not student:
        return "No student found in the database."

    cursor.execute("SELECT date_time, amount_paid, remaining_balance FROM payment_history WHERE admission_number = ? ORDER BY date_time", (admission_no,))
    payments = cursor.fetchall()

    conn.close()

    dates = [payment[0] for payment in payments]
    amounts = [payment[1] for payment in payments]
    remaining_balance = [payment[2] for payment in payments]

    return dates,amounts,remaining_balance
