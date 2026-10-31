---
title: "Cerebras"
category: azienda
tags: [cerebras, cloud, hardware, inference, inferenza, llm, usa]
related_puntate: [20260521, 20260701]
created: 2026-08-12
updated: 2026-10-28
sources: [raw/puntate/ainews20260521.md, raw/puntate/ainews20260701.md, raw/pillitteri/pillitteri20260925-chatgpt-pro-max-500-dollari-cerebras.md, raw/pillitteri/pillitteri20260214-gpt-codex-spark-modello-ai-coding-tempo-reale.md, raw/tldr/tldr20260928.md, raw/tldr/tldr20261023.md, raw/controrumore/controrumore20261028-diario-ai-sicurezza-mercati-e-agenti.md]
---

# Cerebras

## Introduzione

Azienda statunitense di hardware e cloud per l'inferenza AI, nota per velocità di inferenza estremamente elevate tramite i wafer-scale engine.

## Modelli

- [[gemma-4-31b]]

## Strumenti

- [[free-llms]]

## Timeline delle notizie

- **2026-05-21** — Cerebras è stata citata tra i 14 provider aggregati da Free LLMs, che offre 800 milioni di token gratuiti al mese. [Fonte: raw/puntate/ainews20260521.md]
- **2026-07-01** — Ha messo in anteprima pubblica Gemma 4 31B, primo modello multimodale sulla loro piattaforma, che gira a oltre 1.800 token al secondo per flussi di lavoro testo e immagini. [Fonte: raw/puntate/ainews20260701.md]
- **2026-09-25** — Il piano ChatGPT Pro Max da 500 dollari trapelato viene indicato come il primo indiziato dell'etichetta "Fastest": l'accordo pluriennale firmato con OpenAI porta online 750 megawatt di sistemi dedicati alle risposte a bassa latenza e ha prodotto GPT-5.3-Codex-Spark a febbraio e dal 13 agosto il livello Ultrafast con GPT-5.6 Sol, fino a 750 token al secondo e quattordici volte più veloce del servizio standard, oggi in anteprima limitata nelle API con prezzi mai comunicati. Il legame fra il piano e l'azienda resta però una deduzione di TestingCatalog, non un dato confermato. [Fonte: raw/pillitteri/pillitteri20260925-chatgpt-pro-max-500-dollari-cerebras.md]
- **2026-02-14** — GPT Codex Spark viene rilasciato il 12 febbraio 2026: genera oltre 1.000 token al secondo ed è il primo modello di OpenAI a girare su chip Cerebras invece che su [[nvidia]]. La scelta risponde al collo di bottiglia del coding agentico, dove ogni passaggio di un agente è una chiamata al modello e la velocità di generazione si moltiplica per decine o centinaia di passaggi. [Fonte: raw/pillitteri/pillitteri20260214-gpt-codex-spark-modello-ai-coding-tempo-reale.md]

- **2026-09-28** — L'Ultrafast API di [[openai]], in anteprima su [[gpt-5-6-sol]] con velocità dichiarate fino a 750 token di output al secondo e fino a 14 volte l'inferenza standard, è alimentata da hardware Cerebras: OpenAI ne prepara l'estensione a più utenti e l'accesso resta per ora limitato a clienti selezionati. [Fonte: raw/tldr/tldr20260928.md]
- **2026-10-23** — Spiega come distribuisce modelli frontier da mille miliardi di parametri su più wafer WSE-3T, ciascuno con 44 GB di memoria on-chip: i pesi da soli richiedono terabyte di memoria, quindi il modello viene riempito nella memoria on-chip e mappato su più chip, con una gestione dedicata delle richieste concorrenti. [Fonte: raw/tldr/tldr20261023.md]
- **2026-10-28** — [[oracle]] prevede di aggiungere i suoi acceleratori all'offerta cloud, insieme alle TPU di Google e agli acceleratori di SambaNova, accanto ai sistemi Nvidia Vera Rubin in espansione multi-gigawatt. Oracle non ha reso noto il valore dell'accordo né i tempi delle consegne. [Fonte: raw/controrumore/controrumore20261028-diario-ai-sicurezza-mercati-e-agenti.md]







## Collegamenti

- [[free-llms]]
- [[gemma-4-31b]]
- [[google]]
- [[index]]

