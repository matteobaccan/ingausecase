---
title: "Contabo"
category: azienda
tags: [hosting, gpu, vps, inferenza, europa]
related_puntate: []
created: 2026-09-21
updated: 2026-09-21
---

# Contabo

## Introduzione

Provider di hosting tedesco che il 21 settembre 2026 ha messo in vendita la propria GPU VPS, un server virtuale con una scheda NVIDIA RTX PRO 6000 da 96 GB riservata a un solo cliente a 999 euro al mese IVA esclusa. Il 15 giugno il blog dell'azienda indicava Hetzner a chi cercava una GPU a canone fisso rimandando i propri piani a un annuncio futuro: tre mesi e sei giorni dopo Contabo ha mantenuto la promessa e ha messo il canone quasi 200 euro sotto il GEX131 del rivale di Gunzenhausen, che parte da 1.197,30 euro al mese più 599 euro di setup.

## Timeline delle notizie

- **2026-09-21** — La configurazione di lancio è una sola: scheda della generazione Blackwell con 24.064 core CUDA, 120 TFLOPS in FP32 e circa 1,8 TB/s di banda di memoria, 18 vCPU, 96 GB di RAM e 900 GB di storage NVMe, con sconti del 15 per cento a 12 mesi e del 20 a 24 mesi. Il post firmato da Christopher Carter precisa che la GPU è dedicata, quindi non condivisa né sovrallocata.
- **2026-09-21** — Il sistema di partenza è Ubuntu 24.04 con i driver CUDA già installati e la messa in servizio richiede pochi minuti; le sedi al debutto sono l'Europa e gli Stati Uniti centrali, con ampliamenti previsti in base alla domanda, e il listino è espresso in tre valute, 999 euro, 1.199 dollari e 969 sterline.
- **2026-09-21** — I paletti sono dichiarati apertamente: al lancio manca Windows, non si può migrare la macchina da una regione all'altra, le scorte sono limitate e l'azienda esclude i cluster di addestramento multi-nodo che richiedono NVLink, proponendo la macchina per quattro usi, cioè inferenza e serving di modelli linguistici, rendering 3D, calcolo scientifico su un singolo nodo e fine-tuning con LoRA su una sola GPU.

## Collegamenti

- [[ai-locale]]
- [[vllm]]
- [[index]]
