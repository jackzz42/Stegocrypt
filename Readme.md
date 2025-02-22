# StegoCrypt - Secure Chat & File Sharing

StegoCrypt is a **secure, real-time chat and file-sharing app** that uses **encryption & steganography** to protect user data.

## 🚀 Features
✅ **Admin-controlled chat** (Only approved users can join)  
✅ **Real-time chat** (Instant messaging via WebSockets)  
✅ **File encryption & sharing** (Send encrypted files securely)  
✅ **Steganography** (Hide messages inside images)  
✅ **Voice & video sharing** (Secure multimedia communication)  

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR-USERNAME/stegocrypt.git
cd stegocrypt
```
### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
### 3️⃣ Run StegoCrypt
#### **Linux/macOS:**
```sh
chmod +x start_stegocrypt.sh
./start_stegocrypt.sh
```
#### **Windows:**
```sh
python stegocrypt.py
```
## 🌍 Deploy on Render (Free Hosting)
1. Push your code to GitHub
2. Sign up on [Render](https://render.com/)
3. Create a **New Web Service** → Connect GitHub repo
4. Set the **Start Command**:
   ```sh
   gunicorn stegocrypt:app
   ```

## 🤝 Contributing
We welcome contributions! Check [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
