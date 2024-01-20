function sendMessage() {
    var userMessage = document.getElementById('user-message').value;
    if (userMessage.trim() === "") return;

    var chatMessages = document.getElementById('chat-messages');
    
    // Create a message element with a class to distinguish user messages
    var newMessage = document.createElement('div');
    newMessage.className = 'message user-message';
    newMessage.innerHTML = userMessage;

    chatMessages.appendChild(newMessage);

    // Clear the user input field
    document.getElementById('user-message').value = '';

    // Scroll to the bottom of the chat messages
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
