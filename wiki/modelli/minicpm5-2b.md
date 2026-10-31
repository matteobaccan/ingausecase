---
title: "MiniCPM5-2B"
category: modello
tags: [2b, edge, efficiente, open-source, open-weight, agent, ragionamento]
related_puntate: [20260908]
created: 2026-09-08
updated: 2026-09-21
---

# MiniCPM5-2B

## Introduzione

Modello da 2 miliardi di parametri di [[openbmb]] che porta intelligenza avanzata su dispositivi edge. Primo tra i modelli open source sotto i 4 miliardi di parametri secondo l'Artificial Analysis Intelligence Index, con punteggio di 23. Completamente open source, inclusi dati, ricette di training e stack RL.

## Capacità e performance

- Intelligenza avanzata per edge, con capacità agent di uso generale direttamente su dispositivi edge.
- Primo tra i modelli open source sotto i 4 miliardi di parametri sull'Artificial Analysis Intelligence Index (punteggio 23).
- Raggiunge 20 sull'Agentic Index.

## Disponibilità

- Completamente open source: dati, ricette di training e stack RL aperti. Open weight per deployment edge.

## Azienda di riferimento

- [[openbmb]]

## Timeline delle notizie

- **2026-09-08** — MiniCPM5-2B: modello da 2 miliardi di parametri per edge, primo tra gli open source sotto i 4B sull'Artificial Analysis Intelligence Index (23 punti) e 20 sull'Agentic Index, capacità agent generali su edge. Progetto completamente open source con dati, ricette di training e stack RL.

- **2026-09-21** — La news di Pillitteri ricostruisce i pesi pubblicati il 7 settembre 2026 da OpenBMB: 2,52 miliardi di parametri, solo testuale, contesto da 131.072 token, licenza Apache 2.0, architettura LlamaForCausalLM con 42 strati e attenzione a query raggruppate (16 teste per le query contro 2 per chiavi e valori) che gli permette di girare senza codice personalizzato, e un solo checkpoint con due modalità selezionabili dal parametro enable_thinking. Sul test set di 34 benchmark scelti dal laboratorio la media è 53,9 contro 51,1 di Qwen3.5-4B, con il vantaggio concentrato su codice e ragionamento — 69,1 contro 56,4 su LiveCodeBench v6, 46,4 contro 33,6 su SWE-bench Verified, 86,5 contro 78,8 su AIME 2025 — e la perdita su conoscenza e task lunghi (70,2 contro 77,1 su GPQA Diamond, 70,8 contro 78,0 su MMLU-Pro, 8,6 contro 25,8 su Terminal-Bench). Insieme ai pesi sono usciti i dati di addestramento UltraData-SFT-Agent-2609 (500.000 esempi agentici) e UltraData-RL-2609 (oltre 80.000 campioni) e i checkpoint intermedi Base e SFT.

## Collegamenti

- [[openbmb]]
- [[minicpm5-1b]]
- edge AI
- [[agenti-ai]]
- [[open-source]]
- [[index]]
