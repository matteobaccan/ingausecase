---
title: "Stack open source startup AI"
category: strumento
tags: [github, infrastruttura, open-source, repository]
related_puntate: []
created: 2026-09-25
updated: 2026-09-25
sources: [raw/pillitteri/pillitteri20260813-stack-open-source-startup-ai-7-repository-github.md]
---

# Stack open source startup AI

## Introduzione

I sette repository che compongono, livello per livello, il backend della maggior parte delle startup AI, come emerge dalla reference architecture per le applicazioni LLM pubblicata da a16z: ogni strato ha un componente aperto che le startup adottano per controllare costi e margini. I numeri di stelle della tabella sono quelli verificati su GitHub il 13 agosto 2026. [Fonte: raw/pillitteri/pillitteri20260813-stack-open-source-startup-ai-7-repository-github.md]

## Funzionalità principali

- Livello API: `fastapi/fastapi` con 101.550 stelle, licenza MIT. [Fonte: raw/pillitteri/pillitteri20260813-stack-open-source-startup-ai-7-repository-github.md]
- Vector database: `pgvector/pgvector` (22.607, PostgreSQL License); inferenza: `vllm-project/vllm` (88.930, Apache 2.0); orchestrazione: `langchain-ai/langchain` (144.131, MIT). [Fonte: raw/pillitteri/pillitteri20260813-stack-open-source-startup-ai-7-repository-github.md]
- Model hub: `huggingface/transformers` (164.033, Apache 2.0); cache: `redis/redis` (75.996, AGPLv3/source-available); runtime locale: `ollama/ollama` (178.403, MIT). [Fonte: raw/pillitteri/pillitteri20260813-stack-open-source-startup-ai-7-repository-github.md]

## Modelli supportati / correlati

- [[langchain]]
- [[vllm]]
- [[ollama]]
- [[hugging-face]]

## Timeline delle notizie

- **2026-08-13** — La ricognizione mette in fila i sette repository dello stack con le stelle reali verificate quel giorno: FastAPI per le API, pgvector come vector database, vLLM per l'inferenza, LangChain per l'orchestrazione, transformers come model hub, Redis per la cache e Ollama come runtime locale. [Fonte: raw/pillitteri/pillitteri20260813-stack-open-source-startup-ai-7-repository-github.md]

## Collegamenti

- [[hugging-face]]
- [[langchain]]
- [[ollama]]
- [[vllm]]
- [[index]]
