---
title: "Infisical"
category: azienda
tags: [infisical, sicurezza, secrets, agenti, usa]
related_puntate: []
created: 2026-10-30
updated: 2026-10-30
sources: [raw/pillitteri/pillitteri20261030-infisical-40-milioni-agenti-ai-password.md]
---

# Infisical

## Introduzione

Società di San Francisco che vende software per gestire i secrets aziendali — password, chiavi API, chiavi di cifratura e certificati — e che con Agent Vault punta a far lavorare gli agenti AI sui sistemi aziendali senza consegnare loro le credenziali vere. [Fonte: raw/pillitteri/pillitteri20261030-infisical-40-milioni-agenti-ai-password.md]

## Prodotti

- Agent Vault, proxy open source su GitHub che sta fra l'agente e le API: l'agente lavora con segnaposto come `__anthropic_api_key__` e il proxy sostituisce la credenziale reale solo al momento della chiamata. Registra il traffico, filtra le uscite per agente ed endpoint e si aggancia agli strumenti esistenti impostando `HTTPS_PROXY`. [Fonte: raw/pillitteri/pillitteri20261030-infisical-40-milioni-agenti-ai-password.md]

## Timeline delle notizie

- **2026-10-30** — Ha raccolto 40 milioni di dollari in un round di serie B che la valuta 600 milioni, annunciato il 27 ottobre e guidato da Elad Gil con Gradient e Y Combinator nel gruppo: con la serie A da 16 milioni del giugno 2025 il totale raccolto sfiora i 60 milioni. I prodotti della piattaforma sono usati da più di 1.300 organizzazioni, tra cui Airbus, Volkswagen, Hugging Face e Wise, mentre nessuna fonte indica quanti clienti abbia Agent Vault. [Fonte: raw/pillitteri/pillitteri20261030-infisical-40-milioni-agenti-ai-password.md]

## Collegamenti

- [[sicurezza-ai]]
- [[agenti-ai]]
- [[hugging-face]]
- [[index]]
