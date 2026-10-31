---
title: "Cloudflare Workers AI"
category: strumento
tags: [cloud, inference, serverless]
related_puntate: [20260627, 20260628]
created: 2026-08-12
updated: 2026-10-29
---

# Cloudflare Workers AI

## Introduzione

Piattaforma serverless di Cloudflare per l'inferenza di modelli AI su edge, con free tier giornaliero senza carta di credito.

## Funzionalità principali

- Ora ospita GLM-5.2 con contesto da 262.144 token, tool calling nativo e compatibilità OpenAI. Offre 10.000 neuroni gratis al giorno senza carta di credito.
- Ora esegue GLM 5.2 gratis senza limiti, compatibile con OpenCode, Cursor, Aider, Hermes Agent e Claude Code: basta creare un account gratuito e copiare Account ID e token API.

## Azienda / Autore

- [[zhipu-ai]]

## Modelli supportati / correlati

- [[glm-5-2]]

## Timeline delle notizie

- **2026-06-27** — Ora ospita GLM-5.2 con contesto da 262.144 token, tool calling nativo e compatibilità OpenAI. Offre 10.000 neuroni gratis al giorno senza carta di credito.
- **2026-06-28** — Ora esegue GLM 5.2 gratis senza limiti, compatibile con OpenCode, Cursor, Aider, Hermes Agent e Claude Code: basta creare un account gratuito e copiare Account ID e token API.
- **2026-10-29** — Un problema di isolamento tra clienti ha coinvolto il modello GLM-5.3 tra il 27 agosto e il 9 settembre: 155 risposte hanno contenuto dati di richieste precedenti di altri utenti, tutte con prompt molto lunghi, per un difetto che combinava la cache KV e la modalità di esecuzione di SGLang. [[cloudflare]] ha disattivato e poi ripristinato il modello con correzioni e non ha trovato prove di sfruttamento intenzionale.




## Collegamenti

- [[freellmapi]]
- [[glm-5-2]]
- [[zhipu-ai]]
- [[index]]

