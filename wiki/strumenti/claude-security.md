---
title: "Claude Security"
category: strumento
tags: [anthropic, claude, plugin, sicurezza]
related_puntate: [20260524, 20260525, 20260724]
created: 2026-08-12
updated: 2026-10-25
sources: [raw/puntate/ainews20260524.md, raw/puntate/ainews20260525.md, raw/puntate/ainews20260724.md, raw/pillitteri/pillitteri20260524-anthropic-mythos-1-claude-code-security-lancio.md, raw/pillitteri/pillitteri20260526-anthropic-cambia-rotta-claude-mythos-claude-code-security.md, raw/pillitteri/pillitteri20260723-claude-security-plugin-sicurezza-claude-code.md, raw/pillitteri/pillitteri20260821-claude-security-mythos-5-scansioni.md, raw/pillitteri/pillitteri20260527-anthropic-security-guidance-plugin-claude-code-25-pattern-vulnerabili.md, raw/pillitteri/pillitteri20261024-migliori-strumenti-ai-audit-sicurezza-codice-confronto.md]
---

# Claude Security

## Introduzione

Plugin di Anthropic per Claude Code che scansiona modifiche o intero repository alla ricerca di vulnerabilità critiche, suggerendo fix concreti nel terminale.

## Funzionalità principali

- Claude Security è stato citato come uno dei due ambienti (con Claude Code) in cui Anthropic probabilmente rilascerà Claude Mythos.
- Claude Security è stato citato come ambiente di preparazione per Claude Mythos 1, modello focalizzato su coding e security.
- Anthropic ha lanciato il plugin Claude Security per Claude Code: scansionava modifiche o intero repository alla ricerca di vulnerabilità critiche, suggerendo fix concreti direttamente nel terminale.

## Azienda / Autore

- [[anthropic]]

## Modelli supportati / correlati

- [[claude-mythos-5]]

## Timeline delle notizie

- **2026-05-24** — Claude Security è stato citato come uno dei due ambienti (con Claude Code) in cui Anthropic probabilmente rilascerà Claude Mythos. [Fonte: raw/puntate/ainews20260524.md]
- **2026-05-25** — Claude Security è stato citato come ambiente di preparazione per Claude Mythos 1, modello focalizzato su coding e security. [Fonte: raw/puntate/ainews20260525.md]
- **2026-05-26** — Anthropic pubblica Security Guidance, plugin gratuito del marketplace che intercetta in tempo reale le scritture di Claude Code e blocca circa 25 pattern vulnerabili in otto famiglie con matching locale, senza chiamate all'API esterna; il rilascio arriva dopo le disclosure di maggio su vulnerabilità dell'ecosistema agentico. [Fonte: raw/pillitteri/pillitteri20260527-anthropic-security-guidance-plugin-claude-code-25-pattern-vulnerabili.md]



- **2026-07-24** — Anthropic ha lanciato il plugin Claude Security per Claude Code: scansionava modifiche o intero repository alla ricerca di vulnerabilità critiche, suggerendo fix concreti direttamente nel terminale. [Fonte: raw/puntate/ainews20260724.md]

- **2026-05-26** — Entra nel piano di lancio di Mythos-1, il modello frontier cyber di [[anthropic]]: il sorgente di [[claude-code]] riporta la stringa "Access to the Claude Mythos model in Claude Code and Claude Security", e il 22 maggio il dashboard viene aggiornato con grafici a 7 e 30 giorni sulle vulnerabilità scoperte e risultati di triage approfonditi. La funzionalità prevista è il deep triage automatizzato sui bug segnalati dai partner di Project Glasswing. [Fonte: raw/pillitteri/pillitteri20260526-anthropic-cambia-rotta-claude-mythos-claude-code-security.md]
- **2026-05-24** — Il flusso operativo previsto invoca Mythos-1 da Claude Code, lo lascia agire in modo agentico sul codice (recupero file, prove in sandbox, scrittura e validazione di proof-of-concept) e riporta gli esiti nel dashboard, dove l'analista assegna il ticket al team di sviluppo. [Fonte: raw/pillitteri/pillitteri20260524-anthropic-mythos-1-claude-code-security-lancio.md]

- **2026-07-23** — Il 22 luglio 2026 Anthropic apre la beta del plugin Claude Security per Claude Code: il comando /claude-security avvia una squadra di agenti a caccia di vulnerabilità con una pipeline a sei fasi e un panel di tre verificatori che promuove una scoperta solo con due voti su tre, con report e patch verificate da un agente terzo e applicate a mano. Richiede un piano a pagamento e Python 3.9.6 o superiore e gira in locale, quindi raggiunge repository su GitLab, Bitbucket o reti chiuse che il servizio Enterprise non copre. [Fonte: raw/pillitteri/pillitteri20260723-claude-security-plugin-sicurezza-claude-code.md]
- **2026-08-21** — Le scansioni di Claude Security passano a [[claude-mythos-5]], il modello cyber più forte di Anthropic: le aziende Enterprise ottengono l'analisi senza accesso al modello, che resta chiuso dentro Project Glasswing, ogni segnalazione è verificata in modo adversariale e le patch restano soggette a revisione umana. Nello stesso annuncio un fondo da 35 milioni di dollari per la sicurezza open source (Defender Advantage Fund). [Fonte: raw/pillitteri/pillitteri20260821-claude-security-mythos-5-scansioni.md]
- **2026-10-24** — Nel confronto degli strumenti di audit il servizio risulta in beta pubblica per i clienti Claude Enterprise dal 30 aprile, con scansione di base profonda e continua sulle modifiche, verifica avversariale di ogni finding, threat model modificabile e patch consigliata da approvare, senza prezzo pubblicato e su contatto commerciale. Il plugin omonimo per Claude Code è in beta dal 22 luglio e tiene il codice nell'ambiente dell'utente con i modelli del suo account, senza le scansioni Mythos riservate all'app. [Fonte: raw/pillitteri/pillitteri20261024-migliori-strumenti-ai-audit-sicurezza-codice-confronto.md]




## Collegamenti

- [[anthropic]]
- [[claude-code]]
- [[claude-mythos-5]]
- [[sicurezza-ai]]
- [[index]]

