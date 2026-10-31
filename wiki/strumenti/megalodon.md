---
title: "Megalodon"
category: strumento
tags: [malware, supply-chain, github, ci-cd, sicurezza]
related_puntate: []
created: 2026-09-25
updated: 2026-09-25
---

# Megalodon

## Introduzione

Campagna automatizzata che il 18 maggio 2026, tra le 11:36 e le 17:48 UTC, ha spinto 5.718 commit malevoli in 5.561 repository GitHub distinti, iniettando in ognuno un workflow GitHub Actions per esfiltrare segreti CI/CD, credenziali cloud e chiavi SSH verso un server di comando e controllo. L'evento è stato documentato da SafeDep con il motore di analisi della supply chain Malysis e da OX Security.

## Funzionalità principali

- Account GitHub temporanei con username casuali di otto caratteri hanno pubblicato i commit firmati con quattro identità ricorrenti scelte per somigliare a bot di automazione interna: build-bot, auto-ci, ci-bot e pipeline-bot, con le email build-system@noreply.dev e ci-bot@automated.dev.
- La variante SysDiag aggiunge un file `.github/workflows/ci.yml` attivato su ogni push e su `pull_request_target`, quindi con i segreti del repository anche quando la pull request arriva da un fork esterno.
- La variante Optimize-Build sostituisce i workflow esistenti usando il trigger `workflow_dispatch`, e resta dormiente finché l'attaccante non la invoca a mano con le credenziali API di un account ancora valido.
- Entrambe richiedono i permessi `id-token: write` e `actions: read`, e il primo consente di chiedere token OIDC validi per impersonare il runner verso AWS, Google Cloud o Azure.
- Il payload è uno script bash da 111 righe che raccoglie tutte le variabili d'ambiente CI/CD (anche da `/proc/*/environ`), le credenziali AWS di ogni profilo, i token GCP, i metadata server AWS/GCP/Azure, le chiavi SSH private, `.npmrc`, `.netrc`, kubeconfig, token Vault e Terraform Cloud, oltre a oltre trenta pattern regex di chiavi API e stringhe di connessione.
- L'esfiltrazione avviene in POST HTTPS verso `216.126.225.129:8443` con la stringa megalodon come parametro identificativo; bloccare quell'indirizzo in egress è il primo contenimento raccomandato da SafeDep.

## Casi d'uso

- Il caso Tiledesk mostra la propagazione lato pacchetti: il commit malevolo è atterrato nel repository tiledesk-server fra altri otto repository dell'organizzazione, e nei giorni successivi il manutentore ignaro ha pubblicato su npm le versioni 2.18.6-2.18.12 del pacchetto tra il 19 e il 21 maggio, distribuendo il payload a tutti i progetti downstream.
- Le firme di ricerca suggerite sono tre: commit degli ultimi trenta giorni attribuiti alle quattro identità bot, workflow che contengono insieme `id-token: write` e il prefisso base64 fisso dell'IoC SafeDep, e connessioni in uscita verso l'indirizzo del C2.
- La contromisura strutturale è il minimo privilegio: `permissions: { contents: read }` come default di organizzazione, nessun segreto ai workflow che eseguono codice di fork esterni e azioni fissate a uno SHA di commit immutabile invece che a un tag.

## Azienda / Autore

- SafeDep, che ha documentato la campagna con il motore Malysis e ha pubblicato la targeting list del payload; OX Security, con un report autonomo sul caso.
- Il caso è una delle quattro ondate supply chain di maggio 2026: la campagna Mini Shai-Hulud aveva compromesso oltre 170 pacchetti npm e PyPI con 404 versioni malevole, e il 19-20 maggio il gruppo [[teampcp]] ha colpito GitHub con un'estensione VS Code avvelenata esfiltrando circa 3.800 repository interni.

## Timeline delle notizie

- **2026-05-22** — SafeDep e OX Security rendono pubblica Megalodon, la campagna che in sei ore ha backdoorato 5.561 repository GitHub con workflow malevoli: circa quindici nuovi commit malevoli al minuto, account temporanei con identità di bot interni e un payload bash da 111 righe che esfiltra credenziali cloud e segreti CI/CD verso un C2. Al momento della pubblicazione GitHub non aveva rilasciato una nota ufficiale, ma aveva rimosso gli account fittizi e bloccato i due indirizzi email usati; l'unico pacchetto npm confermato come propagazione è `@tiledesk/tiledesk-server` nelle versioni dalla 2.18.6 alla 2.18.12. SafeDep tratta Megalodon come operativamente distinta da Mini Shai-Hulud, che usa un worm autopropagante mentre qui l'iniezione è massiva e senza autopropagazione.

## Collegamenti

- [[attacco-supply-chain-npm]]
- [[cybersicurezza]]
- [[github]]
- [[nx-console]]
- [[sicurezza-supply-chain]]
- [[tanstack]]
- [[teampcp]]
- [[index]]
