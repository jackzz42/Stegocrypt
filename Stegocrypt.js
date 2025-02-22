var socket = io();

// AES Encryption Function function encryptMessage(message, key) { return CryptoJS.AES.encrypt(message, key).toString(); }

// AES Decryption Function function decryptMessage(encryptedMessage, key) { var bytes = CryptoJS.AES.decrypt(encryptedMessage, key); return bytes.toString(CryptoJS.enc.Utf8); }

function login() { let username = document.getElementById("username").value; let password = document.getElementById("password").value;

fetch("/login", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: `username=${username}&password=${password}`
}).then(response => {
    if (response.ok) {
        document.getElementById("stegocrypt-login-container").style.display = "none";
        document.getElementById("stegocrypt-chat-container").style.display = "block";
    } else {
        document.getElementById("login-status").innerText = "Login failed. Wait for approval.";
    }
});

}

function sendMessage() { let key = prompt("Enter encryption key:"); let msg = document.getElementById("message").value; let encryptedMsg = encryptMessage(msg, key); socket.send({ sender: sessionStorage.getItem("username"), message: encryptedMsg }); document.getElementById("message").value = ""; }

socket.on("message", function(data) { let key = prompt("Enter decryption key:"); let decryptedMsg = decryptMessage(data.message, key); let chatBox = document.getElementById("stegocrypt-chat-box"); chatBox.innerHTML += <p><strong>${data.sender}:</strong> ${decryptedMsg}</p>; chatBox.scrollTop = chatBox.scrollHeight; });

function logout() { fetch("/logout").then(() => { document.getElementById("stegocrypt-chat-container").style.display = "none"; document.getElementById("stegocrypt-login-container").style.display = "block"; }); }

  
