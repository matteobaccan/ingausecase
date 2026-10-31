---
title: "Timestral"
category: modello
tags: [mistral, open-weight, previsioni, serie-temporali]
related_puntate: [20261019]
created: 2026-10-19
updated: 2026-10-23
sources: [raw/puntate/ainews20261019.md, raw/pillitteri/pillitteri20261023-mistral-timestral-ai-prevede-numeri-cpu.md]
---

# Timestral

## Introduzione

Foundation model di [[mistral]] da duecentonove milioni di parametri per le previsioni su serie temporali, pensato per girare su CPU. [Fonte: raw/puntate/ainews20261019.md]

## Capacità e performance

- Gira su CPU in circa centoquaranta millisecondi, senza GPU. [Fonte: raw/puntate/ainews20261019.md]
- Gestisce fino a trentaduemila step storici e produce previsioni fino a milleventiquattro step in avanti. [Fonte: raw/puntate/ainews20261019.md]
- Su GIFT-Eval, TIME e fev-bench si posiziona primo tra i modelli pretrained zero-shot. [Fonte: raw/puntate/ainews20261019.md]

## Disponibilità

- Esiste anche una versione da cinque milioni di parametri che pesa ventuno megabyte. [Fonte: raw/puntate/ainews20261019.md]

## Azienda di riferimento

- [[mistral]]

## Modelli correlati

- [[timesfm]]

## Timeline delle notizie

- **2026-10-19** — [[mistral]] ha rilasciato Timestral, foundation model da duecentonove milioni di parametri per le previsioni su serie temporali: gira su CPU in circa centoquaranta millisecondi, gestisce fino a trentaduemila step storici e produce previsioni fino a milleventiquattro step in avanti, primo tra i pretrained zero-shot su GIFT-Eval, TIME e fev-bench. [Fonte: raw/puntate/ainews20261019.md]
- **2026-10-23** — La famiglia completa conta quattro modelli da 5, 28, 123 e 209 milioni di parametri, legge fino a 32.768 punti di storia e restituisce 21 quantili per ogni passo, con covariate note solo fino a oggi o anche nel futuro. Mistral dichiara 10 millisecondi sul modello da 5 milioni e 140 su quello da 209 su una CPU server a 8 thread, e un primo posto tra i modelli zero-shot pre-addestrati su GIFT-Eval, TIME e fev-bench, con margini di tre millesimi sul secondo. [Fonte: raw/pillitteri/pillitteri20261023-mistral-timestral-ai-prevede-numeri-cpu.md]

- **2026-10-23** — I pesi sono gratis solo sotto i 20 milioni di dollari di fatturato mensile dell'azienda o del datore di lavoro: sopra quella soglia serve una licenza commerciale che Mistral può rifiutare, e il vincolo si trasmette ai modelli derivati; il codice di inferenza su GitHub è invece Apache 2.0. Il modello separa storia e valori da prevedere con la tecnica Decoupled Horizon Forecasting e si è addestrato in gran parte su dati sintetici, prima con contesto 8.192 e poi a 32.768 passi. [Fonte: raw/pillitteri/pillitteri20261023-mistral-timestral-ai-prevede-numeri-cpu.md]




## Collegamenti

- [[mistral]]
- [[timesfm]]
- [[index]]
