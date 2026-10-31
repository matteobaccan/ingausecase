---
title: "WhatsApp MCP Server"
category: strumento
tags: [mcp, whatsapp, open-source, claude, privacy]
related_puntate: []
created: 2026-10-03
updated: 2026-10-01
sources: [raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]
---

# WhatsApp MCP Server

## Introduzione

Progetto open source pubblicato su GitHub dallo sviluppatore Luke Harries con licenza MIT che collega un assistente AI come [[claude]] al proprio account WhatsApp personale, permettendo di cercare conversazioni, leggere messaggi e inviarne di nuovi senza passare dall'app. Al 1° ottobre 2026 il repository ha superato le 6.346 stelle e conta oltre 1.346 fork, a più di un anno dalla pubblicazione iniziale nel marzo 2025. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]

## Funzionalità principali

- Implementa un server [[mcp]] dedicato a WhatsApp: una volta configurato, l'assistente può cercare contatti, scorrere la cronologia dei messaggi, inviare testo a singoli o a gruppi e gestire immagini, video, documenti e audio. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]
- Dietro le quinte lavorano due componenti separati: un bridge scritto in Go basato sulla libreria whatsmeow si collega a WhatsApp tramite la stessa API multi-dispositivo di WhatsApp Web dopo la scansione del QR code, e i messaggi vengono salvati in un database SQLite locale sul computer dell'utente, non su un server di terzi. Solo quando l'assistente chiama uno degli strumenti esposti dal server quella porzione di dati passa al modello. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]

## Installazione e uso

- Servono tre passaggi: clonare il repository, avviare il bridge in Go scansionando il QR code con l'app WhatsApp del telefono (l'autenticazione va ripetuta circa ogni venti giorni) e collegare il client MCP indicando il percorso locale nel file di configurazione. Serve avere Go installato e sapere dove il proprio client si aspetta il file JSON, quindi non è un'installazione alla portata di chi non ha mai aperto un terminale. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]

## Casi d'uso

- Il progetto esiste da marzo 2025 ma a inizio ottobre 2026 è tornato a circolare grazie a un giro di post e reel che lo presentano come novità: il codice, l'architettura locale e la licenza MIT sono reali e verificabili, ma la cornice da scoperta dell'ultima ora è fuorviante, perché lo strumento gira da oltre diciotto mesi e non è un prodotto ufficiale di [[anthropic]] né di [[meta]]. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]
- I rischi sono due: il bridge, una volta autenticato, ha accesso a tutta la cronologia salvata nel database locale, quindi chi condivide il computer o lo compromette eredita lo stesso accesso; e dare al modello la capacità di scrivere messaggi apre la porta a un prompt injection ricevuto da un contatto e interpretato come comando. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]

## Repository

- GitHub, licenza MIT, oltre 6.346 stelle al 1° ottobre 2026.

## Timeline delle notizie

- **2026-10-01** — WhatsApp MCP Server, progetto open source di Luke Harries con licenza MIT, supera le 6.346 stelle: collega [[claude]] al proprio WhatsApp personale via [[mcp]], con un bridge in Go basato su whatsmeow e un database SQLite locale. Il repository esiste dal marzo 2025 ma torna a circolare a inizio ottobre 2026 come se fosse una novità, presentato in alcuni reel come collegamento gratuito a Sonnet 5.5. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]
- **2026-10-01** — WhatsApp MCP Server, progetto open source di Luke Harries con licenza MIT, supera le 6.346 stelle al 1° ottobre 2026: implementa un server [[mcp]] dedicato a WhatsApp che collega [[claude]] al proprio account personale, con un bridge in Go basato sulla libreria whatsmeow collegato tramite la stessa API multi-dispositivo di WhatsApp Web e un database SQLite locale. Il repository esiste dal marzo 2025 ma torna a circolare a inizio ottobre 2026 presentato come novità, con frasi come "ora puoi collegare Sonnet 5.5 direttamente a WhatsApp, gratis al 100%": non è un prodotto ufficiale di Anthropic né di Meta. [Fonte: raw/pillitteri/pillitteri20261001-whatsapp-mcp-server-claude.md]




## Collegamenti

- [[mcp]]
- [[claude]]
- [[privacy-online]]
- [[index]]
