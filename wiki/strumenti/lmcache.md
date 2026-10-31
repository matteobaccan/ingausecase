---
title: "LMCache"
category: strumento
tags: [cache, inferenza, open-source]
related_puntate: [20260710, 20260718]
created: 2026-08-12
updated: 2026-10-09
sources: [raw/puntate/ainews20260710.md, raw/puntate/ainews20260718.md, raw/controrumore/controrumore20261009-diario-ai-gpt-6-cambia-forma-a-chatgpt.md]
---

# LMCache

## Introduzione

Gestione open source della KV cache per vLLM, SGLang e TensorRT-LLM, quattordici volte più veloce sul time-to-first-token con novanta per cento di risparmio sui costi.

## Funzionalità principali

- LMCache è una gestione KV cache open source per vLLM, SGLang e TensorRT-LLM: quattordici volte più veloce time-to-first-token e novanta per cento di risparmio sui costi.
- LMCache riutilizza il testo in qualsiasi posizione del prompt, anche tra nodi diversi, per vLLM e SGLang: riduce il time-to-first-token da tre a dieci volte su workload RAG e multi-round, già adottato da Google Cloud, CoreWeave e NVIDIA.

## Timeline delle notizie

- **2026-07-10** — LMCache è una gestione KV cache open source per vLLM, SGLang e TensorRT-LLM: quattordici volte più veloce time-to-first-token e novanta per cento di risparmio sui costi. [Fonte: raw/puntate/ainews20260710.md]
- **2026-07-18** — LMCache riutilizza il testo in qualsiasi posizione del prompt, anche tra nodi diversi, per vLLM e SGLang: riduce il time-to-first-token da tre a dieci volte su workload RAG e multi-round, già adottato da Google Cloud, CoreWeave e NVIDIA. [Fonte: raw/puntate/ainews20260718.md]
- **2026-10-09** — JFrog documenta una vulnerabilità in LMCache che può consentire esecuzione remota di codice senza autenticazione quando il trasporto multiprocesso ZeroMQ è esposto alla rete: il difetto CVE-2026-105192 ha punteggio CVSS 9,8, la configurazione locale predefinita non presenta la stessa raggiungibilità esterna e al momento dell'analisi non era disponibile una versione correttiva, rendendo decisive verifica delle installazioni, segmentazione e limitazione dell'accesso. [Fonte: raw/controrumore/controrumore20261009-diario-ai-gpt-6-cambia-forma-a-chatgpt.md]




## Collegamenti

- [[turbo-vec]]
- [[index]]

