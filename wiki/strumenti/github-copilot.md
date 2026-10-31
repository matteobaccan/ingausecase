---
title: "GitHub Copilot"
category: strumento
tags: [assistente, coding, github, ia, microsoft]
related_puntate: [20260616, 20260703]
created: 2026-08-12
updated: 2026-10-29
sources: [raw/puntate/ainews20260616.md, raw/puntate/ainews20260703.md, raw/pillitteri/pillitteri20260908-microsoft-codice-a-mano-finito-sviluppatori-ollama.md, raw/pillitteri/pillitteri20260921-plugin4shell-falla-zero-click-agenti-ai.md, raw/tldr/tldr20261029.md, raw/pillitteri/pillitteri20261029-vulnerabilita-embrace-browser-integrati-codex-vs-code.md]
---

# GitHub Copilot

## Introduzione

Assistente di coding IA di GitHub/Microsoft, che ha integrato il primo modello open-weight selezionabile nel model picker.

## Funzionalità principali

- GitHub Copilot distribuisce gratuitamente su tutti i livelli MAI-Code-1-Flash, il modello di programmazione proprietario di Microsoft.
- Integra Kimi K2.7 Code: primo modello open-weight selezionabile nel model picker. I testing mostrano performance paragonabili ai frontier model a costo inferiore.

## Modelli supportati / correlati

- [[kimi-k2-7-code]]
- [[mai-code-1-flash]]

## Timeline delle notizie

- **2026-06-16** — GitHub Copilot distribuisce gratuitamente su tutti i livelli MAI-Code-1-Flash, il modello di programmazione proprietario di Microsoft. [Fonte: raw/puntate/ainews20260616.md]
- **2026-07-03** — Integra Kimi K2.7 Code: primo modello open-weight selezionabile nel model picker. I testing mostrano performance paragonabili ai frontier model a costo inferiore. [Fonte: raw/puntate/ainews20260703.md]

- **2026-09-08** — L'agente di Copilot non completa più la singola riga: prepara l'ambiente, mette mano al repository, lancia i test e apre una pull request già pronta per la revisione, prendendosi la parte meccanica del lavoro. Secondo Windows Latest Microsoft sviluppa già pezzi di Windows 11 in questo modo; nella stessa settimana David Fowler ([[microsoft]]) scrive che "digitare codice è assolutamente finito". Il carico si sposta sulla revisione, che diventa più pesante e non più leggera. [Fonte: raw/pillitteri/pillitteri20260908-microsoft-codice-a-mano-finito-sviluppatori-ollama.md]

- **2026-09-21** — È l'unico dei quattro agenti di Plugin4Shell senza una correzione disponibile: secondo AIR Security la segnalazione di giugno 2026 non ha avuto risposta, e al 21 settembre le note di rilascio del Copilot CLI, arrivate alla v1.0.87-0 del 18 settembre, non citano correzioni sui plugin. GitHub sostiene che il servizio non consente di creare rami o tag con nomi simili a uno SHA, quindi gli attacchi non lo riguardano, ma i ricercatori replicano che i marketplace di Copilot possono vivere anche su piattaforme come Bitbucket, dove quel blocco non esiste, e che il pin viene risolto sulla macchina dell'utente. [Fonte: raw/pillitteri/pillitteri20260921-plugin4shell-falla-zero-click-agenti-ai.md]
- **2026-10-29** — Introduce Copilot Fusion, che instrada e orchestra i modelli per ogni compito combinando l'orchestrazione multi-modello di Project HydraFusion con la selezione automatica di Copilot: il sistema sceglie quali modelli usare e come farli collaborare in base allo sforzo richiesto dall'utente, e gli amministratori possono limitare i modelli disponibili o disattivarlo come impostazione predefinita. [Fonte: raw/tldr/tldr20261029.md]

- **2026-10-29** — Copilot Automations ora apprende dagli esiti reali delle attività su GitHub e si auto-migliora. [Fonte: raw/tldr/tldr20261029.md]
- **2026-10-29** — Nella ricerca EMBRACE la scheda di anteprima dell'app desktop 1.1.27 lasciava che fosse la pagina a comunicare all'app il proprio indirizzo, permettendo a un dominio dell'attaccante di mostrare github.com/login nella barra e di far credere all'agente di trovarsi su GitHub; GitHub ha chiuso il problema nella build 1.1.29 del 13 ottobre, prima della segnalazione dei ricercatori. [Fonte: raw/pillitteri/pillitteri20261029-vulnerabilita-embrace-browser-integrati-codex-vs-code.md]







## Collegamenti

- [[kimi-k2-7-code]]
- [[mai-code-1-flash]]
- [[index]]

