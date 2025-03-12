document.addEventListener('DOMContentLoaded', function () {
    let popup = document.getElementById('newsletter-popup');
    let closeButton = document.getElementById('close-popup');

    // Show the popup when the page loads
    setTimeout(function () {
        popup.style.display = 'flex'; // Makes the popup visible
    }, 2000); // Delays appearance by 2 seconds for a better experience

    // Close the popup when the close button is clicked
    closeButton.addEventListener('click', function () {
        popup.style.display = 'none';
    });

    // Close the popup if the user clicks outside the popup content
    popup.addEventListener('click', function (event) {
        if (event.target === popup) {
            popup.style.display = 'none';
        }
    });
});
