---
title: "GitLab"
category: azienda
tags: [developer-tools, devops, agent, usa]
created: 2026-10-01
updated: 2026-10-03
---

# GitLab

## Introduzione

Piattaforma di sviluppo software e DevSecOps che il 10 giugno 2026 ha portato in beta pubblica Orbit, un grafo di contesto che indicizza l'intero ciclo di vita del software e lo espone come sorgente unica ad agenti AI e sviluppatori.

## Strumenti

- **Orbit**: grafo vivo e interrogabile che riunisce codice, merge request, pipeline, deployment, vulnerabilità, incident e ownership in un unico schema. Nei test interni un agente collegato a Orbit risponde fino a 11 volte più in fretta, consuma fino a 4,5 volte meno token e produce fino a 45 volte meno allucinazioni; sull'istanza interna copre oltre 40.000 progetti, circa 500 milioni di nodi e 2 miliardi di archi, con indicizzazione in 45 minuti. L'architettura usa change data capture su ClickHouse, parser dedicati per dodici linguaggi e un linguaggio di query simile a Cypher, con autorizzazione limitata al namespace; al lancio gira solo su GitLab.com nei piani Premium e Ultimate, senza versione self-managed.

## Timeline delle notizie

- **2026-08-09** — GitLab porta in beta pubblica Orbit, il grafo di contesto per gli agenti AI, presentato alla conferenza GitLab Transcend; resta fuori chi ha l'istanza in casa per vincoli di sovranità del dato.
- **2026-10-02** — GitLab corregge la vulnerabilità CVE-2026-90970 (CVSS 9,9) nell'AI Gateway, il servizio che alimenta le funzioni AI di GitLab Duo: un utente autenticato con accesso a Duo Agent Platform poteva uscire dalla sandbox dei template di prompt ed eseguire comandi arbitrari sul gateway. Riguarda solo chi ospita il gateway in proprio; nessuno sfruttamento noto secondo la CISA.




## Collegamenti

- [[codegraph]]
- [[sviluppo-software-ai]]
- [[agenti-ai]]
- [[index]]
