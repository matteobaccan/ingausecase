---
title: "Claude S40"
category: strumento
tags: [claude, client, java, mit, nokia, terminale]
related_puntate: []
created: 2026-09-29
updated: 2026-09-29
---

# Claude S40

## Introduzione

Client Java non ufficiale pubblicato su GitHub il 26 settembre 2026 con licenza MIT dallo sviluppatore turco Emir Karşıyakalı, che porta Claude su un Nokia 6300 del 2007: sul telefono resta un MIDlet da circa 100 KB, mentre a fare il lavoro moderno è un piccolo server in Go distribuito come immagine Docker da circa 7 MB, che chiude il TLS e parla con le API di [[anthropic]] tramite l'SDK ufficiale.

## Funzionalità principali

- Il telefono (Nokia 6300 RM-217, firmware V06.60) offre solo TLS 1.0 senza SNI e certificati radice dei primi anni Duemila: il server installa una volta sul dispositivo un certificato firmato da un'autorità privata e si occupa di tutto il resto.
- La ricerca sul web la fa il server, quindi il browser del 2007 non entra mai in gioco e le fonti compaiono sotto la risposta; il corpo di ogni risposta è limitato a 8 KiB e con il tasto 0 si chiede la parte successiva, già in memoria sul server e quindi senza una nuova chiamata a Claude.
- Modalità lettura a schermo intero, messaggi vocali da 30 secondi trascritti sul server e riaperti nell'editor prima dell'invio, foto ridotte a 1.024 pixel su cui fare domande di seguito, voci di calendario che si salvano solo premendo Salva.
- Ogni invio passa da un pulsante e il server applica limiti giornalieri per dispositivo su richieste, token, ricerche, voce e foto; la chiave API resta sul server, al telefono arriva un token per singolo dispositivo ottenuto con un abbinamento a sei cifre.

## Azienda / Autore

- [[anthropic]]

## Timeline delle notizie

- **2026-09-29** — Claude S40 porta Claude su un Nokia 6300 del 2007: client Java non ufficiale su GitHub, licenza MIT, 225 stelle e 23 fork, con il video pubblicato su X il 27 settembre che ha superato i 3,2 milioni di visualizzazioni; il progetto dichiara di non essere prodotto né sostenuto da Anthropic o Nokia, è verificato solo su quel modello e richiede un server con IP pubblico (un VPS da 4-6 dollari al mese) più le normali API a pagamento.

## Collegamenti

- [[anthropic]]
- [[claude]]
- [[index]]
