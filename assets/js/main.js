// Screen-only helpers for the Data Science Interview Prep ebook.
// Print/PDF works fine without this file.

(() => {
  // Keyboard nav: PageDown / PageUp / arrows scroll one page height.
  const pageH = () => {
    const p = document.querySelector('.page');
    return p ? p.getBoundingClientRect().height + 14 : window.innerHeight;
  };

  window.addEventListener('keydown', (e) => {
    if (e.target.matches('input, textarea, [contenteditable]')) return;
    if (e.key === 'PageDown' || e.key === 'ArrowDown' || e.key === ' ') {
      e.preventDefault();
      window.scrollBy({ top: pageH(), behavior: 'smooth' });
    } else if (e.key === 'PageUp' || e.key === 'ArrowUp') {
      e.preventDefault();
      window.scrollBy({ top: -pageH(), behavior: 'smooth' });
    } else if (e.key === 'Home') {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else if (e.key === 'End') {
      e.preventDefault();
      window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
    } else if (e.key.toLowerCase() === 'p' && (e.ctrlKey || e.metaKey)) {
      // let the browser handle it; nothing to do
    }
  });

  // Number the pages in the footer automatically if a page carries no <fnum>
  document.querySelectorAll('.page').forEach((page, i) => {
    const foot = page.querySelector('.fnum');
    if (foot && !foot.textContent.trim()) foot.textContent = String(i + 1).padStart(2, '0');
  });
})();
