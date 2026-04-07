function start() {
    document.getElementById("status").innerText = "Starting...";
    eel.startListening()();
}

// receive updates from Python
eel.expose(updateStatus);
function updateStatus(message) {
    document.getElementById("status").innerText = message;
}