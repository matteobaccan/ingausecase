---
title: "Graphify"
category: strumento
tags: [agent, analisi, claude-code, developer-tools, github, knowledge-graph, obsidian, open-source, tree-sitter, wiki]
related_puntate: [20260510, 20260611, 20260710, 20260717, 20260722, 20260805, 20261018, 20261020]
created: 2026-08-12
updated: 2026-10-20
---

# Graphify

## Introduzione

Strumento open source che trasforma un progetto in una knowledge graph collegando codice, interfacce, SQL e documenti. Compatibile con i principali agenti di coding.

## Funzionalità principali

- Graphify è comparso 48 ore dopo che Karpathy ha postato il suo workflow LLM Knowledge Bases: un comando, qualsiasi cartella, knowledge graph completo, vault Obsidian con backlink, wiki navigabile e Q&A in linguaggio naturale, con 71,5 volte meno token per query rispetto a file raw; supporta codice in 13 linguaggi, PDF, immagini e markdown.
- safishamsi/graphify costruisce knowledge graph del codebase per Claude Code: tree-sitter mappa la struttura del codice gratis e in locale, l'LLM analizza la semantica dei documenti una sola volta e Claude interroga la mappa invece di scansionare i file; ricostruzione automatica dopo ogni commit con risparmi drastici di token su repository grandi.
- Graphify trasforma codice e documenti in un knowledge graph interrogabile.

## Azienda / Autore

- [[andrej-karpathy]]
- [[cursor]]
- [[github]]

## Timeline delle notizie

- **2026-05-10** — Graphify è comparso 48 ore dopo che Karpathy ha postato il suo workflow LLM Knowledge Bases: un comando, qualsiasi cartella, knowledge graph completo, vault Obsidian con backlink, wiki navigabile e Q&A in linguaggio naturale, con 71,5 volte meno token per query rispetto a file raw; supporta codice in 13 linguaggi, PDF, immagini e markdown.
- **2026-06-11** — safishamsi/graphify costruisce knowledge graph del codebase per Claude Code: tree-sitter mappa la struttura del codice gratis e in locale, l'LLM analizza la semantica dei documenti una sola volta e Claude interroga la mappa invece di scansionare i file; ricostruzione automatica dopo ogni commit con risparmi drastici di token su repository grandi.
- **2026-07-10** — Graphify trasforma codice e documenti in un knowledge graph interrogabile.
- **2026-07-17** — Graphify ha ottantaseimila stelle: mappa il progetto invece di farlo leggere file per file all'IA, segna ogni connessione come reale o inferita, compatibile con Claude Code, Cursor e oltre venti agenti, tutto locale.
- **2026-07-22** — Tool open source che trasformava codebase in knowledge graph. Funzionava con Claude Code, Cursor e Codex, con parsing locale senza LLM per il codice.
- **2026-08-05** — Graphify ha raggiunto ottantatremila stelle su GitHub: trasforma un progetto in una knowledge graph con codice, interfacce, SQL e documenti tutti collegati; compatibile con Claude Code, Codex, OpenCode e Cursor, open source e modificabile senza limiti.
- **2026-10-18** — [[graphify]] è un tool sostenuto da Y Combinator con centoventisettemilacinquecento stelle: dopo `graphify install` genera una mappa dell'intera architettura senza usare LLM, tutta in locale, che l'agente legge al posto dei file; è compatibile con [[claude-code]], [[cursor]], [[codex]] e [[gemini-cli]].
- **2026-10-20** — Graphify, tool di Y Combinator, supera le 128.000 stelle: trasforma il progetto in una mappa di connessioni che l'AI segue invece di rileggere i file, funziona con Claude Code, Codex, Cursor e Gemini CLI, analizza in locale senza LLM e dichiara il 67% di token in meno.







## Collegamenti

- [[andrej-karpathy]]
- [[claude-code]]
- [[codex]]
- [[cursor]]
- [[github]]
- [[open-source]]
- [[understand-anything]]
- [[index]]

