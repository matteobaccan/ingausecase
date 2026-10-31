---
title: "Microsoft Execution Containers"
category: strumento
tags: [agenti, contenitori, microsoft, sicurezza, windows]
related_puntate: [20261012]
created: 2026-10-08
updated: 2026-10-12
---

# Microsoft Execution Containers

## Introduzione

Libreria di [[microsoft]] che permette a uno sviluppatore di dichiarare a che
cosa può accedere un agente — file e rete compresi — e a Windows di far
rispettare quei confini mentre l'agente lavora. È nota anche come MXC e al Build
del 2 giugno 2026 era una early preview.

## Capacità e performance

- La libreria è descritta sul palco come «cross-platform library for secure agent
  containment» e con essa un agente gira in un perimetro dichiarato: un programma
  sbagliato non vede tutto il disco.
- Agent 365, il pannello con cui un amministratore IT governa gli agenti
  dell'azienda, è collegato a Windows e alle funzioni di gestione enterprise dei
  contenitori.
- Nella demo del keynote Code costruisce un'app nativa di Windows da un solo
  prompt con il supporto a MXC nel sandbox, passando il lavoro ai modelli locali.

## Azienda di riferimento

- [[microsoft]]

## Timeline delle notizie

- **2026-10-07** — Microsoft Execution Containers, annunciati come early preview al Build del 2 giugno, passano in disponibilità generale: la slide dell'evento Windows porta la dicitura «Generally available» e la libreria diventa il perimetro standard per chi sviluppa agenti su Windows.
- **2026-10-12** — Microsoft Execution Containers definiscono via configurazione JSON quali file, reti e risorse di sistema un agente può accedere, in sandbox multipiattaforma su Windows, Linux e macOS, e sono già supportati da GitHub Copilot, OpenAI Codex, Replit e OpenClaw.




## Collegamenti

- [[microsoft]]
- [[copilot]]
- [[openclaw]]
- [[agenti-ai]]
- [[index]]
