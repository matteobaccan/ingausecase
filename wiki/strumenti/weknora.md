---
title: "WeKnora"
category: strumento
tags: [go, knowledge-base, rag, tencent]
related_puntate: [20260524, 20260913, 20260916]
created: 2026-08-12
updated: 2026-09-16
---

# WeKnora

## Introduzione

Progetto RAG di [[tencent]]: un singolo binario in Go che trasforma PDF, Docs e wiki interni in una knowledge base interrogabile con reasoning agent integrato. Con la presentazione del 16 settembre 2026 il perimetro si allarga: non è più un tool di chat sui documenti ma una base completa per agent enterprise, che tiene insieme conoscenza, memoria, strumenti e ambiente sandbox.

## Funzionalità principali

- WeKnora di Tencent ha raggiunto 15000 stelle in pochi giorni: prendi PDF, Docs e wiki interni e li trasforma in RAG interrogabile con un solo binario in Go e reasoning agent integrato, rendendo la knowledge base aziendale ricercabile senza configurazione manuale.
- Il progetto è arrivato a oltre ventitremila stelle su GitHub con licenza open source e copre i formati che una knowledge base aziendale incontra davvero: PDF, presentazioni, Excel complessi, audio e screenshot.
- Integrazioni dichiarate: Feishu, Notion, Yuque e GitLab, così le risorse sparse restano dove sono e vengono indicizzate da WeKnora.
- Recupero ibrido: vettoriale più BM25, rerank con RRF e supporto GraphRAG, per far convivere la ricerca semantica con quella lessicale e con le relazioni del grafo di conoscenza.
- Gli agent non parlano agli umani ma interrogano il sistema come contesto lungo: ogni sessione può lanciare un ambiente Docker o E2B isolato, e l'agent gira shell, modifica codice, chiama API e restituisce file pronti.
- **Auto-Wiki**: le risorse sparse diventano una wiki Markdown con grafo di conoscenza, e un **Wiki Fixer Agent** controlla i link rotti, risolve i conflitti, marca le policy obsolete e supporta il diff tra versioni.

## Azienda / Autore

- [[tencent]]

## Timeline delle notizie

- **2026-05-24** — WeKnora di Tencent ha raggiunto 15000 stelle in pochi giorni: prendi PDF, Docs e wiki interni e li trasforma in RAG interrogabile con un solo binario in Go e reasoning agent integrato, rendendo la knowledge base aziendale ricercabile senza configurazione manuale.
- **2026-09-13** — Progetto open source di [[tencent]] con ventiduemila stelle su GitHub: trasforma documenti sparsi in Feishu, Notion o Yuque in una knowledge base interrogabile, con le domande semplici che ottengono risposte rapide via retrieval e quelle complesse che attivano agenti che cercano nella base di conoscenza e sul web.

- **2026-09-16** — WeKnora viene ripresentato come base per agent enterprise e non come tool di chat sui documenti: oltre ventitremila stelle, licenza open source, gestione di PDF, presentazioni, Excel complessi, audio e screenshot, integrazione con Feishu, Notion, Yuque e GitLab, richiamo ibrido vettoriale più BM25 con rerank RRF e supporto GraphRAG, ambienti Docker o E2B isolati per sessione in cui l'agent gira shell, modifica codice e chiama API, più un Auto-Wiki che trasforma le risorse sparse in una wiki Markdown con grafo di conoscenza e un Wiki Fixer Agent che controlla link rotti, conflitti e policy obsolete.

## Collegamenti

- [[tencent]]
- [[rag-over-retrieval]]
- [[index]]

