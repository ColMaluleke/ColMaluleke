document.addEventListener('DOMContentLoaded', function() {
  const hamburgerMenu = document.querySelector('.hamburger-menu');
  const navLinks = document.querySelector('.nav-links ul');

  // Hide navigation links initially
  navLinks.style.display = 'none'; 

  hamburgerMenu.addEventListener('click', function() {
    navLinks.classList.toggle('show');
    hamburgerMenu.classList.toggle('active');
  });
});
