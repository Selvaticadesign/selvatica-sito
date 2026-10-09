# Selvatica Design Studio — sito web

Questo file descrive il progetto. Leggilo all'inizio di ogni sessione e aggiorna la sezione "Decisioni prese" ogni volta che decidiamo qualcosa di importante.

## Chi è il cliente (sono io)
- **Greta**, web designer specializzata in siti web 3D, interattivi e ad alto impatto visivo.
- Attività: **Selvatica Design Studio**. Dominio: **selvaticadesign.it**
- Cosa faccio: costruisco siti 3D interattivi.
- Per chi: chi non ha ancora un sito, chi ha un sito obsoleto, chi vuole essere tra i primi in Italia ad avere un sito 3D.
- Il sito stesso è la mia prima demo: deve dimostrare ciò che vendo.

## Obiettivo della pagina
Azione principale: **il visitatore mi lascia il suo contatto** tramite un modulo (nome, email, telefono facoltativo, breve messaggio, consenso privacy).
Azione secondaria, nel footer: i miei contatti diretti.
- Telefono: +39 375 573 8832 (link `tel:+393755738832`)
- Email: greta@selvaticadesign.it (link `mailto:`)

## Identità visiva
- **Marrone terra scuro**: `#20190F` (colore esatto del logo). Sfondo principale.
- **Beige cotone**: `#ECE5DD`. Testi e superfici chiare.
- Ammessi solo toni derivati da questi due: marroni più caldi e beige più scuri per livelli e bordi. Un solo accento, usato con parsimonia: **brace `#E8743B`** (contrasto 5,8:1 sul marrone, ok per testo; MAI per testo su beige, 2,4:1).
- Tema scuro: atmosfera notturna e misteriosa.

### Font
- **Bostaire**: solo nel logo. Il logo si usa come immagine, quindi il font non va caricato sul sito.
- **Cinzel** (Google Fonts) per i titoli, in maiuscolo con spaziatura ampia.
- **Archivo** (Google Fonts) per testi e interfaccia, al posto di Acumin Variable Concept (vedi "Decisioni prese").

### Tono dei testi
Sintetico, elegante, misterioso. Frasi brevi, niente gergo tecnico, niente superlativi da agenzia. Si suggerisce più di quanto si spieghi. Seconda persona ("il tuo sito"). In italiano.

## File del brand (`/assets/brand/`)
- `logo-completo-beige.png` / `logo-completo-marrone.png`: logo con scritta, sfondo trasparente
- `simbolo-beige.png` / `simbolo-marrone.png`: solo il simbolo (per header e caricamento)
- `simbolo.svg`: simbolo vettoriale, da usare per l'animazione del caricamento
- `logo-completo.svg`: logo vettoriale in versione marrone (testo in tracciati, senza sfondo). Per lo sfondo scuro del sito serve una variante beige, derivata scambiando i colori.
- `favicon.ico`, `favicon-32.png`, `favicon-512.png`, `apple-touch-icon.png`
- `foto-greta-1.png`, `foto-greta-2.png`: mie foto al lavoro, per la sezione "Chi sono". Vanno convertite in WebP e ridimensionate.

## Concetto creativo: "La discesa"
Ispirazione: una camera che scende dentro un canyon di roccia mentre l'utente scorre la pagina, con una sfera luminosa sempre al centro.
Versione Selvatica: una **discesa nella terra selvaggia**. Pareti di roccia scura color terra, radici e foglie affilate come quelle del logo, luce calda color beige che filtra dall'alto. Al centro una **sfera di vetro** con un bagliore caldo all'interno, che cambia sfumatura a ogni sezione. È il "seme" della selva.

### Architettura tecnica (ibrida, leggera)
1. **Sfondo**: sequenza di fotogrammi WebP (da un video Higgsfield) disegnata su una tela grafica e collegata allo scroll. Una serie per desktop (16:9, 1200px) e una per mobile (9:16, 800px).
2. **Sfera**: scena Three.js trasparente sopra lo sfondo. Una sola sfera sempre centrata, con uno shader leggero (effetto fresnel sul bordo e sfumatura interna). **Niente riflessi in tempo reale.**
3. **Testi**: sempre in HTML sopra la scena, mai dentro il 3D, con entrate animate in CSS e JS leggero.

## Struttura della pagina
1. **Hero**: logo, frase principale, invito a scorrere.
2. **La discesa** (scroll collegato): 3–4 frasi brevi che compaiono durante la discesa (il problema: siti piatti, obsoleti, tutti uguali).
3. **Cosa faccio**: siti 3D interattivi. Tre servizi o vantaggi al massimo.
4. **Per chi**: chi non ha un sito / chi ha un sito obsoleto / chi vuole essere tra i primi in Italia.
5. **Metodo**: 3–4 passaggi, dalla prima call alla pubblicazione.
6. **Chi sono**: foto e poche righe.
7. **Contatto**: modulo, che è l'azione principale.
8. **Footer**: logo, telefono, email, P.IVA, link alla privacy policy, anno.

## Regole tecniche
- HTML, CSS e JavaScript puri, più Three.js caricato come modulo. Niente framework.
- Pubblicazione su **GitHub Pages** con dominio personalizzato selvaticadesign.it.
- Il modulo contatti usa un servizio esterno compatibile con siti statici (es. Formspree o Web3Forms), con casella di consenso privacy obbligatoria.
- Prestazioni: rendering in pausa quando la scena non è visibile, pixel ratio limitato a 2 (1.5 su mobile), nessun bloom su mobile, immagini in WebP con caricamento differito.
- Accessibilità: rispettare `prefers-reduced-motion` (scena statica e testi visibili), contrasto adeguato, navigazione da tastiera, testi alternativi alle immagini.
- SEO: titolo e descrizione, Open Graph con immagine di anteprima, `lang="it"`, un solo H1.
- Una modifica per volta. Dopo ogni passaggio che funziona: commit con un messaggio chiaro in italiano.
- Prima di modifiche grandi, spiegami il piano e aspetta la mia conferma.

## Decisioni prese
- 2026-10-08 — Cartella di lavoro: `Sito Web/selvatica-sito/`. Fuori da questa cartella restano solo la guida dei prompt e lo zip originale.
- 2026-10-08 — GitHub: account gratuito, repository pubblico (GitHub Pages gratis richiede repository pubblico).
- 2026-10-08 — Font dei testi: **Archivo** (Google Fonts, variabile con asse di larghezza come Acumin) al posto di Acumin. Niente kit Adobe Fonts.
- 2026-10-08 — Modulo contatti: **Web3Forms**, chiave di accesso `11baadcd-31ba-42bc-b127-c455aa1a8645` (chiave pubblica, è normale che stia nell'HTML).
- 2026-10-08 — File sorgente (es. `source/logo-completo.ai`) in `source/`, esclusi da git: non vanno pubblicati.
- 2026-10-09 — Accento: brace `#E8743B`, scelto da Claude su richiesta di Greta ("qualcosa che spicca di contrasto").
- 2026-10-08 — Foto di "Chi sono": si possono ritoccare (viraggio caldo, verdi smorzati) per renderle coerenti con la palette.

## Da fare / in sospeso
- P.IVA e testo della privacy policy
- Video Higgsfield della discesa
