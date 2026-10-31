---
title: "GitHub"
category: azienda
tags: [github, breach, open-source, piattaforma, sicurezza, sviluppo, usa]
related_puntate: [20260521, 20260629, 20260712, 20260901]
created: 2026-08-12
updated: 2026-10-28
sources: [raw/puntate/ainews20260521.md, raw/puntate/ainews20260629.md, raw/puntate/ainews20260712.md, raw/puntate/ainews20260901.md, raw/pillitteri/pillitteri20261024-migliori-strumenti-ai-audit-sicurezza-codice-confronto.md, raw/controrumore/controrumore20261028-diario-ai-sicurezza-mercati-e-agenti.md]
---

# GitHub

## Introduzione

Piattaforma di hosting di codice di Microsoft; a maggio 2026 subisce una compromissione interna via estensione VS Code infetta con 3800 repository esposti.

## Strumenti

- [[nx-console]]
- [[openmythos]]
- [[spec-kit]]

## Timeline delle notizie

- **2026-05-21** — GitHub è stato compromesso: un dipendente ha installato un'estensione VS Code infetta (Nx Console, 2,2 milioni di installazioni) rimasta online 11 minuti; esposti 3800 repository interni, con token rubati da GitHub, npm, AWS, Kubernetes e 1Password e dati venduti da TeamPCP sul dark web, partito da un commit orfano nascosto. [Fonte: raw/puntate/ainews20260521.md]
- **2026-06-29** — Ha rilasciato Spec Kit, strumento in sei step per far capire all'IA cosa deve fare prima di scrivere codice, che ha già superato le 110.000 stelle. [Fonte: raw/puntate/ainews20260629.md]
- **2026-07-12** — GitHub ha lanciato Spec Kit, che ha superato centoventimila stelle in pochi giorni: obbliga l'IA a creare una specifica strutturata prima di toccare codice. [Fonte: raw/puntate/ainews20260712.md]
- **2026-09-01** — Sepia, progetto GitHub con cinquemiladuecento star, identifica la scrittura generata da IA al 93,2% di precisione analizzando la struttura narrativa. [Fonte: raw/puntate/ainews20260901.md]
- **2026-10-24** — CodeQL con Copilot Autofix resta la via più corta per chi ha i repository su GitHub: Autofix non richiede un abbonamento Copilot, copre nove linguaggi per un sottoinsieme delle query e la documentazione ammette che non è deterministico, fatica sui flussi fra più file e può inventare le dipendenze proposte nelle correzioni. Dal 10 luglio esiste anche l'autofix agentico in anteprima pubblica, che assegna un alert a Copilot e apre una pull request in due-quattro minuti consumando crediti AI, e non cerca difetti nuovi; Code Security costa 30 dollari per committer attivo al mese secondo il listino di marzo 2025. [Fonte: raw/pillitteri/pillitteri20261024-migliori-strumenti-ai-audit-sicurezza-codice-confronto.md]
- **2026-10-28** — Afferma che il 99,99999 per cento dei repository è conservato nei propri data center e in Azure, dove si trova la maggior parte dei progetti e transita circa metà del traffico Git; presenta l'architettura come preparazione a uno sviluppo «agent-scale», in cui cicli automatizzati potrebbero aumentare l'attività sulle infrastrutture, e come misura di resilienza. Il post non dice che tutti i dati siano stati trasferiti ad Azure né quantifica un aumento di richieste già causato dagli agenti. [Fonte: raw/controrumore/controrumore20261028-diario-ai-sicurezza-mercati-e-agenti.md]







## Collegamenti

- [[nx-console]]
- [[openmythos]]
- [[spec-kit]]
- [[teampcp]]
- [[index]]

