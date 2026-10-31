---
title: "Nemotron 3.5 Super VL"
category: modello
tags: [nvidia, vlm, moe, open-weight]
related_puntate: []
created: 2026-10-15
updated: 2026-10-16
sources: [raw/pillitteri/pillitteri20261015-nemotron-3-5-super-vl-nvidia-repository-gtc-berlino.md, raw/puntate/ainews20261016.md, raw/controrumore/controrumore20261016-diario-ai-lintelligenza-artificiale.md]
---

# Nemotron 3.5 Super VL

## Introduzione

Modello visione-linguaggio di [[nvidia]] da circa 120 miliardi di parametri con 12 attivi per token (121 e 13 secondo il codice dei repository, dove la torre visiva pesa circa un miliardo): legge immagini e video oltre al testo ed è ancora senza annuncio ufficiale, benché il supporto software sia già fuso nei repository NVIDIA. [Fonte: raw/pillitteri/pillitteri20261015-nemotron-3-5-super-vl-nvidia-repository-gtc-berlino.md]

## Capacità e performance

- Il linguaggio poggia su un decoder ibrido Nemotron-H, che alterna blocchi Mamba a blocchi di esperti, con 512 esperti instradabili e 22 scelti per ogni parola; la torre visiva è RADIO da 0,65 miliardi di parametri, collegata al linguaggio da un proiettore, con un embedder video temporale distinto dal percorso delle immagini. [Fonte: raw/pillitteri/pillitteri20261015-nemotron-3-5-super-vl-nvidia-repository-gtc-berlino.md]
- Non ha encoder audio, a differenza di Nemotron 3 Nano Omni da cui lo stack è ereditato, e nelle ricette pubblicate la testa di multi-token prediction è lasciata a zero in addestramento. [Fonte: raw/pillitteri/pillitteri20261015-nemotron-3-5-super-vl-nvidia-repository-gtc-berlino.md]

## Disponibilità

- La pull request 3801 su NeMo AutoModel è stata aperta il 3 settembre e fusa il 9; Megatron-Bridge ha ricette di pre-addestramento, SFT e PEFT per H100 e GB200, mentre TensorRT-LLM ha ricevuto il supporto al video in ingresso, alle varianti NVFP4 e al multi-LoRA. [Fonte: raw/pillitteri/pillitteri20261015-nemotron-3-5-super-vl-nvidia-repository-gtc-berlino.md]
- La pagina di integrazione LangChain porta l'identificativo nvidia/nemotron-3.5-super-vl-120b-a12b ma avverte che l'endpoint pubblico su NVIDIA Build non è ancora verificato; su Hugging Face il modello non c'è e non è indicata una licenza. [Fonte: raw/pillitteri/pillitteri20261015-nemotron-3-5-super-vl-nvidia-repository-gtc-berlino.md]

## Azienda di riferimento

- [[nvidia]]

## Timeline delle notizie

- **2026-10-15** — Nemotron 3.5 Super VL, modello visione-linguaggio da circa 121 miliardi di parametri con 13 attivi, non è ancora annunciato ma il codice per farlo girare è già nei repository NVIDIA: il 9 ottobre l'autore Chen Cui ha ritirato la guida (la pagina risponde 404) e il GTC di Berlino dal 20 al 22 ottobre resta una finestra possibile, non una conferma. [Fonte: raw/pillitteri/pillitteri20261015-nemotron-3-5-super-vl-nvidia-repository-gtc-berlino.md]
- **2026-10-16** — Nemotron 3.5 Super VL combina ragionamento e uso di tool con comprensione di testo, immagini, documenti e video, da 120 miliardi di parametri, pensato per agenti di lunga durata e rilasciato come open source. [Fonte: raw/puntate/ainews20261016.md] Secondo VentureBeat la presentazione include anche Bolt 74B-A9B e la variante Bolt E4B per dispositivi, con pesi accessibili e opzioni commerciali; i confronti su benchmark specifici non dimostrano superiorità generale. [Fonte: raw/controrumore/controrumore20261016-diario-ai-lintelligenza-artificiale.md]




## Collegamenti

- [[nemotron]]
- [[nvidia]]
- [[index]]
