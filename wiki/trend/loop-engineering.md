---
title: "Loop Engineering"
category: trend
tags: [agent, automazione, ingegneria-software, metodologia, workflow]
related_puntate: [20260611, 20260627, 20260630, 20260910, 20260912, 20260916, 20261017]
created: 2026-08-12
updated: 2026-10-17
sources: [raw/puntate/ainews20260912.md, raw/puntate/ainews20260611.md, raw/puntate/ainews20260627.md, raw/puntate/ainews20260630.md, raw/puntate/ainews20260910.md, raw/puntate/ainews20260916.md, raw/pillitteri/pillitteri20260702-fable-5-orchestratore-risparmiare-token-claude-code.md, raw/puntate/ainews20261017.md]
---

# Loop Engineering

## Introduzione

Approccio emergente allo sviluppo con agenti IA: invece di promptare l'agente si costruisce il sistema che lo prompta, con loop autonomi (discover, isolate, verify, persist, schedule) e revisione di un secondo agente.

## Attori coinvolti

- [[addy-osmani]]
- [[agent-skills]]
- [[andrej-karpathy]]
- [[anthropic]]
- [[cyrilxbt]]
- [[hermes-agent]]
- [[obsidian-vault-autosufficiente]]

## Timeline delle notizie

- **2026-06-11** — Addy Osmani spiega il passaggio dal prompt manuale al design di sistema con Loop Engineering: un ciclo ricorsivo che scopre, esegue, verifica e itera in autonomia, con cinque componenti fondamentali che trasformano Codex e Claude in sistemi più intelligenti. [Fonte: raw/puntate/ainews20260611.md]
- **2026-06-27** — Un ingegnere senior di Anthropic ha pubblicato un PDF di 11 pagine sul Loop Engineering: il loop autonomo include discover, isolate, verify, persist e schedule, un secondo agente rivede il lavoro e mai auto-valutazione. CyrilXBT ha reso open source un framework completo con triage giornaliero, sweep CI, aggiornamento dipendenze e bozze changelog. [Fonte: raw/puntate/ainews20260627.md]
- **2026-06-30** — Il playbook interno di Anthropic è appena trapelato: cinque principi (discovery, handoff, verification, persistence, scheduling), separare sempre generatore e valutatore, usare git worktrees per parallelizzare, scrivere lo stato su disco e far girare tutto su timer. È stato rilasciato anche un framework completo con sei pattern production-ready: daily triage, CI sweeper, PR babysitter, con CLI per valutare la readiness del codebase e template SKILL.md e STATE.md. [Fonte: raw/puntate/ainews20260630.md]
- **2026-07-02** — Il pattern orchestratore-esecutore applicato a Claude Code divide la sessione in due strati: il modello di frontiera pianifica e sintetizza — genera 2.000-3.000 token per sessione — mentre subagent con modello fissato nel frontmatter YAML, uno su Opus per il ragionamento e uno su Sonnet per il lavoro meccanico, macinano il resto in context window separati. Ogni subagent paga i propri token al proprio prezzo, il rumore dei log resta confinato e la spesa si sposta sui modelli economici; il plugin ufficiale codex-plugin-cc aggiunge Codex come pari, non come revisore, con il comando /codex:rescue --background. [Fonte: raw/pillitteri/pillitteri20260702-fable-5-orchestratore-risparmiare-token-claude-code.md]



- **2026-09-10** — Un video gratuito di quarantadue minuti mostra un ingegnere Anthropic al lavoro su come il team Claude costruisce loop che si auto-promptano: niente più prompt manuali, solo loop. [Fonte: raw/puntate/ainews20260910.md]

- **2026-09-12** — Un loop engineering con Claude e Obsidian rende la vault lo stato del loop: ogni informazione vive in un file Markdown, Claude raccoglie contesto ed edita in un worktree git separato e un agente critico rivede le diff prima del commit. [Fonte: raw/puntate/ainews20260912.md]

- **2026-09-16** — [[andrej-karpathy]] tiene la sua prima conferenza dopo l'ingresso in [[anthropic]] e la costruisce su quattro temi centrali — agenti, loop, harness e sistemi auto-miglioranti — con materiale denso pensato sia per chi inizia sia per chi già lavora con questi strumenti. È la stessa griglia con cui la pagina segue il passaggio dal prompt manuale al sistema che prompta, e arriva dalla persona che a maggio aveva già messo in fila agent, loop, grafi e sistemi auto-miglioranti nella sua lezione sugli otto anni tra [[openai]] e Tesla. [Fonte: raw/puntate/ainews20260916.md]
- **2026-10-17** — [[terminal-rsi|Terminal-RSI]], ricerca sul miglioramento ricorsivo auto-supervisionato, porta in due cicli il successo su Terminal-Bench 2.1 dal 51,7 all'86,5 per cento e su Terminal-Bench 4.0 da zero al 19,8 per cento, nuovo stato dell'arte. [Fonte: raw/puntate/ainews20261017.md]




## Collegamenti

- [[addy-osmani]]
- [[agent-skills]]
- [[andrej-karpathy]]
- [[anthropic]]
- [[cyrilxbt]]
- [[hermes-agent]]
- [[obsidian-vault-autosufficiente]]
- [[index]]

