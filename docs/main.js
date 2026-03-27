/* ============================================
   NYCBC CSC Home — Interactions
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  // --- Scroll Reveal ---
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  reveals.forEach(el => observer.observe(el));

  // --- Mobile Nav Toggle ---
  const toggle = document.querySelector('.mobile-toggle');
  const nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', nav.classList.contains('open'));
    });
  }

  // --- Mobile Nav Folder Toggle ---
  document.querySelectorAll('.nav-item > button').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.nav-item');
      item.classList.toggle('open');
    });
  });

  // --- Close mobile nav on link click ---
  document.querySelectorAll('.main-nav a').forEach(link => {
    link.addEventListener('click', () => {
      if (nav) nav.classList.remove('open');
      if (toggle) toggle.setAttribute('aria-expanded', 'false');
    });
  });

});
