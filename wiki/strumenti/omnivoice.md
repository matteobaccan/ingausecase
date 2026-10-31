---
title: "OmniVoice"
category: strumento
tags: [open-source, sintesi-vocale, tts, voice-cloning]
related_puntate: [20260907, 20260912]
created: 2026-09-07
updated: 2026-09-12
---

# OmniVoice

## Introduzione

Sistema Python open source con circa 10.000 stelle che permette sintesi vocale zero-shot in oltre 600 lingue. Clona voci da campioni audio, con controllo su età, altezza vocale, dialetto e sussurro, e genera fino a 40 volte più veloce del tempo reale.

## Funzionalità principali

- Sintesi vocale zero-shot in oltre 600 lingue con clonazione da campioni audio.
- Controllo su età, altezza vocale, dialetto e sussurro.
- Generazione fino a 40 volte più veloce del tempo reale.

- **Requisiti e licenza**: pubblicato il 31 marzo 2026 dal gruppo Next-gen Kaldi (progetto k2-fsa), addestrato secondo il paper su circa 581.000 ore di audio in 646 lingue. Il codice è Apache 2.0, i pesi sono CC-BY-NC per via dei dati di addestramento, quindi l'uso commerciale è escluso.
- **Voice prompt riutilizzabile**: si congela l'identità vocale in un file `.pt` da poche decine di kilobyte e le sessioni successive lo ricaricano in una frazione di secondo, senza ripassare dall'audio di riferimento né dalla trascrizione.

## Timeline delle notizie

- **2026-09-07** — OmniVoice, sistema Python da circa 10.000 stelle, permette sintesi vocale zero-shot in oltre 600 lingue con clonazione vocale ad alta qualità e generazione fino a 40x realtime.

- **2026-09-12** — OmniVoice clona voci a partire da una registrazione breve, supporta oltre seicento lingue, regola età, tono e dialetto e genera quaranta volte più veloce del tempo reale; quasi diecimila stelle su GitHub.

- **2026-09-11** — La guida all'installazione su Mac Apple Silicon mette in fila i passi concreti: Python 3.10-3.13 (i wheel di torch non esistono per la 3.14), ambiente virtuale, pesi scaricati a mano con `curl` quando il downloader Xet non regge una rete debole, generazione in modalità offline con `HF_HUB_OFFLINE=1` e trascrizione esatta del campione per migliorare il clone. Dal lavoro nasce anche un sistema multi-voce con due script, `say.sh` e `enroll.sh`, e il trucco del microfono virtuale BlackHole per mandare una voce clonata come nota vocale su WhatsApp, sempre con l'avvertenza del consenso.

## Collegamenti

- [[omnivoice-studio]]
- [[voce-ai]]
- [[index]]
