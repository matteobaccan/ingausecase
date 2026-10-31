---
title: "Qwen 3.5"
category: modello
tags: [alibaba, cina, llm, moe, open-weight]
related_puntate: [20260621, 20260627, 20260725, 20260727, 20260728, 20260909, 20260924]
created: 2026-08-12
updated: 2026-10-25
---

# Qwen 3.5

## Introduzione

Generazione della famiglia Qwen di Alibaba, usata come base per modelli computer-use (Fara 1.5) e dimostrata capace di girare offline su cluster Nvidia GB10. Nel periodo è stata presa come riferimento nei confronti con Nanbeige 4.2.

## Capacità e performance

- Qwen tre punto cinque è tra i cinque modelli cinesi di frontiera resi accessibili gratuitamente da NVIDIA con una sola chiave API.
- Usato come base di post-training per Ornith 1.0, che ha segnato 77,5 su TerminalBench; licenza MIT.
- È la base di Fara1.5-27B di Microsoft, modello per computer use che naviga web, compila form ed estrae dati da screenshot.

## Azienda di riferimento

- [[alibaba]]
- [[nvidia]]

## Timeline delle notizie

- **2026-06-21** — Qwen tre punto cinque è tra i cinque modelli cinesi di frontiera resi accessibili gratuitamente da NVIDIA con una sola chiave API.
- **2026-06-27** — Usato come base di post-training per Ornith 1.0, che ha segnato 77,5 su TerminalBench; licenza MIT.
- **2026-07-25** — È la base di Fara1.5-27B di Microsoft, modello per computer use che naviga web, compila form ed estrae dati da screenshot.
- **2026-07-27** — Un cluster di otto nodi Nvidia GB10 lo ha fatto girare offline: 397 miliardi di parametri, un terabyte di memoria pooled, solo 17 miliardi attivi per token con sparsità MoE, 24 token al secondo, costo totale 32.000 dollari, dati che non escono mai dalla stanza.
- **2026-07-28** — Nanbeige 4.2-3B potrebbe aver dimostrato che un modello da tre miliardi di parametri può superare Qwen 3.5-9B e Gemma 4-12B.
- **2026-09-09** — FrogNano è un Qwen tre punto cinque quattro B post-addestrato solo con RL su task sintetici da TaskPilot, senza distillazione, con sessantuno punto cinque percento su SWE-bench Verified.
- **2026-09-24** — Un fine-tune di Qwen 3.5-9B pubblicato su Hugging Face trasforma i documenti lunghi in piccole immagini di pagina per risparmiare token, poi recupera il testo completo solo delle pagine rilevanti alla domanda.
- **2026-10-02** — Qwen 3.5 9B diventa la base del modello Ajax di PewDiePie, un fine-tuning da 9 miliardi di parametri con supporto alle immagini e finestra di contesto di 262.144 token, pensato per girare in locale su una singola GPU con almeno 22 GB di VRAM in BF16 o 11 GB in FP8. È un caso in cui il modello open-weight cinese finisce al centro di una vicenda di distillazione: secondo Kjellberg OpenAI ha disattivato il suo account perché avrebbe usato le catene di ragionamento del modello Sol per generare dati con cui addestrare Ajax.
- **2026-10-24** — pplx-decider-flash-v1.2, il decision model da 4 miliardi di parametri che [[perplexity]] distribuisce con Decider for Mac, è costruito su Qwen3.5-4B e distillato dai modelli da 27 miliardi dell'azienda, circa un settimo delle dimensioni.







## Collegamenti

- [[alibaba]]
- [[fara-1-5]]
- [[frognano]]
- [[nvidia]]
- [[ornith-1-0]]
- [[qwen-3-6]]
- [[index]]

