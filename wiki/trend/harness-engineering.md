---
title: "Harness engineering"
category: trend
tags: [agenti, harness, prompt, memoria, ricerca, auto-miglioramento]
related_puntate: []
created: 2026-10-19
updated: 2026-10-19
sources: [raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md, raw/pillitteri/pillitteri20261018-harness2-google-agenti-ai-migliorano-da-soli.md]
---

# Harness engineering

## Introduzione

La disciplina che migliora un agente AI intervenendo sul suo harness, cioè su tutto ciò che sta attorno al modello linguistico - istruzioni di sistema, guardrail, memoria, guida agli strumenti, skill, script, sotto-agenti e plugin - lasciando congelati i pesi. A parità di modello il risultato cambia di diversi punti percentuali, e il paper di MBZUAI quantifica la sproporzione parlando del 98,4% di infrastruttura contro l'1,6% di AI. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]

## Evoluzione nel tempo

- Claude Code, Codex CLI di OpenAI, OpenCode e Gemini CLI sono prima di tutto degli harness: costruiscono il contesto che il modello legge, decidono quali strumenti può chiamare, conservano la memoria tra sessioni e controllano il ciclo di lavoro. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]
- Il 2026 ha portato cinque famiglie di metodi che non toccano i pesi: ricerca offline sull'harness (Meta-Harness), memoria di strategie (ReasoningBank), raffinamento per compito (Harness Scaling), evoluzione durante l'uso (TTHE e Recursive Harness Self-Improvement) e ricorsione su due livelli ([[harness2|Harness²]]). Più si sale di livello, meno si dipende da un punteggio esterno e più dal giudizio del modello su se stesso, con un guadagno di praticità e un costo di affidabilità. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]
- NVIDIA ha portato lo stesso Claude Opus 5 dal 30% al 100% su ARC-AGI-3 con AVO, cambiando soltanto ciò che sta attorno al modello; il DeepSeek Harness è nato come alternativa open source all'harness di Claude Code. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]

## Attori coinvolti

- [[google]] Cloud AI Research, autrice di [[harness2|Harness²]] con la Northwestern University.
- Stanford e MIT con KRAFTON, autori di Meta-Harness.
- Il gruppo di ReasoningBank, accettato a ICLR 2026.
- Wang e colleghi per Harness Scaling; Nie e altri per TTHE; Hyunin Lee, Matei Zaharia e Yujin Tang per Recursive Harness Self-Improvement.
- La community DAIR.AI, che il 15 ottobre 2026 ha indicato il paper di Harness² come lettura consigliata per chi costruisce harness su misura.

## Notizie rilevanti

- Gli otto componenti dell'harness si dividono per momento di attivazione: prompt di sistema, guardrail, memoria e guida agli strumenti sono sempre nel contesto; skill, script e sotto-agenti si caricano a richiesta; il plugin agisce dentro il ciclo degli strumenti. La distinzione che pesa di più è tra istruire e imporre: un prompt può essere ignorato, un plugin o un hook no. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]
- Meta-Harness cerca offline il miglior codice di harness e riporta 7,7 punti in più su una classificazione di testi, con quattro volte meno token di contesto, e 4,7 punti in più su 200 problemi di matematica olimpionica; ReasoningBank distilla strategie dalle esperienze riuscite e fallite senza cambiare strumenti o regole. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]
- Harness Scaling rivede l'harness a ogni compito senza memoria; su Terminal-Bench 2.1 l'evoluzione automatica non ha battuto il semplice test-time scaling e ha generalizzato male, mentre nei giochi a lungo orizzonte ha superato dell'80% su ARC-AGI-3 e dell'11% su EdgeBench la ricerca di riferimento. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]
- Il caso pratico più citato viene da JobBench: un compito di riconciliazione di file di produzione prese 43,1 con Gemini 3.5 Flash sotto OpenCode; un guardrail, uno script di verifica, una skill e una guida agli strumenti hanno portato il punteggio a 77,8. Le due regole trasferibili sono inventariare gli input all'inizio e riaprire gli output alla fine. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]
- Per misurare una modifica servono cinque o dieci compiti reali e ripetibili, ogni esecuzione ripetuta tre volte, cambiando un componente per volta; senza un criterio per dire che un risultato è migliore, nessun metodo automatico può aiutare. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]

## Timeline delle notizie

- **2026-10-09** - Il paper di Harness² su arXiv dedica una tabella ai metodi concorrenti e descrive la ricorsione su due livelli: modifiche provate sul singolo compito e una libreria di lezioni che orienta i compiti successivi, senza verificatore e senza risposte esatte. [Fonte: raw/pillitteri/pillitteri20261018-harness2-google-agenti-ai-migliorano-da-soli.md]
- **2026-10-15** - DAIR.AI indica il paper di Google sull'harnessing ricorsivo come lettura consigliata per chi costruisce harness su misura, sottolineando il tema dell'auto-miglioramento ricorsivo per compiti aperti. [Fonte: raw/pillitteri/pillitteri20261018-harness2-google-agenti-ai-migliorano-da-soli.md]
- **2026-10-18** - La guida di riferimento sull'harness engineering mette in fila gli otto componenti, le cinque famiglie di metodi pubblicati nel 2026 e ciò che si può copiare a mano oggi: un guardrail che inventaria gli input, uno script che riapre gli output e una guida agli strumenti per gli errori ricorrenti. [Fonte: raw/pillitteri/pillitteri20261018-come-migliorare-agente-ai-senza-riaddestrare-modello.md]

## Collegamenti

- [[agenti-ai]]
- [[harness2]]
- [[claude-code]]
- [[codex]]
- [[opencode]]
- [[google]]
- [[index]]
