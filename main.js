function displayMessage() {
    var messageDiv = document.getElementById("message");
    messageDiv.innerHTML = "The button was clicked.";
}

document.addEventListener("DOMContentLoaded", function(event) {
    var button1 = document.getElementById("button1");
    button1.addEventListener("click", displayMessage, false);
});
