---
title: "CrashStealer"
category: strumento
tags: [malware, macos, infostealer, sicurezza]
related_puntate: []
created: 2026-09-25
updated: 2026-09-25
---

# CrashStealer

## Introduzione

Infostealer per macOS analizzato il 13 luglio 2026 da Jamf Threat Labs, a firma del ricercatore Thijs Xhaflaire, che si installa con il nome CrashReporter.app e ruba portachiavi, credenziali dei browser, wallet crypto e password manager. Il dropper che lo porta sul Mac è firmato e notarizzato da [[apple]], quindi Gatekeeper lo lascia passare senza mostrare un solo avviso.

## Funzionalità principali

- Il primo stadio è un file `.dmg` che contiene Werkbit.app, binario universale per Apple Silicon e Intel con bundle identifier `dev.golove.velto`, con hardening attivo, notarizzazione concessa con ticket allegato, Gatekeeper soddisfatto e firma verificata; il certificato è un Developer ID valido a nome di Emil Grigorov (WWB7JA7AQV).
- Werkbit.app non contiene il malware: chiama l'API di [[github|GitHub]] e scarica un file `sys.cache` dal repository `mgothiclove/pkeys`, dentro cui c'è un comando curl verso `endpoint-api-v1[.]com` in HTTP non cifrato.
- Lo script scompatta CrashReporter.dmg in una cartella nascosta sotto `/tmp`, gli toglie la firma originale e lo rifirma ad-hoc, poi lo avvia da `/private/tmp/.CrashReporter/`; la persistenza passa da un LaunchAgent `com.apple.crashreporter.helper` in `~/Library/LaunchAgents/`.
- La password del Mac non viene indovinata ma chiesta, con una finestra che imita la richiesta di autorizzazione di macOS, e viene validata in locale con `dscl -authonly`: se è sbagliata la finestra ricompare finché l'utente non digita quella giusta.
- I bersagli sono le credenziali di Safari, le password Wi-Fi, chiavi private, certificati e token del portachiavi, i dati di Chrome, Brave, Edge, Opera, Vivaldi, Chromium, NAVER Whale e Firefox, circa 80 estensioni di wallet crypto e 14 password manager tra cui 1Password, Bitwarden, LastPass, Dashlane, Keeper, KeePassXC e NordPass.
- I file raccolti vengono cifrati con AES-256-GCM prima di lasciare la macchina, con chiave derivata via PBKDF2-HMAC-SHA256 a 10.000 iterazioni su un salt fisso `panel_salt_v1`, e impacchettati in archivi `.zx_*.zip` divisi per categoria (`.brw_`, `.ext_`, `.sw_`).
- L'anti-analisi è curata: control-flow flattening con jump table, stringhe operative cifrate e decifrate a runtime, doppio anti-debugging con `sysctl KERN_PROC` più un controllo che termina il processo con exit code 45, tutto in C++ nativo.

## Casi d'uso

- Jamf ha intercettato un campione sospetto su VirusTotal all'inizio di maggio 2026, quando il progetto sembrava immaturo; a inizio luglio le regole interne hanno iniziato a segnalare rilevamenti reali su macchine di utenti.
- La distribuzione passa dal sito `werkbit[.]io`, registrato a fine giugno 2026, con il download protetto da un PIN da riunione: la vittima crede di installare un software di videoconferenza richiesto da un interlocutore, e il gating tiene lontani crawler e sandbox dei ricercatori.
- Gli indicatori pronti per le blocklist sono l'IP `179.43.166.242` e i domini `endpoint-api-v1[.]com`, `werkbit[.]io`, `cohezo[.]io`, `cohezo[.]com` e `cordinex[.]io`; le tracce che il malware non ripulisce sono il LaunchAgent, la cartella `~/.cache/com.apple.crashreporter/` e i file `.zx_*.zip`.
- La regola comportamentale che vale più di ogni indicatore: nessun software di videoconferenza ha bisogno della password di sistema per funzionare, quindi una finestra che la chiede fuori da un'azione appena avviata dall'utente va chiusa e verificata.

## Azienda / Autore

- Jamf Threat Labs, che ha pubblicato l'analisi tecnica; l'infrastruttura di comando e controllo espone un "Command Panel" su `endpoint-api-v1[.]com/login`.

## Timeline delle notizie

- **2026-07-15** — L'analisi di Jamf Threat Labs mostra che la notarizzazione di Apple non è un certificato di buona condotta: è una scansione automatica che certifica l'assenza di malware noto al momento del controllo, e un binario mai visto prima la supera senza problemi, mentre il Developer ID dice solo che dietro c'è un account registrato. La cifratura lato client è la scelta più significativa del progetto, perché chi cattura il traffico in uscita vede byte opachi.

## Collegamenti

- [[apple]]
- [[cybersicurezza]]
- [[github]]
- [[malware-slop]]
- [[mercato-dati-rubati]]
- [[sicurezza-ai]]
- [[index]]
