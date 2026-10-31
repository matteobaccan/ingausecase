---
title: "RemoveMacAI"
category: strumento
tags: [apple, macos, on-device, open-source, privacy]
related_puntate: []
created: 2026-10-06
updated: 2026-10-06
sources: [raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
---

# RemoveMacAI

## Introduzione

Strumento a riga di comando gratuito e open source con licenza MIT che su macOS 27 spegne Apple Intelligence, cancella dal disco circa 12 GB di modelli e impedisce al sistema di riscaricarli. Funziona solo sui Mac con chip Apple e si annulla con un comando, removemacai revert. Nasce da un problema preciso: con macOS 27 «Golden Gate», uscito il 14 settembre 2026, Apple ha tolto l'interruttore unico per Apple Intelligence e spegnere le singole funzioni non restituisce nemmeno un megabyte. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]

## Funzionalità principali

- **Spegne le funzioni**: un profilo di configurazione `.mobileconfig` imposta le chiavi di restrizione di Apple e forza le impostazioni che una chiave non ce l'hanno. Le funzioni spente sono tredici, dalle voci di Siri (compreso «Ehi Siri») a Writing Tools, Genmoji, Image Playground e l'estensione ChatGPT, poi i riassunti in Mail, Messaggi, Safari, Note e notifiche, le risposte intelligenti, le previsioni di testo, le Foto spaziali, Pulizia in Foto e il completamento del codice in Xcode. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- **Cancella i modelli**: chiede al servizio di asset di Apple (il componente di sistema che si occupa dei modelli) di azzerare cinque gruppi di file, base, immagini con Genmoji, Foto spaziali, Pulizia in Foto e Xcode. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- **Impedisce il ritorno**: lo stesso profilo dirotta ogni download verso 127.0.0.1 sulla porta 9, un indirizzo locale dove nessuno ascolta, quindi il download fallisce. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- **Resta dentro i limiti di sistema**: la protezione dell'integrità di sistema resta accesa e nessun file sotto /System viene toccato direttamente; il profilo non si installa da solo, perché il tool apre Impostazioni di Sistema e aspetta che sia l'utente ad approvarlo. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- **Cosa si perde**: oltre alle funzioni spente, smettono di lavorare le app che usano i modelli di Apple sul dispositivo (il framework Foundation Models e l'azione «Usa modello» di Comandi Rapidi), Visual Intelligence e la modifica in linguaggio naturale di Calendario; la dettatura resta, perché ha modelli vocali a parte. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]

## Installazione e uso

- Installazione e anteprima: `brew install omlahore/tap/removemacai`, poi `removemacai off --dry-run` per vedere cosa cambierebbe senza applicare nulla. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- Applicazione e ritorno: `removemacai` chiede conferma e apre Impostazioni di Sistema, `removemacai revert` rimuove il profilo e ripristina le impostazioni precedenti. A mano si elimina il profilo «RemoveMacAI» da Impostazioni di Sistema oppure con `sudo profiles remove -identifier io.github.omlahore.removemacai`. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- Selezione delle funzioni: `removemacai features` stampa i nomi accettati e `--keep` salva quelle indicate, per esempio `removemacai off --keep spatial-photos,photos-clean-up`; `removemacai status` mostra le dimensioni dei modelli e cosa il servizio considera presente senza cambiare nulla. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- Requisiti: Mac con chip Apple e macOS 27; la versione provata è la 27.0, sulla 27.0.1 serve la release 0.2.3 o successiva e l'ultima è la 0.2.5 del 5 ottobre, mentre sotto macOS 26 il tool non è supportato. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]

## Repository

- omlahore/RemoveMacAI su GitHub, creato il 29 settembre 2026, licenza MIT: al 5 ottobre conta 2.302 stelle e 51 fork, con cinque segnalazioni aperte. Nove file in Swift più un frammento di Objective-C per circa 48 KB, senza alcuna chiamata di rete. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]

## Azienda/autore

- Om Lahore, sviluppatore indipendente (su Reddit firma i post come checkpointdev). Le chiavi e i gruppi di modelli di macOS 27 erano stati mappati per primo dal progetto pared, altro progetto MIT nato il 22 settembre e citato dal README. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]

## Limiti e avvertenze

- Per cancellare i modelli il tool carica il framework privato UnifiedAssetFramework e parla con il servizio com.apple.siri.uaf.subscription.service, dove chiede l'operazione ResetAssetSets: sono interfacce che Apple non documenta e che possono cambiare con qualsiasi aggiornamento, e le sei release in una settimana dicono che la fragilità è reale. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- Il progetto ha di fatto un solo autore e una vita brevissima; le chiavi di configurazione usate erano già in parte deprecate in macOS 26.4, quindi dopo ogni aggiornamento maggiore conviene rilanciare `removemacai status`. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]
- Lo script `curl ... | bash` dell'installer resta la via che molti preferiscono evitare; il README indica Homebrew come alternativa e la verifica di provenienza `gh attestation verify removemacai-darwin-arm64.tar.gz -R omlahore/RemoveMacAI`. Su un Mac aziendale i profili di configurazione li decide di norma il reparto IT. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]

## Timeline delle notizie

- **2026-10-06** — RemoveMacAI, tool a riga di comando open source con licenza MIT, spegne Apple Intelligence su macOS 27, cancella circa 12 GB di modelli e impedisce al sistema di riscaricarli, in risposta all'interruttore unico che Apple ha tolto con Golden Gate. Il repository omlahore/RemoveMacAI è stato creato il 29 settembre 2026 e al 5 ottobre conta 2.302 stelle e 51 fork, con un solo autore e sei release in una settimana. Il tool usa il framework privato UnifiedAssetFramework e il servizio com.apple.siri.uaf.subscription.service, quindi può rompersi a ogni aggiornamento di macOS. [Fonte: raw/pillitteri/pillitteri20261006-removemacai-disattivare-apple-intelligence-macos-27.md]

## Collegamenti

- [[apple]]
- [[apple-intelligence]]
- [[siri-ai]]
- [[privacy-online]]
- [[index]]
