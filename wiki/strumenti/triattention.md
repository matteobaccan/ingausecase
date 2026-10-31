---
title: "TriAttention"
category: strumento
tags: [attenzione, efficienza, inference, nvidia]
related_puntate: [20260628]
created: 2026-08-12
updated: 2026-08-12
sources: [raw/puntate/ainews20260628.md]
---

# TriAttention

## Introduzione

Tecnica di NVIDIA per la compressione della KV cache: evita l'out-of-memory facendo scoring dei token dalla geometria dei vettori key e query.

## Funzionalità principali

- Pubblicata da NVIDIA: risolve la compressione della KV cache evitando l'out-of-memory con scoring dei token dalla geometria dei vettori key e query. Compattazione ogni 128 token decodificati, 2,5 volte più veloce e 10,7 volte meno memoria.

## Azienda / Autore

- [[nvidia]]

## Modelli supportati / correlati

- [[locateanything-3b]]

## Timeline delle notizie

- **2026-06-28** — Pubblicata da NVIDIA: risolve la compressione della KV cache evitando l'out-of-memory con scoring dei token dalla geometria dei vettori key e query. Compattazione ogni 128 token decodificati, 2,5 volte più veloce e 10,7 volte meno memoria. [Fonte: raw/puntate/ainews20260628.md]

## Collegamenti

- [[locateanything-3b]]
- [[nvidia]]
- [[index]]

