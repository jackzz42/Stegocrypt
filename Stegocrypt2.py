from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file from flask_socketio import SocketIO, send, emit from werkzeug.utils import secure_filename from cryptography.fernet import Fernet from stegano import lsb import os import random import base64 import time import secrets

StegoCrypt - Secure Chat & File Sharing App

Generate encryption key

key = Fernet.generate_key() cipher = Fernet(key)

def generate_secure_token(): return secrets.token_hex(16)

app = Flask(name) app.secret_key = os.getenv("SECRET_KEY", generate_secure_token()) socketio = SocketIO(app, cors_allowed_origins="*") UPLOAD_FOLDER = 'uploads' os.makedirs(UPLOAD_FOLDER, exist_ok=True)

Admin control

admin_password = os.getenv("ADMIN_PASSWORD", "adminpass") users = {"admin": admin_password}  # Store approved users pending_users = []  # Users waiting for approval

@app.route('/') def index(): if "user" in session: return render_template("stegocrypt.html", username=session["user"]) return render_template("stegocrypt_login.html")

@app.route('/login', methods=['POST']) def login(): username = request.form["username"] password = request.form["password"]

if username in users and users[username] == password:
    session["user"] = username
    return redirect(url_for("index"))
elif username not in users:
    pending_users.append(username)
    return "Waiting for admin approval", 403
return "Invalid credentials", 401

@app.route('/approve', methods=['POST']) def approve_user(): if "user" in session and session["user"] == "admin": user = request.form["username"] users[user] = "approved" pending_users.remove(user) return "User approved" return "Unauthorized", 403

@socketio.on('message') def handle_message(data): encrypted_msg = data['message'] sender = data['sender'] emit('message', {"sender": sender, "message": encrypted_msg}, broadcast=True)

@app.route('/upload', methods=['POST']) def upload(): file = request.files['file'] file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)) file.save(file_path) return "File uploaded"

@app.route('/encrypt', methods=['POST']) def encrypt_file(): file = request.files['file'] file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)) file.save(file_path)

with open(file_path, 'rb') as f:
    encrypted_data = cipher.encrypt(f.read())
encrypted_file_path = file_path + ".enc"
with open(encrypted_file_path, 'wb') as f:
    f.write(encrypted_data)

return send_file(encrypted_file_path, as_attachment=True)

@app.route('/decrypt', methods=['POST']) def decrypt_file(): file = request.files['file'] file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)) file.save(file_path)

with open(file_path, 'rb') as f:
    decrypted_data = cipher.decrypt(f.read())
decrypted_file_path = file_path.replace(".enc", "")
with open(decrypted_file_path, 'wb') as f:
    f.write(decrypted_data)

return send_file(decrypted_file_path, as_attachment=True)

@app.route('/hide_file', methods=['POST']) def hide_file(): file = request.files['file'] cover_file = request.files['cover_file'] file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)) cover_path = os.path.join(UPLOAD_FOLDER, secure_filename(cover_file.filename)) file.save(file_path) cover_file.save(cover_path)

with open(file_path, "rb") as f:
    file_data = base64.b64encode(f.read()).decode()

secret_img = lsb.hide(cover_path, file_data)
hidden_file_path = cover_path + "_hidden.png"
secret_img.save(hidden_file_path)

return send_file(hidden_file_path, as_attachment=True)

@app.route('/reveal_file', methods=['POST']) def reveal_file(): file = request.files['file'] file_path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)) file.save(file_path)

hidden_data = lsb.reveal(file_path)
revealed_file_path = file_path.replace("_hidden.png", "_revealed")

with open(revealed_file_path, "wb") as f:
    f.write(base64.b64decode(hidden_data))

return send_file(revealed_file_path, as_attachment=True)

if name == 'main': port = int(os.getenv("PORT", random.randint(5000, 9000))) print(f"StegoCrypt running at http://127.0.0.1:{port}") socketio.run(app, host="0.0.0.0", port=port, debug=True)

