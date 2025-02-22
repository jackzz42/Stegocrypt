var socket = io();

// AES Encryption Function
function encryptMessage(message, key) {
    return CryptoJS.AES.encrypt(message, key).toString();
}

// AES Decryption Function
function decryptMessage(encryptedMessage, key) {
    try {
        var bytes = CryptoJS.AES.decrypt(encryptedMessage, key);
        return bytes.toString(CryptoJS.enc.Utf8);
    } catch (error) {
        console.error("Decryption failed. Invalid key or corrupted data.", error);
        return "[Decryption Error]";
    }
}

function login() {
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `username=${encodeURIComponent(username)}&password=${encodeURIComponent(password)}`
    }).then(response => {
        if (response.ok) {
            sessionStorage.setItem("username", username);
            document.getElementById("stegocrypt-login-container").style.display = "none";
            document.getElementById("stegocrypt-chat-container").style.display = "block";
        } else {
            document.getElementById("login-status").innerText = "Login failed. Wait for approval.";
        }
    }).catch(error => console.error("Login request failed.", error));
}

function sendMessage() {
    let key = prompt("Enter encryption key:");
    if (!key) {
        alert("Encryption key is required!");
        return;
    }
    let msg = document.getElementById("message").value;
    let encryptedMsg = encryptMessage(msg, key);
    let sender = sessionStorage.getItem("username") || "Unknown";
    socket.send({ sender: sender, message: encryptedMsg });
    document.getElementById("message").value = "";
}

socket.on("message", function(data) {
    let key = prompt("Enter decryption key:");
    if (!key) {
        alert("Decryption key is required!");
        return;
    }
    let decryptedMsg = decryptMessage(data.message, key);
    let chatBox = document.getElementById("stegocrypt-chat-box");
    let messageElement = document.createElement("p");
    messageElement.innerHTML = `<strong>${data.sender}:</strong> ${decryptedMsg}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
});

function logout() {
    fetch("/logout").then(() => {
        sessionStorage.removeItem("username");
        document.getElementById("stegocrypt-chat-container").style.display = "none";
        document.getElementById("stegocrypt-login-container").style.display = "block";
    }).catch(error => console.error("Logout failed.", error));
        }
