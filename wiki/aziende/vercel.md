---
title: "Vercel"
category: azienda
tags: [vercel, claude-marketplace, cloud, developer-tools, usa]
related_puntate: [20260910, 20261001]
created: 2026-09-10
updated: 2026-10-30
---

# Vercel

## Introduzione

Azienda di strumenti per sviluppatori: il suo prodotto è ora disponibile nel Claude Marketplace di [[anthropic]]; in precedenza era già comparso nella wiki come sviluppatrice dell'[[ai-sdk-7]] e partner dello standard Agent Plugins.

## Timeline delle notizie

- **2026-06-20** — Vercel racconta che in sei mesi gli agenti AI sono passati dal generare meno del 3 per cento dei deploy sulla propria piattaforma a circa il 29, con la previsione di superare presto il 50, e per questo rilascia il 17 giugno eve, framework open source per agenti in cui la struttura del progetto definisce il comportamento dell'agente: tool, skill, subagent, connection, channel e schedule al posto dell'impalcatura riscritta a ogni progetto.

- **2026-09-10** — Vercel è tra i prodotti ora disponibili nel Claude Marketplace: le aziende possono usare il commitment di spesa Anthropic per comprare più prodotti e agenti basati su Claude.

- **2026-08-10** — Due pacchetti dell'AI SDK di Vercel sono tra le quattro CVE presentate al Black Hat USA come CoreBreak: il runtime accettava un blocco di tipo tool call senza verificarne la provenienza, quindi chi riusciva a inserirlo nel flusso otteneva l'esecuzione dello strumento senza che il modello avesse mai prodotto la richiesta. Le falle sono state corrette.
- **2026-09-29** — Il registro skills.sh ha raggiunto un milione di skill riutilizzabili per agenti e quasi 280 milioni di installazioni in sette mesi, secondo l'analisi di Vercel su cosa gli utenti insegnano agli agenti e quali skill attirano installazioni.
- **2026-10-01** — Il Vercel AI Gateway serve GLM 5.3 Flash con i kernel riscritti da RunInfra: 670 token al secondo e un cache hit rate del 99,7% nelle ultime ventiquattro ore.
- **2026-10-21** — Annuncia [[durable-harness]], che fa girare in modo durevole nel cloud gli harness di Pi, OpenCode, Codex e Claude Code, su Vercel o in self-hosting con Postgres: le sessioni sopravvivono ai crash a metà turno e alle disconnessioni del browser, ripartendo dal log senza retry manuale.
- **2026-10-30** — L'adattatore fx esegue ora l'harness sull'host tramite libfx, separando le operazioni di host e quelle di sandbox.










## Collegamenti

- [[agent-plugins]]
- [[ai-sdk-7]]
- [[anthropic]]
- [[claude-marketplace]]
- [[runinfra]]
- [[index]]
