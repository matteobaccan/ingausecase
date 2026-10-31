---
title: "Colibri"
category: strumento
tags: [efficienza, inferenza, open-source]
related_puntate: [20260711, 20260712, 20260713, 20261017]
created: 2026-08-12
updated: 2026-10-17
sources: [raw/puntate/ainews20260711.md, raw/puntate/ainews20260712.md, raw/puntate/ainews20260713.md, raw/pillitteri/pillitteri20260712-colibri-glm-5-2-744b-25gb-ram.md, raw/pillitteri/pillitteri20260913-streaming-disco-modelli-moe-portatile.md, raw/puntate/ainews20261017.md]
---

# Colibri

## Introduzione

Motore di inferenza in puro C che esegue modelli MoE enormi su laptop senza GPU, caricando in memoria solo gli expert necessari per ogni token.

## Funzionalità principali

- Colibri è un motore di inferenza in puro C che fa girare GLM-5.2 (settecentoquarantaquattro miliardi di parametri MoE) in venticinque GB di RAM: parti dense in memoria, expert su disco in streaming, zero dipendenze e zero Python.
- Colibri è un motore inference in puro C che esegue GLM-5.2 da settecentoquarantaquattro miliardi di parametri su soli venticinque gigabyte di RAM: nessuna GPU necessaria, velocità attuale tra 0,05 e un token al secondo.
- Colibri fa girare GLM-5.2, modello da settecentoquarantaquattro miliardi di parametri, su un laptop con venticinque GB di RAM senza GPU: l'intero modello resta su disco e si caricano in memoria solo gli expert necessari per ogni token, risposta lenta ma reale di circa un token ogni dieci-venti secondi, licenza Apache 2.0.
- Il trucco sta nel Mixture-of-Experts: GLM-5.2 attiva circa 40 miliardi di parametri per token e solo 11 GB cambiano da un token all'altro, quindi la parte densa (attenzione, esperti condivisi ed embedding, circa 17 miliardi di parametri) resta in RAM a int4 per 9,9 GB, mentre i 21.504 esperti instradati (75 livelli MoE da 256 esperti, 19 MB l'uno, per circa 370 GB in int4) e la testa di predizione multi-token vivono su disco NVMe e vengono letti quando il router li chiama.
- La gestione della memoria è la parte ingegneristica vera: cache LRU per ogni livello, un magazzino opzionale di esperti "caldi" tenuti fissi, la page cache del sistema operativo come secondo livello gratuito e un file .coli_usage che registra quali esperti vengono usati e li fissa automaticamente in memoria, diventando più rapido con l'uso continuato. Le conversazioni si riaprono "calde" anche dopo il riavvio grazie alla cache KV persistente su file .coli_kv (circa 182 KB per token), con attenzione MLA che comprime la cache a 576 valori per token contro i 32.768 di un'attenzione classica.
- Non è pensato per la velocità: il README dichiara "This is not fast" e il throughput va da 0,05-0,1 token al secondo su WSL2 a disco lento a 0,28 su Ryzen 9 9950X con NVMe PCIe 5.0, 0,40 su Framework 13 con esperti fissati a 47,6 GB e 1,06 su Apple M5 Max con 128 GB e 14,2 GB/s. Il collo di bottiglia non è la CPU ma la banda del disco: una decodifica a freddo legge circa 11 GB per token.
- Si distingue da [[llama-cpp]], [[ollama]] e [[vllm]] perché rinuncia a tenere il modello intero in RAM o VRAM e accetta di streammarlo dal disco: implementa fedelmente le feature di GLM-5.2 (testa MTP per la decodifica speculativa, attenzione DSA con selezione top-2048, MLA), è un unico file C da circa 2.400 righe senza dipendenze a runtime compilabile con GCC su Linux, macOS e Windows 11 nativo via MinGW-w64, e offre un server con API compatibile OpenAI.

## Modelli supportati / correlati

- [[glm-5-2]]
- [[kimi-k3]]
- [[deepseek-v4-flash]]
- [[twotower]]

## Timeline delle notizie

- **2026-07-11** — Colibri è un motore di inferenza in puro C che fa girare GLM-5.2 (settecentoquarantaquattro miliardi di parametri MoE) in venticinque GB di RAM: parti dense in memoria, expert su disco in streaming, zero dipendenze e zero Python. [Fonte: raw/puntate/ainews20260711.md]
- **2026-07-12** — Colibri è un motore inference in puro C che esegue GLM-5.2 da settecentoquarantaquattro miliardi di parametri su soli venticinque gigabyte di RAM: nessuna GPU necessaria, velocità attuale tra 0,05 e un token al secondo. [Fonte: raw/puntate/ainews20260712.md] Il progetto dell'utente JustVugg, licenza Apache 2.0, ha raccolto 4.611 stelle e 403 fork in undici giorni e 453 punti su Hacker News, dove il commento più votato è "This is the hacker spirit"; l'autore dichiara l'ispirazione a [[antirez]]. [Fonte: raw/pillitteri/pillitteri20260712-colibri-glm-5-2-744b-25gb-ram.md]
- **2026-07-13** — Colibri fa girare GLM-5.2, modello da settecentoquarantaquattro miliardi di parametri, su un laptop con venticinque GB di RAM senza GPU: l'intero modello resta su disco e si caricano in memoria solo gli expert necessari per ogni token, risposta lenta ma reale di circa un token ogni dieci-venti secondi, licenza Apache 2.0. [Fonte: raw/puntate/ainews20260713.md]
- **2026-09-13** — Colibri gira otto famiglie di modelli (GLM-5.3, Kimi K3 da 2,8 trilioni di parametri, DeepSeek 4 Flash, Qwen e altri), ha aggiunto la visione e un launcher per Windows ed è salito oltre 28.000 stelle su GitHub, davanti a [[ds4]] di [[antirez]]; sul confronto, ds4 è più maturo e ampio, Colibri più nuovo e stretto sul singolo modello. [Fonte: raw/pillitteri/pillitteri20260712-colibri-glm-5-2-744b-25gb-ram.md] Nella classifica delle stelle il sorpasso è netto: 28.756 contro 22.318 di [[ds4]] e 19.505 di [[ktransformers]], e la lista dei modelli supportati si è allungata a otto famiglie — GLM-5.2 e 5.3 (744B), GLM-5.3-Flash (321B, con visione), [[inkling]] (975B), [[kimi-k3]] (2,8 trilioni), [[deepseek-v4-flash]] (284B, con la variante compressa REAP a 150B che scende a circa 85 GB), Qwen3.8-Flash-Next, Qwen3.6 e OLMoE — con MiniMax già tra i candidati; ogni modello resta un motore gemello, un singolo file C dietro la stessa interfaccia. [Fonte: raw/pillitteri/pillitteri20260913-streaming-disco-modelli-moe-portatile.md]
- **2026-10-17** — Colibri, progetto GitHub con quasi 42.000 stelle, esegue modelli IA potenti su laptop con appena otto gigabyte di RAM usando gestione intelligente della memoria, e supporta Claude Code trasformando il laptop in un server IA privato. [Fonte: raw/puntate/ainews20261017.md]




## Collegamenti

- [[antirez]]
- [[deepseek-v4-flash]]
- [[ds4]]
- [[glm-5-2]]
- [[inkling]]
- [[kimi-k3]]
- [[ktransformers]]
- [[llama-cpp]]
- [[neutronstar]]
- [[ollama]]
- [[twotower]]
- [[vllm]]
- [[index]]

