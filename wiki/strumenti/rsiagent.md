---
title: "RSIAgent"
category: strumento
tags: [agent, self-improvement, framework, open-source, benchmark]
related_puntate: [20260916]
created: 2026-09-16
updated: 2026-09-16
sources: [raw/puntate/ainews20260916.md]
---

# RSIAgent

## Introduzione

Framework per l'auto-miglioramento ricorsivo attraverso l'esplorazione autonoma: l'agente non viene riaddestrato, impara a usare meglio se stesso. I pesi del modello restano fissi e la crescita sta in ciò che l'agente sceglie di esplorare e in ciò che decide di ricordare. [Fonte: raw/puntate/ainews20260916.md]

## Funzionalità principali

- Il ciclo è esplicito: l'agente decide cosa esplorare, esegue il task, verifica il risultato e consolida in memoria le relazioni stabili azione-condizione-risultato, cioè la conoscenza su cosa ha funzionato in quale situazione. [Fonte: raw/puntate/ainews20260916.md]
- Modelli base dichiarati: [[kimi-k3]] e GLM 5.3, con i pesi fissi e nessun fine-tuning. [Fonte: raw/puntate/ainews20260916.md]
- Numeri dichiarati: 78,98% di Partial Score su OSWorld 2.0, contro il 72,60% di [[gpt-6-astra]], e 84,82% su Agents' Last Exam. [Fonte: raw/puntate/ainews20260916.md]

## Performance

Il confronto che il progetto mette in evidenza è con un modello di frontiera su un ambiente di computer use: RSIAgent supera [[gpt-6-astra]] di circa sei punti percentuali sul Partial Score di OSWorld 2.0, pur appoggiandosi a modelli base con i pesi congelati. [Fonte: raw/puntate/ainews20260916.md]

## Repository

La puntata non riporta l'indirizzo del repository né il numero di stelle: RSIAgent è presentato con licenza e natura di framework, senza dettagli di pubblicazione. [Fonte: raw/puntate/ainews20260916.md]

## Timeline delle notizie

- **2026-09-16** — RSIAgent viene presentato come framework di auto-miglioramento ricorsivo per esplorazione autonoma: pesi fissi, [[kimi-k3]] e GLM 5.3 come modelli base, 78,98% di Partial Score su OSWorld 2.0 contro il 72,60% di [[gpt-6-astra]] e 84,82% su Agents' Last Exam. [Fonte: raw/puntate/ainews20260916.md]

## Collegamenti

- [[agenti-ai]]
- [[gpt-6-astra]]
- [[kimi-k3]]
- [[loop-engineering]]
- [[openrsi]]
- [[index]]
