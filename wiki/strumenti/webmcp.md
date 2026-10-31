---
title: "WebMCP"
category: strumento
tags: [agenti, browser, chrome, mcp, protocollo, w3c]
related_puntate: []
created: 2026-10-27
updated: 2026-10-27
---

# WebMCP

## Introduzione

Proposta di standard per il browser, nata nel Web Machine Learning Community Group del W3C con editori di Google e Microsoft, che permette a una pagina di dichiarare all'agente quali azioni sa compiere mentre la scheda è aperta. Non sostituisce [[mcp]], che resta il protocollo lato server.

## Differenze con MCP

- MCP vive nel backend, è persistente, arriva su desktop, mobile e cloud e richiede una registrazione specifica per ogni agente; WebMCP vive nel frontend, dura quanto la scheda, si scopre durante la visita e lavora dentro il browser a contatto con il DOM.
- Con WebMCP le azioni avvengono in vista e sfruttano la sessione già aperta; un lavoro che deve girare di notte o senza browser resta territorio di MCP.

## Come funziona

- API imperativa: lo strumento si registra con `registerTool` sull'oggetto `document.modelContext`, con nome, descrizione, schema JSON degli input e funzione `execute`; le annotazioni `readOnlyHint`, `consequentialHint` e `untrustedContentHint` dicono al browser con che cautela trattarlo.
- API dichiarativa: basta aggiungere `toolname` e `tooldescription` a un form HTML e il browser ricava lo schema dei campi; senza `toolautosubmit` l'invio resta all'utente.
- Il campo `agentInvoked` nell'evento di invio dice all'applicazione che il modulo è stato compilato da un agente; `respondWith`, `toolactivated` e `toolcancel` gestiscono l'esito e il ripensamento dell'utente.

## Stato e limiti

- Chrome 149 offre un origin trial; in locale si prova con il flag `chrome://flags/#enable-webmcp-testing`. La bozza è un Draft Community Group Report del 20 ottobre 2026 e non è uno standard W3C.
- Non funziona senza scheda aperta, non esiste un indice degli strumenti consultabile dall'esterno e l'API può cambiare: le prime guide parlavano di `navigator.modelContext`, oggi la documentazione usa `document.modelContext`.
- Il capitolo sicurezza della specifica è non normativo: fra i rischi elencati la prompt injection in tre varianti, il disallineamento fra ciò che lo strumento dichiara e ciò che fa, la perdita di privacy per eccesso di parametri e i confini same-origin.

## Timeline delle notizie

- **2026-10-26** — Il team Chrome for Developers precisa che WebMCP non sostituisce MCP: il primo collega gli agenti a un sito finché la scheda è aperta, il secondo ai servizi di un'azienda ovunque e a qualsiasi ora, e l'architettura proposta li tiene su due livelli.

## Collegamenti

- [[mcp]]
- [[agenti-ai]]
- [[index]]
