---
title: "WordPress"
category: strumento
tags: [cms, sicurezza, supply-chain, rce, plugin]
related_puntate: []
created: 2026-09-21
updated: 2026-10-06
---

# WordPress

## Introduzione

Piattaforma di gestione dei contenuti su cui gira circa il 43 per cento del web, stimato in 500 milioni di siti nel rapporto di pwn.ai: una quota che spiega perché ogni difetto del Core o dell'ecosistema dei plugin diventi un problema di scala. Nel 2026 quattro vicende diverse hanno mostrato i quattro punti deboli del sistema: il trasferimento di proprietà dei plugin, il Core stesso, il comportamento dei temi scaricati dal catalogo ufficiale e una chiamata di controllo mancante rimasta nel Core per quasi dieci anni.

## Funzionalità principali

- Il Core viene aggiornato automaticamente e, nei casi più gravi, WordPress.org attiva l'aggiornamento forzato su tutte le installazioni interessate: una misura che però non raggiunge i siti che hanno disabilitato del tutto gli aggiornamenti in background.
- Il Customizer carica il codice PHP di un tema anche quando a essere attivo è un altro, perché serve a mostrarne l'anteprima: un tema installato ma mai attivato non è un pacchetto morto, e i suoi hook ed endpoint possono girare dentro la sessione del pannello.
- Il codice di sicurezza che non deve mai essere disattivato per errore va scritto come must-use plugin, che non si può spegnere dalla bacheca come un plugin normale.

## Azienda / Autore

- WordPress.org Plugins Team

## Timeline delle notizie

- **2026-04-14** — Patchstack, TechCrunch e il Plugins Team confermano la vicenda Essential Plugin: tra il 2015 e il 2024 il portfolio di 31 plugin gratuiti con oltre 400.000 installazioni dichiarate era cresciuto fino a essere venduto su Flippa a fine 2024, quando il fatturato era calato del 35-45 per cento. L'acquirente, presentatosi come Kris e con un background in SEO e gambling marketing, ha pagato una cifra a sei zeri, ha ricevuto l'accesso SVN il 12 maggio 2025 e l'8 agosto 2025 ha pubblicato la versione 2.6.7 con changelog "Check compatibility with WordPress version 6.8.2" che nascondeva 191 righe di PHP, compresa una backdoor di deserializzazione.
- **2026-04-14** — La backdoor è rimasta dormiente per otto mesi e si è attivata il 5 e 6 aprile 2026 nella finestra 04:22-11:06 UTC, per circa sei ore e quarantaquattro minuti, distribuendo SEO spam visibile solo a Googlebot; il 7 aprile il Plugins Team ha chiuso permanentemente tutti e 31 i plugin. Il punto strutturale è che il trasferimento era perfettamente legale: WordPress.org non ha alcun meccanismo per rivedere il codice quando un plugin cambia proprietario, quindi chi compra eredita accesso SVN, reputazione e la fiducia implicita di tutti i siti con gli aggiornamenti automatici attivi.
- **2026-07-17** — Il progetto rilascia le versioni 7.0.2 e 6.9.5 e attiva l'aggiornamento automatico forzato per una catena di vulnerabilità battezzata wp2shell, CVE-2026-63030, che permette a un attaccante senza credenziali di eseguire codice sul server partendo da una singola richiesta HTTP anonima: non servono plugin né configurazioni particolari, un'installazione appena scaricata e mai toccata è sufficiente. La segnalazione arriva da Adam Kues di Assetnote, mentre la SQL injection che completa la catena è stata segnalata da tre ricercatori che firmano come TF1T, dtro e haongo.
- **2026-07-19** — Il PoC esplode: il repository Icex0/wp2shell-poc passa da 44 a 282 stelle e da 15 a 62 fork in poco più di ventiquattro ore, i progetti GitHub che citano wp2shell salgono da 14 a 46, Patchstack e watchTowr segnalano le prime attività di sfruttamento già la sera del 17 luglio e [[cloudflare]] blocca la catena dalle 17:03 UTC con due regole in azione Block, con il paradosso che i piani gratuiti sono protetti in automatico mentre su Pro, Business ed Enterprise le Managed Rules vanno verificate a mano.
- **2026-09-20** — Il 18 settembre il team pwn.ai divulga Click2Shell, la catena che parte da un indirizzo web e finisce con l'esecuzione di codice PHP sul server, chiusa da WordPress 7.1.1: tre falle diverse che da sole non portano all'esecuzione — un selettore jQuery non filtrato in wp-admin/js/theme.js che fa premere da solo il pulsante Installa con i cookie dell'amministratore, il caricamento del PHP di un tema non attivo tramite l'anteprima del Customizer e una falla in un tema di terze parti del catalogo ufficiale — e montate in sequenza fanno quello che il nome promette.
- **2026-09-20** — A differenza di wp2shell, Click2Shell richiede un amministratore già dentro al pannello che apra il link con la sessione aperta, e al 20 settembre non risultano sfruttamenti in attacchi reali. La segnalazione porta la firma di Paulos Yibelo e del team pwn.ai, il progetto ha riprodotto il problema sulla 7.1.0 il 22 agosto 2026 e ha pagato la taglia massima, 300 dollari: su un progetto open source che muove il 43 per cento del web è una cifra che dice molto sui budget del bug bounty.
- **2026-09-23** — Con la 7.1.2, rilasciata il 22 settembre, il Core chiude CVE-2026-87902, un attraversamento di percorso non autenticato nella risoluzione del template di una Pagina (CWE-98) che permette di includere un file PHP fuori dalla cartella del tema e, in certe condizioni, di eseguire codice sul server: il difetto è presente in tutte le versioni dalla 4.7 di fine 2016 fino alla 7.1.1. Il punteggio è 9,2 in CVSS 4.0 con vettore di rete, complessità bassa, nessun privilegio e nessuna interazione dell'utente, ma la sigla AT:P segnala che servono prerequisiti d'ambiente, ed è proprio la parte che l'allarme virale sui social ha omesso. La correzione aggiunge la chiamata mancante a validate_file() sulla variabile decodificata e un controllo di contenimento che obbliga ogni template a risolversi dentro le cartelle ammesse, quella dello stylesheet, quella del template e theme-compat.
- **2026-09-23** — Per arrivare all'esecuzione devono verificarsi insieme tre condizioni: una cartella di primo livello che comincia per page- nel tema attivo o in quello padre (l'advisory cita Twenty Twelve, Twenty Fourteen e temi diffusi come Neve, Hestia e Sydney), un file PHP leggibile dall'utente del web server come pearcmd.php di PEAR con register_argc_argv attivo (configurazione dell'immagine Docker ufficiale di PHP e di cPanel su PHP precedente alla 8.5), e almeno una Pagina pubblicata e raggiungibile senza login. La falla è stata segnalata il 20 luglio via HackerOne dal ricercatore Robert Ressl, la release è stata coordinata da John Blackbourn con oltre trenta collaboratori e la patch è stata riportata a tutti i rami ancora mantenuti fino alla 4.7; al 22 settembre non risultano sfruttamenti reali e la vulnerabilità non compare nel catalogo KEV del CISA, ma la prova di concetto è pubblica dal giorno dell'advisory e su GitHub gira già un template per lo scanner Nuclei. In poco più di due mesi il progetto ha chiuso tre falle serie, wp2shell a luglio, Click2Shell nei giorni scorsi e adesso questa.
- **2026-10-06** — La versione 0.7.0 di [[mcp-adapter]], il plugin ufficiale con cui WordPress collega la Abilities API (nel core dalla 6.9) al Model Context Protocol, è la prima pubblicata nella directory dei plugin di wordpress.org dopo oltre un anno di presenza solo su GitHub e Composer. Espone tre strumenti generali (scoperta, informazioni ed esecuzione delle abilities) sull'endpoint /wp-json/mcp/mcp-adapter-default-server, con trasporti HTTP e STDIO via WP-CLI, parla le revisioni MCP 2025-11-25 e 2026-07-28 e al 6 ottobre conta oltre 40.000 installazioni attive e 1.794 stelle su GitHub. Le abilities restano private finché non vengono marcate pubbliche, quindi il rischio si sposta sul permission_callback di ciascuna.




## Collegamenti

- [[attacco-supply-chain-npm]]
- [[cloudflare]]
- [[cybersicurezza]]
- [[brevo]]
- [[mcp-adapter]]
- [[index]]
