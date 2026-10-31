---
title: "GLM 5.3 Flash (Ox Alpha)"
category: modello
tags: [cina, llm, moe, open-source, open-weight]
related_puntate: [20260827, 20260828, 20260830, 20260901, 20260905, 20260918, 20261001, 20261004, 20261013]
created: 2026-08-28
updated: 2026-10-13
sources: [raw/puntate/ainews20260905.md, raw/puntate/ainews20260827.md, raw/puntate/ainews20260828.md, raw/puntate/ainews20260830.md, raw/puntate/ainews20260901.md, raw/puntate/ainews20260918.md, raw/pillitteri/pillitteri20260828-ox-alpha-glm-5-3-flash-zhipu-reveal.md, raw/puntate/ainews20261001.md, raw/puntate/ainews20261004.md, raw/puntate/ainews20261013.md]
---

# GLM 5.3 Flash (Ox Alpha)

## Introduzione

Modello LLM MoE open source di Z.ai, rilasciato come "Ox Alpha", costruito per girare su chip cinesi.

## Capacità e performance

- Trecentoventi miliardi di parametri totali, diciotto miliardi attivi per token, finestra nativa da un milione di token.
- La versione non censurata di GLM 5.3 Flash (rilasciata da OrcaRouter): trecentoventi miliardi di parametri, diciotto miliardi attivi, rimozione dei rifiuti (refusal) integrata nei pesi senza LoRA o jailbreak. I test mostrano tassi di rifiuto crollati dal novantasei all'undici percento su MaliciousInstruct.

## Disponibilità

- Open source sotto licenza MIT; gira su chip cinesi.

## Azienda di riferimento

- [[z-ai]]

## Timeline delle notizie

- **2026-08-27** — Z.ai rilascia GLM 5.3 Flash (Ox Alpha): trecentoventi miliardi di parametri, diciotto miliardi attivi, finestra nativa da un milione di token, open source sotto licenza MIT e dedicato ai chip cinesi. [Fonte: raw/puntate/ainews20260827.md] Dettagli dalla conferma del 26 agosto 2026 a Bloomberg: i pesi sono usciti il giorno dopo con licenza MIT su Hugging Face, l'API è a 0,15 dollari per milione di token in input e il traffico è stato servito da un cluster di 100.000 chip prodotti in Cina, non Nvidia. Il modello era apparso su OpenRouter con lo slug stealth/ox-alpha il 20 agosto, gratis per una settimana, e il fingerprint forense (tokenizer, comportamento del video encoder, latenze) aveva già indicato Zhipu. [Fonte: raw/pillitteri/pillitteri20260828-ox-alpha-glm-5-3-flash-zhipu-reveal.md]
- **2026-08-28** — GLM 5.3 Flash è ora gratuito: disponibile su diverse piattaforme e segnalato anche su Cline (basta installare e fare login, senza chiave API). Novanta percento di sconto su Merge Gateway fino a fin settembre. [Fonte: raw/puntate/ainews20260828.md]
- **2026-08-30** — OrcaRouter ha rilasciato la versione non censurata di GLM 5.3 Flash: rimozione dei rifiuti integrata nei pesi, senza LoRA o jailbreak. Tasso di rifiuto crollato dal novantasei all'undici percento su MaliciousInstruct. [Fonte: raw/puntate/ainews20260830.md]
- **2026-09-05** — Unsloth ha ottimizzata l’inferenza GGUF di GLM 5.3-Flash in locale: decodifica migliorata e predizione multi-token la rendono tre punto tre volte più veloce, con una versione a tre bit utilizzabile su configurazioni da centoventi gigabyte di RAM. [Fonte: raw/puntate/ainews20260905.md]
- **2026-09-01** — OrcaRouter ha rilasciato quantizzazione UF ufficiale per GLM 5.3 Flash Uncensored: 320 miliardi, 18 attivi, Q4 K M 109,9 gigabyte, 89,8% top-1. [Fonte: raw/puntate/ainews20260901.md]
- **2026-09-18** — L'infrastruttura che serve GLM-5.3-Flash è stata costruita e ottimizzata da GLM-5.3: dal primo avvio alla produzione in meno di due settimane, throughput triplicato, con feedback denso da test di correttezza locale, trace di esecuzione, microbenchmark e misurazioni end-to-end. [Fonte: raw/puntate/ainews20260918.md]
- **2026-10-01** — RunInfra riscrive i kernel dietro GLM 5.3 Flash: 670 token al secondo su Vercel AI Gateway, 0,11 dollari per milione di token in input e 0,45 in output, cache hit rate del 99,7% nelle ultime ventiquattro ore, e il modello ora gira anche su AMD. [Fonte: raw/puntate/ainews20261001.md]
- **2026-10-04** — GLM 5.3 Flash senza censura è offerto gratis: tredici milioni di token al minuto condivisi e un picco di trecentosessanta token al secondo, pensato per cybersecurity e coding. [Fonte: raw/puntate/ainews20261004.md]
- **2026-10-13** — Su questa base viene costruito GLM-Legal, modello per i flussi di lavoro del settore legale che raggiunge performance competitive sui benchmark legali mainstream. [Fonte: raw/puntate/ainews20261013.md]










## Collegamenti

- [[glm-5-2]]
- [[open-source]]
- [[z-ai]]
- [[runinfra]]
- [[index]]
