---
title: "OpenCode"
category: strumento
tags: [agent, claude-code, cli, coding, integrazione, open-source]
related_puntate: [20260601, 20260616, 20260731, 20260825, 20261019]
created: 2026-08-12
updated: 2026-10-20
sources: [raw/puntate/ainews20260601.md, raw/puntate/ainews20260616.md, raw/puntate/ainews20260731.md, raw/puntate/ainews20260825.md, raw/tldr/tldr20261014.md, raw/pillitteri/pillitteri20261018-opencode-attacco-console-chiavi-api.md, raw/puntate/ainews20261019.md, raw/pillitteri/pillitteri20261020-ransomware-inc-gentlemen-claude-server-aperto-socradar.md]
---

# OpenCode

## Introduzione

Versione open source di Claude Code: gira in terminale o come app desktop, si integra con Claude, GPT e Kimi, funziona con MCP e ha integrazione GitHub.

## Funzionalità principali

- OpenCode è citato tra gli strumenti compatibili con Everything Claude Code, la collection che conta trenta agenti, sessantaquattro skill e trentatré comandi.
- opencode è citato tra gli agenti di coding con cui QVAC SDK 0.13.0 si integra direttamente, insieme ad altri framework.
- OpenCode, versione open source di Claude Code: gira in terminale o come app desktop, si integra con Claude, GPT e Kimi, funziona con MCP, integrazione GitHub, sforzo di pensiero adattativo. Completamente gratuito.

## Azienda / Autore

- [[cursor]]

## Timeline delle notizie

- **2026-06-01** — OpenCode è citato tra gli strumenti compatibili con Everything Claude Code, la collection che conta trenta agenti, sessantaquattro skill e trentatré comandi. [Fonte: raw/puntate/ainews20260601.md]
- **2026-06-16** — opencode è citato tra gli agenti di coding con cui QVAC SDK 0.13.0 si integra direttamente, insieme ad altri framework. [Fonte: raw/puntate/ainews20260616.md]
- **2026-07-31** — OpenCode, versione open source di Claude Code: gira in terminale o come app desktop, si integra con Claude, GPT e Kimi, funziona con MCP, integrazione GitHub, sforzo di pensiero adattativo. Completamente gratuito. [Fonte: raw/puntate/ainews20260731.md]
- **2026-08-25** — OpenCode è citato tra gli ambienti supportati da session-migrate per migrare le sessioni di coding agent verso altri tool. [Fonte: raw/puntate/ainews20260825.md]
- **2026-10-14** — OpenCode 2.0 porta il server a girare come un unico processo in background, i client programmatici a scoprire da soli il servizio locale e il tool a poter essere usato come libreria con il pacchetto SDK, oltre a correzioni e miglioramenti di prestazione. [Fonte: raw/tldr/tldr20261014.md]
- **2026-10-18** — OpenCode conferma su X il 17 ottobre un attacco alla sua Console che ha colpito l'1,4% degli utenti, cioè quelli con provider esterni collegati: le chiavi API di OpenAI, Anthropic e Google salvate nel workspace potrebbero essere state esposte, l'accesso non autorizzato è passato da un sistema «legacy» e l'azienda dice di aver lavorato con i tre provider per rimediare. Il programma open source installato in locale non risulta compromesso, e [[anthropic]] ha scritto di aver revocato le chiavi di Claude coinvolte. [Fonte: raw/pillitteri/pillitteri20261018-opencode-attacco-console-chiavi-api.md] TechCrunch riporta che dopo l'incidente alcuni clienti hanno segnalato consumi e addebiti non autorizzati, che i fornitori hanno bloccato alcune chiavi e che OpenCode ha avviato i rimborsi; l'indagine è in corso, l'azienda ha parlato di distillazione ma non ha chiarito l'accesso iniziale né provato che le chiavi siano state usate per addestrare modelli. [Fonte: raw/controrumore/controrumore20261021-diario-ai-regole-salute-e-infrastrutture.md]
- **2026-10-19** — OpenCode è finito sotto attacco informatico e durante l'incident response i modelli frontier usati per la difesa hanno iniziato a rifiutarsi di analizzare gli attacchi: le safety guardrail si sono attivate proprio mentre l'azienda cercava di identificare gli agenti malevoli, lo stesso problema già visto su [[hugging-face|Hugging Face]]. È lo scontro tra la sicurezza informatica e i filtri di sicurezza dell'IA stessa. [Fonte: raw/puntate/ainews20261019.md]
- **2026-10-20** — I log recuperati da SOCRadar su sette server degli affiliati di INC Ransom e The Gentlemen contengono 8.257 messaggi distribuiti su 133 sessioni di OpenCode, lo strumento da terminale usato per far lavorare i modelli sulle intrusioni. [Fonte: raw/pillitteri/pillitteri20261020-ransomware-inc-gentlemen-claude-server-aperto-socradar.md]













## Collegamenti

- [[claude-code]]
- [[codex-cli]]
- [[cursor]]
- [[everything-claude-code]]
- [[mcp]]
- [[open-source]]
- [[qvac-sdk]]
- [[warp-terminal]]
- [[session-migrate]]
- [[index]]

