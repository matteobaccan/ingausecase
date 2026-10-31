---
title: "Google Colab"
category: strumento
tags: [cloud, google, gpu, notebook]
related_puntate: [20260512, 20260923]
created: 2026-08-12
updated: 2026-09-23
---

# Google Colab

## Introduzione

Piattaforma Google di notebook e computazione cloud, ora collegabile direttamente a VS Code, con GPU T4 gratuita.

## Funzionalità principali

- Google ha collegato VS Code direttamente a Google Colab: GPU T4 gratuita dentro il tuo editor, i tuoi file locali con la loro potenza di calcolo, niente affitti mensili né configurazioni complesse.

## Timeline delle notizie

- **2026-05-12** — Google ha collegato VS Code direttamente a Google Colab: GPU T4 gratuita dentro il tuo editor, i tuoi file locali con la loro potenza di calcolo, niente affitti mensili né configurazioni complesse.

- **2026-09-23** — Google Colab entra nei piani Google AI: gli abbonati ottengono accesso prioritario ad acceleratori più veloci, e il piano Ultra include esecuzione in background più lunga e GPU Premium.

- **2025-11-13** — L'estensione ufficiale Colab per VS Code arriva sul Marketplace Microsoft e su Open VSX (licenza Apache 2.0, repository googlecolab/colab-vscode): si apre un notebook .ipynb locale, si seleziona il kernel Colab e si lavora su una GPU T4 da 16 GB ospitata da Google senza spostare i file, con i fork compatibili Open VSX (VSCodium, Cursor, Windsurf) supportati. Un fine-tuning che su CPU richiede 50 minuti per epoca scende a circa 3 minuti sulla T4; il piano gratuito dà T4 e TPU v5e con timeout di inattività di 90 minuti, Pro costa 11,99 dollari al mese con A100 da 40 GB, L4 e 51 GB di RAM, Pro+ 49,99 dollari con esecuzione in background fino a 24 ore.
- **2026-06-05** — Google for Developers pubblica la [[google-colab-cli]]: oltre venti comandi da terminale (colab new, run, exec, repl, download, log) per provisionare GPU T4, L4, A100 e H100 e TPU v5e e v6e senza aprire il browser, con un file COLAB_SKILL.md nel repository che la rende usabile dagli agenti autonomi. Progetto open source Apache-2.0, complementare al Colab MCP Server di marzo 2026.
- **2026-09-22** — Colab entra nei piani a pagamento Google AI: Plus (4,99 euro al mese) e Pro (21,99) portano priorità su acceleratori e macchine, Ultra (99,99-219,99 euro) aggiunge GPU Premium ed esecuzione in background. Gli abbonamenti Colab Pro e Pro+ restano separati e i benefici si sommano, mentre la disponibilità italiana arriva account per account nelle settimane successive.

## Collegamenti

- [[google-colab-cli]]
- [[google]]
- [[index]]

