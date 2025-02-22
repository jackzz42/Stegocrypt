var socket = io();

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

function sendMessage() { let msg = document.getElementById("message").value; socket.send(msg); document.getElementById("message").value = ""; }

socket.on("message", function(msg) { let chatBox = document.getElementById("stegocrypt-chat-box"); chatBox.innerHTML += <p>${msg}</p>; chatBox.scrollTop = chatBox.scrollHeight; });

function logout() { fetch("/logout").then(() => { document.getElementById("stegocrypt-chat-container").style.display = "none"; document.getElementById("stegocrypt-login-container").style.display = "block"; }); }

