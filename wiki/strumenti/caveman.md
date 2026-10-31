---
title: "Caveman"
category: strumento
tags: [claude-code, open-source, plugin, risparmio-token, skill]
related_puntate: []
created: 2026-10-11
updated: 2026-10-11
sources: [raw/pillitteri/pillitteri20260414-claude-code-caveman-mode-risparmio-token.md, raw/pillitteri/pillitteri20260421-claude-code-token-10-repo-github-risparmio.md, raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]
---

# Caveman

## Introduzione

Skill e plugin per [[claude-code]] di Julius Brussee che impone al modello uno stile telegrafico — niente articoli, convenevoli o riepiloghi — lasciando intatto il codice generato. [Fonte: raw/pillitteri/pillitteri20260414-claude-code-caveman-mode-risparmio-token.md]

## Funzionalità principali

- Tre livelli di intensità: `/caveman lite` toglie solo le formule di cortesia, `full` rimuove gli articoli e `ultra` comprime al massimo; da maggio 2026 la modalità 文言文 in cinese classico è diventata stabile, con i suoi tre livelli. [Fonte: raw/pillitteri/pillitteri20260414-claude-code-caveman-mode-risparmio-token.md]
- La suite comprende tre strumenti separabili: caveman per le risposte, cavemem per la memoria persistente tra sessioni e cavekit per build e tooling. [Fonte: raw/pillitteri/pillitteri20260414-claude-code-caveman-mode-risparmio-token.md]
- Alternativa senza plugin: tre righe nel CLAUDE.md di progetto o globale, efficaci su Cursor, Cline, Copilot, Codex e Gemini CLI. [Fonte: raw/pillitteri/pillitteri20260414-claude-code-caveman-mode-risparmio-token.md]

## Repository

- github.com/JuliusBrussee/caveman — 51.690 stelle al 1 maggio 2026, 89.591 al 15 luglio 2026.

## Timeline delle notizie

- **2026-04-14** — Caveman di Julius Brussee promette di far rispondere Claude come un cavernicolo e di tagliare l'output del modello: il claim pubblicitario del 75 per cento viene ridotto dai benchmark del repository al 65 per cento medio sui soli token di output, che in una sessione reale vale un 4-5 per cento sul totale. [Fonte: raw/pillitteri/pillitteri20260414-claude-code-caveman-mode-risparmio-token.md]
- **2026-04-21** — Caveman è il primo dei dieci repository per risparmiare token su Claude Code con 41.288 stelle al 21 aprile: il taglio riguarda la prosa — «Let me explain what I'm going to do», i riepiloghi finali, le riformulazioni — mentre codice e dati tecnici restano intatti. [Fonte: raw/pillitteri/pillitteri20260421-claude-code-token-10-repo-github-risparmio.md]
- **2026-07-11** — Caveman arriva a 87.872 stelle su GitHub e resta il più popolare degli strumenti per i token perché non installa nulla a livello di rete: nessun proxy e nessuna dipendenza esterna, solo un'istruzione nel prompt di sistema e un hook che scrive il flag a ogni sessione; la misura dichiarata è un taglio del 65 per cento sull'output. [Fonte: raw/pillitteri/pillitteri20260711-caveman-rtk-pxpipe-headroom-token-claude-code.md]

## Collegamenti

- [[claude-code]]
- [[rtk]]
- [[ponytail]]
- [[headroom]]
- [[index]]
