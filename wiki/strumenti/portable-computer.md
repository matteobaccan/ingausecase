---
title: "Portable Computer"
category: strumento
tags: [perplexity, nvidia, agent, locale, gpu, privacy]
related_puntate: []
created: 2026-09-15
updated: 2026-09-15
---

# Portable Computer

## Introduzione

Versione completamente locale dell'agente [[perplexity-computer]], annunciata da [[perplexity]] il 25 agosto 2026 insieme a [[nvidia]]: non un modello nuovo ma un pacchetto che sposta sul dispositivo il modello, il motore di inferenza, il harness e i connettori, con la stessa interfaccia della versione cloud. Il lavoro svolto in locale non consuma crediti e i file sensibili non lasciano il computer.

## Funzionalità principali

- L'agente esegue comandi shell, legge PDF, analizza contenuti e si collega a Gmail, Google Drive, Slack e GitHub tramite server MCP; su Windows si aggiungono Outlook, OneDrive e Word.
- Codice e strumenti girano in una sandbox imposta dal sistema operativo, che limita processi, percorsi del filesystem e accesso alla rete: se la sandbox non è disponibile l'esecuzione degli strumenti viene disabilitata invece di proseguire in modo degradato, una scelta fail-secure.
- Il ponte verso il cloud è un escalation gate: l'agente non decide da solo di uscire dal dispositivo, si ferma e chiede il permesso quando serve ricerca web dal vivo o il ragionamento di un modello di frontiera, applicando prima una classificazione dei dati personali.
- Per far stare l'agente su una macchina sola il harness è stato riscritto: prompt di sistema più corto, skill caricate solo quando servono, interfacce a riga di comando compatte al posto di alcune definizioni MCP verbose e compressione dei dati più vecchi man mano che il compito cresce.

## Requisiti e modelli locali

- Al lancio serviva un [[dgx-spark]] con superchip GB10 Grace Blackwell e 128 GB di memoria unificata, collegabile fino a otto unità, oppure un PC Ubuntu ARM o x86 con GPU NVIDIA RTX da almeno 24 GB di VRAM; il DGX Spark è partito a 3.999 dollari e si trova intorno ai 4.699.
- Su Windows, dal 14 settembre 2026, basta una GPU NVIDIA GeForce RTX o RTX PRO con almeno 24 GB di VRAM e l'app dal Microsoft Store; il supporto alla [[dgx-station]] è annunciato a breve.
- Modelli offerti: [[qwen3-8-27b]] quantizzato a 3 bit (circa 17,4 GB di download, 32 GB di RAM richiesti), PPLX 27B, la variante post-addestrata da Perplexity per il proprio harness, e in arrivo [[nemotron]] 3.5 Lightning, MoE da 30 miliardi di parametri a 4 bit con 36 GB di RAM, più Nemotron 3.5 ASR per la dettatura vocale locale.
- Su Terminal Bench 2.1 il modello locale segna il 59,6 percento a costo praticamente nullo, sale al 73 percento con l'escalation al cloud per circa 0,415 dollari, mentre Claude Opus 5 arriva all'82,4 percento a circa 0,65 dollari; su Local Knowledge Work Bench il solo locale segna 82,6 percento e BrowseComp 66,7 percento.

## Disponibilità

- Riservato agli abbonati ai piani Pro e Max, incluse le versioni Enterprise equivalenti; al lancio solo Linux (DGX OS o Ubuntu), Windows dal 14 settembre 2026 su app del Microsoft Store, mentre macOS non è nella tabella di marcia perché il prodotto è legato all'hardware NVIDIA.

## Azienda / Autore

- [[perplexity]]

## Modelli supportati / correlati

- [[nemotron]]
- [[qwen3-8-27b]]

## Timeline delle notizie

- **2026-08-25** — Perplexity e NVIDIA lanciano Portable Computer su DGX Spark e PC Linux: zero costi di token per il lavoro locale, sandbox di sistema ed escalation al cloud solo su autorizzazione. Lo zero riguarda i token, non la spesa complessiva, perché l'hardware parte da qualche migliaio di dollari.
- **2026-09-14** — Portable Computer arriva nell'app per Windows, scaricabile dal Microsoft Store e utilizzabile su GPU GeForce RTX o RTX PRO da almeno 24 GB di VRAM, con Qwen 3.8 27B post-addestrato da Perplexity già pronto all'uso. Il vincolo dei ventiquattro GB è preciso: sotto quella soglia il modello e la finestra di contesto finirebbero a scambiare col disco.

## Collegamenti

- [[dgx-spark]]
- [[nemotron]]
- [[nvidia]]
- [[perplexity]]
- [[perplexity-computer]]
- [[qwen3-8-27b]]
- [[index]]
