---
title: "Nemotron 3.5 Bolt 74B"
category: modello
tags: [nvidia, moe, open-weight, ai-locale, agenti]
related_puntate: []
created: 2026-10-15
updated: 2026-10-25
---

# Nemotron 3.5 Bolt 74B

## Introduzione

Modello linguistico MoE di [[nvidia]] con 74 miliardi di parametri totali e 9 miliardi attivi per token, quantizzato a 2 bit con addestramento consapevole della quantizzazione per occupare 24 GB di memoria: è pensato per gli agenti AI che girano in locale sui portatili con chip RTX Spark. Il nome ufficiale completo è Nemotron 3.5 Bolt 74B A9B.

## Capacità e performance

- NVIDIA lo presenta come più veloce della maggior parte dei modelli densi più usati e più capace della maggior parte dei modelli MoE con ingombro simile, ma l'annuncio non porta cifre.
- Su una piattaforma con 128 GB di memoria unificata, come RTX Spark, i 24 GB dei pesi lasciano spazio al contesto e agli altri programmi aperti; il comportamento sulle schede RTX con memoria dedicata non è precisato.

## Disponibilità

- Al lancio NVIDIA indica cinque runtime (llama.cpp, vLLM, Ollama, Unsloth e LM Studio) e due agenti, Hermes e OpenClaw; mancano benchmark, nome della licenza e pagina di download, con la promessa di pesi, ricette e dati di addestramento aperti.

## Azienda di riferimento

- [[nvidia]]

## Timeline delle notizie

- **2026-10-15** — NVIDIA annuncia Nemotron 3.5 Bolt 74B A9B, modello MoE da 74 miliardi di parametri totali e 9 attivi per token compresso a 2 bit in 24 GB, per gli agenti AI locali sui portatili RTX Spark: al lancio lo supportano llama.cpp, vLLM, Ollama, Unsloth e LM Studio e gli agenti Hermes e OpenClaw, mentre mancano benchmark, licenza e pagina di download.
- **2026-10-16** — La famiglia cresce con Bolt 74B-A9B e la variante [[nemotron-3-5-bolt-e4b]] per dispositivi, prevista per il 23 ottobre: pesi accessibili e opzioni commerciali per la personalizzazione.
- **2026-10-22** — Fa parte della catena di addestramento dei robot Microduck presentata al GTC di Berlino, insieme a Isaac Lab e a Hermes Agent; NVIDIA non dettaglia il ruolo dei tre componenti.
- **2026-10-25** — Il modello è indicato da [[nvidia]] fra i software di lancio dei PC con [[rtx-spark]], dove sta in 24 GB di memoria.










## Collegamenti

- [[ai-locale]]
- [[nemotron]]
- [[nvidia]]
- [[nemotron-3-5-bolt-e4b]]
- [[index]]
