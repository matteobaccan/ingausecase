---
title: "Reverse-SynthID"
category: strumento
tags: [watermark, sicurezza, synthid, ricerca]
related_puntate: []
created: 2026-10-06
updated: 2026-10-06
---

# Reverse-SynthID

## Introduzione

Repository di Alosh Denny pubblicato a marzo 2026 che rimuove il watermark SynthID di Google dalle immagini generate da Nano Banana con la sola analisi spettrale, senza reti neurali né accesso al modello: sfrutta il fatto che SynthID codifica frequenze carrier a fase costante, con coerenza di fase tra immagini diverse superiore al 99,5 per cento.

## Funzionalità principali

- Applica la trasformata di Fourier 2D ai canali RGB, estrae i bin di energia e sottrae bin per bin con un codebook per risoluzione, rimuovendo il 91 per cento dell'energia del watermark con qualità quasi intatta (PSNR 43,5 dB, SSIM 0,997) e un detector che lo identifica con accuratezza del 90 per cento.
- Il database di riferimento usato per l'attacco contava 123.000 coppie di immagini generate da Nano Banana a 1024x1024 e 1536x2816.

## Timeline delle notizie

- **2026-04-15** — Mille fork in poche settimane per reverse-SynthID, che aggira il watermark invisibile di Google con analisi spettrale: rimozione del 91 per cento dell'energia e detector al 90 per cento di accuratezza.

## Collegamenti

- [[digital-provenance]]
- [[google]]
- [[synthid-bio]]
- [[watermarks-remover]]
- [[index]]
