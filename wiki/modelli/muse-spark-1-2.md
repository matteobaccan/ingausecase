---
title: "Muse Spark 1.2"
category: modello
tags: [agent, beta, coding, generazione-app, llm, meta]
related_puntate: [20260806, 20260807, 20260903]
created: 2026-08-12
updated: 2026-10-04
sources: [raw/puntate/ainews20260806.md, raw/puntate/ainews20260807.md, raw/puntate/ainews20260903.md, raw/pillitteri/pillitteri20260807-muse-code-meta-spark-1-2-terminal-bench.md, raw/pillitteri/pillitteri20260813-meta-muse-glimmer-30b-open-weight-locale.md]
---

# Muse Spark 1.2

## Introduzione

Modello di generazione applicativa in beta: dall'idea alla produzione automatica con team di agenti che pianificano, scrivono e affinano il codice.

## Capacità e performance

- Muse Spark uno virgola due e' in beta: dall'idea alla produzione automatica, con un team di agenti che pianifica, scrive e affina, e deploy su repository multipli.
- Muse Code di Meta e' basato sul nuovo modello Spark uno virgola due, con skill predefinite e sub-agenti e prezzi sotto DeepSeek V4 Flash.
- Nei numeri pubblicati da Meta, tutti misurati dentro l'agente della casa, Muse Spark 1.2 raggiunge 82,9% su Terminal-Bench 2.1 (contro 86,7% di Claude Opus 5 in Claude Code, 81,8% di GPT-5.6 Terra in Codex, 81,6% di Grok 4.5 in Grok Build e 78,9% di Gemini 3.6 Flash in Antigravity CLI), 59,3% su DeepSWE 1.1 (dietro Opus 5 al 65,0% e Terra al 64,8%) e 70,6% sulla Meta Internal Coding Bench, con un contesto di 1.048.576 token. [Fonte: raw/pillitteri/pillitteri20260807-muse-code-meta-spark-1-2-terminal-bench.md]
- Il modello e l'agente sono co-addestrati: Muse Spark 1.2 ha visto durante l'addestramento le stesse tracce di strumenti, gli stessi formati di chiamata e le stesse strutture di approvazione che poi trova in Muse Code, una scelta che rende più difficile usarlo altrove. [Fonte: raw/pillitteri/pillitteri20260807-muse-code-meta-spark-1-2-terminal-bench.md]
- Non ha pesi scaricabili: il post di lancio non menziona nessun rilascio open weight, quindi il modello va trattato come una dipendenza ospitata da Meta, al contrario della linea Llama e dei laboratori cinesi con Kimi K3 e Qwen3.8-Max. [Fonte: raw/pillitteri/pillitteri20260807-muse-code-meta-spark-1-2-terminal-bench.md]
- Due tier di prezzo per lo stesso modello: standard a 1,25 dollari per milione di token in input e 4,25 in output, contributor a 0,10 in input e 0,20 in output in cambio dell'autorizzazione ad addestrare sui prompt inviati. [Fonte: raw/pillitteri/pillitteri20260807-muse-code-meta-spark-1-2-terminal-bench.md]

## Azienda di riferimento

- [[meta]]

## Strumenti correlati

- [[muse-code]]

## Timeline delle notizie

- **2026-08-06** — Muse Spark uno virgola due e' in beta: dall'idea alla produzione automatica, con un team di agenti che pianifica, scrive e affina, e deploy su repository multipli. [Fonte: raw/puntate/ainews20260806.md]
- **2026-08-07** — Muse Code di Meta e' basato sul nuovo modello Spark uno virgola due, con skill predefinite e sub-agenti e prijzen sotto DeepSeek V4 Flash. [Fonte: raw/puntate/ainews20260807.md]
- **2026-08-07** — I numeri dichiarati da Meta per Muse Spark 1.2 dentro Muse Code: 82,9% su Terminal-Bench 2.1, 59,3% su DeepSWE 1.1 e 70,6% sulla Meta Internal Coding Bench, con il salto di 6,7 punti sul predecessore nei compiti da terminale e il terzo posto su DeepSWE. Il documento metodologico avverte che gli strumenti dell'agente e i prompt di sistema non sono ottimizzati per i modelli concorrenti, quindi i confronti vanno letti come dichiarazione del fornitore; il modello resta senza pesi scaricabili e il tier contributor da 0,10 dollari per milione di token fa dei prompt di chi lo usa materia di addestramento. [Fonte: raw/pillitteri/pillitteri20260807-muse-code-meta-spark-1-2-terminal-bench.md]
- **2026-08-13** — Muse Glimmer è la versione distillata e aperta di Muse Spark 1.2, il modello chiuso lanciato il 5 agosto 2026: ne eredita gran parte delle capacità di ragionamento in un pacchetto abbastanza piccolo da stare su un portatile. [Fonte: raw/pillitteri/pillitteri20260813-meta-muse-glimmer-30b-open-weight-locale.md]



- **2026-09-03** — Meta ha lanciato Muse Spark uno virgola tre con un salto su coding e lavoro agente, promette prestaciones frontier a costi contenuti, disponibile in Muse Code e via API, in arrivo le versioni open weights. [Fonte: raw/puntate/ainews20260903.md]

## Collegamenti

- [[claude-opus-5]]
- [[gpt-5-6]]
- [[meta]]
- [[muse-code]]
- [[muse-spark]]
- [[muse-spark-1-3]]
- [[index]]

