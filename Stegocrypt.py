from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
from flask_socketio import SocketIO, send, emit
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
from stegano import lsb
import os
import random
import base64
import time
import secrets

# StegoCrypt - Secure Chat & File Sharing App

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

def generate_secure_token():
    return secrets.token_hex(16)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", generate_secure_token())
socketio = SocketIO(app, cors_allowed_origins="*")
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Admin control
admin_password = os.getenv("ADMIN_PASSWORD", "adminpass")
users = {"admin": admin_password}  # Store approved users
pending_users = []  # Users waiting for approval

@app.route('/')
def index():
    if "user" in session:
        return render_template("stegocrypt.html", username=session["user"])
    return render_template("stegocrypt_login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    if username in users and users[username] == password:
        session["user"] = username
        return redirect(url_for("index"))
    elif username not in users:
        pending_users.append(username)
        return "Waiting for admin approval", 403
    return "Invalid credentials", 401

@app.route('/approve', methods=['POST'])
def approve_user():
    if "user" in session and session["user"] == "admin":
