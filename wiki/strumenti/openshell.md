---
title: "NVIDIA OpenShell"
category: strumento
tags: [nvidia, agent, sicurezza-ai, sandbox, open-source]
related_puntate: []
created: 2026-10-01
updated: 2026-10-26
sources: [raw/tldr/tldr20261001.md, raw/pillitteri/pillitteri20261026-nvidia-licenza-2000-dollari-gpu-agenti.md]
---

# NVIDIA OpenShell

## Introduzione

Runtime con policy per agenti autonomi rilasciato da [[nvidia]]. [Fonte: raw/tldr/tldr20261001.md]

## Funzionalità principali

- Applica a livello di kernel il controllo degli accessi a file, system call, rete e credenziali. [Fonte: raw/tldr/tldr20261001.md]
- Usa la verifica formale per individuare i permessi rischiosi prima che le modifiche di policy vengano applicate. [Fonte: raw/tldr/tldr20261001.md]

## Azienda / Autore

- [[nvidia]]

## Timeline delle notizie

- **2026-10-01** — NVIDIA rilascia OpenShell, runtime con policy per agenti autonomi che applica a livello di kernel i controlli su file, system call, rete e credenziali e usa la verifica formale per individuare i permessi rischiosi prima di applicare le modifiche di policy. [Fonte: raw/tldr/tldr20261001.md]
- **2026-10-26** — Il 21 ottobre Nvidia ha presentato la OpenShell Reference Architecture per far girare agenti in azienda, che mette insieme i sistemi Vera Rubin per l'inferenza, le CPU Vera per eseguire gli agenti e le schede BlueField-4 su cui gira Nvidia Sentry, il componente che osserva ciò che fanno gli agenti in modo indipendente e può metterne uno in quarantena se supera i confini assegnati. Secondo Tom's Hardware Anthropic integra OpenShell e le BlueField con [[claude-managed-agents]] per dare alle imprese più controllo su ciò a cui gli agenti possono accedere, e Salesforce ha costruito per OpenShell un ponte con Slack che permette agli amministratori di approvare o respingere le richieste di permessi. [Fonte: raw/pillitteri/pillitteri20261026-nvidia-licenza-2000-dollari-gpu-agenti.md]




## Collegamenti

- [[nvidia]]
- [[agenti-ai]]
- [[sicurezza-ai]]
- [[index]]
