// Entrate animate dei testi: dissolvenza e lieve sfocatura quando entrano nello schermo.
// Le frasi della discesa invece compaiono e scompaiono, una alla volta.

const STAGGER = 0.12; // secondi tra un elemento e il successivo nello stesso gruppo

export function initReveal() {
  const items = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window)) {
    items.forEach((el) => el.classList.add('is-visible'));
    return;
  }

  // Ritardo progressivo tra fratelli (es. le tre schede di "Cosa faccio")
  items.forEach((el) => {
    const siblings = [...el.parentElement.children].filter((c) => c.classList.contains('reveal'));
    const index = siblings.indexOf(el);
    if (index > 0) el.style.setProperty('--delay', `${index * STAGGER}s`);
  });

  const once = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-visible');
        once.unobserve(entry.target);
      });
    },
    { rootMargin: '0px 0px -12% 0px', threshold: 0.15 }
  );

  // Ogni frase occupa uno schermo: è visibile quando il suo blocco riempie più di metà schermo
  const toggle = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        entry.target.classList.toggle('is-visible', entry.intersectionRatio >= 0.55);
      });
    },
    { threshold: [0, 0.55] }
  );

  items.forEach((el) => {
    if (el.classList.contains('descent__line')) {
      el.style.removeProperty('--delay');
      toggle.observe(el);
    } else {
      once.observe(el);
    }
  });
}
