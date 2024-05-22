// Select the header element.
const red_header = document.getElementById('red_header');

// Listen for a click event on the header element.
red_header.addEventListener('click', function() {
    // Change the header's text color to red.
    const header = document.querySelector('header');
    header.style.color = '#FF0000';
    });