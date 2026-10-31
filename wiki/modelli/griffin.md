---
title: "Griffin"
category: modello
tags: [tavus, video, voce, avatar, full-duplex]
related_puntate: []
created: 2026-10-11
updated: 2026-10-11
---

# Griffin

## Introduzione

Griffin è il modello video-to-video di [[tavus]] presentato il 1 ottobre 2026 e definito dall'azienda "Human Interaction Model": riceve in ingresso audio e video di chi parla e restituisce in tempo reale il video di un volto che risponde, in modalità full-duplex, quindi ascolta, guarda e parla nello stesso istante.

## Capacita' e performance

- Fonde percezione, conversazione e generazione audiovisiva in un modello solo, dove la piattaforma precedente di Tavus metteva in fila Phoenix-4.5 per il volto, Raven-1 per la comprensione e Sparrow-2 per i turni di parola: se distogli lo sguardo per pensare capisce che non hai finito, se sorridi reagisce.
- Genera video a 720p partendo da una sola immagine di riferimento, con un ritardo medio di 0,43 secondi su una GPU NVIDIA H100 (0,27 il migliore, 0,59 il peggiore), circa la metà del sistema concorrente più veloce, che dichiara 0,86 secondi.
- Griffin-Lite clona una voce con circa dieci secondi di audio.
- Nei benchmark VideoFDB citati da Tavus sulla generazione Griffin-Lite ottiene 3,83 punti contro 3,92 di un riferimento umano e 2,80 del miglior rivale, mentre sulla percezione il punteggio è 3,73 contro 4,20 dell'umano e 3,44 del rivale; secondo l'azienda la valutazione è stata condotta da NVIDIA in modo indipendente.

## Disponibilita'

- Griffin-Lite è un'anteprima di ricerca riservata a tester selezionati: non è sulla piattaforma Tavus e non è in vendita, l'accesso passa da una lista d'attesa e una versione più potente è annunciata per "molto presto".
- Tavus dichiara di voler aggiungere procedure di sicurezza e funzioni di segnalazione prima di una diffusione più ampia, senza pubblicare dettagli tecnici sui segnali di riconoscimento.

## Azienda di riferimento

- [[tavus]]

## Timeline delle notizie

- **2026-10-05** — Tavus presenta Griffin, modello video-to-video per conversazioni faccia a faccia che combina voce, espressioni, pause e risposta audiovisiva: in uno studio aziendale 26 partecipanti su 54, il 48 per cento, hanno creduto dopo una videochiamata di un minuto di parlare con una persona reale, contro 1 su 41 (2,4 per cento) con la piattaforma precedente. Griffin-Lite genera 720p con 0,43 secondi di ritardo medio su H100, clona una voce con dieci secondi di audio e resta fuori dalla piattaforma Tavus, in attesa di tester selezionati.

## Collegamenti

- [[tavus]]
- [[voce-ai]]
- [[deepfake]]
- [[video-ai]]
- [[index]]
