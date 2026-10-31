---
title: "Perplexity"
category: azienda
tags: [perplexity, usa, agent, ricerca, browser, memoria]
related_puntate: [20261008, 20261016, 20261021]
created: 2026-09-15
updated: 2026-10-25
sources: [raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md, raw/pillitteri/pillitteri20260620-perplexity-brain-memoria-agente-computer.md, raw/pillitteri/pillitteri20260828-perplexity-nvidia-portable-computer-agente-locale.md, raw/pillitteri/pillitteri20260902-perplexity-hybrid-compute-mac.md, raw/pillitteri/pillitteri20260915-perplexity-portable-computer-windows-rtx.md, raw/pillitteri/pillitteri20260925-perplexity-fast-search-photon-rust.md, raw/puntate/ainews20261008.md, raw/tldr/tldr20261008.md, raw/tldr/tldr20261016.md, raw/puntate/ainews20261016.md, raw/pillitteri/pillitteri20261018-siti-bloccano-agenti-ai-yelp-delta-jpmorgan.md, raw/puntate/ainews20261021.md, raw/tldr/tldr20261023.md, raw/pillitteri/pillitteri20261024-perplexity-decider-for-mac-decision-model-locale.md]
---

# Perplexity

## Introduzione

Azienda americana di ricerca AI, guidata dal cofondatore e CEO Aravind Srinivas, che ha esteso il suo prodotto dal motore di ricerca agli agenti: [[perplexity-computer]] nel cloud, [[perplexity-brain]] come memoria persistente, [[portable-computer]] in locale sul dispositivo e il browser [[comet]]. A inizio giugno 2026 ha raccolto 200 milioni di dollari per spingere Comet come porta d'ingresso alla cosiddetta agent economy. [Fonte: raw/pillitteri/pillitteri20260620-perplexity-brain-memoria-agente-computer.md]

Nel periodo è sotto pressione sul fronte legale — dalla causa del New York Times di fine 2025 alla disputa con Forbes — e cerca finanziamenti a valutazioni crescenti; la spinta sul calcolo locale diversifica il modello economico e allenta la dipendenza dal conteggio dei token. [Fonte: raw/pillitteri/pillitteri20260828-perplexity-nvidia-portable-computer-agente-locale.md]

## Strumenti

- [[comet]]
- [[perplexity-brain]]
- [[perplexity-computer]]
- [[portable-computer]]

## Modelli

- [[pii-tracer]]
- [[pplx-embed-v2-late]]

## Annunci recenti

- **25 febbraio 2026** — Presenta Perplexity Computer, definito da Srinivas un "lavoratore digitale di uso generale", con architettura a diciannove modelli di frontiera orchestrati e l'estensione Computer for Professional Finance. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- **18 giugno 2026** — Presenta Brain, il sistema di memoria persistente dell'agente Computer, in research preview per i piani Max ed Enterprise Max. [Fonte: raw/pillitteri/pillitteri20260620-perplexity-brain-memoria-agente-computer.md]
- **25 agosto 2026** — Annuncia Portable Computer con [[nvidia]]: l'agente gira per intero sul dispositivo, senza costi di token per il lavoro locale. [Fonte: raw/pillitteri/pillitteri20260828-perplexity-nvidia-portable-computer-agente-locale.md]

## Persone chiave

- Aravind Srinivas — cofondatore e CEO.

## Timeline delle notizie

- **2026-02-25** — Perplexity presenta Computer: un servizio cloud che fonde in un'unica interfaccia ragionamento profondo, ricerca web, generazione di documenti, scrittura di codice, esecuzione nel browser e automazione di flussi ripetuti nel tempo, orchestrando diciannove modelli di frontiera dentro microVM Firecracker. [Fonte: raw/pillitteri/pillitteri20260506-perplexity-computer-finanza-bloomberg-terminal-2026.md]
- **2026-06-18** — Perplexity presenta Brain, memoria persistente che costruisce un context graph del lavoro dell'agente invece di ricordare le preferenze dell'utente, con miglioramenti dichiarati del venticinque percento sulla correttezza, sedici sul recall e tredici percento di costo in meno per task. [Fonte: raw/pillitteri/pillitteri20260620-perplexity-brain-memoria-agente-computer.md]
- **2026-08-25** — Lancia Portable Computer su DGX Spark e PC Linux insieme a NVIDIA, con l'orchestratore, il harness e i modelli che girano sul dispositivo e l'escalation al cloud solo su autorizzazione dell'utente. [Fonte: raw/pillitteri/pillitteri20260828-perplexity-nvidia-portable-computer-agente-locale.md]
- **2026-09-01** — Attiva Hybrid Compute sull'app per Mac: i compiti di Computer si spezzano tra i modelli di frontiera nel cloud e un modello locale, con il classificatore PII-Tracer dietro il Privacy Gate. [Fonte: raw/pillitteri/pillitteri20260902-perplexity-hybrid-compute-mac.md]
- **2026-09-14** — Porta Portable Computer nell'app per Windows, scaricabile dal Microsoft Store e utilizzabile su GPU NVIDIA RTX o RTX PRO con almeno ventiquattro GB di VRAM. [Fonte: raw/pillitteri/pillitteri20260915-perplexity-portable-computer-windows-rtx.md]
- **2026-09-25** — Il 24 settembre Perplexity lancia Fast Search, la modalità della Search API che restituisce il 95 per cento dei risultati in 230 millisecondi o meno con una latenza mediana di 160, attivabile impostando search_type su "fast" in una richiesta a POST /search e disponibile dagli SDK Python 0.43.4 e TypeScript 0.38.5, oltre che via cURL. Il prezzo è la leva commerciale: un dollaro ogni mille richieste contro i cinque della ricerca web standard, cioè un quinto, che su un agente da venti ricerche per compito vale due centesimi invece di dieci e su un milione di compiti al mese fa la differenza fra 20.000 e 100.000 dollari. La modalità nasce per gli agenti, che devono cercare sul web decine di volte in un solo compito, e la documentazione stessa la consiglia per le chiamate di routine lasciando la ricerca standard alle domande rare, difficili o ambigue. [Fonte: raw/pillitteri/pillitteri20260925-perplexity-fast-search-photon-rust.md]
- **2026-10-08** — Perplexity rilascia in open source PPLX-Embed-v2-Late, embedding multi-vettore per testo e immagini in uno spazio condiviso, nelle versioni da nove e da zero virgola sei miliardi di parametri, con la piccola che gira on-device: permette di indicizzare dati multimodali e cercare nei PDF senza OCR, con il novantadue virgola quattro percento su MADQA e il sessantaquattro percento su BrowseComp+. [Fonte: raw/puntate/ainews20261008.md] [Fonte: raw/tldr/tldr20261008.md]
- **2026-10-16** — Rilascia come open source SPACE, la piattaforma sandbox che alimenta [[perplexity-computer]]: servirne milioni sotto traffico production richiede architettura specifica, ora disponibile all'ecosistema. [Fonte: raw/puntate/ainews20261016.md]
- **2026-10-18** — Nella causa con Amazon, il 4 agosto 2026 il Nono Circuito ha annullato l'ingiunzione che a marzo aveva fermato Comet, il browser agentico di [[perplexity]], sugli acquisti di Amazon, stabilendo che a entrare nei computer è l'utente e non Perplexity; il riesame chiesto da Amazon è stato respinto il 10 settembre, ma la causa torna in primo grado dove Amazon ha ampliato le accuse il 21 settembre. Secondo la ricostruzione di The Verge, Perplexity dice apertamente che il motivo economico è la pubblicità che i siti di terzi perdono. [Fonte: raw/pillitteri/pillitteri20261018-siti-bloccano-agenti-ai-yelp-delta-jpmorgan.md]
- **2026-10-21** — [[perplexity-computer]] ora gira completamente in locale su Mac, senza inferenza cloud e senza WiFi. [Fonte: raw/puntate/ainews20261021.md]
- **2026-10-23** — Pubblica JOLT, metodo di auto-distillazione che addestra lo stesso modello come insegnante e studente adattando il feedback alle capacità dello studente: dichiara miglioramenti su ragionamento matematico, coding e compiti agentici, insieme a una maggiore efficienza di addestramento. [Fonte: raw/tldr/tldr20261023.md]
- **2026-10-24** — Il 22 ottobre annuncia Decider for Mac, app da barra dei menu che tiene in memoria pplx-decider-flash-v1.2 ed espone la Decisions API in locale su 127.0.0.1:8080, senza chiave API e senza costi a consumo, richiedendo Apple silicon, macOS 13, 16 GB di memoria e circa 6 GB liberi. Chiude un pezzo della strategia locale già passata da Hybrid Compute e Portable Computer. [Fonte: raw/pillitteri/pillitteri20261024-perplexity-decider-for-mac-decision-model-locale.md]



















## Collegamenti

- [[comet]]
- [[nvidia]]
- [[pii-tracer]]
- [[portable-computer]]
- [[perplexity-brain]]
- [[perplexity-computer]]
- [[index]]
