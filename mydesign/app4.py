# app.py
from flask import Flask, request, jsonify, render_template, redirect, url_for
import base64
import cv2
import numpy as np
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, image BLOB)')
    conn.close()

create_table()

def compare_images(img1, img2):
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(img1_gray, img2_gray)
    mean_diff = np.mean(diff)
    return mean_diff

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    image_bytes = base64.b64decode(image_data)
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()

    for user in users:
        stored_image_bytes = user['image']
        stored_nparr = np.frombuffer(stored_image_bytes, np.uint8)
        stored_img = cv2.imdecode(stored_nparr, cv2.IMREAD_COLOR)

        diff = compare_images(img, stored_img)
        if diff < 10: # Adjust threshold for sensitivity
            return jsonify({'success': True, 'message': f'Welcome, {user["username"]}!'})

    return jsonify({'success': False, 'message': 'Access Denied.'})

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    image_data = data['image'].split(',')[1]
    image_bytes = base64.b64decode(image_data)
    username = data['username']

    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, image) VALUES (?, ?)', (username, image_bytes))
    conn.commit()
    conn.close()

    return jsonify({'success': True, 'message': f'User {username} registered successfully.'})

@app.route('/success')
def success():
    return "Login Successful"

if __name__ == '__main__':
    app.run(debug=True)
