---
title: "Claude Haiku 5.5"
category: modello
tags: [anthropic, economico, haiku, llm, piccolo]
related_puntate: [20261008]
created: 2026-10-08
updated: 2026-10-11
sources: [raw/puntate/ainews20261008.md, raw/tldr/tldr20261008.md, raw/pillitteri/pillitteri20261007-anthropic-lancia-claude-haiku-5-5-prezzo.md, raw/pillitteri/pillitteri20261009-openai-supera-anthropic-openrouter-guerra-prezzi-borsa.md]
---

# Claude Haiku 5.5

## Introduzione

Modello small di [[anthropic]], presentato come il più economico mai rilasciato
dalla famiglia Haiku. È disponibile sia su Claude Platform sia su [[claude-code]].

## Capacità e performance

- Costa circa il settantacinque percento in meno di Haiku 4.5 sui prompt fino a
  centomila token. [Fonte: raw/puntate/ainews20261008.md]
- È pensato per compiti ad alto volume come riassunti, compattazione di dati o
  query su database, e può funzionare come subagent in coppia con Opus o
  Sonnet. [Fonte: raw/puntate/ainews20261008.md]
- TLDR AI segnala costi operativi più bassi e prestazioni più rapide su
  applicazioni come i riassunti e l'assistenza clienti, salvaguardie di
  sicurezza e cybersicurezza rafforzate e una disponibilità più ampia sulle
  principali piattaforme cloud, AWS e Azure. [Fonte: raw/tldr/tldr20261008.md]

## Azienda di riferimento

- [[anthropic]]

## Timeline delle notizie

- **2026-10-07** — Il listino di Haiku 5.5 ha due scaglioni con il confine a centomila token di prompt: 0,10 dollari in ingresso e 0,50 in uscita sotto soglia, 0,50 e 2,50 sopra, cioè un decimo del predecessore sotto e la metà sopra; lettura dalla cache a 0,01 dollari e scrittura a 0,125. Anthropic parla di un 75 per cento di risparmio medio sul carico reale al posto del 90 per cento per token, perché il nuovo tokenizer consuma un po' più di token a parità di testo. [Fonte: raw/pillitteri/pillitteri20261007-anthropic-lancia-claude-haiku-5-5-prezzo.md]

- **2026-10-07** — È il primo Haiku con un'impostazione di effort a cinque livelli (Low, Medium, High, Xhigh e Max, predefinito Medium): i numeri della tabella di Anthropic sono 1.620 punti Elo su GDPval-AA v2.1 contro 735 di Haiku 4.5, 72,4 per cento su OSWorld 2.1 contro 15,7 e 39,2 per cento su Terminal-Bench 4.0 contro lo zero del predecessore, ma il punteggio sul terminale scende intorno al 20 per cento a effort medio e Sonnet 5.5 resta avanti in ogni riga, quindi il leak di fine settembre che prometteva un Haiku superiore a Opus non trova conferma. [Fonte: raw/pillitteri/pillitteri20261007-anthropic-lancia-claude-haiku-5-5-prezzo.md]

- **2026-10-07** — Anthropic abbassa anche la lettura dalla cache di Sonnet 5.5 da 0,20 a 0,10 dollari per milione di token, stimando un costo inferiore di circa il 20 per cento sui compiti agentici tipici; per gli abbonati Max 5x, Max 20x e Team arrivano crediti API mensili da 100, 200 e fino a 500 dollari, spendibili su qualsiasi modello di Claude Platform, e gli SDK Python e TypeScript supportano in beta l'uso del computer e del browser. [Fonte: raw/pillitteri/pillitteri20261007-anthropic-lancia-claude-haiku-5-5-prezzo.md]

- **2026-10-08** — [[anthropic]] lancia Claude Haiku 5.5, il modello small più economico della famiglia: circa il settantacinque percento in meno di Haiku 4.5 sui prompt fino a centomila token, disponibile su Claude Platform e su Claude Code e pensato per compiti ad alto volume. [Fonte: raw/puntate/ainews20261008.md] [Fonte: raw/tldr/tldr20261008.md]
- **2026-10-09** — Il listino di Haiku 5.5 è di 0,10 dollari per milione di token in ingresso e 0,50 in uscita per richieste fino a 100.000 token, oltre quella soglia i prezzi salgono: sono le stesse cifre di GPT-6 Luna e l'azienda dichiara per Haiku 5.5 un costo medio del 75 per cento inferiore a quello di Haiku 4.5. [Fonte: raw/pillitteri/pillitteri20261009-openai-supera-anthropic-openrouter-guerra-prezzi-borsa.md]




## Collegamenti

- [[anthropic]]
- [[claude]]
- [[claude-code]]
- [[index]]
