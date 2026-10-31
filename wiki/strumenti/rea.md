---
title: "REA"
category: strumento
tags: [agent, mcp, open-source, reverse-engineering]
related_puntate: [20261010, 20261011, 20261020]
created: 2026-10-11
updated: 2026-10-20
---

# REA

## Introduzione

REA (Reverse Engineer Anything) è uno strumento open source che analizza binari nativi, app Electron, assembly .NET e firmware e ne restituisce pseudocodice C e logica interna.

## Funzionalità principali

- Usa Ghidra, Hopper o IDA come motori di analisi.
- Espone un server MCP completo per [[claude-code]] e altri agenti.
- Ha circa 29.900 stelle su GitHub.

## Timeline delle notizie

- **2026-10-10** — REA analizza binari nativi, app Electron, assembly .NET e firmware con Ghidra, Hopper o IDA e restituisce pseudocodice C e logica interna, con MCP completo per gli agenti: 29,9 mila stelle su GitHub.
- **2026-10-11** — REA supera le cinquantottomila stelle su GitHub: collega strumenti di analisi binaria a Claude Code, Codex e Cursor, ispeziona software senza codice sorgente e ricostruisce funzionalità nel progetto dell'utente, coprendo programmi nativi, Electron, APK Android, firmware e contratti Ethereum; un utente ha ricreato una funzione audio del gioco DX-Ball del 1996, validata su tremiladuecentocinque test.
- **2026-10-14** — Il repository morluto/rea, nato il 14 aprile 2026, arriva a 234.477 stelle e 58.512 fork, con il pacchetto npm rea-agents alla versione 6.5.0 e 231.579 installazioni nella sola settimana dal 6 al 12 ottobre; il progetto è in licenza MIT, conta 30 contributor e il disclaimer esclude esplicitamente l'aggiramento di DRM, controlli di licenza e anti-cheat. Le stelle misurano l'attenzione e non la qualità: nessuno può dire quante vengano da lettori reali, e il resto del quadro è fatto di pseudocodice e prove citate, non di codice sorgente originale ricostruito.

- **2026-10-14** — Il 13 ottobre una copia del repository ospitata sotto l'organizzazione rea-tools ricalca il README e aggiunge un «Windows Standalone .exe»: l'archivio da 82,6 MB presentato come release 6.3.0 viene classificato da Microsoft Defender come trojan della famiglia Wacatac e da 8 motori su 45 su VirusTotal come dropper, ed è stato scaricato 172 volte prima della segnalazione. Il README ufficiale ora invita a scaricare REA solo da github.com/morluto/rea, dal sito rea.tools o dal pacchetto npm, e il setup dell'agente registra il server REA nella configurazione di Claude Code e copia la skill in ~/.claude/skills, dove tutti i progetti aperti da quel momento possono chiamarlo.
- **2026-10-20** — REA analizza un software, ne ricostruisce il funzionamento, genera una specifica, rigenera il codice e verifica il comportamento rispetto all'originale, collegandosi a Claude Code e Codex via MCP.










## Collegamenti

- [[claude-code]]
- [[leanrea]]
- [[mcp]]
- [[index]]
- [[sicurezza-supply-chain]]
