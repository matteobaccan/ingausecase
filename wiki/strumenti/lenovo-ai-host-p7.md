---
title: "Lenovo AI Host P7"
category: strumento
tags: [ai-locale, cina, hardware, inferenza, lenovo]
related_puntate: []
created: 2026-10-27
updated: 2026-10-27
sources: [raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]
---

# Lenovo AI Host P7

## Introduzione

Mini computer di [[lenovo]] grande quanto un palmo e da circa 300 grammi, mostrato in anteprima il 24 ottobre 2026 alla conferenza CSDN 1024 Programmers' Day: secondo il produttore esegue in locale modelli fino a 125 miliardi di parametri con contesto da 256K, senza passare dal cloud. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]

## Specifiche dichiarate

- Due chip cinesi: l'M50 di Houmo per l'inferenza, con 160 TOPS a 10 watt, e il SoC P1 di CIX, a 6 nanometri con CPU a 12 core Armv9.2 e NPU da 30 TOPS. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]
- A maggio la scheda parlava di 190 TOPS di sistema, 30 watt al massimo, 80 GB di memoria, modelli fino a 122 miliardi di parametri, contesto da 128K e 50 token al secondo; a ottobre le cifre sono salite a 125 miliardi e 256K. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]
- Quantizzazione mista INT4/INT8, dichiarata al 98,3 per cento del punteggio BF16 sulla media di quattro benchmark. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]
- Fra i modelli citati ci sono [[qwen3-8-flash-next|Qwen3.8-Flash-Next]], [[qwen3-8-27b|Qwen3.8-27B]] e [[qwen-3-6-35b-a3b|Qwen3.6-35B-A3B]], accanto a modelli per immagini, documenti e voce. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]

## Limiti noti

- Le cifre cambiano da un evento all'altro e nessuna descrive una configurazione acquistabile: prezzo e data di vendita non sono stati comunicati. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]
- I 50 token al secondo sono dichiarati senza modello, lunghezza del prompt e quantizzazione, e un calcolo indipendente sulla banda di memoria di un modello denso da 122 miliardi a 4 bit non regge con una LPDDR5. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]

## Software

- Token Manager per impostare un indirizzo API e collegare i modelli locali a strumenti di programmazione e applicazioni con agenti, più una dashboard su risorse e stato dei modelli. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]
- L'assistente Tianxi AI in modalità Auto sceglie fra modello locale e cloud in base alla difficoltà del compito. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]

## Timeline delle notizie

- **2026-10-24** — Lenovo mostra in anteprima l'AI Host P7 e apre il programma di accesso anticipato: modelli fino a 125 miliardi di parametri in locale con contesto da 256K, chip Houmo M50 e CIX P1, software Token Manager per collegare i modelli a strumenti di programmazione, senza prezzo né data di vendita. [Fonte: raw/pillitteri/pillitteri20261027-lenovo-ai-host-p7-125b-locale.md]

## Collegamenti

- [[lenovo]]
- [[ai-locale]]
- [[qwen3-8-flash-next]]
- [[index]]
