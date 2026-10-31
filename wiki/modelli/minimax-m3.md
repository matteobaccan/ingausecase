---
title: "MiniMax M3"
category: modello
tags: [cina, coding, contesto-lungo, efficienza, llm, m3, minimax, multimodale, open-weight]
related_puntate: [20260602, 20260603, 20260607, 20260610, 20260614, 20260621, 20260630, 20260702, 20260810, 20260812, 20260825]
created: 2026-08-12
updated: 2026-10-19
sources: [raw/puntate/ainews20260602.md, raw/puntate/ainews20260603.md, raw/puntate/ainews20260607.md, raw/puntate/ainews20260610.md, raw/puntate/ainews20260614.md, raw/puntate/ainews20260621.md, raw/puntate/ainews20260630.md, raw/puntate/ainews20260702.md, raw/puntate/ainews20260810.md, raw/puntate/ainews20260812.md, raw/puntate/ainews20260825.md, raw/pillitteri/pillitteri20260601-minimax-m3-open-weights-coding-1m-context.md, raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]
---

# MiniMax M3

## Introduzione

Modello open-weight multimodale di MiniMax con capacita' coding e agentiche frontier-level, contesto fino a un milione di token; l'ambiente MiniMax Code include browser integrato.

## Capacità e performance

- MiniMax M3 è il primo modello open weights con tre capacità di frontiera: cinquantanove punto zero percento su SWE-Bench Pro, sessantasei su Terminal-Bench 2.1, trentaquattro punto otto su SWE-fficiency, ventotto punto otto su KernelBench Hard e settantaquattro punto due su MCP Atlas; con MiniMax Sparse Attention scala a un milione di token, nativamente multimodale; pesi e report tecnico in circa dieci giorni. In un test ha trasformato uno schizzo di platformer in gioco HTML: seimilanovecentoventi token in input, novemilanovecentotrentatré in output, costo zero virgola zero due otto dollari.
- MiniMax M3 è citato tra i competitor di DeepSeek V4.1 nel mercato dei modelli di frontiera.
- Allo stesso codice con diciassette bug piantati, MiniMax M3 ne ha trovati tredici per sette centesimi mentre Claude Opus 4.8 ne ha trovati tredici per un dollaro e trenta: stessa precisione, costo molto diverso.

## Azienda di riferimento

- [[nvidia]]

## Strumenti correlati

- [[browser-use]]
- [[clinepass]]
- [[freebuff]]
- [[hermes-desktop]]
- [[minimax-sparse-attention]]
- [[nararouter]]
- [[vllm]]

## Timeline delle notizie

- **2026-06-01** — I dettagli tecnici del rilascio: addestramento su oltre cento trilioni di token con immagini e testo allineati dal primo passo, architettura MiniMax Sparse Attention con lettura dei blocchi di memoria una sola volta ("KV outer gather Q"), oltre quattro volte più veloce di Flash-Sparse-Attention, con prefill nove volte e decodifica fino a quindici punto sei volte più rapidi della generazione precedente. Fra i casi reali raccontati da MiniMax, la riproduzione autonoma di un paper ICLR 2025 in dodici ore con diciotto commit e ventitré figure, e un kernel CUDA FP8 GEMM portato dal 7,6 al 71,3 per cento di utilizzo dell'hardware, per un guadagno di 9,4 volte dopo centoquarantasette sottomissioni. [Fonte: raw/pillitteri/pillitteri20260601-minimax-m3-open-weights-coding-1m-context.md]
- **2026-06-02** — MiniMax M3 è il primo modello open weights con tre capacità di frontiera: cinquantanove punto zero percento su SWE-Bench Pro, sessantasei su Terminal-Bench 2.1, trentaquattro punto otto su SWE-fficiency, ventotto punto otto su KernelBench Hard e settantaquattro punto due su MCP Atlas; con MiniMax Sparse Attention scala a un milione di token, nativamente multimodale; pesi e report tecnico in circa dieci giorni. In un test ha trasformato uno schizzo di platformer in gioco HTML: seimilanovecentoventi token in input, novemilanovecentotrentatré in output, costo zero virgola zero due otto dollari. L'articolo di lancio aggiunge i numeri che la puntata lasciava fuori: ottantatré punto cinque su BrowseComp e risultati sopra Gemini 3.1 Pro su OmniDocBench, tariffe di 0,30 dollari per milione di token in ingresso e 1,20 in uscita su OpenRouter con sconto di debutto del cinquanta per cento, e Token Plan da 20, 50 e 120 dollari al mese per i piani Plus, Max e Ultra. [Fonte: raw/puntate/ainews20260602.md] [Fonte: raw/pillitteri/pillitteri20260601-minimax-m3-open-weights-coding-1m-context.md]
- **2026-06-03** — MiniMax M3 è citato tra i competitor di DeepSeek V4.1 nel mercato dei modelli di frontiera. [Fonte: raw/puntate/ainews20260603.md] addestramento su oltre cento trilioni di token con immagini e testo allineati dal primo passo, architettura MiniMax Sparse Attention con lettura dei blocchi di memoria una sola volta ("KV outer gather Q"), oltre quattro volte più veloce di Flash-Sparse-Attention, con prefill nove volte e decodifica fino a quindici punto sei volte più rapidi della generazione precedente. Fra i casi reali raccontati da MiniMax, la riproduzione autonoma di un paper ICLR 2025 in dodici ore con diciotto commit e ventitré figure, e un kernel CUDA FP8 GEMM portato dal 7,6 al 71,3 per cento di utilizzo dell'hardware, per un guadagno di 9,4 volte dopo centoquarantasette sottomissioni. [Fonte: raw/pillitteri/pillitteri20260601-minimax-m3-open-weights-coding-1m-context.md]
- **2026-06-07** — Allo stesso codice con diciassette bug piantati, MiniMax M3 ne ha trovati tredici per sette centesimi mentre Claude Opus 4.8 ne ha trovati tredici per un dollaro e trenta: stessa precisione, costo molto diverso. [Fonte: raw/puntate/ainews20260607.md]
- **2026-06-10** — MiniMax M3 ha risolto il problema del reset del contesto di Claude Code: costruisce giochi completi dall'inizio alla fine senza mai dimenticare cosa sta facendo, come un gioco tipo Contra generato in una sessione continua. [Fonte: raw/puntate/ainews20260610.md]
- **2026-06-14** — MiniMax M3 è il modello su cui è basato Hermes Desktop Agent nell'apprendimento di TouchDesigner da zero. [Fonte: raw/puntate/ainews20260614.md]
- **2026-06-21** — Minimax M3 è tra i cinque modelli cinesi di frontiera resi accessibili gratuitamente da NVIDIA con una sola chiave API. [Fonte: raw/puntate/ainews20260621.md]
- **2026-06-30** — Incluso nel benchmark comparativo di Browser Use con GLM 5.2, Opus 4.7 e GPT 5.5, e tra i modelli open-weight di ClinePass. [Fonte: raw/puntate/ainews20260630.md]
- **2026-07-02** — Supportato da vLLM 0.25 con quantizzazione FP8 e MXFP4. [Fonte: raw/puntate/ainews20260702.md]
- **2026-08-10** — MiniMax M3 e' tra i modelli supportati da NaraRouter, gateway con sette milioni di token ogni ventiquattro ore senza carta o abbonamento. [Fonte: raw/puntate/ainews20260810.md]
- **2026-08-12** — MiniMax M3 e' un modello open-weight multimodale con capacita' coding e agentiche frontier-level: comprensione nativa multimodale e finestra di contesto fino a un milione di token; MiniMax Code ora include un browser integrato, con cui M3 cerca sul web, legge pagine, cattura screenshot e visualizza output HTML. [Fonte: raw/puntate/ainews20260812.md]
- **2026-08-25** — GMI Cloud offre due miliardi di token gratuiti per MiniMax M3 e MiniMax 2.7 per i próximos quattordici giorni, con accesso API senza pagamento anticipato. [Fonte: raw/puntate/ainews20260825.md]
- **2026-10-19** - MiniMax lancia [[minimax-m3-1-flash|M3.1 Flash]] come variante veloce e leggera della famiglia, con contesto da un milione di token, ingresso multimodale e prezzi dimezzati rispetto a M3 sotto i 512.000 token (0,15 e 0,60 dollari per milione) e un quarto sopra; i pesi arriveranno il 23 ottobre. [Fonte: raw/pillitteri/pillitteri20261019-minimax-m3-1-flash-annuncio-anteprima-space-bunny.md]




## Collegamenti

- [[browser-use]]
- [[claude-opus-4-8]]
- [[clinepass]]
- [[deepseek-v4-1]]
- [[fable-5]]
- [[freebuff]]
- [[glm-5-2]]
- [[hermes-desktop]]
- [[minimax-sparse-attention]]
- [[minimax-agent]]
- [[nararouter]]
- [[gmi-cloud]]
- [[nvidia]]
- [[vllm]]
- [[index]]

