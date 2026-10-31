---
title: "cleanyourtv"
category: strumento
tags: [android-tv, debloat, open-source, mit, privacy, claude-code]
related_puntate: []
created: 2026-10-20
updated: 2026-10-25
sources: [raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md, raw/pillitteri/pillitteri20261025-claude-opus-5-5-blocca-reverse-engineering-smart-tv.md]
---

# cleanyourtv

## Introduzione

Progetto open source con licenza MIT che fa disattivare a un assistente di programmazione come [[claude-code]] le app pubblicitarie e i servizi di tracciamento preinstallati su una TV con Android TV o Google TV: lavora dal computer via Wi-Fi, senza root e senza cancellare nulla, e al posto della Home piena di annunci installa una schermata pulita da 300 KB. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]

## Funzionalità principali

- Il flusso è in tre mosse: salva l'elenco dei pacchetti installati e delle impostazioni, disattiva con `pm disable-user` i servizi di telemetria e pubblicità, poi installa un launcher nativo e lo imposta come Home predefinita. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]
- Nulla viene disinstallato: ogni pacchetto resta sulla TV e si può riaccendere, dallo script di ripristino o dal menu Impostazioni → App. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]
- Il launcher è scritto in Java semplice, senza sfocature né servizi in background, perché deve girare su TV con 1 GB di memoria. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]
- Funziona su Android TV e Google TV in forma completa, solo come debloat su Fire TV; Samsung (Tizen) e LG (webOS) restano fuori. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]

## Installazione e uso

- Il repository non pubblica APK precompilati: si clona il progetto, si passa il file `PROMPT.md` all'assistente indicando il modello della TV e il launcher si costruisce sul computer, con Python 3, JDK 17 e Android SDK 34. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]
- Servono una TV con Android TV o Google TV, le opzioni sviluppatore con debug USB e di rete attivi e un computer sulla stessa rete Wi-Fi; a lavoro finito il debug va spento, perché l'ADB di rete viaggia in chiaro sulla porta 5555. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]
- Chi non vuole usare un assistente trova nel repository gli script Python e i file di shell per applicare e annullare un elenco a mano. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]

## Repository

- Il 20 ottobre 2026, tre giorni dopo la pubblicazione, il repository contava 6.976 stelle e 810 fork, con 80 elenchi di pacchetti per 28 marchi. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]

## Casi d'uso

- Nasce da una Xiaomi che mostrava un annuncio sponsorizzato prima di Netflix: l'assistente ha trovato la TV sulla rete, disattivato 25 pacchetti Xiaomi e scritto una Home nuova, mentre il metodo era stato descritto prima da Mert Cobanov per una Android TV lenta. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]

## Modelli supportati

- Qualunque assistente di programmazione con accesso alla shell; Claude Code è l'esempio citato dal progetto. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]

## Timeline delle notizie

- **2026-10-20** — Il progetto cleanyourtv, nato dal post di Gathin del 17 ottobre e ribattezzato il 19, raccoglie 6.976 stelle in tre giorni: disattiva app pubblicitarie e telemetria su Android TV e Google TV via ADB e sostituisce la Home con un launcher da 300 KB, senza root e senza disinstallare nulla. [Fonte: raw/pillitteri/pillitteri20261020-togli-pubblicita-smart-tv-claude-code-cleanyourtv.md]
- **2026-10-25** — Il progetto supera le 10.700 stelle su GitHub al 20 ottobre e copre TV Android e Google TV di Sony, TCL, Hisense, Philips e Xiaomi, con 107 modelli di 37 marchi nelle configurazioni testate. Le segnalazioni di rifiuti di Claude riguardano il root e il reverse engineering, non il debloat via ADB senza privilegi di amministratore. [Fonte: raw/pillitteri/pillitteri20261025-claude-opus-5-5-blocca-reverse-engineering-smart-tv.md]




## Collegamenti

- [[claude-code]]
- [[xiaomi]]
- [[privacy-online]]
- [[index]]
