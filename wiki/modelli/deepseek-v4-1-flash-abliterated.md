---
title: "DeepSeek V4.1 Flash Abliterated"
category: modello
tags: [abliterated, cina, deepseek, locale, open-weight]
related_puntate: []
created: 2026-09-13
updated: 2026-09-13
sources: [raw/pillitteri/pillitteri20260913-deepseek-41-flash-senza-censura-abliterated.md]
---

# DeepSeek V4.1 Flash Abliterated

## Introduzione

Le build abliterated e uncensored di [[deepseek-v4-1-flash]] comparse su Hugging Face a poche ore dal rilascio ufficiale del 10 settembre 2026, con licenza MIT: versioni caricate da terzi che tolgono al modello i rifiuti di sicurezza. Nessuna porta la firma di DeepSeek, che distribuisce solo il modello base con le sue protezioni; la più scaricata è dealignai/DeepSeek-V4.1-Flash-UNCENSORED-FP8, con 2.254 download e 87 like, ed è la punta di una decina di repository quasi identici. [Fonte: raw/pillitteri/pillitteri20260913-deepseek-41-flash-senza-censura-abliterated.md]

## Capacità e performance

- La base è un modello da 748 miliardi di parametri con vista nativa, e le build abliterated ereditano tutto quello che sa fare, vista e finestra da un milione di token comprese, togliendo soltanto lo strato che filtra. Il metodo più diffuso è l'abliterazione a livello di pesi, che scrive la modifica dentro il file; il control vector di Matt Suiche, un file da 800 KB applicato durante l'inferenza, lascia invece il modello ufficiale intatto ed è reversibile. [Fonte: raw/pillitteri/pillitteri20260913-deepseek-41-flash-senza-censura-abliterated.md]
- Il dato che colpisce sulla distributedcognition firmata dal ricercatore grimjim è la perdita di capacità sul benchmark MMLU: zero. Togliere il filtro non ha reso il modello più stupido. Il control vector di Suiche, ad alpha 0,5, alza le risposte accettate da 4 su 32 a 24 su 32 nei test di rifiuto e arriva a 31 su 32 sugli scenari di sicurezza informatica, con un comportamento però non lineare: spingere alpha più in alto oltre un certo punto riduce l'effetto invece di aumentarlo. [Fonte: raw/pillitteri/pillitteri20260913-deepseek-41-flash-senza-censura-abliterated.md]
- Le schede degli stessi autori avvertono che il modello risponderà a richieste dannose, non etiche, offensive o illegali e consigliano di mettere uno strato di moderazione esterno, come Llama Guard, prima di qualsiasi uso reale. La build MLX per Apple Silicon occupa 458,7 GB a 4 bit e la s-zaizen arriva a 510 GB su 48 file: servono workstation con 256 o 512 GB di memoria unificata o server multi-GPU, non un portatile. [Fonte: raw/pillitteri/pillitteri20260913-deepseek-41-flash-senza-censura-abliterated.md]

## Azienda di riferimento

- [[deepseek]]

## Strumenti correlati

- [[ds4]]
- [[heretic]]

## Timeline delle notizie

- **2026-09-13** — La scena uncensored si accende poche ore dopo il rilascio open weight: accanto alla dealignai (pesi riscritti in FP8, abliterazione "chirurgica" a livello di pesi, cloni identici come Openintelligent123, schwyzquant, Solstice-AI e codingforfun) ci sono la distributedcognition di grimjim dichiarata anche per sintesi chimiche e biologiche, cybercrime, armi, molestie e frode e proposta per il red-teaming, la s-zaizen su 48 shard per 510 GB, la orcarouter Uncensored-MLX per Mac Apple Silicon, la drowzeys Cybersecurity-Unleashed come overlay da 1,1 GB e il GGUF di audreyt convertito per [[ds4]] via [[heretic]]. Per una parte di queste il guadagno vero non è la tecnica ma l'accesso: un modello da 748 miliardi di parametri senza freni resta fuori dalla portata di chi non ha un datacenter, e la disponibilità pubblica di versioni sbloccate esiste da mesi con Qwen e Llama; quello che cambia è la normalizzazione, perché ogni rilascio sbloccato in poche ore rende l'operazione sempre più banale e sempre meno discussa. [Fonte: raw/pillitteri/pillitteri20260913-deepseek-41-flash-senza-censura-abliterated.md]

## Collegamenti

- [[deepseek]]
- [[deepseek-v4-1-flash]]
- [[ds4]]
- [[heretic]]
- [[ai-locale]]
- [[index]]
