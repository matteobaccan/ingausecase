---
title: "jevlike"
category: strumento
tags: [encoder, jev, mit, open-source, scorer]
related_puntate: []
created: 2026-09-21
updated: 2026-09-21
---

# jevlike

## Introduzione

Clone open source di [[jev]] che segue la strada opposta a quella degli altri: invece di leggere i logit di un modello linguistico esistente addestra in casa un piccolo scorer, dove ogni opzione diventa un vettore che interroga il contesto e produce un punteggio, con un encoder che impara byte per byte (contesto tagliato a 192 byte, opzioni a 32).

## Funzionalità principali

- Le demo dichiarate sono Doom e gli scacchi: nel film sugli scacchi il modello totalizza 4 vittorie, 46 patte e zero sconfitte contro un avversario che muove a caso, ma zero vittorie, 2 patte e 48 sconfitte contro Stockfish a livello 0, e l'autore avvisa che le finestre mostrate sono state scelte per l'azione e non per la bravura.
- Al 21 settembre 2026 conta 1.122 stelle su GitHub, con licenza MIT.

## Timeline delle notizie

- **2026-09-21** — jevlike è il terzo clone per seguito: 1.122 stelle, licenza MIT, encoder byte-level o encoder pretrained congelato addestrato in casa invece di una lettura di logit su un modello grosso; su Hacker News il progetto ha raccolto 166 punti, con più di un commentatore a obiettare che un Jev non interessa se il modello sotto non è intelligente.

## Collegamenti

- [[jev]]
- [[kev]]
- [[semif]]
- [[index]]
