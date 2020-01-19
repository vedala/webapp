function displayMessage() {
    var mainDiv = document.getElementsByTagName("main")[0];
    var messageDiv = document.createElement('div')
    messageDiv.id = 'message';
    messageDiv.innerHTML = "The button was clicked.";
    mainDiv.appendChild(messageDiv);
}

document.addEventListener("DOMContentLoaded", function(event) {
    var button1 = document.getElementById("button1");
    button1.addEventListener("click", displayMessage, false);
});
