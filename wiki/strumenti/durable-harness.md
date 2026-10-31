---
title: "durable-harness"
category: strumento
tags: [vercel, agent, harness, postgres, cloud]
related_puntate: []
created: 2026-10-21
updated: 2026-10-21
sources: [raw/tldr/tldr20261021.md]
---

# durable-harness

## Introduzione

Componente di [[vercel]] presentato il 21 ottobre 2026 che fa girare in modo durevole nel cloud gli harness degli agenti di coding: sostiene Pi, [[opencode]], [[codex]] e [[claude-code]] su Vercel o in auto-hosting con un proprio database Postgres. [Fonte: raw/tldr/tldr20261021.md]

## Funzionalità principali

- Le sessioni sopravvivono a un crash a metà turno e continuano anche se il browser si disconnette. [Fonte: raw/tldr/tldr20261021.md]
- Un turno che perde una funzione a metà riparte dal log su uno nuovo, senza retry manuale e senza ripetere quello che era già finito. [Fonte: raw/tldr/tldr20261021.md]

## Casi d'uso

- Eseguire sessioni di coding agent lunghe senza doverle tenere agganciate a una singola macchina o a una finestra aperta. [Fonte: raw/tldr/tldr20261021.md]

## Azienda/autore

- [[vercel]]

## Timeline delle notizie

- **2026-10-21** — Vercel annuncia durable-harness, che fa girare in modo durevole nel cloud gli harness di Pi, OpenCode, Codex e Claude Code, su Vercel o in self-hosting con Postgres: le sessioni sopravvivono ai crash a metà turno e ai browser disconnessi, ripartendo dal log senza retry manuale. [Fonte: raw/tldr/tldr20261021.md]

## Collegamenti

- [[vercel]]
- [[harness-engineering]]
- [[claude-code]]
- [[index]]
