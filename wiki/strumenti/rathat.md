---
title: "RatHat"
category: strumento
tags: [malware, android, zimperium, ai, accessibility]
related_puntate: []
created: 2026-09-22
updated: 2026-09-22
---

# RatHat

## Introduzione

Malware Android scoperto da Zimperium che usa IA generativa per leggere schermate via accessibilità e automatizzare tocchi.

## Funzionalità principali

- Converte albero accessibilità in XML e riceve coordinate e comandi SCROLL_DOWN da assistente IA.
- Persistenza con liblocal-service.so in Go e tunnel FRP libmedia_codec.so, reinstalla dopo disinstallazione.
- Rubina PIN, OTP, tocchi da /dev/input e overlay su banche/crypto.

## Timeline delle notizie

- **2026-09-21** — Zimperium pubblica 162 hash APK e domini RatHat, vettore smishing e portali fuori Play.

## Collegamenti

- [[sicurezza-ai]]
- Zimperium
- [[index]]
