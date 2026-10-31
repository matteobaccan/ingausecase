---
title: "Memoria AI"
category: trend
tags: [memoria, second-brain, token]
related_puntate: [20260726, 20260731, 20260801, 20260907, 20260910, 20260916, 20260917, 20260927, 20260928]
created: 2026-08-12
updated: 2026-10-28
sources: [raw/puntate/ainews20260726.md, raw/puntate/ainews20260731.md, raw/puntate/ainews20260801.md, raw/puntate/ainews20260907.md, raw/puntate/ainews20260910.md, raw/puntate/ainews20260916.md, raw/puntate/ainews20260917.md, raw/pillitteri/pillitteri20260814-openai-computer-history-chatgpt-mac-chronicle.md, raw/puntate/ainews20260927.md, raw/puntate/ainews20260928.md, raw/controrumore/controrumore20261003-diario-ai-lai-ridisegna-lavoro-tribunali.md, raw/controrumore/controrumore20261014-diario-ai-sicurezza-lavoro-e-nuovi.md, raw/tldr/tldr20261021.md, raw/tldr/tldr20261028.md]
---

# Memoria AI

## Introduzione

Tema trasversale sulla memoria persistente per gli agenti: sistemi per ricordare tra sessioni, tagliare i token e costruire knowledge base personali.

## Attori coinvolti

- [[anthropic]]
- [[andrej-karpathy]]
- [[mem0]]
- [[memmy]]
- [[memos]]

## Timeline delle notizie

- **2026-07-26** — book-to-skill trasformava qualsiasi libro in una skill consultabile capitolo per capitolo, caricando i capitoli solo quando servono. [Fonte: raw/puntate/ainews20260726.md]
- **2026-07-31** — Mem0 ha testato la memoria in Claude Code: 13.700 token contro 445 con memoria attiva; Karpathy ha condiviso un'architettura per un second brain persistente con Obsidian. [Fonte: raw/puntate/ainews20260731.md]
- **2026-08-01** — Metis ha integrato la memoria direttamente nell'architettura del modello senza RAG esterno; MemOS ha ridotto del 61 percento il consumo di token per gli agenti. [Fonte: raw/puntate/ainews20260801.md]
- **2026-09-07** — Manuale tecnico sulla KV cache: tensori memorizzati, formule di memoria, calcoli per MHA/GQA/MQA, prefill vs decode, MLA, PagedAttention, riuso prefissi, quantizzazione ed eviction, basato su paper originali e documentazione framework. [Fonte: raw/puntate/ainews20260907.md]
- **2026-09-10** — Memmy, sistema open source, unifica la memoria tra Codex, Grok e Cursor: cambio finestra con zero perdite; chiedendo di ritrovare un progetto recupera obiettivi, decisioni, prodotti e prossimo passo, tutto collegato. [Fonte: raw/puntate/ainews20260910.md]

- **2026-09-16** — [[anthropic]] pubblica un white paper di tredici pagine sulla memoria degli agenti e la divide in cinque livelli: memoria di lavoro, episodica, semantica, procedurale e il **motore di oblio**. L'ultimo è il pezzo controintuitivo, perché un agente che non dimentica mai finisce per impazzire, con conflitti tra preferenze vecchie e istruzioni nuove; nei test reali il pacchetto riduce i token del 90 percento e la latenza del 91 percento. Nella lettura che ne fa la puntata del 17 settembre lo stesso documento porta due casi di misura: [[mem0]] passa da 26.000 a 1.800 token per query e Snowflake, aggiungendo un'ontologia, guadagna il 20 percento di precisione con il 39 percento di chiamate in meno. [Fonte: raw/puntate/ainews20260917.md]
- **2026-08-14** — [[openai]] attiva [[computer-history|Computer History]] sull'app desktop per macOS: invece di catturare screenshot e leggerli con l'OCR come faceva l'anteprima Chronicle, la funzione legge gli eventi di interazione dalle API di accessibilità e ne ricava promemoria testuali che [[chatgpt]] e [[codex]] usano nelle conversazioni successive, con i file salvati in Markdown sotto `~/.codex/memories/extensions/skysight/`. [Fonte: raw/pillitteri/pillitteri20260814-openai-computer-history-chatgpt-mac-chronicle.md]
- **2026-08-14** — Gli eventi grezzi restano sul Mac in file temporanei per un massimo di 48 ore e i riassunti passano dai server di OpenAI, che dichiara di non conservarli dopo l'elaborazione né di usarli per addestrare i modelli; i file di memoria restano però in chiaro e non cifrati e la documentazione riconosce che la funzione aumenta la superficie di attacco, perché una pagina ostile può inserire comandi che il modello legge dalla cronologia. [Fonte: raw/pillitteri/pillitteri20260814-openai-computer-history-chatgpt-mac-chronicle.md]

- **2026-09-28** — Su GitHub si moltiplicano i progetti che impediscono agli agenti di ripartire da zero a ogni nuova sessione: [[mem0]], Hindsight, [[cognee]] e [[graphiti]] trasformano esperienze e conversazioni in grafi di conoscenza persistenti, in modo che l'agente ricordi, colleghi, recuperi e agisca, con centinaia di migliaia di stelle cumulative. [Fonte: raw/puntate/ainews20260928.md]
- **2026-10-02** — Context Language Models propone di affidare al modello la gestione del proprio contesto, trattandolo come un file che il sistema può leggere, riscrivere e organizzare durante l'esecuzione, con l'impostazione estesa ai sistemi multi-agente: su BrowseComp-Plus l'approccio zero-shot migliora l'accuratezza dell'11,4% usando il 21,5% di FLOPs in meno, e su EdgeBench a dodici ore aumenta il punteggio del 5% con il 59% di compute in meno. [Fonte: raw/controrumore/controrumore20261003-diario-ai-lai-ridisegna-lavoro-tribunali.md]
- **2026-10-14** — Uno studio su modelli della famiglia DeepSeek V4 segnala che le tecniche di compressione della memoria possono compromettere il recupero dei dettagli nei contesti lunghi: in prove fino a circa 128.000 token la precisione varia anche di quaranta punti percentuali a seconda della posizione delle informazioni, e la ricerca non è ancora sottoposta a revisione paritaria. [Fonte: raw/controrumore/controrumore20261014-diario-ai-sicurezza-lavoro-e-nuovi.md]
- **2026-10-21** — Databricks presenta [[memcurrent]], architettura di memoria persistente per agenti in produzione che secondo l'azienda triplica il tasso di successo rispetto a un agente senza memoria, riducendo anche tempi e costi. [Fonte: raw/tldr/tldr20261021.md]
- **2026-10-28** — I ricercatori di Google propongono il «sleep framework», un ciclo periodico in cui il modello alterna l'interazione attiva alla consolidazione offline della memoria, così da integrare nuovi fatti senza dimenticanze catastrofiche né tagli statici della conoscenza. Ne rivendicano la capacità di trattenere conoscenza su contesti fino a 10 milioni di token e di migliorare il ragionamento complesso. [Fonte: raw/tldr/tldr20261028.md]













## Collegamenti

- [[anthropic]]
- [[andrej-karpathy]]
- [[company-brain]]
- [[mem0]]
- [[memmy]]
- [[memos]]
- [[index]]

