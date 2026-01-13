function addMessage(text, sender) {
    const chatBox = document.getElementById("chat-box");
    const msg = document.createElement("div");

    // Match CSS classes: message + user/bot
    msg.classList.add("message", sender);
    msg.innerText = text;

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const question = input.value.trim();

    if (!question) return;

    // Show user message
    addMessage(question, "user");
    input.value = "";

    fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    })
    .then(res => res.json())
    .then(data => {
        // Show bot response
        addMessage(data.answer, "bot");
    })
    .catch(err => {
        addMessage("Something went wrong. Please try again.", "bot");
        console.error(err);
    });
}
