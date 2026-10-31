---
title: "PGX"
category: strumento
tags: [database, postgres, rust, agenti, open-source]
related_puntate: [20261021]
created: 2026-10-21
updated: 2026-10-21
sources: [raw/puntate/ainews20261021.md]
---

# PGX

## Introduzione

Database Postgres per agenti AI scritto in Rust: un solo runtime tiene migliaia di database, senza un container per database, ed è open source. [Fonte: raw/puntate/ainews20261021.md]

## Funzionalità principali

- Mille database occupano 659 megabyte di RAM e un database inattivo pesa circa 0,7 megabyte. [Fonte: raw/puntate/ainews20261021.md]
- La clonazione di un database da 674 megabyte richiede 85 millisecondi. [Fonte: raw/puntate/ainews20261021.md]
- Non usa container: i database sono gestiti da un unico runtime. [Fonte: raw/puntate/ainews20261021.md]

## Casi d'uso

- Dare a ogni agente o a ogni sessione un database Postgres isolato senza il costo di un'istanza per volta. [Fonte: raw/puntate/ainews20261021.md]

## Timeline delle notizie

- **2026-10-21** — Presenta PGX, database Postgres per agenti scritto in Rust: mille database in 659 megabyte di RAM, cloni da 674 megabyte in 85 millisecondi, 0,7 megabyte per database inattivo, open source e senza container per database. [Fonte: raw/puntate/ainews20261021.md]

## Collegamenti

- [[agenti-ai]]
- [[open-source]]
- [[index]]
