// main.js
document.addEventListener('DOMContentLoaded', function() {
    // If the success message exists, hide it after 3 seconds
    var successMessage = document.getElementById('success-message');
    if (successMessage) {
        setTimeout(function() {
            successMessage.style.display = 'none';
        }, 3000); // Hide the success message after 3 seconds
    }
});
