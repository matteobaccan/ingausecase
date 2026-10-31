---
title: "TightVNC"
category: strumento
tags: [controllo-remoto, vnc, sicurezza, open-source]
related_puntate: []
created: 2026-10-29
updated: 2026-10-29
---

# TightVNC

## Introduzione

Programma gratuito per il controllo remoto di un computer, sviluppato da GlavSoft e distribuito anche con licenza GNU GPL. Usa il protocollo VNC (Virtual Network Computing) e si divide in due componenti: il Server, installato sul PC da controllare, e il Viewer, la finestra con cui il tecnico vede e comanda quel PC. Lo usano soprattutto helpdesk, sistemisti e piccoli fornitori IT che assistono i clienti senza pagare licenze come quelle di TeamViewer o AnyDesk.

## Sicurezza

- La falla del 2026 riguarda solo il Viewer: sta nel codice che riceve e disegna lo schermo remoto. Il Server della 2.8.88 aveva comunque ricevuto altre correzioni di stabilità.
- In modalità di ascolto (tvnviewer.exe -listen, porta 5500 su tutte le interfacce) il Viewer è un servizio esposto: da limitare agli indirizzi noti, far passare da una VPN o chiudere a fine sessione.
- Le correzioni che non ottengono un codice CVE restano invisibili agli scanner aziendali come Nessus, Qualys o Defender Vulnerability Management, che lavorano su quei codici: l'inventario delle versioni va fatto a mano.

## Timeline delle notizie

- **2026-10-29** — SSD Secure Disclosure ha pubblicato i dettagli di una vulnerabilità RCE pre-autenticazione nella versione 2.8.88 del Viewer per Windows a 64 bit: il server dichiara dimensioni di schermo enormi, il calcolo della dimensione del framebuffer viene troncato a 32 bit da FrameBuffer::getBufferSize() e gli aggiornamenti di schermo scrivono fuori dal buffer, portando all'esecuzione di codice con i privilegi dell'utente. Il server malevolo può dichiarare sicurezza «None», quindi la password non protegge il tecnico; la falla è stata trovata da SeongJoon Cho di SSD Labs Korea.
- **2026-10-29** — La correzione è nella 2.8.89 del 2 ottobre, arrivata senza bollettino, senza credito al ricercatore e senza codice CVE, con i ricercatori che dicono di non aver mai ricevuto risposta da GlavSoft; sul ramo 2 la versione consigliata è la 2.8.90 del 5 ottobre, che chiude anche un overrun nel decodificatore Tight, mentre sul ramo 4 la base gratuita è la 4.0.2 del 28 ottobre e il piano Pro da un dollaro al mese aggiunge la cifratura TLS 1.3.

## Collegamenti

- [[cybersicurezza]]
- [[index]]
