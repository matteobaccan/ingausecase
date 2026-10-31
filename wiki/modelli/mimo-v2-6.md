---
title: "MiMo-V2.6"
category: modello
tags: [xiaomi, llm, omnimodale, reasoning, open-weight, agent]
related_puntate: [20260922, 20260927]
created: 2026-09-22
updated: 2026-09-27
sources: [raw/puntate/ainews20260922.md, raw/tldr/tldr20260922.md, raw/pillitteri/pillitteri20260923-xiaomi-mimo-v2-6-open-source.md, raw/puntate/ainews20260927.md]
---

# MiMo-V2.6

## Introduzione

Famiglia omnimodale di [[xiaomi]] (MiMo-V2.6 Pro e Flash) addestrata con reinforcement learning su scala, con Pro alla pari di [[claude-opus-5]] e [[gpt-5-6-sol]] sui benchmark agente e 46 punti sull'Artificial Analysis Intelligence Index, il più alto tra gli open source. [Fonte: raw/puntate/ainews20260922.md]

## Capacità

- Pro e Flash coordinano agenti per costruire e testare visivamente scene 3D interattive, creare asset Blender, controllare braccio robotico da camera, produrre frontend/presentazioni, assemblare video e comporre musica come score e MIDI. [Fonte: raw/tldr/tldr20260922.md]
- L'architettura resta una Mixture-of-Experts da 1,02 trilioni di parametri totali e 42 miliardi attivi, con finestra di contesto a un milione di token; smette di essere un modello text-in-text-out e legge testo, immagini, video e audio nella stessa rete, con un encoder visivo da 681 milioni di parametri e un tokenizzatore audio da 308 milioni. [Fonte: raw/pillitteri/pillitteri20260923-xiaomi-mimo-v2-6-open-source.md]
- Aggiunge ragionamento spaziale in 3D, uso diretto del computer (mouse e tastiera su uno schermo) e un client desktop dedicato, quindi è pensato per lavorare da solo su un compito lungo, dalla scrittura di codice alla navigazione di un sito. [Fonte: raw/pillitteri/pillitteri20260923-xiaomi-mimo-v2-6-open-source.md]

## Performance

- Pro: 46 punti Intelligence Index, pari a Claude Opus 5 e GPT-5.6 Sol. [Fonte: raw/puntate/ainews20260922.md]
- Con quei 46 punti Pro supera [[glm-5-3]] (45) e [[kimi-k3]] (44) ed è il modello ad accesso aperto più capace al mondo in quella classifica; resta sotto i proprietari di punta, che stanno a 53. Cinque mesi prima MiMo-V2.5-Pro si fermava a 26 punti, contro una mediana degli open weight di 18. [Fonte: raw/pillitteri/pillitteri20260923-xiaomi-mimo-v2-6-open-source.md]
- Sui benchmark singoli vince su AutomationBench (53,1) e Terminal Bench 2.1 (89,9) e pareggia con Claude Opus 5 su Agents' Last Exam (31,6); su CyberGym, che misura la capacità di trovare ed eseguire exploit reali, segna il 94%. [Fonte: raw/pillitteri/pillitteri20260923-xiaomi-mimo-v2-6-open-source.md]

## Disponibilità

- Pesi aperti, report tecnico, ambienti RL e codice di training rilasciati; disponibili su AI Studio, MiMo Code, MiMo Desktop, MiMo API e OpenRouter. [Fonte: raw/puntate/ainews20260922.md]
- Prezzi invariati rispetto alla generazione precedente: su [[openrouter]] Flash costa 0,14 dollari per milione di token in ingresso e 0,28 in uscita, Pro 0,435 e 0,87, la variante Pro-UltraSpeed venti volte più veloce 4,35 e 8,70. Pesi e report tecnico sono su Hugging Face con licenza MIT, con quantizzazioni MLX per Apple Silicon e GGUF per la CPU; esiste anche la distillazione MiMo-V2.6-Distill-Qwen-9B per chi non ha un cluster di GPU. [Fonte: raw/pillitteri/pillitteri20260923-xiaomi-mimo-v2-6-open-source.md]

## Azienda di riferimento

- [[xiaomi]]

## Timeline delle notizie

- **2026-09-22** — Xiaomi rilascia MiMo-V2.6 Pro e Flash omnimodali con RL su scala, Pro a 46 punti Intelligence Index e pesi/report/ambienti/codice aperti. [Fonte: raw/puntate/ainews20260922.md]
- **2026-09-22** — TLDR dettaglia le capacità agentico-creative dei due modelli e la disponibilità multipiattaforma. [Fonte: raw/tldr/tldr20260922.md]
- **2026-09-22** — Il salto da 26 a 46 punti non arriva da un addestramento titanico: la fase di reinforcement learning è durata meno di sei giorni, con 750.000 traiettorie generate e un algoritmo GRPO completamente asincrono su 1.568 prompt e 16 rollout paralleli. Il costo dichiarato è di 2,62 milioni di dollari per la versione Pro e 850.000 per la Flash. [Fonte: raw/pillitteri/pillitteri20260923-xiaomi-mimo-v2-6-open-source.md]
- **2026-09-22** — Il rilascio cade nello stesso giorno della presentazione dello [[zhenwu-v900]] da parte di T-Head: gli embarghi americani sui processori Nvidia hanno spinto i produttori cinesi di acceleratori dal quasi nulla del 2022 al 41 per cento del mercato interno nel 2025. [Fonte: raw/pillitteri/pillitteri20260923-xiaomi-mimo-v2-6-open-source.md]
- **2026-09-27** — Xiaomi rilascia i settemila ambienti di reinforcement learning usati per addestrare MiMo, tra i più grandi rilasci di dati per RL frontier open source, e apre l'intero training stack di MiMo-V2.6: non solo i pesi, ma codice di addestramento, ambienti eseguibili in Docker e ricompense basate su regole e verificabili. Su benchmark long-range fuori dal training set Flash passa da quarantotto punto otto a sessantacinque punto sette e Pro da cinquantotto punto quattro a settantadue punto sei su DeepSWE v1.1. [Fonte: raw/puntate/ainews20260927.md]

## Collegamenti

- [[xiaomi]]
- [[claude-opus-5]]
- [[gpt-5-6-sol]]
- [[kimi-k3]]
- [[glm-5-3]]
- [[openrouter]]
- [[zhenwu-v900]]
- [[index]]
