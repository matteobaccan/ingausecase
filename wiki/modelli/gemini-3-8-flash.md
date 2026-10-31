---
title: "Gemini 3.8 Flash"
category: modello
tags: [coding, frontier, google, llm, lavoro-agente]
related_puntate: [20260903]
created: 2026-09-03
updated: 2026-09-01
sources: [raw/puntate/ainews20260903.md, raw/pillitteri/pillitteri20260902-google-gemini-3-8-flash-cyber.md, raw/pillitteri/pillitteri20260901-gemini-3-8-flash-leak-tencent.md]
---

# Gemini 3.8 Flash

## Introduzione

Modello di Google, terzo rilascio Flash in sei settimane (dopo Gemini 3.7 Flash), con miglioramenti significativi su software engineering, task agentici e ragionamento multi-step. Fa parte della famiglia [[gemini]].

## Capacità e performance

- Terzo rilascio Flash in sei settimane, con miglioramenti significativi rispetto a Gemini 3.7 Flash su software engineering, task agentici e ragionamento multi-step.
- Sul benchmark DeepSWE V uno virgola uno, sembra superare la maggior parte dei modelli frontier più grandi nel risolvere autonomamente problemi engineering complessi end-to-end, a una frazione del costo.
- La differenza più concreta rispetto al 3.7 sta nella diligenza: il modello prende qualche passo di ragionamento in più sui problemi complessi, chiama gli strumenti in modo iterativo e a livelli di sforzo alti consuma più token pur di chiudere il compito, l'opposto della fretta che era il difetto tipico delle versioni Flash. [Fonte: raw/pillitteri/pillitteri20260902-google-gemini-3-8-flash-cyber.md]
- Segna 54,9% su HLE-Verified e su compiti verticali come l'analisi finanziaria (Vals Finance Agent v2) e legale (Harvey's Legal Agent) supera sia il 3.7 sia rivali più costosi, mentre su DeepSWE v1.1 resta dietro a Claude Opus 5 (71% contro 74%). [Fonte: raw/pillitteri/pillitteri20260902-google-gemini-3-8-flash-cyber.md]
- Prezzo: 0,75 dollari per milione di token in ingresso e 3,75 in uscita, tariffa introduttiva valida fino al 31 dicembre 2026, poi 1,50 e 7,50; sei o sette volte più economico di Claude Opus 5 (5,00 e 25,00) e di GPT-5.6 Sol (4,00 e 20,00). [Fonte: raw/pillitteri/pillitteri20260902-google-gemini-3-8-flash-cyber.md]

## Azienda di riferimento

- [[google]]

## Strumenti correlati

- [[gemini-3-7-flash]]

## Timeline delle notizie

- **2026-09-02** — Google rilascia il modello, presentato come il più intelligente dell'azienda per ragionamento e coding alla stessa velocità e allo stesso costo del predecessore, e lo distribuisce ovunque: Google AI Studio, Android Studio, Antigravity, l'API, Gemini Enterprise, l'app Gemini per gli abbonati Pro e Ultra, la modalità AI della Ricerca e i Fogli Google. In Italia è raggiungibile da subito via API e AI Studio, senza attese di rollout geografico. Il rilascio arriva a tre settimane dal 3.7, terzo Flash in sei settimane, mentre nello stesso periodo DeepSeek porta V4 Flash in locale e Zhipu svela un altro Flash a pesi aperti. [Fonte: raw/pillitteri/pillitteri20260902-google-gemini-3-8-flash-cyber.md]
- **2026-09-03** — Google ha rilasciato Gemini tre virgola otto Flash, terzo rilascio Flash in sei settimane, con miglioramenti significativi rispetto a Gemini tre virgola sette Flash su software engineering, task agentici e ragionamento multi-step; sul benchmark DeepSWE uno virgola uno sembra superare la maggior parte dei modelli frontier nel risolvere autonomamente problemi engineering end-to-end a una frazione del costo. [Fonte: raw/puntate/ainews20260903.md]

- **2026-09-01** — L'unica traccia pubblica è una menzione in un paper di Tencent del 10 agosto, dove il nome compare una volta tra i tre giudici automatici usati nello studio accanto a GPT-5.5 e Claude Opus 4.8, tre giorni prima del rilascio di Gemini 3.7 Flash. Il 2 settembre il Wall Street Journal scrive che il modello, con nome in codice interno "Skimaki", potrebbe uscire già il mercoledì successivo: nei test interni sulla piattaforma di coding Jetski gli ingegneri di Google lo avrebbero preferito al modello Opus di Anthropic sul codice, con capacità di programmazione nettamente migliorate. [Fonte: raw/pillitteri/pillitteri20260901-gemini-3-8-flash-leak-tencent.md]

## Collegamenti

- [[gemini-3-7-flash]]
- [[gemini-3-8-flash-cyber]]
- [[gemini-3-8-live]]
- [[gemini]]
- [[google]]
- [[index]]
