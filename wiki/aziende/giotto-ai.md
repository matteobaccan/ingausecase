---
title: "Giotto AI"
category: azienda
tags: [svizzera, ai-sovrana, modelli-aperti, on-premise, europa]
related_puntate: []
created: 2026-10-28
updated: 2026-10-28
---

# Giotto AI

## Introduzione

Laboratorio di ricerca con sede a Losanna, fondato nel 2017 da ex studenti di matematica dell'EPFL, che lavora su modelli linguistici, sistemi di ragionamento e interpretabilità; finora vendeva soprattutto a enti pubblici e aziende svizzere con una licenza a pagamento per ogni scheda grafica. Il 27 ottobre 2026 ha lanciato la famiglia Giotto, presentata come «i modelli AI sovrani europei più intelligenti sul mercato».

## Modelli

- **Giotto Alto** è il modello di punta per il ragionamento avanzato, gira su otto GPU Nvidia B300 ed è gratuito per tutti sul web e nelle app per iPhone e Android, con server in Europa; l'uso aziendale e l'API con più richieste in parallelo sono a pagamento.
- **Giotto Solo** è dichiarato «il modello più intelligente che gira su una sola GPU» e serve alle organizzazioni che vogliono tenere l'AI in casa, su workstation o server in sede.
- L'azienda non ha comunicato né il numero di parametri né la finestra di contesto: descrive l'architettura come una rete coordinata di modelli più piccoli e specializzati, non un unico modello gigante, e punta sul test-time compute.

## Benchmark dichiarati

| Prova | Giotto Alto | Giotto Solo |
| --- | --- | --- |
| GPQA-Diamond | 91,9% | 88,3% |
| Humanity's Last Exam | 52,0% | 37,5% |
| AIME 2026 | 100% | 96,6% |

I punteggi sono quelli della pagina dei modelli di giotto.ai e li ha misurati l'azienda: stando ai suoi stessi grafici Alto resta dietro a GPT-6 Astra e a Claude Fable 5.1 su GPQA-Diamond e Humanity's Last Exam, e pareggia i migliori su AIME 2026.

## Disponibilità e prezzi

- Alto si usa gratis da cloud.giotto.ai anche in modalità anonima, senza account, oppure dall'app; l'API ha un canone fisso «a consumo illimitato» con una sola richiesta alla volta, più pacchetti di token per il parallelismo. Le cifre in euro o franchi non sono state comunicate.
- Il cloud dedicato affitta istanze isolate a partire da una GPU al mese in data center partner in Svizzera o nel resto d'Europa; l'installazione in sede passa da integratori certificati con licenza annuale o pluriennale calcolata sul numero e sul tipo di GPU.
- Il cliente più noto è RUAG, che secondo swissinfo integrerà il motore nel proprio chatbot interno LLARA.

## Critiche ricevute

- A poche ore dal lancio alcuni utenti hanno mostrato Alto rispondere di essere un modello Kimi di Moonshot AI in esecuzione come servizio «giotto-model», da cui l'accusa che erediti i pesi di un modello cinese; l'azienda non ha commentato pubblicamente.
- La licenza vieta di fare reverse engineering del modello e di sottoporlo a benchmark destinati alla pubblicazione senza consenso scritto, e il confronto sulla matematica usa Claude Sonnet 4, uscito a maggio 2025; nessuna classifica indipendente di fine ottobre include Giotto.

## Timeline delle notizie

- **2026-10-28** — La svizzera Giotto AI lancia Giotto Alto e Giotto Solo, presentati come i modelli AI sovrani europei più intelligenti sul mercato: Alto gira su otto GPU Nvidia B300 ed è gratuito per tutti sul web e nelle app con server in Europa, Solo sta su una singola GPU per chi vuole tenere l'AI in sede. L'azienda non comunica parametri né finestra di contesto, dichiara su GPQA-Diamond 91,9 e 88,3 per cento e su Humanity's Last Exam 52,0 e 37,5, e resta dietro a GPT-6 Astra e Claude Fable 5.1 sulle prove più difficili. A poche ore dal lancio arrivano tre critiche: il modello che si presenta come Kimi di Moonshot AI, i benchmark misurati in casa e una licenza che vieta di pubblicarne di propri senza consenso scritto.

## Collegamenti

- [[ai-europea]]
- [[ai-locale]]
- [[kimi-k3]]
- [[mistral]]
- [[moonshot-ai]]
