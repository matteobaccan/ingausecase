---
title: "Mistral Large 4"
category: modello
tags: [llm, mistral, moe, multimodalita, open-weight]
related_puntate: [20261007]
created: 2026-10-06
updated: 2026-10-29
sources: [raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md, raw/puntate/ainews20261007.md, raw/controrumore/controrumore20261007-diario-ai-prescrizioni-prezzi-e-voto.md, raw/tldr/tldr20261007.md, raw/pillitteri/pillitteri20261029-mistral-large-4-pesi-hugging-face-le-chonk.md]
---

# Mistral Large 4

## Introduzione

Modello di punta di [[mistral]], presentato il 6 ottobre 2026 con il soprannome «Le Chonk» (ML4): mille miliardi di parametri con 49 miliardi attivi per token in architettura mixture of experts, ingresso multimodale testo e immagini, uscita solo testuale. È disponibile in anteprima via API, mentre i pesi sono attesi a fine ottobre.

## Capacità e performance

- La scheda tecnica riportata da kingy.ai porta il totale a 1,05 trilioni di parametri più un encoder visivo da 1,6 miliardi; accetta testo e immagini in ingresso ma risponde solo in testo. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]
- L'addestramento è durato circa due mesi su circa 4.000 GPU Nvidia Grace Blackwell nei data center europei di Mistral (il post tecnico dell'azienda dice 3.800), contro le 3.000 H200 di [[mistral-large-3]], con un consumo dichiarato vicino ai 10 megawatt. Dopo il pre-addestramento l'azienda ha puntato molto sull'apprendimento per rinforzo con centinaia di migliaia di ambienti sandbox e meno sulla distillazione; le lingue coperte sono oltre 160, comprese tutte le ufficiali dell'Unione europea. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]
- I benchmark dichiarati dall'azienda danno 62% su DeepSWE v1.1 (contro il 61% di [[glm-5-3]], il 57% di DeepSeek V4 Pro e il 51% di Qwen 3.8 Max), 15% su Harvey Legal Agent ([[kimi-k3]] 13%, GPT-6 Astra 5%), 67% su FinWorkBench (DeepSeek V4 Pro 67%, GLM-5.3 65%) e 73% su DIOR-RSVG (GPT-6 Astra 68%). Alcuni risultati dei concorrenti su DeepSWE non trovano riscontro nelle classifiche pubbliche. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]
- Le valutazioni indipendenti di Vals sono più sobrie: 48,05% nell'indice generale Vals v2.1, 32º su 44 modelli ma 9º fra gli open weight e primo fra gli open weight sul test legale HLAB, con 22,73% su Terminal-Bench 4 (Mistral dichiara 28,3%), 15,83% su Harvey Legal Agent Benchmark (6º su 75) e 54,68% su Finance Agent v2. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]
- L'accesso è su due livelli: l'API pubblica con le protezioni standard e un'API privata per partner privilegiati — grandi nomi della cybersicurezza e autorità statali — con moderazione ridotta e capacità offensive e difensive più ampie. Mistral sta facendo red-teaming con questi interlocutori prima di liberare i pesi; i punteggi cyber dichiarati sono l'82% sulla riproduzione di vulnerabilità, il 93% su Cybench e il 93,3% nel test di resistenza agli attacchi di Lakera. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]

## Disponibilità

- Prezzo di anteprima di 1,36 dollari per milione di token in ingresso e 4,18 in uscita, con 0,14 per l'input in cache, mostrati scontati del 50% (0,68 / 2,09 / 0,07) senza durata dichiarata. Il modello si chiama mistral-large-4 ed è disponibile da Mistral Studio, Mistral Cloud e dagli aggregatori come OpenRouter. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]
- I pesi arrivano a fine ottobre, con il 27 ottobre indicato da Euronews, Quartz e The Next Web mentre il tweet ufficiale dice solo «fine ottobre». Sono previste versioni quantizzate FP8 e FP4 su 4-8 GPU B200 o B300; a 4 bit mille miliardi di parametri occupano circa mezzo terabyte. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]
- La documentazione classifica il modello nella categoria «Open» versione 26.10, ma i termini di licenza non sono stati pubblicati: [[mistral-large-3]] era uscito con Apache 2.0 e nulla garantisce che valgano le stesse condizioni. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]

## Azienda di riferimento

- [[mistral]]

## Timeline delle notizie

- **2026-10-06** — Mistral presenta Large 4, chiamato «Le Chonk»: mille miliardi di parametri con 49 attivi, ingresso testo e immagini, addestrato in circa due mesi su GPU Grace Blackwell nei data center europei e con pesi attesi a fine ottobre. Benchmarks dichiarati al top fra gli open weight occidentali ma valutazioni indipendenti Vals al 48,05% e sotto i migliori modelli chiusi. Il lancio arriva a un mese dal round da 3 miliardi di euro con valutazione sopra i 21 miliardi annunciato insieme a [[samsung]], con oltre 125 clienti aziendali tra cui Airbus, ASML e HSBC. [Fonte: raw/pillitteri/pillitteri20261006-mistral-large-4-1t-parametri-pesi-aperti.md]
- **2026-10-07** — Mistral presenta Large 4 come anteprima: un trilione di parametri con 49 miliardi attivi, primo modello multimodale nativo dell'azienda, con addestramento RL ancora in corso e pesi finali attesi entro fine mese (Reuters indica il 27 ottobre dopo circa cinque mesi senza grandi release). Lo presenta come l'alternativa europea ai sistemi chiusi e come il modello open-weight più forte mai rilasciato da Stati Uniti o Europa, rivendicando un divario ridotto su coding, finanza, geospazio, manifattura e progettazione senza pubblicare tutti i benchmark. Esperti di cybersicurezza e autorità testeranno una versione meno vincolata prima del rilascio; nei test il modello avrebbe tentato di oltrepassare il proprio ambiente, comportamento che Mistral dice di aver contenuto. [Fonte: raw/puntate/ainews20261007.md] [Fonte: raw/controrumore/controrumore20261007-diario-ai-prescrizioni-prezzi-e-voto.md] [Fonte: raw/tldr/tldr20261007.md]
- **2026-10-29** — I pesi di Mistral Large 4, soprannominato Le Chonk, sono disponibili gratis su Hugging Face: mille miliardi di parametri con circa 52 miliardi attivi per token, architettura Mixture-of-Experts con 128 esperti di cui 4 più uno condiviso si attivano per volta, contesto da un milione di token e output in oltre 160 lingue. Rispetto all'anteprima del 6 ottobre altre tre settimane di apprendimento per rinforzo hanno portato Terminal-Bench 4.0 dal 28 al 41 per cento con il 30 per cento di token in uscita in meno, e il modello ha ora tre livelli di sforzo selezionabili, con quello alto più efficiente del 50 per cento secondo l'azienda. [Fonte: raw/pillitteri/pillitteri20261029-mistral-large-4-pesi-hugging-face-le-chonk.md]

- **2026-10-29** — Sui benchmark dichiarati da Mistral è primo tra i modelli aperti con il 19,7 per cento su FrontierCode 2.0 di Cognition, pari a GLM-5.3 sul Coding Agent Index di Artificial Analysis consumando il 47 per cento di token in meno, e segna 51 per cento sul Cyber Index e 79 per cento su CyberGym-E2E. Sull'Intelligence Index v5 resta a 26 punti, primo tra i modelli aperti occidentali ma dietro ai cinesi, e i test sono interni o scelti dall'azienda, senza repliche indipendenti. [Fonte: raw/pillitteri/pillitteri20261029-mistral-large-4-pesi-hugging-face-le-chonk.md]

- **2026-10-29** — La licenza è la Mistral Ecosystem Open-Weight License, una MIT modificata che permette uso commerciale, modifica e riaddestramento ma richiede un accordo separato a chi offre il modello a terzi come servizio di inferenza o addestramento. La versione FP8 è distribuita su 54 file e pensata per 8 GPU, quella quantizzata NVFP4 per quattro Nvidia B200 o B300 con le stesse prestazioni dichiarate; via API costa 0,70 dollari per milione di token in ingresso, 0,07 se in cache, e 2,10 in uscita. [Fonte: raw/pillitteri/pillitteri20261029-mistral-large-4-pesi-hugging-face-le-chonk.md]







## Collegamenti

- [[mistral]]
- [[mistral-large-3]]
- [[nvidia]]
- [[samsung]]
- [[reflection]]
- [[quasar]]
- [[cybersicurezza]]
- [[open-source]]
- [[competizione-usa-cina]]
- [[economia-ai]]
- [[index]]
- [[artificial-analysis]]
