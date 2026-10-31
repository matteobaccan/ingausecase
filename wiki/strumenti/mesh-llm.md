---
title: "Mesh LLM"
category: strumento
tags: [inferenza, open-source, rust]
related_puntate: [20260714, 20260715]
created: 2026-08-12
updated: 2026-08-12
---

# Mesh LLM

## Introduzione

Sistema open source in Rust che distribuisce l'inferenza di modelli da settanta miliardi di parametri su più dispositivi, con sharding per layer.

## Funzionalità principali

- Mesh LLM distribuisce l'inferenza di modelli da settanta miliardi di parametri su più dispositivi: se un nodo può gestire il modello lo esegue localmente, altrimenti lo shard per layer; open source in Rust.
- Mesh LLM risolve il problema VRAM distribuendo l'inferenza di modelli grandi su più dispositivi consumer: espone API compatibile OpenAI su localhost, con esecuzione locale, routing a peer o pipeline distribuita per layer; modelli da duecento miliardi in su girano su hardware esistente, scritto in Rust e open source.

## Azienda / Autore

- [[nvidia]]

## Modelli supportati / correlati

- [[mach-mind-4-flash]]

## Timeline delle notizie

- **2026-07-14** — Mesh LLM distribuisce l'inferenza di modelli da settanta miliardi di parametri su più dispositivi: se un nodo può gestire il modello lo esegue localmente, altrimenti lo shard per layer; open source in Rust.
- **2026-07-15** — Mesh LLM risolve il problema VRAM distribuendo l'inferenza di modelli grandi su più dispositivi consumer: espone API compatibile OpenAI su localhost, con esecuzione locale, routing a peer o pipeline distribuita per layer; modelli da duecento miliardi in su girano su hardware esistente, scritto in Rust e open source.

## Collegamenti

- [[mach-mind-4-flash]]
- [[nvidia]]
- [[pulsar]]
- [[index]]

