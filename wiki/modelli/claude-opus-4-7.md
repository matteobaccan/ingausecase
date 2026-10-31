---
title: "Claude Opus 4.7"
category: modello
tags: [anthropic, coding, frontier, llm]
related_puntate: [20260508, 20260514, 20260521, 20260523, 20260530, 20260625, 20260626]
created: 2026-08-12
updated: 2026-10-28
sources: [raw/puntate/ainews20260508.md, raw/puntate/ainews20260514.md, raw/puntate/ainews20260521.md, raw/puntate/ainews20260523.md, raw/puntate/ainews20260530.md, raw/puntate/ainews20260625.md, raw/puntate/ainews20260626.md, raw/pillitteri/pillitteri20260619-project-fetch-fase-2-claude-opus-robot-dog.md, raw/pillitteri/pillitteri20260415-claude-opus-4-7-leak-anthropic-design-tool.md, raw/pillitteri/pillitteri20260509-claude-code-novita-maggio-2026.md, raw/pillitteri/pillitteri20261028-claude-watermark-3-novembre-opus-4-7-sonnet-4-6.md]
---

# Claude Opus 4.7

## Introduzione

Modello top di gamma di Anthropic, al primo posto sul leaderboard Refactoring di Scale AI quando usato con Claude Code.

## Capacità e performance

- Claude Opus 4.7 con Claude Code prende il primo posto su Refactoring, l'ultimo leaderboard della suite SWE Atlas di Scale AI, che testa la capacità di ristrutturare codice senza rompere il sistema.
- Claude Opus 4.7 si è piazzato quinto in una gara live di coding con otto modelli, vinta da Kimi K2; GPT-5.5 terzo.
- Claude Opus 4.7 è stato citato come riferimento: Gemini 3.5 Pro sarà più vicino a GPT-5.5 o Claude Opus 4.7 che a un modello Mythos.

## Azienda di riferimento

- [[scale-ai]]

## Strumenti correlati

- [[claude-code]]
- [[genspark-design]]

## Timeline delle notizie

- **2026-05-08** — Claude Opus 4.7 con Claude Code prende il primo posto su Refactoring, l'ultimo leaderboard della suite SWE Atlas di Scale AI, che testa la capacità di ristrutturare codice senza rompere il sistema. [Fonte: raw/puntate/ainews20260508.md]
- **2026-05-09** — Claude Opus 4.7 porta la finestra di contesto da 200 mila a un milione di token in modo nativo e introduce gli effort levels accessibili da /effort (low, medium, high, xhigh e Auto per Max); due nuove variabili d'ambiente (ENABLE_PROMPT_CACHING_1H e FORCE_PROMPT_CACHING_5M) cambiano la matematica del costo su sessioni lunghe e ripetitive. [Fonte: raw/pillitteri/pillitteri20260509-claude-code-novita-maggio-2026.md]



- **2026-05-14** — Claude Opus 4.7 si è piazzato quinto in una gara live di coding con otto modelli, vinta da Kimi K2; GPT-5.5 terzo. [Fonte: raw/puntate/ainews20260514.md]
- **2026-05-21** — Claude Opus 4.7 è stato citato come riferimento: Gemini 3.5 Pro sarà più vicino a GPT-5.5 o Claude Opus 4.7 che a un modello Mythos. [Fonte: raw/puntate/ainews20260521.md]
- **2026-05-23** — Claude Opus 4.7 è stato citato come riferimento battuto da Qwen 3.7 Max sul test multimodale di spatial reasoning. [Fonte: raw/puntate/ainews20260523.md]
- **2026-05-30** — Claude Opus 4.7 è stato usato da un ricercatore per alimentare Opus 4.8 con frammenti di 'materiali educativi', provocandone il jailbreak in sette minuti dal rilascio. [Fonte: raw/puntate/ainews20260530.md]
- **2026-06-19** — È il modello usato in autonomia nella seconda fase di Project Fetch, lo studio del Frontier Red Team di [[anthropic]] su un robot quadrupede commerciale: completa quattro compiti in nove minuti e trentacinque secondi contro i 361 minuti della squadra umana senza AI, con 1.045 righe di codice contro 10.309 e risultati pari o migliori. Il controllo fine in tempo reale resta il suo limite, perché non riesce a spingere con delicatezza una palla da spiaggia. [Fonte: raw/pillitteri/pillitteri20260619-project-fetch-fase-2-claude-opus-robot-dog.md]
- **2026-06-25** — Claude Opus 4.7 è il modello che alimenta Genspark Design per la generazione di prototipi UI, video, animazioni HTML e poster. [Fonte: raw/puntate/ainews20260625.md]
- **2026-06-26** — Claude Opus quattro punto sette è il confronto del flagship di Ornith uno punto zero, che raggiunge punteggi comparabili sui benchmark di coding. [Fonte: raw/puntate/ainews20260626.md]

- **2026-04-15** — The Information pubblica il leak del 14 aprile: [[anthropic]] sta per rilasciare Opus 4.7 insieme a un tool di design AI che crea siti, landing page e presentazioni da linguaggio naturale, con finestra "entro questa settimana". Il mercato reagisce subito, con Adobe a -3,8 per cento, Wix a -5,2, Figma a -4,1 e GoDaddy a -2,7 intraday. Il 16 aprile il Chief Product Officer di Anthropic Mike Krieger si dimette dal board di Figma, e il 17 aprile, dopo il lancio di Claude Design, Figma perde un altro 6,8 per cento in giornata (oltre l'80 dall'IPO), Wix il 4,7, Adobe il 2,7 e GoDaddy il 3; gli analisti parlano di "SaaSpocalypse". [Fonte: raw/pillitteri/pillitteri20260415-claude-opus-4-7-leak-anthropic-design-tool.md]
- **2026-04-15** — I codename circolati non appartengono a 4.7: dal leak del source code di [[claude-code]] del 31 marzo 2026 (512.000 righe pubblicate per errore sul registro npm) Fennec è una variante di Opus 4.6, Capybara una variante interna di Claude 4.6 e Tengu il codename di Claude Code come prodotto, mentre Numbat resta un modello in testing e non è confermato come 4.7. [Fonte: raw/pillitteri/pillitteri20260415-claude-opus-4-7-leak-anthropic-design-tool.md]
- **2026-10-28** — Dal 3 novembre riceve la filigrana testuale di [[anthropic]] sulla Claude Platform, insieme a Mythos 5, Opus 4.6 e Sonnet 4.6, con Amazon Bedrock qualche giorno dopo: è la stessa filigrana dei modelli lanciati dal 2 agosto, applicata a livello di modello e senza opzione per disattivarla. La filigrana non si applica all'indietro, quindi i testi generati prima del 3 novembre restano senza segnale. [Fonte: raw/pillitteri/pillitteri20261028-claude-watermark-3-novembre-opus-4-7-sonnet-4-6.md]




## Collegamenti

- [[claude-code]]
- [[claude-opus-4-8]]
- [[gemini-3-5]]
- [[genspark-design]]
- [[gpt-5-5]]
- [[kimi-k2]]
- [[ornith-1-0]]
- [[physical-ai]]
- [[qwen-3-7-max]]
- [[scale-ai]]
- [[index]]

