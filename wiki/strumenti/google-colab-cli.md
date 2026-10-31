---
title: "Google Colab CLI"
category: strumento
tags: [agent, cloud, google, gpu, open-source]
created: 2026-09-23
updated: 2026-09-23
sources: [raw/pillitteri/pillitteri20260606-google-colab-cli-terminale-agenti-ai.md]
---

# Google Colab CLI

## Introduzione

Interfaccia a riga di comando di [[google-colab]] pubblicata il 5 giugno 2026 da Google for Developers: trasforma le sessioni Colab in un servizio di calcolo remoto pilotabile dal terminale, pensato anche per gli agenti AI. [Fonte: raw/pillitteri/pillitteri20260606-google-colab-cli-terminale-agenti-ai.md]

## Funzionalità principali

- Oltre venti comandi (colab new, run, exec, repl, download, log, sessions, status, stop) per gestire sessioni remote senza aprire il browser, con installazione via `uv tool install google-colab-cli` o pip. [Fonte: raw/pillitteri/pillitteri20260606-google-colab-cli-terminale-agenti-ai.md]
- GPU T4, L4, A100 e H100 e TPU v5e e v6e, provisionate in base al piano Colab attivo; il log in formato .ipynb è un notebook rieseguibile. [Fonte: raw/pillitteri/pillitteri20260606-google-colab-cli-terminale-agenti-ai.md]
- Un file COLAB_SKILL.md nel repository insegna agli agenti autonomi a usarla, così Claude Code o Gemini CLI possono provisionare runtime ed eseguire pipeline come un fine-tuning QLoRA di gemma-3-1b-it su T4. [Fonte: raw/pillitteri/pillitteri20260606-google-colab-cli-terminale-agenti-ai.md]

## Repository

- Progetto open source con licenza Apache-2.0, repository googlecolab/google-colab-cli, 96 stelle al 6 giugno 2026.

## Azienda / Autore

- [[google]]

## Timeline delle notizie

- **2026-06-05** — Google pubblica la Colab CLI: oltre venti comandi per usare GPU e TPU dal terminale, con COLAB_SKILL.md per gli agenti e il comando `colab run` che provisiona, esegue, recupera gli artefatti e distrugge la VM in un'unica istruzione. [Fonte: raw/pillitteri/pillitteri20260606-google-colab-cli-terminale-agenti-ai.md]

## Collegamenti

- [[google-colab]]
- [[claude-code]]
- [[agenti-ai]]
- [[mcp]]
- [[index]]
