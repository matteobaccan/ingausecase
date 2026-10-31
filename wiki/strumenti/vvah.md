---
title: "Visa Vulnerability Agentic Harness"
category: strumento
tags: [sicurezza, open-source, agent, vulnerability, visa]
related_puntate: []
created: 2026-09-30
updated: 2026-09-30
---

# Visa Vulnerability Agentic Harness

## Introduzione

Framework open source di [[visa]] che usa agenti IA per scoprire, verificare e correggere vulnerabilità nel software, con controllo umano su ogni fase critica: pipeline model-agnostic in quattro fasi e undici stadi (S1-S11) che combina controlli deterministici e policy gate con il ragionamento dei modelli, nasce da Project Glasswing con [[anthropic]].

## Funzionalità principali

- Quattro fasi: scoperta e modellazione (S1-S3), analisi profonda con verifica avversariale (S4-S6), sintesi e reportistica in Markdown e SARIF (S7-S9), correzione con convalida avversariale (S10-S11).
- Model-agnostic: supporta Claude di Anthropic e modelli compatibili con le API OpenAI, la correzione automatica del codice richiede però Anthropic.
- Licenza Apache 2.0, requisiti Python 3.11 e chiave API Anthropic.
- Metrica MTTA (Mean Time to Adapt) al posto di MTTD e conteggio CVE: freshness dell'inventario, percorsi d'attacco sfruttabili per release e tempo di ciclo della validazione.

## Repository

- GitHub: 2.816 stelle e 408 fork (da 595 stelle il 20 luglio), decine di migliaia di sviluppatori che lo hanno installato; Anthropic ha messo a disposizione fino a 100 milioni di dollari in crediti per Project Glasswing, più 4 milioni per il lavoro open source.

## Azienda / Autore

- [[visa]], con [[anthropic]]

## Timeline delle notizie

- **2026-09-30** — Visa rende open source il Visa Vulnerability Agentic Harness, il framework agentic che ha scovato decine di migliaia di falle: dentro Project Glasswing, Claude Mythos ha mostrato di concatenare debolezze minori in catene di exploit funzionanti contro l'infrastruttura di pagamento, e la risposta di Visa è "in un mondo di attacchi agentici, anche la difesa deve essere agentica" (Rajat Taneja); con VVAH alcuni cicli di correzione passano da settimane a poche ore.

## Collegamenti

- [[visa]]
- [[anthropic]]
- [[claude-mythos-5]]
- [[bug-hunting-ai]]
- [[index]]
