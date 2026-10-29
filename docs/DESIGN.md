# ForgeNox · Attack on Titan README

Il README usa immagini SVG esterne con CSS keyframes incorporati nei file SVG, non stili applicati all'HTML del README. Non richiede JavaScript, GitHub Actions o GitHub Pages.

## Animazioni

- Intestazione: tratto progressivo e segnale pulsante.
- Fondatore: GIF animata di 128 fotogrammi, 6,4 secondi, incorporata da Tenor. Non è generata, non contiene audio. Fonte: https://tenor.com/view/eren-founding-titan-the-rumbling-colossal-titan-the-founding-titan-gif-25291484
- Pannelli: linee disegnate progressivamente, mappa del percorso e indicatori pulsanti.
- Chiusura desktop: rivelazione progressiva del testo.
- SVG con prefers-reduced-motion; questa impostazione non controlla la GIF esterna.

I pannelli hanno sfondo proprio verde scuro, avorio e rosso ossido, cornici da dossier, griglia cartografica e simbolo alato stilizzato. Il tema del sito GitHub resta indipendente. Le varianti mobile sono selezionate mediante picture/source. Il testo è ripetuto in un blocco details per leggibilità e accessibilità.

## Modifiche

Modificare build.py, poi eseguire `python3 build.py` per rigenerare assets/*.svg. Non sono necessarie dipendenze. Il README usa percorsi relativi. La GIF dipende dalla disponibilità di Tenor e dalla cache immagini GitHub.

La bio deriva dal README pubblico preesistente. Nessun dato di repository privati è pubblicato. Non sono presenti statistiche inventate o progetti fittizi. Il precedente README GitSkins è conservato in backups/README-before-aot-2026-10-29.md; la prima variante statica è conservata in backups/README-static-aot.md.

## Ricerca

- Supporto GIF nei README: https://docs.github.com/en/account-and-profile/concepts/personal-profile
- Sanitizzazione HTML: https://github.com/github/markup
- Esempio GitSkins con SVG animati: https://github.com/asamassekou10/demo-gitskins
- Approccio SVG con keyframes incorporati: https://github.com/ryanpolasky/ryme.md

## Crediti

Attack on Titan e i suoi personaggi appartengono ai rispettivi titolari. La GIF è un embed dalla pagina Tenor attribuita a RealPrez. I pannelli SVG sono creati per questo profilo. Il fan theme non implica affiliazione ufficiale o concessione di diritti commerciali sul franchise o sulla GIF.
