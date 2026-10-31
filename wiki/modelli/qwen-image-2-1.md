---
title: "Qwen-Image 2.1"
category: modello
tags: [qwen, alibaba, image, open-weight, uncensored]
related_puntate: [20260922, 20260923, 20260924, 20260925, 20260928, 20261004, 20261005]
created: 2026-09-22
updated: 2026-10-11
---

# Qwen-Image 2.1

## Introduzione

Qwen-Image 2.1 è la versione locale senza restrizioni del generatore di immagini di [[qwen]]. Due categorie: Uncensored GGUF con pesi originali e Heretic con text encoder modificato per ridurre i rifiuti di prompt.

## Capacità

- Generazione immagini senza filtri aggiuntivi nella variante Uncensored.
- Heretic riduce i rifiuti con encoder modificato.

## Disponibilità

- Varianti quantizzate da 4 a 16 GB per hardware 8-24 GB VRAM.

## Azienda di riferimento

- [[qwen]]
- [[alibaba]]

## Timeline delle notizie

- **2026-09-22** — Arriva Qwen-Image 2.1 locale senza restrizioni in due linee Uncensored GGUF e Heretic, quantizzate 4-16 GB.

- **2026-09-23** — Una versione aggiornata riduce i rifiuti da cento su cento a cinque, porta l'editing fino a dieci immagini di riferimento con trasparenza nativa, funziona su ComfyUI e gira in locale su laptop con la quantizzazione Q4_K_M da quattro punto sessantotto gigabyte.

- **2026-09-24** — La versione ufficiale contiene ancora il prompt rewriter nascosto e rifiuta novantotto richieste su cento: la variante Heretic abbassa i rifiuti a tre su cento, con accanto una versione distillata a quattro step e una in formato NVFP4 per RTX 50. Qwen-Image 2.1 gira già su smartphone Android, dove uno Snapdragon 8 Gen 2 con sedici GB di RAM produce un'immagine 512x512 in circa otto minuti.
- **2026-09-25** — Qwen-Image-2.1 genera in modo nativo a due K con una qualità paragonata a GPT-Image-2.5 e senza moderazione né validazione locale, ed è indicato come ideale per i frame di riferimento nei video AIGC: trentatré gigabyte di pesi, due minuti di caricamento e circa tre minuti per un'immagine 2K a trenta step su una singola RTX 4090.

- **2026-09-28** — Un modello distillato accelerato porta la velocità end-to-end a cinque volte quella del modello base a quaranta step: funziona in locale, senza connessione e senza censura, supporta NSFW di default ed è eseguibile anche con bassa VRAM.
- **2026-10-04** — BFS-Best-Face-Swap ora supporta Qwen-Image 2.1 con face swap, head swap e body swap, con workflow inclusi per ComfyUI e Draw Things.
- **2026-10-05** — Qwen rilascia Consistent Lighting, un LoRA per Qwen-Image 2.1 che inserisce oggetti nella scena con ombre naturali e highlight speculari, senza riflessi falsi.
- **2026-10-05** — Le versioni GGUF etichettate «uncensored» pubblicate su Hugging Face da abenzerps sono in realtà quantizzazioni del modello originale di Alibaba (Q4_K_M da 4,60 GB, con circa 1,55 milioni di download nell'ultimo mese): la scheda descrive un modello senza safety checker ma non dichiara né fine-tuning né abliteration, e l'autore ammette che la versione davvero senza censure non è ancora pronta. Nella pipeline di Qwen-Image-2.1 non esiste un filtro da togliere, perché i rifiuti segnalati stanno nei servizi ospitati e non nei pesi, e il rilascio resta sotto Qwen Research License, che non consente l'uso commerciale senza un accordo con Alibaba.
- **2026-10-10** — AtomicChat pubblica il 9 ottobre su Hugging Face Qwen-Image-2.1-Turbo-Uncensored-GGUF, versione senza rifiuti del text encoder: la scheda ammette che su 45 prompt sensibili nessun risultato cambia rispetto all'encoder originale, perché il generatore di Qwen non aveva filtri da togliere.













## Collegamenti

- [[qwen]]
- [[alibaba]]
- [[index]]
