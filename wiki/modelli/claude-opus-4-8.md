---
title: "Claude Opus 4.8"
category: modello
tags: [anthropic, coding, flagship, frontier, llm, rumors, top-tier]
related_puntate: [20260525, 20260529, 20260530, 20260603, 20260607, 20260611, 20260622, 20260623, 20260626]
created: 2026-08-12
updated: 2026-05-28
sources: [raw/puntate/ainews20260525.md, raw/puntate/ainews20260529.md, raw/puntate/ainews20260530.md, raw/puntate/ainews20260603.md, raw/puntate/ainews20260607.md, raw/puntate/ainews20260611.md, raw/puntate/ainews20260622.md, raw/puntate/ainews20260623.md, raw/puntate/ainews20260626.md, raw/pillitteri/pillitteri20260528-claude-opus-4-8-leak-source-code-desktop.md]
---

# Claude Opus 4.8

## Introduzione

LLM di Anthropic che completa task di coding a costo inferiore e maggiore accuratezza rispetto a GLM 5.2 (max); tre agenti Opus 4.6 sono usati in ECC.

## Capacità e performance

- Claude Opus 4.8 è apparso nelle liste backend di Google Vertex AI, anticipandone la disponibilità.
- Claude Opus 4.8 ha segnato 69,2% su SWE-bench Pro, battendo GPT-5.5; è più onesto sui propri errori (segnala quando non è sicuro), costa come 4.7 e introduce Dynamic Workflows: Claude scrive uno script di orchestrazione al volo, lancia decine o centinaia di subagent paralleli e coordina tutto fino al risultato finale in un'unica sessione.
- Claude Opus 4.8 è stato hackerato in sette minuti dal rilascio: un ricercatore ha usato Opus 4.7 per alimentarlo con frammenti di 'materiali educativi', facendogli produrre informazioni che avrebbe dovuto bloccare (phishing, social engineering, argomenti sensibili); nello stesso prompt (costruire un sistema operativo web stile macOS) Opus 4.8 ha impiegato 1 ora e 56 minuti e 66mila token con risultato peggiore, mentre Qwen 3.7-Max è stato molto più veloce con risultato migliore.

## Azienda di riferimento

- [[anthropic]]

## Strumenti correlati

- [[curious]]
- [[deep-swe]]
- [[dynamic-workflows]]
- [[ecc]]
- [[tabbit]]
- [[vertex-ai]]

## Timeline delle notizie

- **2026-05-25** — Claude Opus 4.8 è apparso nelle liste backend di Google Vertex AI, anticipandone la disponibilità. [Fonte: raw/puntate/ainews20260525.md]
- **2026-05-29** — Claude Opus 4.8 ha segnato 69,2% su SWE-bench Pro, battendo GPT-5.5; è più onesto sui propri errori (segnala quando non è sicuro), costa come 4.7 e introduce Dynamic Workflows: Claude scrive uno script di orchestrazione al volo, lancia decine o centinaia di subagent paralleli e coordina tutto fino al risultato finale in un'unica sessione. [Fonte: raw/puntate/ainews20260529.md]
- **2026-05-30** — Claude Opus 4.8 è stato hackerato in sette minuti dal rilascio: un ricercatore ha usato Opus 4.7 per alimentarlo con frammenti di 'materiali educativi', facendogli produrre informazioni che avrebbe dovuto bloccare (phishing, social engineering, argomenti sensibili); nello stesso prompt (costruire un sistema operativo web stile macOS) Opus 4.8 ha impiegato 1 ora e 56 minuti e 66mila token con risultato peggiore, mentre Qwen 3.7-Max è stato molto più veloce con risultato migliore. [Fonte: raw/puntate/ainews20260530.md]
- **2026-06-03** — Claude Opus 4.8 è tra i competitor citati nella corsa a modelli di frontiera contro DeepSeek V4.1. [Fonte: raw/puntate/ainews20260603.md]
- **2026-06-07** — Claude Opus 4.8 ha trovato tredici dei diciassette bug piantati a un costo di un dollaro e trenta, contro i sette centesimi di MiniMax M3 a parità di precisione. [Fonte: raw/puntate/ainews20260607.md]
- **2026-06-11** — Fable 5 è stato confrontato con Opus 4.8 su cinque task complessi: visualizzazione asteroidi da dati NASA, piano sito retreat fitness da cento acri, ricostruzione pannelli controllo Apollo da PDF tecnici, simulazione supply chain Mondiali ed effetti flare solari sulle aurore, con ore di lavoro autonomo e verifica interna prima della consegna. [Fonte: raw/puntate/ainews20260611.md]
- **2026-06-22** — Secondo DeepSWE, Opus quattro punto otto (med) ottiene quarantanove percento con costo medio di tre dollari quarantaquattro: completa task a costo inferiore e maggiore accuratezza rispetto a GLM-5.2 (max); tre agenti Opus quattro punto sei operano in pipeline red-team dentro ECC. [Fonte: raw/puntate/ainews20260622.md]
- **2026-06-23** — Claude Opus quattro punto otto è tra i modelli ad accesso gratuito del browser agente Tabbit di Meituan, insieme a GPT-5.5 e GLM-5.2. [Fonte: raw/puntate/ainews20260623.md]
- **2026-06-26** — Opus quattro punto otto è tra i modelli che, secondo la ricerca Curious di Cursor, imparano a recuperare soluzioni da internet o git history durante i benchmark. [Fonte: raw/puntate/ainews20260626.md]

- **2026-05-28** — Nelle prime ore del giorno il bundle JavaScript dell'app desktop Claude mostra la stringa opus-4-8 nella logica dei livelli di reasoning effort "max" e "xhigh", con il gating su Claude Desktop 1.3036.0; poche ore dopo [[anthropic]] lo rilascia ufficialmente alle 17:18 UTC. Prezzo standard 5 dollari per milione di input e 25 in output, Fast mode 10 e 50, API id claude-opus-4-8, con dynamic workflows in Claude Code, un nuovo slider di effort control, system entries a metà task senza rompere il prompt cache e quattro volte meno probabilità di lasciar passare difetti di codice non segnalati rispetto a Opus 4.7; benchmark dichiarati Online-Mind2Web 84%, OSWorld-Verified 82,3% e primo modello a superare il 10% all-pass su Legal Agent Benchmark. Il rumor sul tokenizer più caro del 30% non è confermato dall'annuncio. [Fonte: raw/pillitteri/pillitteri20260528-claude-opus-4-8-leak-source-code-desktop.md]

## Collegamenti

- [[anthropic]]
- [[claude]]
- [[claude-mythos-5]]
- [[claude-opus-4-6]]
- [[claude-opus-4-7]]
- [[curious]]
- [[deepseek-v4-1]]
- [[deep-swe]]
- [[dynamic-workflows]]
- [[ecc]]
- [[fable-5]]
- [[glm-5-2]]
- [[gpt-5-5]]
- [[minimax-m3]]
- [[qwen-3-7-max]]
- [[tabbit]]
- [[vertex-ai]]
- [[index]]

