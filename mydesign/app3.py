# app.py
from flask import Flask, request, jsonify, render_template, redirect, url_for
import base64
import cv2
import numpy as np
import face_recognition
import sqlite3
import io

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, face_encoding BLOB)')
    conn.close()

create_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    image_bytes = base64.b64decode(image_data)
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    face_locations = face_recognition.face_locations(img)
    if not face_locations:
        return jsonify({'success': False, 'message': 'No face detected.'})

    face_encodings = face_recognition.face_encodings(img, face_locations)
    if not face_encodings:
        return jsonify({'success': False, 'message': 'No face encodings found.'})

    unknown_face_encoding = face_encodings[0]

    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    for user in users:
        known_face_encoding = np.frombuffer(user['face_encoding'])
        known_face_encoding = known_face_encoding.reshape((128,))
        results = face_recognition.compare_faces([known_face_encoding], unknown_face_encoding, tolerance=0.5) #lower tolerance for stricter matching.
        if results[0]:
            return jsonify({'success': True, 'message': f'Welcome, {user["username"]}!'})

    return jsonify({'success': False, 'message': 'Access Denied.'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    image_bytes = base64.b64decode(image_data)
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    username = data['username']

    face_locations = face_recognition.face_locations(img)
    if not face_locations:
        return jsonify({'success': False, 'message': 'No face detected.'})

    face_encodings = face_recognition.face_encodings(img, face_locations)
    if not face_encodings:
        return jsonify({'success': False, 'message': 'No face encodings found.'})

    face_encoding = face_encodings[0].tobytes()

    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, face_encoding) VALUES (?, ?)', (username, face_encoding))
    conn.commit()
    conn.close()

    return jsonify({'success': True, 'message': f'User {username} registered successfully.'})

@app.route('/success')
def success():
    return "Login Successful"

if __name__ == '__main__':
    app.run(debug=True)
