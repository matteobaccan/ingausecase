---
title: "LiteLLM"
category: strumento
tags: [attacco, credenziali, open-source, pypi, supply-chain]
related_puntate: []
created: 2026-09-21
updated: 2026-10-29
sources: [raw/pillitteri/pillitteri20260816-litellm-supply-chain-attacco-2026.md, raw/tldr/tldr20261022.md, raw/controrumore/controrumore20261023-diario-ai-agenti-sotto-osservazione.md, raw/controrumore/controrumore20261029-diario-ai-dati-chip-e-prove-per-i.md]
---

# LiteLLM

## Introduzione

Libreria open source che fa da traduttore universale verso i modelli di intelligenza artificiale: invece di scrivere codice diverso per parlare con OpenAI, Anthropic, Google Vertex o Amazon Bedrock, lo sviluppatore usa un unico formato e la libreria gira la richiesta al fornitore giusto. L'account ufficiale del progetto dichiara circa 97 milioni di download al mese, un numero che spiega perché un singolo pacchetto avvelenato possa toccare migliaia di aziende in pochi minuti; chi installa la libreria le mette in mano, per forza di cose, tutte le chiavi API dei fornitori AI che vuole usare. [Fonte: raw/pillitteri/pillitteri20260816-litellm-supply-chain-attacco-2026.md]

## Timeline delle notizie

- **2026-08-16** — Il 24 marzo 2026, alle 10:39 UTC, due versioni infette restano online sul repository ufficiale dei pacchetti Python per circa quaranta minuti, il tempo che basta per quella che gli analisti hanno poi definito la più grande violazione della supply chain nel software di AI del 2026: chi ha installato il pacchetto nella finestra sbagliata si è portato in casa un ladro di credenziali che rubava chiavi cloud, token SSH e password appena installato, e il malware sfruttava un file .pth eseguito da Python all'avvio, quindi bastava avere in progetto una libreria che a sua volta dipendeva da LiteLLM. [Fonte: raw/pillitteri/pillitteri20260816-litellm-supply-chain-attacco-2026.md]
- **2026-08-16** — Gli aggressori non hanno toccato LiteLLM direttamente: hanno compromesso uno strumento a monte, lo scanner [[trivy]], che la pipeline del progetto installava senza bloccare la versione, e da lì il codice è entrato nella build in automatico. CloudSEK ha ricostruito un archivio da 153 gigabyte con 433.909 file provenienti da 2.488 organizzazioni, tra cui NVIDIA, AWS, Cisco, Samsung e Siemens, e a cinque mesi dall'attacco molte credenziali risultavano ancora valide. [Fonte: raw/pillitteri/pillitteri20260816-litellm-supply-chain-attacco-2026.md]
- **2026-08-16** — La difesa indicata dalla fonte non è controllare a posteriori se il pacchetto era infetto, ma bloccare le versioni delle dipendenze su hash verificati e dare alle pipeline credenziali usa-e-getta, così un token rubato scade prima di poter fare danni. [Fonte: raw/pillitteri/pillitteri20260816-litellm-supply-chain-attacco-2026.md]
- **2026-10-22** — La versione 1.107.0 distribuita su PyPI è stata compromessa: un pacchetto malevolo è rimasto online circa due ore prima di essere rimosso, secondo la nota di sicurezza del progetto del 21 ottobre. [Fonte: raw/tldr/tldr20261022.md]
- **2026-10-23** — Wiz ha rilevato che credenziali sottratte tramite una versione malevola di LiteLLM sono state usate per verificare l'accesso ad Amazon Bedrock; secondo il resoconto non sono emerse prove di chiamate ai modelli, furto di dati o costi generati. [Fonte: raw/controrumore/controrumore20261023-diario-ai-agenti-sotto-osservazione.md]
- **2026-10-29** — Attribuisce la compromissione della versione 1.107.0 a una chiave master della propria piattaforma sperimentale, pubblicata per errore a maggio e mai revocata: l'attaccante l'avrebbe usata a ottobre per ottenere un token GitHub OAuth, sottrarre segreti e intervenire sul processo di rilascio, e il 21 ottobre il pacchetto malevolo è stato pubblicato su PyPI e sui registry dei container prima di essere rimosso. L'azienda riferisce di aver bloccato nuove pubblicazioni e avviato la revoca delle credenziali, con ulteriori modifiche di processo da documentare. [Fonte: raw/controrumore/controrumore20261029-diario-ai-dati-chip-e-prove-per-i.md]










## Collegamenti

- [[attacco-supply-chain-npm]]
- [[cybersicurezza]]
- [[trivy]]
- [[index]]
