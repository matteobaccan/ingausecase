---
title: "Amazon Bedrock"
category: strumento
tags: [aws, cloud, piattaforma]
related_puntate: [20260625]
created: 2026-08-12
updated: 2026-10-23
---

# Amazon Bedrock

## Introduzione

Piattaforma di hosting modelli di AWS; su di essa è ricomparso Fable 5.

## Funzionalità principali

- Amazon Bedrock è la piattaforma su cui Fable 5 è già ricomparso, segno del possibile ritorno del modello annunciato dagli indizi in Claude Code 2.1.190.

## Modelli supportati / correlati

- [[fable-5]]

## Timeline delle notizie

- **2026-06-25** — Amazon Bedrock è la piattaforma su cui Fable 5 è già ricomparso, segno del possibile ritorno del modello annunciato dagli indizi in Claude Code 2.1.190.

- **2026-08-10** — Al Black Hat USA i ricercatori Hedi Ingber e Aviyam Ivgi mostrano CoreBreak su Bedrock AgentCore: la falla CVE-2026-18830 (CVSS v4.0 8,6, validazione impropria dell'input) permetteva a un chiamante remoto già autenticato di includere un blocco di tipo tool-use direttamente nell'ultimo messaggio della richiesta dell'API InvokeHarness, e il ciclo di eventi lo raccoglieva facendo partire lo strumento senza interpellare il modello; il requisito dell'autenticazione limita la platea, ma in un'organizzazione con molte utenze applicative chiunque possa chiamare l'endpoint può pilotare gli strumenti dell'agente. La quinta strada di attacco, quella che passa dallo Strands Agents SDK di AWS, resta aperta per scelta esplicita del vendor.
- **2026-09-21** — Il report di Unit 42 del 18 settembre 2026 mostra che un agente in esecuzione su AgentCore Harness può consegnare a un attaccante le credenziali custodite nel vault Identity: la shell integrata, attiva di default e in esecuzione come root, condivide il processo in cui il runtime (PID 1) decifra il segreto, quindi uno script avviato da un ticket con un commento HTML nascosto legge /proc/1/mem ed estrae un JWT, senza che nessuna configurazione risulti sbagliata nel test. AWS ha chiuso la segnalazione come informativa, considerandola una questione di configurazione e non una vulnerabilità.
- **2026-10-23** — Wiz ha rilevato credenziali sottratte con una versione malevola di LiteLLM usate per testare l'accesso a Bedrock: non sono emerse prove di chiamate ai modelli, furto di dati o costi generati, ma la credenziale era valida.




## Collegamenti

- [[alexa-plus]]
- [[amazon]]
- [[fable-5]]
- [[index]]

