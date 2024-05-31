// script.js

// Reload the page when the "Home" link is clicked
const homeLink = document.getElementById("home-link");

homeLink.addEventListener("click", function() {
  window.location.reload();
});

// Toggle the display of the navigation links when the hamburger menu is clicked
document.addEventListener('DOMContentLoaded', function() {
  const hamburgerMenu = document.querySelector('.hamburger-menu');
  const navLinks = document.querySelector('.nav-links ul');

  hamburgerMenu.addEventListener('click', function() {
    navLinks.classList.toggle('show');
    hamburgerMenu.classList.toggle('active');
  });
});
