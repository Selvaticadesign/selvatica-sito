import { initReveal } from './reveal.js';

initReveal();

// Anno nel footer
document.getElementById('year').textContent = new Date().getFullYear();

// Modulo: per ora solo controllo dei campi. L'invio a Web3Forms arriverà in js/form.js.
const form = document.getElementById('contact-form');
const status = form.querySelector('.form__status');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!form.checkValidity()) {
    const firstInvalid = form.querySelector(':invalid');
    status.textContent = firstInvalid.type === 'checkbox'
      ? 'Serve il consenso alla privacy per poterti rispondere.'
      : 'Controlla i campi: nome, email e messaggio sono necessari.';
    status.classList.add('is-error');
    firstInvalid.focus();
    return;
  }
  status.classList.remove('is-error');
  status.textContent = 'Anteprima: l\'invio non è ancora attivo.';
});
