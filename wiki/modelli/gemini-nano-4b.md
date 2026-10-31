---
title: "Gemini Nano 4B"
category: modello
tags: [google, llm, on-device]
related_puntate: [20260618]
created: 2026-08-12
updated: 2026-10-09
sources: [raw/puntate/ainews20260618.md, raw/pillitteri/pillitteri20260829-gemini-nano-4-primi-telefoni-gemma-4.md, raw/pillitteri/pillitteri20260507-chrome-gemini-nano-4gb-download-segreto.md]
---

# Gemini Nano 4B

## Introduzione

LLM on-device di Google integrato in Chrome, esposto da un developer come API compatibile OpenAI.

## Capacità e performance

- Chrome integra Gemini Nano 4B locale: un developer lo ha esposto come API compatibile OpenAI, senza chiave API, senza chiamate esterne e funzionante senza ollama.
- Gemini Nano 4 è il modello on-device costruito sopra [[gemma-4]], disponibile in due tagli: Nano 4 Fast su Gemma 4 E2B (circa 2 miliardi di parametri, 4,2 GB) per la velocità e Nano 4 Full su Gemma 4 E4B (circa 4 miliardi, 5,9 GB) per la qualità, entrambi con almeno 12 GB di RAM richiesti. [Fonte: raw/pillitteri/pillitteri20260829-gemini-nano-4-primi-telefoni-gemma-4.md]
- Il 29 agosto 2026 Google elenca i primi sette dispositivi nano-v4: Pixel 11, Pixel 11 Pro, Pixel 11 Pro XL e Pixel 11 Pro Fold, più Galaxy Z Flip8, Galaxy Z Fold8 e Galaxy Z Fold8 Ultra; Pixel 10 e Galaxy S26 restano a Nano 3, con la formula "distribuzione a ondate" che non garantisce il passaggio per i modelli recenti. [Fonte: raw/pillitteri/pillitteri20260829-gemini-nano-4-primi-telefoni-gemma-4.md]
- I test di Android Authority danno 19,14 token al secondo a Nano 4 Fast e 5,3 a Nano 4 Full, contro i 9,6 di Nano 3: circa il doppio, non le quattro volte promesse da Google, e il modello Fast risulta anche più prolisso del predecessore. [Fonte: raw/pillitteri/pillitteri20260829-gemini-nano-4-primi-telefoni-gemma-4.md]

## Timeline delle notizie

- **2026-05-07** — Il 4 maggio il ricercatore Alexander Hanff documenta che Chrome scrive silenziosamente sul disco un file weights.bin da circa quattro gigabyte con i pesi di Gemini Nano, nella cartella OptGuideOnDeviceModel, senza chiedere permesso né permettere una rimozione definitiva via interfaccia; Google ha risposto tramite la VP di Chrome Parisa Tabriz senza affrontare il nodo del consenso. [Fonte: raw/pillitteri/pillitteri20260507-chrome-gemini-nano-4gb-download-segreto.md]

- **2026-08-29** — Google aggiorna la documentazione per sviluppatori e fa nero su bianco i primi telefoni con Gemini Nano 4, costruito su Gemma 4: i quattro Pixel 11 e i tre pieghevoli Galaxy Z8. Entrambe le versioni chiedono almeno 12 GB di RAM, la stessa soglia che pesa su Gemini Intelligence, e il supporto alle funzioni AI on-device viene distinto dagli aggiornamenti di manutenzione: due telefoni possono ricevere la stessa versione di Android e comportarsi in modo diverso sull'AI. Gli sviluppatori possono provare Nano 4 tramite AICore Developer Preview e le API ML Kit GenAI, che espongono riassunto, correzione e riscrittura sopra il modello di sistema. [Fonte: raw/pillitteri/pillitteri20260829-gemini-nano-4-primi-telefoni-gemma-4.md]
- **2026-06-18** — Chrome integra Gemini Nano 4B locale: un developer lo ha esposto come API compatibile OpenAI, senza chiave API, senza chiamate esterne e funzionante senza ollama. [Fonte: raw/puntate/ainews20260618.md]

## Collegamenti

- [[ai-locale]]
- [[gemini-intelligence]]
- [[gemma-4]]
- [[google]]
- [[index]]

