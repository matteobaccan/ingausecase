---
title: "HERMES Agent"
category: strumento
tags: [3d, a2a, agent, auto-evolutivo, automazione, browser, computer-use, context, desktop, ecosistema, framework, harness, mcp, moa, nous-research, open-source, plugin, remoto, serverless, skill, tool-use, voce, webhook]
related_puntate: [20260510, 20260511, 20260516, 20260526, 20260602, 20260607, 20260608, 20260610, 20260611, 20260612, 20260613, 20260626, 20260627, 20260629, 20260706, 20260709, 20260718, 20260729, 20260730, 20260804, 20260805, 20260810, 20260811, 20260912]
created: 2026-08-12
updated: 2026-10-22
---

# HERMES Agent

## Introduzione

Agente AI open source per compiti complessi, capace di fare chiamate tool, computer use e orchestrare modelli. Integra preset MOA di Nous Research e supporta Gemini, ChatGPT e altri runtime.

## Funzionalità principali

- hermes-agent è l'agente IA auto-evolutivo che estrae skill da ogni conversazione e diventa più intelligente più lo usi, tra gli undici repository di cervelli brillanti distillati in IA installabile.
- Hermes Agent ha ora un'app desktop nativa: l'agente autonomo di Nous Research funziona con interfaccia completa invece che solo CLI, con gestione multi-agente, memoria persistente e workflow autonomi.
- Hermes Agent e OpenClaw sono stati testati con Qwen 35B local su MacBook Pro M5 Max 64GB: task di scraping GitHub star history, analisi spike e dashboard live; Hermes ha usato 257.000 token in 33 minuti e 1 secondo, facendo parallel tool calls su GitHub API, web search e browser, e ha consegnato dashboard live con grafici e annotazioni spike.

## Azienda / Autore

- [[copilotkit]]
- [[nous-research]]
- [[nvidia]]

## Modelli supportati / correlati

- [[gemini-3-5-flash]]
- [[gemma-4]]
- [[gpt-5-6-sol]]
- [[kimi-k3]]
- [[nemotron-3-ultra]]
- [[qwopus-3-6-27b-coder]]

## Timeline delle notizie

- **2026-05-10** — hermes-agent è l'agente IA auto-evolutivo che estrae skill da ogni conversazione e diventa più intelligente più lo usi, tra gli undici repository di cervelli brillanti distillati in IA installabile.
- **2026-05-11** — Hermes Agent ha ora un'app desktop nativa: l'agente autonomo di Nous Research funziona con interfaccia completa invece che solo CLI, con gestione multi-agente, memoria persistente e workflow autonomi.
- **2026-05-16** — Hermes Agent e OpenClaw sono stati testati con Qwen 35B local su MacBook Pro M5 Max 64GB: task di scraping GitHub star history, analisi spike e dashboard live; Hermes ha usato 257.000 token in 33 minuti e 1 secondo, facendo parallel tool calls su GitHub API, web search e browser, e ha consegnato dashboard live con grafici e annotazioni spike.
- **2026-05-26** — Hermes Agent di Nous Research è stato citato: Webwright include la sua skill per il browser use agentico.
- **2026-06-02** — Hermes Agent è il framework dietro Hermes Desktop, l'app gratuita con chat streaming, memoria modificabile, quattordici categorie di strumenti e sedici gateway di messaggistica.
- **2026-06-07** — Hermes Agent 0.16 ha app desktop native per macOS, Windows e Linux e dashboard web completa: gestisci canali, server MCP e credenziali, con integrazione NVIDIA Skills Hub e supporto al cinese semplificato.
- **2026-06-07** — Hermes Agent si collega a un modello locale come Gemma 4 tramite l'API compatibile OpenAI di [[ollama]] (base_url http://localhost:11434/v1), con oltre 70 skill pronte e memoria che attraversa le sessioni; richiede un modello con almeno 64.000 token di finestra di contesto e rifiuta all'avvio quelli più corti. Per un agente su modelli locali conviene una temperatura bassa (0,3), che rende le chiamate agli strumenti più deterministiche.
- **2026-06-08** — Nous Research ha lanciato Hermes Agent Desktop App: trasforma laptop da otto GB in un ecosistema autonomo con esecuzione tool, interazione web, DevOps e integrazione Notion e Google Workspace. Hermes Agent include inoltre Nemotron 3 Ultra di NVIDIA gratuitamente fino al diciotto giugno, disponibile tramite Nous Portal.
- **2026-06-10** — L'ecosistema plugin di Hermes include un registry condiviso di skill tra agent, il plugin Graphiti per knowledge graph, la dashboard Mnemosyne per la memoria visuale e YantrikDB come backend vettoriale enterprise.
- **2026-06-11** — Hermes Agent Desktop funziona come sala controllo remota per VPS Agent: Tailscale su entrambe le macchine, OAuth via Nous Portal e connessione tramite gateway remoto, con le stesse sessioni, memoria e skill; niente esposto su internet aperta; gestione sessioni per il controllo costi, sessioni parallele, browser file con preview live, terminale integrato, dettatura vocale e switch modello dalla status bar.
- **2026-06-12** — Hermes Agent è il target di ottimizzazione di Qwopus 3.6 27B-Coder e ospita raccolte di skill: Wondelai/skills ne conta trecentottanta e ZeroPointRepo organizza quelle verificate, con liste curate per frontend design, documenti Office, web access, anti-loop PUA, memoria persistente Claude-mem e Skill Creator.
- **2026-06-13** — Hermes Agent introduce template di automazione con tre trigger: schedule, GitHub event e API call, con consegna su Telegram, Discord, Slack, SMS, email, commenti GitHub o file locali; template come triage notturno del backlog, code review automatico su PR, rilevamento drift della documentazione e audit di sicurezza delle dipendenze. Un utente gli ha consegnato l'intera attività per tre settimane e ha ricevuto analisi competitive, report di intelligence e stato progetto, scoprendo uno shift competitivo durato sei settimane.
- **2026-06-26** — Hermes Agent aggiunge slash learn: costruisce skill PRIMA di eseguire il task; si punta a SDK locale, URL docs, workflow o note e l'agente legge, scrive SKILL punto md, testa live e salva; nessun motore di ingestion separato: slash learn è un normale turn dell'agente.
- **2026-06-27** — Ha integrato i preset MOA di Nous Research (Mixture of Agents: più modelli reference offrono consigli privati, un aggregator decide e agisce; i reference non accedono ai tool). In un test con Gemini 3.5 Flash e Computer Use via trycua ha aperto Chrome, navigato su ChatGPT e generato un'immagine in 1 minuto e 47 secondi, con 30 secondi di analisi.
- **2026-06-29** — Mixture of Agents integrato: più modelli consultati e uno scrive la risposta finale. I preset mescolano OpenAI, Anthropic e DeepSeek senza perdere contesto.
- **2026-07-06** — Estensione browser per Hermes Agent versione 2: gestione sessioni complete, vision con screenshot, side panel su ogni tab, swap modelli mid-chat (Opus, Grok, GPT o locale). Connessione a gateway Hermes locale o remoto.
- **2026-07-09** — Hermes Agent ora si deploya direttamente da Nous Portal in un click: zero VPS, zero SSH, serverless con scala a zero quando idle e memoria persistente tra sessioni.
- **2026-07-18** — Hermes Agent ora funziona con Unreal Engine tramite lo skill MCP per Epic Games: trasforma prompt testuali in scene 3D complete, scopre tool e verifica i risultati visivamente.
- **2026-07-29** — La funzione slash moa (Mixture of Agents) di Hermes inviava lo stesso prompt a due o più modelli in parallelo, poi un terzo sintetizzava la risposta migliore. Risultato su HermesBench: 0,8202.
- **2026-07-30** — Tre harness diversi con lo stesso modello: Kimi K3 testato con Claude Code, Hermes e Kimi Code su 28 task identici, con tasso di successo simile ma costo token fino a trenta volte diverso.
- **2026-08-04** — Hermes Agent versione zero virgola venti offre voce conversazionale con interruzione mid-frase, citazioni verificate con fact-checking, webhooks in uscita e protocollo Agent-to-Agent uno virgola zero per comunicazione tra agenti eterogenei.
- **2026-08-05** — Hermes Agent ora fa girare team multi-agente dentro workspace Buzz condivisi: tre agenti su tre macchine diverse in una sola chat che si cercano info, si controllano a vicenda e correggono gli errori in diretta, ma il setup è ancora ostico.
- **2026-08-10** — Hermes Agent, se usi GPT cinque punto sei, permette la compaction server-side con l'API Responses nativa di OpenAI: OpenAI compatta il vecchio contesto lato server, Hermes tiene il checkpoint cifrato e lo riproduce nei turni successivi, con gestione del contesto migliore per le sessioni lunghe.
- **2026-08-11** — Hermes Agent ha rilasciato Browser Use, modalita' che condensa dodici tool browser in uno solo: l'agente scrive uno script per l'intero flusso invece di chiamare un tool per ogni click, con riduzione token del quarantotto-sessantasei percento e nessun calo di precisione; la v zero virgola venti punto zero introduce grounded citations con ogni claim linkato a pagina e passaggio (confermato, non verificato, contraddetto).

- **2026-09-12** — Hermes è tra gli agenti multipli che Herdr, tool CLI open source, organizza in spazi e tab mostrando quali stanno lavorando e quali aspettano risposta.
- **2026-10-22** — NVIDIA lo cita fra gli ingredienti della catena con cui ha addestrato i robot Microduck, insieme a Isaac Lab e a Nemotron 3.5 Bolt 74B, senza dettagliare quale compito spetti a ciascuno.




## Collegamenti

- [[agenti-ai]]
- [[agent-reach]]
- [[claude-code]]
- [[copilotkit]]
- [[gemini-3-5-flash]]
- [[gemma-4]]
- [[goose]]
- [[gpt-5-6-sol]]
- [[graphiti]]
- [[hermes-desktop]]
- [[kimi-k3]]
- [[mnemosyne]]
- [[nemotron-3-ultra]]
- [[gemini-notebook]]
- [[nous-research]]
- [[nvidia]]
- [[openclaw]]
- [[openmontage]]
- [[open-source]]
- [[openwiki]]
- [[qwopus-3-6-27b-coder]]
- [[red-queen-godel-machine]]
- [[skills-hub]]
- [[trycua]]
- [[webwright]]
- [[yantrikdb]]
- [[zero]]
- [[herdr]]
- [[index]]

