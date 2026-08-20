const sessionId =
  localStorage.getItem("session_id") || crypto.randomUUID();
localStorage.setItem("session_id", sessionId);

const chatLog = document.getElementById("chat-log");
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");

function appendMessage(role, text) {
  const el = document.createElement("div");
  el.className = `message ${role}`;
  el.innerHTML = `<strong>${role === "user" ? "You" : "Bot"}:</strong> `;
  const textNode = document.createTextNode(text);
  el.appendChild(textNode);
  chatLog.appendChild(el);
  chatLog.scrollTop = chatLog.scrollHeight;
  return textNode;
}

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = chatInput.value.trim();
  if (!message) return;
  chatInput.value = "";

  appendMessage("user", message);
  const assistantNode = appendMessage("assistant", "");

  const response = await fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ session_id: sessionId, message }),
  });

  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    assistantNode.textContent += decoder.decode(value, { stream: true });
    chatLog.scrollTop = chatLog.scrollHeight;
  }
});
