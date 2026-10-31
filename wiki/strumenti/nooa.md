---
title: "NOOA"
category: strumento
tags: [agent, framework, nvidia, python]
related_puntate: [20260804]
created: 2026-08-12
updated: 2026-07-29
sources: [raw/puntate/ainews20260804.md, raw/pillitteri/pillitteri20260729-open-secure-ai-alliance-52-soci-assenze.md]
---

# NOOA

## Introduzione

Framework di NVIDIA per definire agenti IA come singole classi Python, in cui i metodi diventano azioni del modello e i campi mantengono lo stato.

## Funzionalità principali

- NOOA di NVIDIA permette di definire un agente come una singola classe Python: i metodi sono le azioni del modello, i campi mantengono lo stato e se il corpo del metodo è vuoto un LLM lo riempie a runtime.

## Azienda / Autore

- [[nvidia]]

## Timeline delle notizie

- **2026-07-29** — NOOA è il contributo tecnico che [[nvidia]] porta all'Open Secure AI Alliance: il framework di ricerca in Python struttura gli agenti come classi, le docstring dei metodi diventano i prompt e le annotazioni di tipo definiscono il contratto con il modello, con l'obiettivo di rendere il comportamento di un agente testabile, tracciabile e verificabile come il software normale. Il repository NVIDIA-NeMo/labs-OO-Agents è stato creato il 20 luglio 2026 e al 29 luglio conta 482 stelle, 62 fork e 12 issue aperte, con l'ultimo tag alla versione v0.0.6; gli autori avvertono nella documentazione che i controlli sull'albero sintattico astratto e le liste di moduli vietati non costituiscono un confine di contenimento, quindi un agente che genera ed esegue codice va isolato a livello di sistema operativo. [Fonte: raw/pillitteri/pillitteri20260729-open-secure-ai-alliance-52-soci-assenze.md]

- **2026-08-04** — NOOA di NVIDIA permette di definire un agente come una singola classe Python: i metodi sono le azioni del modello, i campi mantengono lo stato e se il corpo del metodo è vuoto un LLM lo riempie a runtime. [Fonte: raw/puntate/ainews20260804.md]

## Collegamenti

- [[nvidia]]
- [[index]]

