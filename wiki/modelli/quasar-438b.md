---
title: "Quasar 438B"
category: modello
tags: [compressione, europa, glm, llm, open-weight]
related_puntate: []
created: 2026-09-12
updated: 2026-09-12
---

# Quasar 438B

## Introduzione

Modello presentato il 2 settembre 2026 da [[multiverse-computing]], azienda spagnola di San Sebastián, come il più capace mai costruito in Europa: 438 miliardi di parametri, inglese e spagnolo, pensato per agenti aziendali e scrittura di codice e usabile tramite la CompactifAI API. Il punto che il comunicato non mette in prima riga è la provenienza: Quasar non nasce da zero, è [[glm-5-2]] di [[zhipu-ai]] passato attraverso la compressione che è il vero mestiere di Multiverse. La scheda di Artificial Analysis lo cataloga come "Quasar 438B (max, based on GLM-5.2)".

## Capacità

- Comprensione e ragionamento su contesti lunghi: nella prova AA-LCR dell'Intelligence Index ottiene 75,0, pareggiando Grok 4.6 di [[xai]] e restando a un punto da Claude Opus 5.
- Velocità: 500 token prodotti in 15,3 secondi con il tempo di ragionamento incluso; solo tre modelli nel confronto vanno più veloci e uno solo tra questi, Gemini 3.7 Flash, ha anche un punteggio più alto.
- Orientamento ad agenti aziendali e generazione di codice, in inglese e spagnolo.

## Performance

| Modello | Intelligence Index v4.1.1 | Provenienza |
| --- | --- | --- |
| Claude Opus 5 | 63 | USA (Anthropic) |
| Quasar 438B | 43 | base GLM 5.2 (Cina) |
| Inkling | 42 | USA |
| NVIDIA Nemotron 3 Ultra | 38 | USA (NVIDIA) |
| Mistral Medium 3.5 | 30 | Francia (Mistral AI) |

Quasar è primo tra i modelli europei con 43 punti, ma nella classifica generale è tredicesimo su 178 e resta venti punti sotto Claude Opus 5. Su Terminal-Bench, la prova di coding in ambiente reale, prende 69,3 contro 89,1 di Opus 5. Il confronto con Mistral Medium 3.5 (30) è il più usato nel racconto europeo, ma Mistral è l'unico dei due ad addestrare i propri pesi da zero.

## Disponibilità

Tramite la CompactifAI API di Multiverse, dal dashboard dell'azienda, senza infrastruttura propria. Nella scheda pubblica la colonna "architettura originale" per Quasar resta vuota mentre per altri modelli è compilata, il dettaglio su cui si è concentrata la critica del blog Signal Over Noise.

## Azienda di riferimento

- [[multiverse-computing]]

## Modelli correlati

- [[glm-5-2]]

## Timeline delle notizie

- **2026-09-11** — La ricostruzione della provenienza ridimensiona il racconto della "migliore AI europea": il caso si intreccia con il tema della sovranità digitale e con il precedente italiano di [[emma]] di [[egomnia]], mentre la Cina, con la sua strategia sui pesi aperti, diventa di fatto il fornitore di base di mezzo mondo.

## Collegamenti

- [[competizione-usa-cina]]
- [[glm-5-2]]
- [[multiverse-computing]]
- [[open-source]]
- [[index]]
