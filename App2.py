from flask import Flask, request, send_file, jsonify, render_template from cryptography.fernet import Fernet from stegano import lsb import pyttsx3 import os import time

app = Flask(name, static_folder="static", template_folder="templates")

Generate a key for encryption

key = Fernet.generate_key() cipher = Fernet(key)

UPLOAD_FOLDER = "uploads" os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/") def serve_react(): return render_template("index.html")  # Serves React frontend

@app.route('/encrypt', methods=['POST']) def encrypt_file(): file = request.files['file'] file_path = os.path.join(UPLOAD_FOLDER, file.filename) file.save(file_path)

with open(file_path, 'rb') as f:
    encrypted_data = cipher.encrypt(f.read())

encrypted_file_path = file_path + ".enc"
with open(encrypted_file_path, 'wb') as f:
    f.write(encrypted_data)

return send_file(encrypted_file_path, as_attachment=True)

@app.route('/decrypt', methods=['POST']) def decrypt_file(): file = request.files['file'] file_path = os.path.join(UPLOAD_FOLDER, file.filename) file.save(file_path)

with open(file_path, 'rb') as f:
    decrypted_data = cipher.decrypt(f.read())

decrypted_file_path = file_path.replace(".enc", "")
with open(decrypted_file_path, 'wb') as f:
    f.write(decrypted_data)

return send_file(decrypted_file_path, as_attachment=True)

@app.route('/text_to_speech', methods=['POST']) def text_to_speech(): text = request.form['text'] speech_file = os.path.join(UPLOAD_FOLDER, "speech.mp3")

engine = pyttsx3.init()
engine.save_to_file(text, speech_file)
engine.runAndWait()

return send_file(speech_file, as_attachment=True)

if name == 'main': print("\n✅ Installation complete!") print("🚀 To start the Secure Media Web App, run:") print("-------------------------------------------------") print("   python3 app.py") print("-------------------------------------------------\n") time.sleep(3)

try:
    app.run(debug=True)
except Exception as e:
    print("❌ An error occurred while running the app:", e)

