---
title: "TanStack"
category: azienda
tags: [tanstack, usa, javascript, open-source, sicurezza, supply-chain]
related_puntate: [20260514, 20260521]
created: 2026-08-12
updated: 2026-09-21
sources: [raw/puntate/ainews20260514.md, raw/puntate/ainews20260521.md, raw/pillitteri/pillitteri20260516-tanstack-npm-supply-chain-openai-2026.md]
---

# TanStack

## Introduzione

Ecosistema open source di librerie JavaScript usate in milioni di app web, vittima di un attacco supply chain a maggio 2026.

## Timeline delle notizie

- **2026-05-14** — TanStack è stato hackerato lunedì 11 maggio: un'installazione rubava password, chiavi e credenziali sul computer; la libreria è usata in milioni di app web; protezione urgente con cooldown di 7 giorni su npm, pin delle dipendenze, lock dei token API, audit delle estensioni IDE e monitoring continuo; chi ha installato pacchetti '@tanstack/*' tra le 19:20 e le 19:30 UTC di lunedì 11 maggio deve considerare il sistema compromesso e ruotare ogni credenziale. [Fonte: raw/puntate/ainews20260514.md]
- **2026-05-21** — TanStack è stata avvelenata da TeamPCP a maggio, nell'ambito della supply chain attack a catena su npm e PyPI. [Fonte: raw/puntate/ainews20260521.md]
- **2026-05-16** — L'11 maggio 2026, in una finestra di soli sei minuti tra le 19:20 e le 19:26 UTC, vengono pubblicate 84 versioni malevole di 42 pacchetti npm del progetto: il lasso di tempo basta per colpire due dispositivi interni di [[openai]], che avvia una rotazione completa dei certificati di firma delle applicazioni macOS e chiede di aggiornare [[chatgpt]], [[codex]] e Atlas entro il 12 giugno, chiarindo che nessun dato utente è stato esposto e che il codice dei prodotti non è stato modificato. [Fonte: raw/pillitteri/pillitteri20260516-tanstack-npm-supply-chain-openai-2026.md]
- **2026-05-16** — L'attacco non ruba credenziali nel senso tradizionale: il 10 maggio un account malevolo crea un fork del repository e apre una pull request con un payload JavaScript offuscato da circa 30.000 righe, che attiva un workflow di GitHub Actions configurato con pull_request_target, il meccanismo che se mal configurato esegue codice da fork esterni con i privilegi del repository principale, noto come Pwn Request. Attraverso il cache poisoning la cache condivisa delle dipendenze viene sovrascritta, e quando i workflow di rilascio ufficiali girano ore dopo eseguono il codice dell'attaccante, che estrae un token OIDC dalla memoria del processo e pubblica direttamente le versioni malevole su npm aggirando i controlli di autorizzazione. [Fonte: raw/pillitteri/pillitteri20260516-tanstack-npm-supply-chain-openai-2026.md]
- **2026-05-16** — I pacchetti della famiglia @tanstack/query*, table*, form*, virtual* e store* non sono stati colpiti: solo il monorepo Router/Start è stato compromesso. Il team ha deprecato tutte e 84 le versioni entro un'ora e quarantatré minuti dalla pubblicazione e npm ha rimosso i tarball in circa due ore e ventisette, grazie anche a ricercatori esterni che hanno individuato la compromissione entro venti-ventisei minuti. L'operazione è attribuita al gruppo TeamPCP, lo stesso collettivo che il 20 maggio 2026 ha esfiltrato 3.800 repository interni di GitHub via un'estensione VS Code malevola, ed è battezzata Mini Shai-Hulud. [Fonte: raw/pillitteri/pillitteri20260516-tanstack-npm-supply-chain-openai-2026.md]

## Collegamenti

- [[teampcp]]
- [[index]]

