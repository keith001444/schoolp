import sqlite3

DATABASE = 'database.db'

# Establish a connection to the database
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Create the student table
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    profile_pic TEXT,
    birth_date TEXT,
    gender TEXT,
    email TEXT,
    join_date TEXT
)
''')

# Create the fee_payment table
cursor.execute('''
CREATE TABLE IF NOT EXISTS fee_payment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    date TEXT,
    amount REAL,
    FOREIGN KEY (student_id) REFERENCES student (id)
)
''')

# Insert sample data
cursor.execute('''
INSERT INTO student (name, profile_pic, birth_date, gender, email, join_date) VALUES 
('John Doe', 'profile_pic.png', '2000-01-01', 'Male', 'john@example.com', '2018-09-01')
''')

cursor.executemany('''
INSERT INTO fee_payment (student_id, date, amount) VALUES (?, ?, ?)
''', [
    (1, '2023-01-01', 500.0),
    (1, '2023-02-01', 400.0),
    (1, '2023-03-01', 600.0),
    (1, '2023-04-01', 700.0)
])

conn.commit()
conn.close()

print('Database created and sample data inserted successfully.')

