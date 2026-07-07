console.log("JS Loaded ✅");

const btn = document.getElementById("startBtn");

btn.addEventListener("click", () => {
    document.getElementById("status").innerText = "Starting assistant...";
    
    eel.startListening()();   // 🔥 Calls Python function
});

// Receive updates from Python
eel.expose(updateStatus);
function updateStatus(message) {
    console.log(message);
    document.getElementById("status").innerText = message;
}
