---
title: "Buzz"
category: strumento
tags: [workspace, agenti, nostr, open-source, identita]
related_puntate: []
created: 2026-09-28
updated: 2026-09-28
sources: [raw/pillitteri/pillitteri20260928-buzz-jack-dorsey-workspace-ai.md]
---

# Buzz

## Introduzione

Workspace open source di [[block]] dove dipendenti umani e agenti IA condividono gli stessi canali: chat, messaggi diretti, voce, condivisione file, archivio del codice e automazioni in un'unica applicazione. La novità non è l'elenco delle funzioni ma l'identità: ogni partecipante, umano o agente, ha una propria coppia di chiavi crittografiche secp256k1 e ogni azione è firmata. [Fonte: raw/pillitteri/pillitteri20260928-buzz-jack-dorsey-workspace-ai.md]

## Funzionalità principali

- Un agente non entra con un account di servizio condiviso: ha una chiave personale più una firma secondaria che lo collega al dipendente umano che lo ha autorizzato, così il registro mostra chi ha dato il permesso di agire. [Fonte: raw/pillitteri/pillitteri20260928-buzz-jack-dorsey-workspace-ai.md]
- Il protocollo è Nostr: ogni azione è un evento JSON con hash, chiave pubblica, tipo, metadati e firma Schnorr; anche le patch di codice, i risultati dei test e le decisioni di merge finiscono archiviati come eventi firmati, senza bisogno di un account GitHub separato per ogni agente. [Fonte: raw/pillitteri/pillitteri20260928-buzz-jack-dorsey-workspace-ai.md]
- La specifica di isolamento fra organizzazioni è stata formalizzata in TLA+ e verificata con Tamarin. [Fonte: raw/pillitteri/pillitteri20260928-buzz-jack-dorsey-workspace-ai.md]

## Installazione e uso

Pubblico dal 21 luglio 2026, versione 0.4.21 per macOS, Windows e Linux, licenza Apache 2.0. Block offre un relay pubblico gratuito in beta; il self-hosting richiede Docker, Rust 1.88 o superiore, Node 24 e pnpm. Gli agenti collegabili sono [[goose]], [[codex]] e [[claude-code]], tramite l'Agent Client Protocol. Al 28 settembre 2026 il repository conta 35.150 stelle su GitHub. [Fonte: raw/pillitteri/pillitteri20260928-buzz-jack-dorsey-workspace-ai.md]

## Azienda

- [[block]]

## Timeline delle notizie

- **2026-09-28** — Buzz torna a circolare per un tweet che lo presenta come un framework capace di gestire un'intera azienda con il lavoro al 100 per cento affidato ad agenti IA: la verifica delle fonti mostra che il rilascio risale al 21 luglio 2026, che le stelle sono 35.150 e non le 29.000 del post, e che nessuna azienda lo usa in quel modo. [Fonte: raw/pillitteri/pillitteri20260928-buzz-jack-dorsey-workspace-ai.md]

## Riferimenti

- https://pasqualepillitteri.it/news/18967/buzz-jack-dorsey-workspace-ai

## Collegamenti

- [[block]]
- [[goose]]
- [[agenti-ai]]
- [[index]]
