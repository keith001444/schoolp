from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import base64
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Database configuration
DATABASE = 'database.db'


# Ensure tables exist
def create_tables():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create Student table with profile_pic as BLOB
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        profile_pic BLOB,
        birth_date TEXT,
        gender TEXT,
        email TEXT,
        join_date TEXT
    )
    ''')

    # Create FeePayment table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fee_payment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        amount REAL,
        FOREIGN KEY (student_id) REFERENCES student (id)
    )
    ''')

    conn.commit()
    conn.close()


create_tables()


@app.route('/')
def profile():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM student LIMIT 1")
    student = cursor.fetchone()

    if not student:
        return "No student found in the database."

    cursor.execute("SELECT date, amount FROM fee_payment WHERE student_id = ?", (student[0],))
    payments = cursor.fetchall()

    conn.close()

    dates = [payment[0] for payment in payments]
    amounts = [payment[1] for payment in payments]

    # Convert BLOB to base64 for rendering only if data is of bytes type
    profile_pic_data = None
    if student[2] and isinstance(student[2], bytes):
        profile_pic_data = base64.b64encode(student[2]).decode('utf-8')

    return render_template('profile.html', student=student, dates=dates, amounts=amounts, profile_pic_data=profile_pic_data)


@app.route('/upload', methods=['POST'])
def upload_profile_pic():
    if 'profile_pic' not in request.files:
        return 'No file part'

    file = request.files['profile_pic']
    if file.filename == '':
        return 'No selected file'

    if file:
        # Read the image as binary data (BLOB)
        file_data = file.read()

        # Update the database with the BLOB data using sqlite3.Binary
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("UPDATE student SET profile_pic = ? WHERE id = ?", (sqlite3.Binary(file_data), 1))
        conn.commit()
        conn.close()

        return redirect(url_for('profile'))

    return 'File upload failed'


if __name__ == '__main__':
    app.run(debug=True)
