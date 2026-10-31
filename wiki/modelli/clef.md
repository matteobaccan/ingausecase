---
title: "Clef"
category: modello
tags: [cloudflare, classificazione, decisioni, open-source]
related_puntate: [20261002, 20261003, 20261004]
created: 2026-10-03
updated: 2026-10-12
sources: [raw/puntate/ainews20261002.md, raw/puntate/ainews20261003.md, raw/tldr/tldr20261002.md, raw/pillitteri/pillitteri20261002-cloudflare-clef-sfida-jev.md, raw/puntate/ainews20261004.md, raw/tldr/tldr20261012.md]
---

# Clef

## Introduzione

Famiglia di decision model di [[cloudflare]], composta da Clef e Clef-flash: modelli addestrati internamente che aiutano gli agenti a raccogliere contesto, prendere decisioni ed eseguire azioni, restituendo risposte tipizzate con probabilità. Sono compatibili con l'API di [[jev]] e rilasciati in open source su Hugging Face con licenza Apache 2.0, eseguibili in locale.

## Capacità e performance

- Sono pienamente compatibili con l'API di Jev, così un'applicazione costruita su quello stack può passare a Clef cambiando endpoint e nome del modello. [Fonte: raw/tldr/tldr20261002.md]
- Restituiscono risposte tipizzate con probabilità e possono demandare a un umano quando serve. [Fonte: raw/tldr/tldr20261002.md]
- Nei test della puntata Clef ha battuto Jev in due settimane: con Qwen congelato fa un solo prefill e un piccolo schema head valuta tutte le opzioni in parallelo senza generare testo, risultando quattro volte più veloce di Jev e con doppia precisione su alcuni benchmark. [Fonte: raw/puntate/ainews20261003.md]

## Azienda di riferimento

- [[cloudflare]]

## Timeline delle notizie

- **2026-10-02** — Cloudflare rilascia Clef e Clef-flash, decision model addestrati internamente e compatibili con l'API di Jev, open source su Hugging Face con licenza Apache 2.0 ed eseguibili in locale, presentati insieme a una nuova piattaforma di fine-tuning RL. [Fonte: raw/puntate/ainews20261002.md] [Fonte: raw/tldr/tldr20261002.md]
- **2026-10-02** — Cloudflare rilascia due decision model addestrati internamente, Clef e Clef-flash, un'idea che si sta diffondendo rapidamente. [Fonte: raw/puntate/ainews20261002.md]



- **2026-10-02** — Cloudflare rilascia il 1° ottobre 2026 Clef e Clef-flash, decision model open source su Workers AI e scaricabili da Hugging Face con licenza Apache 2.0, dichiarati "fully Jev-API compatible" e pensati per sostituire [[jev]] senza riscrivere il codice che lo chiama. Clef parte da un backbone Qwen (la pagina ufficiale scrive "Qwen3.8-27B" per Clef e "Qwen3.5-9B" per Clef-flash) e usa un meccanismo non-autoregressivo: un solo passaggio di prefill e poi un punteggio in parallelo su tutte le opzioni valide dello schema, con training che combina cross-entropy con label smoothing e Brier loss più la tecnica proprietaria RLCD. Rispetto a Jev aggiunge un encoder visivo e porta la finestra di contesto a 64.000 token, il doppio; Jev resta avanti su When2Call (80,97 contro 72,37) e su BRIGHT (47,52 contro 45,91). [Fonte: raw/pillitteri/pillitteri20261002-cloudflare-clef-sfida-jev.md]

- **2026-10-03** — La puntata riporta che Clef ha battuto Jev in due settimane: un solo prefill su Qwen congelato, uno schema head che valuta tutte le opzioni in parallelo e zero testo generato, per quattro volte la velocità di Jev e doppia precisione su alcuni benchmark, con codice aperto. [Fonte: raw/puntate/ainews20261003.md]
- **2026-10-03** — Cloudflare Clef batte Jev in due settimane: Qwen congelato fa un solo prefill, un piccolo schema head valuta tutte le opzioni in parallelo e non viene generato testo, per quattro volte la velocità di Jev e doppia precisione su alcuni benchmark, con codice aperto. [Fonte: raw/puntate/ainews20261003.md]
- **2026-10-04** — Cloudflare presenta Decision 2.0: modelli per classificazione e routing da zero virgola sei a ventisette miliardi di parametri, disponibili su Ollama come Clef e Clef Flash. [Fonte: raw/puntate/ainews20261004.md]
- **2026-10-12** — Cloudflare presenta Clef-omni, nuovo membro della famiglia [[clef]] che accetta audio, video, immagine e testo in un'unica chiamata per decidere su qualunque modalità, e abbassa il prezzo di Clef-flash a 0,038 dollari per milione di token in ingresso, mentre Clef diventa più veloce. [Fonte: raw/tldr/tldr20261012.md]










## Collegamenti

- [[cloudflare]]
- [[jev]]
- [[index]]
