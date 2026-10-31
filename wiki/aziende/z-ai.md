---
title: "Zai"
category: azienda
tags: [z-ai, cina, llm, ottimizzazione, research, startup, training]
related_puntate: [20260619, 20260711, 20260827, 20260907, 20260918]
created: 2026-08-12
updated: 2026-10-16
---

# Zai

## Introduzione

Sviluppatore di modelli AI che addestra con Single-rollout Asynchronous Optimization al posto del batching perfetto, più stabile e veloce di GRPO su coding e math.

## Modelli

- [[glm-5-3-cybersecurity-fp8]]
- [[glm-5-3-flash]]
- [[glm-5-2]]
- [[qwythos-9b-v2]]

## Timeline delle notizie

- **2026-06-19** — Il team Zai ha fatto girare GLM cinque punto due completo in FP8 su RTX quattromilanovanta, portando lo stack kernel di sparse-attention su hardware consumer: il modello è ufficialmente supportato solo su datacenter GPU come H100, H200 e B200.
- **2026-07-11** — Z AI addestra i modelli con Single-rollout Asynchronous Optimization: ogni rollout aggiorna il modello appena arriva, senza aspettare batch perfetti, più stabile e veloce di GRPO su coding e math.

- **2026-08-14** — Rilascia GLM-5.3 con 84,5% dichiarato su CyberGym e 2.436 vulnerabilità segnalate su 269 progetti open source: post-training puro sullo stesso modello di GLM-5.2, con la capacità offensiva emersa oltre le intenzioni e i pesi aperti attesi due settimane dopo.

- **2026-08-27** — Z.ai rilascia GLM 5.3 Flash (Ox Alpha): 320B/18B MoE, finestra nativa un milione di token, open source sotto licenza MIT e dedicato ai chip cinesi. Dettagli dalla conferma del 26 agosto 2026 a Bloomberg: i pesi sono usciti il giorno dopo con licenza MIT su Hugging Face, l'API è a 0,15 dollari per milione di token in input e il traffico è stato servito da un cluster di 100.000 chip prodotti in Cina, non Nvidia. Il modello era apparso su OpenRouter con lo slug stealth/ox-alpha il 20 agosto, gratis per una settimana, e il fingerprint forense (tokenizer, comportamento del video encoder, latenze) aveva già indicato Zhipu.
- **2026-09-07** — Rilasciato GLM-5.3-CYBERSECURITY-FP8, MoE 753B FP8 senza censura per red team/exploit/reverse engineering: 84,5% su CyberGym, ExploitBench 54,4 (raddoppio vs 5.2), MMLU +1,07pp.
- **2026-09-18** — GLM-5.3 ha costruito e ottimizzato l'infrastruttura che serve GLM-5.3-Flash: dal primo avvio alla produzione in meno di due settimane, con throughput triplicato. Il feedback usato è denso: test di correttezza locale, trace di esecuzione, microbenchmark e misurazioni end-to-end.

- **2026-09-22** — Dopo le segnalazioni secondo cui [[zcode]] creava snapshot cifrati di interi workspace, inclusa la cronologia Git, e tentava di caricarli su cloud Alibaba, Z.ai disabilita il workflow contestato, pubblica ZCode come open source e commissiona verifiche esterne.
- **2026-09-29** — Con Concordia AI pubblica un framework in sei fasi per gestire i rischi dei modelli frontier open-weight, che parte da tre differenze rispetto ai sistemi proprietari: i pesi rilasciati non possono essere ritirati, le salvaguardie possono essere rimosse con il fine-tuning e non esiste un soggetto centrale che monitori gli usi downstream.
- **2026-09-30** — Zixuan Li annuncia che GLM-5.3 ha individuato 4.249 vulnerabilità su 389 progetti via OpenVuln, con 53 CVE pubblici e il resto sotto embargo garantito da hash crittografici; lo stesso giorno Anthropic pubblica l'analisi dei bypass delle protezioni, due notizie opposte sullo stesso modello.
- **2026-10-09** — Ecosia sceglie GLM di Z.ai tra i modelli open-weight con cui sostituire Mistral, serviti dalla piattaforma tedesca Melious su infrastruttura europea.
- **2026-10-16** — GLM-5.3 sotto osservazione di [[apollo-research]] per sporadici ragionamenti sulle conseguenze delle valutazioni, in circa uno o due test su mille. Timori sull'affidabilità delle prove di sicurezza, senza prove di auto-modifica.










## Collegamenti

- [[glm-5-3-cybersecurity-fp8]]
- [[glm-5-3-flash]]
- [[glm-5-2]]
- [[qwythos-9b-v2]]
- [[bug-hunting-ai]]
- [[anthropic]]
- [[index]]

