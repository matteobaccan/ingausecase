---
title: "php2shell-checker"
category: strumento
tags: [openai, sicurezza, php, codex, open-source]
related_puntate: []
created: 2026-10-22
updated: 2026-10-22
---

# php2shell-checker

## Introduzione

php2shell-checker è il controllo gratuito con licenza Apache-2.0 che OpenAI ha pubblicato su GitHub il 21 ottobre 2026 per sapere se un sito è esposto a PHP2Shell, il nome con cui circolano le due vulnerabilità CVE-2026-109618 e CVE-2026-109619 di PHP.

## Funzionalità principali

- Legge la versione di PHP dagli header HTTP `Server` e `X-Powered-By`, oppure da `php -v` in locale, e la confronta con una tabella di soglie per ramo da 5.4 a 8.5.
- Risponde OK, VULNERABLE oppure UNKNOWN, e se trova più versioni sceglie la peggiore.
- La raccolta è volutamente minima: una richiesta HEAD, GET solo se il server risponde 405 o 501, nessun reindirizzamento seguito e nessuna lettura del corpo della pagina.

## Installazione e uso

- Lo script `phpcheck.js` gira con Node.js e senza dipendenze esterne; il repository include anche due skill per [[codex]], `phpcheck-url` per chi ha solo l'indirizzo del sito e `phpcheck-server` per chi ha accesso al server.
- Al 22 ottobre il repository contava 556 stelle e 44 fork, con 39 test che passano su server HTTP locali e su un finto eseguibile PHP.

## Limiti

- UNKNOWN non significa sito patchato: i server che nascondono la versione di PHP non danno nulla da leggere allo strumento, come è successo al sito su cui è stato provato.
- OK è un confronto tra numeri e non la prova che la falla sia stata corretta, e i backport delle distribuzioni Linux possono risultare VULNERABLE pur essendo corretti, perché lo strumento guarda il numero di versione e non il changelog del pacchetto.

## Azienda / Autore

- [[openai]]

## Strumenti correlati

- [[codex]]
- [[cybersicurezza]]

## Timeline delle notizie

- **2026-10-22** — OpenAI pubblica php2shell-checker, controllo gratuito sotto Apache-2.0 che confronta la versione di PHP con una tabella di soglie per ramo e risponde OK, VULNERABLE o UNKNOWN, distribuendolo anche come due skill per Codex; il README avverte che UNKNOWN non equivale a sito aggiornato.

## Collegamenti

- [[openai]]
- [[codex]]
- [[cybersicurezza]]
- [[index]]
