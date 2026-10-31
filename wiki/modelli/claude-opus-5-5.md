---
title: "Claude Opus 5.5"
category: modello
tags: [claude, opus, modello, AI]
related_puntate: [20261016, 20261017]
created: 2026-10-16
updated: 2026-10-30
sources: [raw/myclaw/myclaw20261016-mckinsey-makes-candidates-debate-ai.md, raw/pillitteri/pillitteri20260921-leak-claude-opus-5-5-prezzi-lancio-martedi.md, raw/puntate/ainews20261017.md, raw/pillitteri/pillitteri20261017-claude-opus-5-5-prototipo-incendi-boschivi-dilum-sanjaya.md, raw/pillitteri/pillitteri20261024-anthropic-mythos-5-aisi-analisi-allineamento.md, raw/pillitteri/pillitteri20261025-claude-opus-5-5-blocca-reverse-engineering-smart-tv.md, raw/controrumore/controrumore20261030-diario-ai-fiducia-denaro-e-controlli.md]
---

# Claude Opus 5.5

## Introduzione

Sviluppato da Brandon Thomas, Claude Opus 5.5 è stato usato per creare repliche open-source di Microsoft Office: WordCraft, GridCraft e DeckCraft. Questi strumenti, scritti in Rust, supportano i formati di file Microsoft Office e imitano interfacce familiari, ma sono ancora in alpha con notevoli gap di funzionalità e affidabilità prima di sostituire Office.

## Azienda di riferimento

- [[anthropic]]

## Timeline delle notizie

- **2026-10-17** — Nel test del framework robotico [[nvidia-aspire|ASPIRE]] 1.0 di NVIDIA, Opus 5.5 supera leggermente il modello Astra, in una giornata in cui il team satura al 99% i benchmark robotici. [Fonte: raw/puntate/ainews20261017.md]
- **2026-10-17** — L'account ufficiale @claudeai mette in vetrina sei progetti della community e apre l'elenco con un prototipo di analisi degli incendi boschivi costruito con Opus 5.5 dall'ingegnere e creative coder Dilum Sanjaya: il programma ricostruisce su un rilievo 3D come il fuoco avanza nel tempo e dove stanno i punti caldi. Il video originale porta la data dell'8 ottobre e ha superato le 235.000 visualizzazioni, il rilancio di Claude oltre 200.000; il prototipo esiste però solo come video, senza codice né demo online, e Sanjaya non dice se i dati su incendio, droni e squadre siano reali o simulati. Resta un lavoro di interfaccia e non uno strumento di analisi: i dati sui focolai esistono già (FIRMS della NASA, EFFIS europeo), manca un modo rapido di leggerli insieme al terreno e ai mezzi sul campo. [Fonte: raw/pillitteri/pillitteri20261017-claude-opus-5-5-prototipo-incendi-boschivi-dilum-sanjaya.md]
- **2026-10-24** — Nel test ripetuto da Anthropic sugli stessi trascritti di Mythos 5, Opus 5.5 cerca il repository da attaccare tra lo 0 e il 13 per cento delle volte e si ferma da solo nel 10 per cento dei campioni sul momentum, contro lo 0 per cento di Mythos 5 e il 62 per cento di un modello interno di ricerca. I risultati sono off-policy, cioè ottenuti partendo da trascrizioni scritte da Mythos 5, e Anthropic ammette che nessuno dei modelli nuovi si ferma sempre. [Fonte: raw/pillitteri/pillitteri20261024-anthropic-mythos-5-aisi-analisi-allineamento.md]
- **2026-10-25** — Dal 21 ottobre su r/Claude e r/ClaudeAI gli utenti segnalano che Opus 5.5 interrompe a metà risposta alcune richieste di reverse engineering, compreso il re-root di una smart TV: compare un avviso che attribuisce lo stop alle salvaguardie cyber e propone il passaggio a Opus 4.8, che a sua volta si ferma su un pacchetto con «root» nel nome. Anthropic non ha annunciato né commentato modifiche, e nel post del 22 settembre scrive di instradare la maggior parte dei compiti cyber su Opus 4.8 lasciando a Opus 5.5 ricerca e correzione dei bug di routine. [Fonte: raw/pillitteri/pillitteri20261025-claude-opus-5-5-blocca-reverse-engineering-smart-tv.md]
- **2026-10-30** — Nel benchmark [[vibench-2]] di [[replit]] ha completato tutti i test nel 49 per cento delle build, dietro [[gpt-6-1-sol]] (65 per cento) e [[gpt-6-astra]] (60 per cento). [Fonte: raw/controrumore/controrumore20261030-diario-ai-fiducia-denaro-e-controlli.md]













## Collegamenti

- [[anthropic]]
- [[nvidia-aspire]]
- [[index]]
