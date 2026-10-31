---
title: "Lean"
category: strumento
tags: [open-source, matematica, verifica-formale, dimostrazioni]
related_puntate: []
created: 2026-09-12
updated: 2026-10-18
sources: [raw/pillitteri/pillitteri20260801-astra-dieci-problemi-matematica-lean.md, raw/pillitteri/pillitteri20260801-openai-astra-modello-multi-agente-senato.md, raw/pillitteri/pillitteri20260814-claude-ipotesi-riemann-zeta.md, raw/controrumore/controrumore20260924-diario-ai-la-nuova-guerra-dei-modelli.md, raw/pillitteri/pillitteri20261018-congettura-grad-gpt-6-astra-pro-fusione.md]
---

# Lean

## Introduzione

Linguaggio in cui ogni passaggio logico di una dimostrazione viene scritto in
modo che un programma possa validarlo meccanicamente. La versione usata nei
lavori di [[openai]] è Lean 4, insieme alla libreria **mathlib**.
[Fonte: raw/pillitteri/pillitteri20260801-astra-dieci-problemi-matematica-lean.md]

## Funzionalità principali

- Un certificato Lean è una versione della prova che un programma può
  controllare riga per riga senza fidarsi di chi l'ha scritta. [Fonte: raw/pillitteri/pillitteri20260801-astra-dieci-problemi-matematica-lean.md]
- Gli assiomi dichiarati nelle dimostrazioni di [[ten-proofs]] sono i tre
  standard della matematica classica in Lean: `propext`, `Classical.choice` e
  `Quot.sound`. Nessun assioma su misura che renderebbe una prova vera per
  costruzione. [Fonte: raw/pillitteri/pillitteri20260801-astra-dieci-problemi-matematica-lean.md]
- Accanto a Lean, il repository include configurazioni per **Comparator**, uno
  strumento che ricontrolla le dimostrazioni con un verificatore esterno
  indipendente, in modo che un difetto del compilatore non passi inosservato.
  [Fonte: raw/pillitteri/pillitteri20260801-astra-dieci-problemi-matematica-lean.md]

## Installazione e uso

- I file di [[ten-proofs]] sono costruibili con Lean 4.32.0 e la libreria
  mathlib attraverso due comandi. [Fonte: raw/pillitteri/pillitteri20260801-astra-dieci-problemi-matematica-lean.md]

## Casi d'uso

- La correttezza smette di essere una questione di fiducia nel laboratorio:
  chiunque abbia un computer può ricompilare le prove, e il tempo di revisione
  crolla da mesi di lettura umana a ore di macchina. Restano fuori dal
  certificato le domande sul metodo: quanti tentativi, quanta selezione, quanto
  lavoro umano. [Fonte: raw/pillitteri/pillitteri20260801-astra-dieci-problemi-matematica-lean.md]

## Timeline delle notizie

- **2026-08-01** — I dieci risultati matematici di [[gpt-6-astra]] escono
  accompagnati da un certificato Lean ciascuno: è il dettaglio che rende
  l'annuncio diverso dai precedenti. [Fonte: raw/pillitteri/pillitteri20260801-astra-dieci-problemi-matematica-lean.md]. [Fonte: raw/pillitteri/pillitteri20260801-openai-astra-modello-multi-agente-senato.md]
- **2026-08-10** — Il risultato di [[anthropic]] sul limite legato all'ipotesi di Riemann arriva anche come formalizzazione Lean pubblica nel repository GitHub `zeta-23-lean`, realizzata insieme a Eric Easley: si clona il repository, si entra nella cartella e `lake build` verifica la dimostrazione riga per riga, senza margini di ambiguità. È la parte controllabile di un lavoro che nel complesso non è riproducibile, perché il modello di ricerca usato non è stato identificato. [Fonte: raw/pillitteri/pillitteri20260814-claude-ipotesi-riemann-zeta.md]

- **2026-09-23** — Vals AI pubblica [[c-hd]], algoritmo shortest-path ideato da dieci agenti [[claude-opus-5-5]] sotto la direzione di un ricercatore, con prova Lean della correttezza e del bound di runtime in circa quindici ore. [Fonte: raw/controrumore/controrumore20260924-diario-ai-la-nuova-guerra-dei-modelli.md]
- **2026-10-18** — L'articolo "Counterexamples to Grad's conjecture" di Gómez-Serrano, Liehr e Taylor dichiara una certificazione in Lean 4, controllata con la versione 4.33.1 e dipendente dai soli tre assiomi standard, mentre le due famiglie di Matt Landreman non hanno verifica formale e poggiano su confronti numerici e simbolici. [Fonte: raw/pillitteri/pillitteri20261018-congettura-grad-gpt-6-astra-pro-fusione.md]




## Collegamenti

- [[anthropic]]
- [[c-hd]]
- [[claude-opus-5-5]]
- [[ten-proofs]]
- [[gpt-6-astra]]
- [[openai]]
- [[frontiermath]]
- [[index]]
