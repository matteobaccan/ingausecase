---
title: "Artemis"
category: strumento
tags: [agent, android, automazione, google, open-source]
related_puntate: [20260909, 20260914, 20261019]
created: 2026-09-09
updated: 2026-10-19
sources: [raw/puntate/ainews20260909.md, raw/puntate/ainews20260914.md, raw/puntate/ainews20261019.md, raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]
---

# Artemis

## Introduzione

Artemis è un agente IA di [[google]] rilasciato come open source che trasforma inglese semplice in automazioni Android complete. [Fonte: raw/puntate/ainews20260909.md]

## Funzionalità principali

- Trasforma istruzioni in inglese semplice in automazioni Android complete. [Fonte: raw/puntate/ainews20260909.md]
- Oltre il novantanove percento di successo su AndroidWorld. [Fonte: raw/puntate/ainews20260909.md]
- Compatibile con Codex, Claude Code e Antigravity. [Fonte: raw/puntate/ainews20260909.md]
- Il repository google/artemis è nato il 13 agosto 2026 e al 18 ottobre conta 12.338 stelle, 1.430 fork e 139 tra segnalazioni e richieste di modifica aperte; il codice è sotto licenza Apache 2.0. [Fonte: raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]
- Si usa da console web su localhost:8000, da riga di comando, dall'SDK Python pensato per pytest e pipeline CI oppure dal server MCP, che espone cinque strumenti tra cui mobile_run_task e mobile_diagnose e collega Claude Code, Antigravity, Codex, Cursor e Windsurf. [Fonte: raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]
- Due profili di lavoro: Flash è un ciclo reattivo da circa 3-5 secondi a passo senza piano né verifica finale; Pro usa un Planner, un Operator e un Checker di sola lettura, costa 15-40 secondi a passo ma regge flussi oltre cento passaggi. [Fonte: raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]
- Al primo uso installa un Accessibility Helper che legge il layout dello schermo, reversibile con artemis helper uninstall; se si guasta ripiega su UIAutomator2. [Fonte: raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]
- Il 12 settembre 2026 il README ha iniziato a citare la libreria mobile-use di Minitap, dopo la segnalazione della startup francese per attribuzione mancante; una richiesta di modifica aperta chiede di sistemare altre attribuzioni. [Fonte: raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]

## Limiti

- Il tasso di completamento superiore al 99% su AndroidWorld è dichiarato nel README di Google, che non descrive il metodo di valutazione e non cita verifiche di terzi; dipende inoltre dal modello multimodale usato dietro l'agente. [Fonte: raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]
- Con un modello in cloud gli screenshot del telefono viaggiano verso il fornitore: per i primi test conviene un emulatore o un dispositivo senza account veri. [Fonte: raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]

## Azienda / Autore

- [[google]]

## Modelli supportati

- [[antigravity]]
- [[claude-code]]
- [[codex]]

## Timeline delle notizie

- **2026-09-09** — Google ha rilasciato come open source Artemis, agente IA che trasforma inglese semplice in automazioni Android complete, oltre il novantanove percento di successo su AndroidWorld, compatibile con Codex, Claude Code e Antigravity. [Fonte: raw/puntate/ainews20260909.md]
- **2026-09-14** — Il dettaglio operativo: Artemis pilota direttamente uno smartphone Android reale, guarda lo schermo, tocca, scorre, digita e cambia app come farebbe una persona, con due modalità, Flash per le operazioni veloci e Pro per i flussi complessi con retry automatico. Su AndroidWorld arriva al 99% di completamento su oltre cento task reali, si integra via MCP con [[claude-code]], [[cursor]] e Windsurf e include un'interfaccia web per vedere il telefono in tempo reale mentre l'agente lavora. [Fonte: raw/puntate/ainews20260914.md]
- **2026-10-18** - Il repository google/artemis conta 12.338 stelle, 1.430 fork e 139 segnalazioni aperte, con licenza Apache 2.0: l'agente si usa da console web, riga di comando, SDK Python e server MCP con cinque strumenti, distingue il profilo Flash dal Pro con Planner, Operator e Checker, installa un Accessibility Helper sul telefono e dal 12 settembre cita la libreria mobile-use di Minitap dopo una segnalazione per attribuzione mancante. [Fonte: raw/pillitteri/pillitteri20261018-google-artemis-agente-ai-open-source-android.md]



- **2026-10-19** — Il sistema [[artemis|ARTEMIS]] controlla un vero telefono Android come farebbe un umano — clicca, scorre, naviga tra app diverse — e sul benchmark AndroidWorld raggiunge il novantanove per cento di completamento su oltre cento task multi-step. Include un server MCP nativo con cui Claude Code, Windsurf e altri possono pilotare direttamente il device, gira in locale, installa un servizio di accessibilità per leggere il layout dello schermo e se fallisce torna automaticamente a UIAutomator2. [Fonte: raw/puntate/ainews20261019.md]




## Collegamenti

- [[antigravity]]
- [[claude-code]]
- [[codex]]
- [[cursor]]
- [[google]]
- [[index]]
