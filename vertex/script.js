document.addEventListener('DOMContentLoaded', function() {
  const hamburgerMenu = document.querySelector('.hamburger-menu');
  const navLinks = document.querySelector('.nav-links ul');

  hamburgerMenu.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default behavior (optional)
    navLinks.classList.toggle('show');
    hamburgerMenu.classList.toggle('active');
  });
});
