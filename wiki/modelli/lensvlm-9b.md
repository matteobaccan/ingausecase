---
title: "LensVLM-9B"
category: modello
tags: [visione, documenti, compressione, apple, token]
related_puntate: [20260925]
created: 2026-09-25
updated: 2026-09-27
---

# LensVLM-9B

## Introduzione

Modello di visione da nove miliardi di parametri rilasciato da [[apple]] su Hugging Face e presentato il 25 settembre 2026: è un fine-tuning di [[qwen-3-5]] dedicato alla compressione visiva dei documenti, che converte pagine e documenti enormi in thumbnail minuscole.

## Capacità e performance

- Analizza prima le thumbnail ed estrae il testo completo solo dalle pagine rilevanti per la domanda, con una riduzione dichiarata di spazio occupato, token e contesto.

## Timeline delle notizie

- **2026-09-25** — Apple rilascia su Hugging Face LensVLM-9B, fine-tuning di Qwen 3.5-9B per la compressione visiva dei documenti: le pagine diventano thumbnail minuscole, il modello le analizza per prime e il testo completo viene estratto solo dalle pagine pertinenti alla domanda, con un risparmio dichiarato di spazio e token.
- **2026-09-26** — Il rilascio nei dettagli: comparso sul profilo Apple di Hugging Face il 21 settembre, con il codice ufficiale su GitHub il 22; il paper, "LensVLM: Selective Context Expansion for Compressed Visual Representation of Text", è stato depositato su arXiv il 7 maggio 2026 con Roy Xie e Bhuwan Dhingra della Duke University tra i firmatari. Il modello rende il testo in pagine-immagine a tre livelli di compressione (5x, 10x o 15x), le scorre per capire dove sta la risposta e chiede il testo originale con lo strumento Expand (nella demo `read_page`) solo per le pagine scelte.
- **2026-09-26** — L'addestramento alterna una fase supervisionata su traiettorie generate da Qwen3.5-397B a un reinforcement learning con l'algoritmo DAPO, con un bonus per l'uso dello strumento che scatta solo se la risposta è corretta; il comportamento di ricerca-e-ingrandimento compare solo a 9 miliardi di parametri, perché i modelli da 2B e 4B imparano la sintassi ma non sanno scegliere le pagine. I numeri del paper: compressione effettiva 4,3x, fino a 10,1x su sette benchmark di domande e risposte, circa 69 per cento di accuratezza a 5x contro il 31 senza strumento di espansione.
- **2026-09-26** — I numeri riportati da Lookonchain, che la fonte non ritrova nel paper, quantificano lo scambio: su un documento di cento pagine 8.090 token contro 51.273 in formato testo e una KV cache da 253 MB contro 1,6 GB, al prezzo di 68,9 per cento di accuratezza in 17 secondi contro 72,4 in 8 secondi con il testo intero. I pesi escono con la Apple Machine Learning Research Model License, che consente il solo uso di ricerca e vieta prodotti e servizi commerciali anche per i modelli derivati, e il repository `ml-lensvlm` aveva 74 stelle e 6 fork; i pesi funzionano con Transformers, vLLM e SGLang.

## Collegamenti

- [[apple]]
- [[headroom]]
- [[qwen-3-5]]
- [[rag-over-retrieval]]
- [[unlimited-ocr]]
- [[index]]
