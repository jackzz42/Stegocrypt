# StegoCrypt - Secure Chat & File Sharing

StegoCrypt is a **highly secure** chat and file-sharing application featuring **End-to-End Encryption (E2EE)**, **Steganography**, and **Admin Controls**.

## 🔐 Features
- **End-to-End Encrypted Chat** (AES-256)
- **Encrypted File Sharing** (Password-Protected)
- **Steganography for Hiding Messages & Files**
- **Admin-Controlled User Access**
- **Self-Destructing Messages**
- **Two-Factor Authentication (2FA) Support**
- **Supports Image, Video, Audio, and PDF Steganography**
- **Secure Randomized Port & Encryption Key**
- **Local & Cloud Deployment Support**

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

### 3️⃣ Run the Application
```sh
chmod +x start_stegocrypt.sh
./start_stegocrypt.sh
```

## 🌐 Accessing StegoCrypt
Once the server starts, access the chat at:
```
http://127.0.0.1:<RANDOM_PORT>
```

## ☁️ Deploying on Cloud Server
### Using Render, Heroku, or VPS:
1. **Upload the project to a cloud server or platform like Render, Heroku, or AWS.**
2. **Set the required environment variables (SECRET_KEY, ADMIN_PASSWORD).**
3. **Run the server using:**
   ```sh
   gunicorn -w 4 -k gevent stegocrypt:app
   ```
4. **Access the app using the public URL provided by the platform.**

## 🏠 Running on Local Network (LAN)
1. **Find your local IP address:**
   ```sh
   ipconfig (Windows) or ifconfig (Linux/Mac)
   ```
2. **Start the server and allow access:**
   ```sh
   python3 stegocrypt.py --host=0.0.0.0 --port=5000
   ```
3. **Other devices on the same network can access it using:**
   ```
   http://<YOUR_LOCAL_IP>:5000
   ```

## 🛡️ Security Notes
- Use strong passwords for admin login.
- Never share your encryption key.
- If deploying on a server, use HTTPS for secure communication.

## 🤝 Contributing
Feel free to submit pull requests and report issues!

## 📜 License
MIT License - Use and modify freely with credit to the original author.
