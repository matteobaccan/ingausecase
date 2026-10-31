---
title: "Headroom"
category: strumento
tags: [agent, compressione, context, efficienza, open-source, proxy, rag, token]
related_puntate: [20260613, 20260615, 20260618, 20260619, 20260620, 20260621, 20260630]
created: 2026-08-12
updated: 2026-10-11
---

# Headroom

## Introduzione

Proxy/strumento di un ingegnere Netflix che comprime il contesto prima dell'invio agli agenti, risparmiando fino al 95% dei token.

## Funzionalità principali

- Headroom comprime log, JSON e chunk RAG: sessanta-novantacinque percento meno token con le stesse risposte, validato su GSM8K, TruthfulQA e SQuAD; novantaquattro punto nove percento di compressione con novantotto punto due percento di recall su pagine HTML; funziona come libreria Python, proxy HTTP o server MCP.
- Creato da un ingegnere di Netflix, comprime tutto quello che l'agente IA legge prima che raggiunga il LLM (output di tool, log, file, chunk RAG, ricerca codice, cronologia): risparmio dichiarato del sessanta-novantacinque percento di token senza perdita di qualità; supporta Python, TypeScript, proxy locale e server MCP, con wrapper per Claude Code, Codex, Cursor, Aider e Copilot.
- Un proxy sviluppato da un ingegnere Netflix riduce l'uso di token AI dal sessanta al novantacinque percento: zero modifiche al codice, accuratezza invariata, ventinove punto nove K stelle su GitHub e licenza Apache due punto zero.

## Azienda / Autore

- [[cursor]]
- [[netflix]]

## Timeline delle notizie

- **2026-06-13** — Headroom comprime log, JSON e chunk RAG: sessanta-novantacinque percento meno token con le stesse risposte, validato su GSM8K, TruthfulQA e SQuAD; novantaquattro punto nove percento di compressione con novantotto punto due percento di recall su pagine HTML; funziona come libreria Python, proxy HTTP o server MCP.
- **2026-06-15** — Creato da un ingegnere di Netflix, comprime tutto quello che l'agente IA legge prima che raggiunga il LLM (output di tool, log, file, chunk RAG, ricerca codice, cronologia): risparmio dichiarato del sessanta-novantacinque percento di token senza perdita di qualità; supporta Python, TypeScript, proxy locale e server MCP, con wrapper per Claude Code, Codex, Cursor, Aider e Copilot.
- **2026-06-18** — Un proxy sviluppato da un ingegnere Netflix riduce l'uso di token AI dal sessanta al novantacinque percento: zero modifiche al codice, accuratezza invariata, ventinove punto nove K stelle su GitHub e licenza Apache due punto zero.
- **2026-06-19** — Un ingegnere Netflix ha trovato un modo per ridurre l'uso di token del novantacinque percento: comprime il contesto prima di inviarlo a Claude, Cursor e Codex, gira al cento percento in locale e conta ventiquattromila stelle su GitHub.
- **2026-06-20** — Un ingegnere Netflix ha rilasciato Headroom su GitHub: trentacinquemila stelle in pochi giorni; è un proxy locale che comprime i dati prima di inviarli a Claude o Cursor, riducendo fino al novantacinque percento i token e mantenendo tutto sul proprio computer. Il nome dell'autore è Tejas Chopra e il progetto, Apache 2.0, ruota attorno a sei compressori specializzati per tipo di contenuto — ContentRouter, SmartCrusher per il JSON, CodeCompressor via AST, Kompress-base per la prosa, CacheAligner e CCR per la compressione reversibile — con quattro modi di integrazione (libreria, proxy, comando `wrap`, server MCP); la cache locale degli originali occupa però memoria e il modello Kompress-base rende meno sui testi non inglesi.
- **2026-06-20** — L'aggiornamento del 15 luglio 2026 porta Headroom a 59.209 stelle, con il repository rinominato `headroomlabs-ai/headroom` e Tejas Chopra uscito da Netflix per costruire Headroom Labs a tempo pieno; la promessa si restringe, perché il taglio del 60-95 per cento vale ora solo per i dati JSON mentre per gli agenti di coding scende al 15-20 per cento. Nel frattempo il progetto aggiunge la riduzione dei token in uscita con verbosity steering ed effort routing gestiti dal proxy.
- **2026-06-21** — Headroom è un proxy locale che comprime log, JSON e codice prima dell'invio al modello: riduce i token fino al novantacinque percento senza modificare una riga di codice, tutto rimane locale e nessun dato esce dalla macchina.
- **2026-06-30** — Comprime tutto prima che arrivi al LLM: 60-95% meno token, compatibile con tutti gli agenti, stesse risposte.
- **2026-07-11** — Headroom, 58.462 stelle e licenza Apache 2.0, comprime al confine con l'API di Anthropic tutto quello che passa — output dei tool, log, blocchi RAG, file e cronologia — con una riduzione dichiarata fino al 60-95 per cento sui dati JSON e del 15-20 per cento sugli agenti di codice. Si offre come libreria con una funzione `compress(messages)`, come proxy drop-in o come server MCP con i tool headroom_compress e headroom_retrieve, e la compressione è reversibile perché gli originali restano in cache.




## Collegamenti

- [[claude-code]]
- [[code2lora]]
- [[codex]]
- [[cursor]]
- [[netflix]]
- [[index]]

