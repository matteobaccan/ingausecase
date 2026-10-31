---
title: "Qwen3.6"
category: modello
tags: [agent, alibaba, cina, llm, open-weight, qwen]
related_puntate: [20260517, 20260711, 20260713, 20260720, 20260722, 20260724, 20260729, 20260812]
created: 2026-08-12
updated: 2026-08-12
---

# Qwen3.6

## Introduzione

Generazione della famiglia Qwen di Alibaba, protagonista di test di efficienza token (Agent Zero) e di ottimizzazioni di inferenza (llama.cpp, quantizzazione a un bit). Nel periodo è la base del quantizzato Bonsai 27B.

## Capacità e performance

- Un developer ha chiesto a Qwen 3.6 di lanciare 64 agenti in parallelo: otto ore di esecuzione, zero permission richieste e zero API call, tutto locale e senza costi; Gemma 4 ha rifiutato, Qwen ha iniziato a costruire senza dire nulla.
- Su un DGX Spark con Qwen 3.6 da trentacinque miliardi di parametri, sessantaquattro utenti simultanei ricevono oltre settecento token al secondo, ognuno con il proprio prompt e cache indipendente.
- Qwen 3.6 da ventisette miliardi di parametri gira a oltre centocinquanta token al secondo su due RTX 3090 usate grazie a DFlash, modello draft che indovina quindici token per volta mentre il modello principale verifica tutto in un pass.

## Azienda di riferimento

- [[alibaba]]
- [[amd-token-factory]]

## Strumenti correlati

- [[agent-zero]]
- [[codex]]
- [[dflash]]
- [[dgx-spark]]
- [[llama-cpp]]
- [[vllm]]

## Timeline delle notizie

- **2026-05-17** — Un developer ha chiesto a Qwen 3.6 di lanciare 64 agenti in parallelo: otto ore di esecuzione, zero permission richieste e zero API call, tutto locale e senza costi; Gemma 4 ha rifiutato, Qwen ha iniziato a costruire senza dire nulla.
- **2026-07-11** — Su un DGX Spark con Qwen 3.6 da trentacinque miliardi di parametri, sessantaquattro utenti simultanei ricevono oltre settecento token al secondo, ognuno con il proprio prompt e cache indipendente.
- **2026-07-13** — Qwen 3.6 da ventisette miliardi di parametri gira a oltre centocinquanta token al secondo su due RTX 3090 usate grazie a DFlash, modello draft che indovina quindici token per volta mentre il modello principale verifica tutto in un pass.
- **2026-07-20** — Qwen 3.6 da ventisette miliardi è stato compresso a 3,9 giga da Bonsai, un bit per peso: venti token al secondo su GTX 1660 Super e tool calling perfetto su loop multi-step.
- **2026-07-22** — La versione 27B è la base di Bonsai 27B, quantizzato a un bit e compresso a 3,9 GB, che gira su iPhone mantenendo il 90% delle capacità originali.
- **2026-07-24** — In un test con Agent Zero su un task identico, con Qwen 3.6-27B sono stati consumati 239.000 token contro i 627.000 di Codex: un'efficienza 2,6 volte superiore per Agent Zero.
- **2026-07-29** — llama.cpp ha fixato un bug di performance MTP che lo rende il 10% più veloce su Qwen 3.6-35B-A3B, incluso nella release b10152 del 27 luglio.
- **2026-08-12** — Qwen3.6 e DeepSeek V4 Flash sono gratis su AMD Token Factory con dieci dollari di utilizzo al giorno e contatore che si resetta quotidianamente.

## Collegamenti

- [[agent-zero]]
- [[alibaba]]
- [[amd-token-factory]]
- [[bonsai-27b]]
- [[codex]]
- [[deepseek-v4-flash]]
- [[dflash]]
- [[dgx-spark]]
- [[gemma-4]]
- [[llama-cpp]]
- [[vllm]]
- [[index]]

