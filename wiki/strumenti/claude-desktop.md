---
title: "Claude Desktop"
category: strumento
tags: [anthropic, claude, desktop, linux, beta, debian, ubuntu]
related_puntate: []
created: 2026-09-21
updated: 2026-10-15
sources: [raw/pillitteri/pillitteri20260630-claude-desktop-linux-beta-ubuntu-debian.md, raw/pillitteri/pillitteri20261015-claude-code-desktop-sessioni-annidate-ambienti-salvati.md]
---

# Claude Desktop

## Introduzione

App desktop ufficiale di [[anthropic]] per usare [[claude]] fuori dal browser: riunisce in un'unica finestra le tre schede Chat, [[claude-cowork|Cowork]] e [[claude-code|Code]]. Fino al 30 giugno 2026 esisteva solo per macOS e Windows, mentre su Linux restavano due strade: la riga di comando o i pacchetti riconfezionati dalla community a partire dalla build Windows. [Fonte: raw/pillitteri/pillitteri20260630-claude-desktop-linux-beta-ubuntu-debian.md]

## Funzionalità principali

- La scheda Code esegue lo stesso motore di [[claude-code]] della CLI, quindi chi conosce lo strumento da terminale ritrova le stesse capacità dentro un'interfaccia grafica. [Fonte: raw/pillitteri/pillitteri20260630-claude-desktop-linux-beta-ubuntu-debian.md]
- Sessioni parallele di coding, revisione visuale delle diff riga per riga, terminale ed editor integrati e anteprima live dell'app costruita. [Fonte: raw/pillitteri/pillitteri20260630-claude-desktop-linux-beta-ubuntu-debian.md]
- La scheda Cowork porta sul desktop la modalità di lavoro autonomo in background, con il dispatch remoto da telefono; Code richiede un abbonamento Pro, Max, Team o Enterprise, mentre Chat e Cowork sono inclusi in qualunque piano a pagamento. [Fonte: raw/pillitteri/pillitteri20260630-claude-desktop-linux-beta-ubuntu-debian.md]

## Azienda / Autore

- [[anthropic]]

## Modelli supportati / correlati

- [[claude]]
- [[claude-code]]
- [[claude-cowork]]

## Timeline delle notizie

- **2026-06-30** — Anthropic pubblica la versione ufficiale di Claude Desktop su Linux in beta, per Ubuntu 22.04 o successivo e Debian 12 o successivo, su x86_64 e arm64: il pacchetto è firmato con la chiave GPG dell'azienda e arriva da un repository apt gestito da Anthropic, quindi gli aggiornamenti seguono il normale meccanismo di sistema, mentre Fedora e RHEL restano fuori con il supporto annunciato come futuro. [Fonte: raw/pillitteri/pillitteri20260630-claude-desktop-linux-beta-ubuntu-debian.md]
- **2026-06-30** — Rispetto al riconfezionamento della community, il progetto aaddrick/claude-desktop-debian con 5.192 stelle GitHub, la differenza è l'origine verificabile del software: firma ufficiale, repository mantenuto dall'azienda e update via apt, un requisito e non un dettaglio per chi lavora in ambienti regolamentati. [Fonte: raw/pillitteri/pillitteri20260630-claude-desktop-linux-beta-ubuntu-debian.md]
- **2026-06-30** — Nella beta mancano Computer Use (il controllo di app e schermo, indicato come in arrivo), la dettatura vocale e, su Wayland nativo, la scorciatoia globale Quick Entry, che richiede il portale GlobalShortcuts dell'ambiente desktop; per il coding puro la beta è invece già completa. [Fonte: raw/pillitteri/pillitteri20260630-claude-desktop-linux-beta-ubuntu-debian.md]
- **2026-10-15** — L'aggiornamento del 14 ottobre porta le sessioni annidate, in cui ogni task lanciato in parallelo diventa una sessione figlia che riporta il risultato nella principale, gli ambienti salvati con cartelle, host SSH o cloud e worktree per cartella, e una barra laterale che distingue le sessioni al lavoro da quelle in attesa di risposta. Completano il quadro il task chip per avviare separatamente il lavoro proposto da Claude, /btw per le domande laterali e le schede di to-do e recap; l'annuncio non indica il numero di versione, quindi la verifica è la schermata di nuova sessione che mostra le cartelle recenti. [Fonte: raw/pillitteri/pillitteri20261015-claude-code-desktop-sessioni-annidate-ambienti-salvati.md]




## Collegamenti

- [[anthropic]]
- [[claude]]
- [[claude-code]]
- [[claude-cowork]]
- [[index]]
