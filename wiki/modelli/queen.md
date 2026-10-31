---
title: "Queen"
category: modello
tags: [llm, open-source, ricerca, scacchi]
related_puntate: []
created: 2026-10-06
updated: 2026-10-06
sources: [raw/pillitteri/pillitteri20261006-princeton-queen-scacchi-4-miliardi-parametri.md]
---

# Queen

## Introduzione

Modello scacchistico-linguistico da 4 miliardi di parametri presentato il 2 ottobre 2026 da Adithya Bhaskar, Jeffrey Cheng e Danqi Chen della Princeton Language and Intelligence, che gioca a 2697 Elo sulla scala Lichess e spiega le proprie mosse in linguaggio naturale. Non nasce da zero: è un modello a due teste con un encoder scacchistico specializzato e un modello linguistico che ne interpreta le rappresentazioni.

## Capacità e performance

- Il decoder è SmolLM3-3B, un modello istruito da 3 miliardi di parametri con 36 strati e dimensione nascosta 2048; l'encoder è una rete BT5 della famiglia Leela Chess Zero da 240 milioni di parametri, 15 strati e dimensione nascosta 1024, collegata al decoder da livelli di cross-attention gated ispirati a Flamingo. Il conto dei «4 miliardi» somma i due componenti e i blocchi di cross-attention, per un calcolo degli autori e non una cifra dichiarata. [Fonte: raw/pillitteri/pillitteri20261006-princeton-queen-scacchi-4-miliardi-parametri.md]
- Il metodo di addestramento è la distillazione iterativa per ricerca: da circa 400.000 posizioni di partenza il modello propone mosse e spiegazioni, scende nelle posizioni figlie quando una mossa cala di almeno il 10% la probabilità di vittoria stimata rispetto all'oracolo Stockfish, fonde le spiegazioni in una sola per la posizione di partenza con Qwen3.8-27B e si riaddestra con fine-tuning supervisionato. Dopo sette giri l'Elo passa da 1782 a 2697, con un calo di 105 punti fra il quinto e il sesto passaggio. [Fonte: raw/pillitteri/pillitteri20261006-princeton-queen-scacchi-4-miliardi-parametri.md]
- I 2697 Elo su scala Lichess vengono da 32 partite contro motori (Stockfish a diversi livelli di nodi, Maia-2200 e reti Lc0 come TinyGyal-8), ancorate alla forza nota delle reti Leela, senza intervalli di confidenza e senza partite contro persone. Nella tabella del paper l'encoder Leela da solo vale 2987 Elo, Gemini-3.1-Pro 2201, GPT-5.6 Sol 2071, GPT-5.6 Luna 1822 e il modello scacchistico C1-4B 514. [Fonte: raw/pillitteri/pillitteri20261006-princeton-queen-scacchi-4-miliardi-parametri.md]
- Sulla coerenza delle spiegazioni Queen prende 2,76 su 5 contro il 3,30 di Gemini-3.1-Pro e il 3,61 di GPT-5.6 Sol (giudice GPT-5.6 Sol), mentre sulle analisi tattiche senza errori è al 68,8% contro il 66,9% di Gemini-3.1-Pro e il 65,1% di GPT-5.6 Sol. Gli autori chiamano «debito di verbalizzazione» i 290 punti di scarto fra l'encoder e il modello completo. [Fonte: raw/pillitteri/pillitteri20261006-princeton-queen-scacchi-4-miliardi-parametri.md]
- Le spiegazioni iniziali del primo giro sono state generate da GPT-5.6 Sol con ragionamento basso, per un costo dichiarato di 652,35 dollari: l'unica voce di spesa quantificata nel paper. [Fonte: raw/pillitteri/pillitteri20261006-princeton-queen-scacchi-4-miliardi-parametri.md]

## Disponibilità

- Codice su GitHub, collezione di modelli su Hugging Face nell'organizzazione princeton-nlp e sito di progetto; il paper è su arXiv (2610.03695). Nelle pagine consultate non compare una licenza dei pesi. [Fonte: raw/pillitteri/pillitteri20261006-princeton-queen-scacchi-4-miliardi-parametri.md]

## Timeline delle notizie

- **2026-10-06** — Princeton Language and Intelligence presenta Queen, modello scacchistico-linguistico da 4 miliardi di parametri a 2697 Elo sulla scala Lichess che spiega le mosse in linguaggio naturale: il risultato nasce dalla distillazione iterativa su circa 400.000 posizioni, con un encoder Leela Chess Zero da 240 milioni di parametri che da solo vale 2987 Elo. Il paper dichiara 652,35 dollari di costo per le spiegazioni iniziali di GPT-5.6 Sol e nessun test contro giocatori umani. [Fonte: raw/pillitteri/pillitteri20261006-princeton-queen-scacchi-4-miliardi-parametri.md]

## Collegamenti

- [[openai]]
- [[google-deepmind]]
- [[open-source]]
- [[matematica-ai]]
- [[index]]
