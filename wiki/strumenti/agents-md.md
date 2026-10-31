---
title: "AGENTS.md"
category: strumento
tags: [agent, coding, standard, openai]
related_puntate: []
created: 2026-09-12
updated: 2026-10-23
sources: [raw/pillitteri/pillitteri20260517-claude-code-codex-7-lezioni-pratiche-migrazione.md, raw/pillitteri/pillitteri20260912-gpt-6-astra-prompt-meno-regole.md, raw/pillitteri/pillitteri20261023-agents-md-design-md-skill-md-agenti-ai.md]
---

# AGENTS.md

## Introduzione

File di istruzioni di progetto in Markdown diventato uno standard aperto per gli agenti di sviluppo: lo leggono [[codex]], Cursor, Jules, Amp e Factory, quindi un solo AGENTS.md nella radice del repository può guidare più strumenti senza duplicare lavoro. Nasce come traduzione del CLAUDE.md di [[claude-code]], ma richiede una riscrittura e non una semplice rinomina. [Fonte: raw/pillitteri/pillitteri20260517-claude-code-codex-7-lezioni-pratiche-migrazione.md]

## Funzionalità principali

- Dove Claude Code tende a interpretare le proprie istruzioni come preferenze conversazionali ("rispondi in italiano", "evita commenti superflui"), Codex tratta AGENTS.md come un manuale operativo: cosa testare, quali comandi di lint eseguire, quali cartelle ignorare, quali standard di commit usare. [Fonte: raw/pillitteri/pillitteri20260517-claude-code-codex-7-lezioni-pratiche-migrazione.md]
- La gerarchia di lookup di Codex è a overlay: prima ~/.codex/AGENTS.md, poi quello del repository, poi eventuali AGENTS.md nelle sottocartelle, con la ricerca che si ferma alla directory corrente. [Fonte: raw/pillitteri/pillitteri20260517-claude-code-codex-7-lezioni-pratiche-migrazione.md]
- Una struttura efficace prevede sezione di overview, regole di stile, comandi di validazione da eseguire prima di un PR e aree off-limits. [Fonte: raw/pillitteri/pillitteri20260517-claude-code-codex-7-lezioni-pratiche-migrazione.md]

## Casi d'uso

- Migrazione da Claude Code a Codex: rinominare CLAUDE.md in AGENTS.md è il primo passo, ma senza aggiungere istruzioni operative concrete l'agente comincia a improvvisare convenzioni di stile e a riempire i PR di refactoring non richiesti. [Fonte: raw/pillitteri/pillitteri20260517-claude-code-codex-7-lezioni-pratiche-migrazione.md]

## Azienda/autore

- Standard adottato da [[openai]] con Codex e dagli altri strumenti che vi aderiscono.

## Timeline delle notizie

- **2026-05-17** — La lezione numero uno della migrazione da Claude Code a Codex: AGENTS.md vince su CLAUDE.md, ma va riscritto, non solo rinominato. [Fonte: raw/pillitteri/pillitteri20260517-claude-code-codex-7-lezioni-pratiche-migrazione.md]

- **2026-09-12** — La guida di [[openai]] su [[gpt-6-astra]] cambia il modo di scriverli: l'imperativo assoluto ("prima di ogni modifica leggi questi tre file") va sostituito con una mappa che dica quale documento serve per cosa, così il modello carica il contesto giusto nel momento giusto invece di aprire mezzo repository per cambiare una virgola. È la stessa logica della progressive disclosure applicata alla memoria di progetto. [Fonte: raw/pillitteri/pillitteri20260912-gpt-6-astra-prompt-meno-regole.md]
- **2026-10-23** — Google Cloud propone uno schema a tre file Markdown con compiti separati: AGENTS.md per comandi, confini e convenzioni del repository, DESIGN.md per lo stile dell'interfaccia e SKILL.md per le procedure caricate solo quando servono. Un AGENTS.md efficace sta intorno alle dodici righe perché l'agente lo rilegge a ogni richiesta, e il formato pubblicato da OpenAI nell'agosto 2025 è passato alla Agentic AI Foundation a dicembre, con 25.057 stelle al 23 ottobre. [Fonte: raw/pillitteri/pillitteri20261023-agents-md-design-md-skill-md-agenti-ai.md]

- **2026-10-23** — Nello studio della Agentic AI Foundation citato da Google, un AGENTS.md da dodici righe su un'estensione per VS Code ha ridotto la dimensione del diff del 26%, il tempo di esecuzione del 27% e i crediti del 24% sul compito ambiguo, con un guadagno mediano del 9-10% sul compito multi-file; il primo test, con una sola esecuzione, aveva dato il risultato opposto. [Fonte: raw/pillitteri/pillitteri20261023-agents-md-design-md-skill-md-agenti-ai.md]




## Collegamenti

- [[codex]]
- [[claude-code]]
- [[index]]
