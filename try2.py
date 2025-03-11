from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def profile():
    admission_no = request.args.get('admission_no', '')  # Get admission number from query parameter

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

    return render_template('graph2.html', dates=dates, amounts=amounts, remaining_balance=remaining_balance)

if __name__ == '__main__':
    app.run(debug=True)
