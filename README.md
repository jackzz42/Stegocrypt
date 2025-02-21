Secure Media Web App

🚀 Overview

This is a Secure Media Web App that allows users to:

Encrypt & Decrypt files (Text, PDFs, Images, Videos, Audio)

Hide & Extract messages inside images, videos, and audio (Steganography)

Convert Text to Speech (TTS)

Extract Text from Images & Audio

Serves React Frontend from Flask Backend


🛠️ Features

✅ File Encryption & Decryption (AES Encryption)
✅ Steganography (Hide text in media files)
✅ Text-to-Speech (Convert text into voice messages)
✅ Speech-to-Text (Extract text from audio files)
✅ Web-based UI (Accessible from any browser)
✅ Flask serves both backend API and React frontend

📂 Project Structure

secure-media-app/
│── backend/        # Flask Backend + React Frontend
│   ├── static/     # React frontend build files
│   ├── templates/  # React index.html
│   ├── app.py      # Main Flask application
│── requirements.txt  # Backend Dependencies

🔧 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/YOUR-USERNAME/secure-media-app.git
cd secure-media-app

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Application

python3 app.py

✅ The web app will be available at http://localhost:5000/
