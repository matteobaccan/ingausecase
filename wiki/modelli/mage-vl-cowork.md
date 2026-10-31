---
title: "Mage-VL-Cowork"
category: modello
tags: [computer-use, agenti, microsoft, open-weight, edge]
related_puntate: []
created: 2026-10-31
updated: 2026-10-31
---

# Mage-VL-Cowork

## Introduzione

Modello visione-linguaggio da 4 miliardi di parametri con cui [[microsoft]] usa un computer, alternando clic sull'interfaccia e comandi nel terminale. Pubblicato il 30 ottobre 2026 su Hugging Face con licenza Apache-2.0, nasce dal team Mage e ha come parte linguistica Qwen3-4B-Instruct-2507 con un encoder visivo Mage-ViT.

## Capacità e performance

- Dichiara il 66,0% di compiti riusciti su OSWorld-Verified entro 50 passaggi, media di due passate (65,33% e 66,75%) misurate dal team Microsoft, contro un riferimento umano del 72,4%.
- Sceglie a ogni turno fra 11 azioni grafiche e una shell persistente con Python: se il lavoro è visivo clicca, se è strutturato scrive uno script.
- Con 4 miliardi di parametri supera Muse Glimmer da 30 miliardi (65,9%) e Qwen3.6-27B (63,9%), mentre GPT-5.5 resta davanti a 78,7%.

## Disponibilità

Pesi su Hugging Face in bfloat16 per 9,48 GB, 32.768 token di contesto, caricabili con `trust_remote_code=True` e Transformers dalla 4.57.3; per riprodurre i risultati Microsoft consiglia SGLang e un container Docker.

## Azienda di riferimento

- [[microsoft]]

## Timeline delle notizie

- **2026-10-31** — Microsoft ha pubblicato il modello il 30 ottobre 2026 su Hugging Face con licenza Apache-2.0: guida un computer da solo alternando clic e comandi nel terminale, con un canale grafico a 11 azioni e una shell persistente, e dichiara il 66,0% su OSWorld-Verified misurato dal proprio team su 361 compiti. L'addestramento parte da 293.806 compiti costruiti su 6.915 competenze elementari con il generatore Mage-CUA-Forge e passa dal rinforzo, che secondo Microsoft aggiunge 10,16 punti e riduce del 25,4% i token in uscita, con 32 GPU B200 impiegate.

## Collegamenti

- [[mage-vl-4b]]
- [[osworld-2-0]]
- [[agenti-ai]]
- [[index]]
