---
title: "rizzo-pii"
category: modello
tags: [anonimizzazione, italiano, open-source, privacy, pii]
related_puntate: []
created: 2026-09-18
updated: 2026-10-02
---

# rizzo-pii

## Introduzione

Modello open source da circa 300 milioni di parametri che riconosce e maschera i dati personali nei testi italiani direttamente sul computer dell'utente, pubblicato il 30 luglio 2026 da Simone Rizzo, ingegnere AI e docente a contratto all'Università di Bologna: il repository GitHub è stato aperto il 28 giugno 2026 e le release desktop per Windows, macOS e Linux hanno superato gli 870 download.

## Capacità

- Riconosce 22 categorie di dati personali, comprese quelle legali italiane: codice fiscale, partita IVA e dati catastali sono i cinque tag che nessun altro modello aperto copre.
- Verifica i checksum di IBAN, codice fiscale, partita IVA e carte di credito, così il riconoscimento passa da probabilistico a matematicamente verificabile.
- Pseudonimizzazione reversibile con dizionario locale: tre passaggi dei quattro girano in locale, uno solo nel cloud.

## Performance

- 0,989 di micro-F1 su 7.000 frasi reali italiane, con punteggio pieno (1.000) su codice fiscale, partita IVA e dati catastali.
- Addestramento su 745.000 righe e validazione su 7.000 frasi reali.

## Disponibilità

- Il sorgente su GitHub è sotto licenza MIT; i pacchetti pronti nelle release (.exe, .dmg, .deb, .AppImage) e l'immagine Docker sono sotto AGPL-3.0, perché incorporano PyMuPDF, la libreria che esegue la redazione dei PDF. Chi mette il servizio Docker in ascolto sulla rete ricade nell'articolo 13 dell'AGPL.

## Limiti

- Solo l'italiano è validato: le altre sette lingue sono nell'addestramento ma non certificate da benchmark.
- Il tag FULLNAME compare circa 97 volte più spesso del numero di carta di credito, e le classi rare pagano lo sbilanciamento.
- A settembre 2026 il repository ha superato le 1.000 stelle e 71 fork, con 4.437 download del modello in trenta giorni, ma l'ultimo commit resta l'8 agosto 2026: chi lo porta in produzione adotta un progetto in pausa.

## Azienda/autore

- Simone Rizzo, autore del modello e docente a contratto all'Università di Bologna.

## Timeline delle notizie

- **2026-07-30** — rizzo-pii è un modello open source da circa 300 milioni di parametri che riconosce e maschera i dati personali nei testi italiani in locale: 22 categorie, cinque identificativi dello studio professionale italiano che nessun altro modello aperto copre, 0,989 di micro-F1 su 7.000 frasi reali e punteggio pieno su codice fiscale, partita IVA e dati catastali, con verifica dei checksum su IBAN e carte.
- **2026-09-18** — Dopo la 2.0.0 dell'8 agosto 2026 il progetto si è fermato: il repository ha superato le 1.000 stelle e 71 fork ma non registra commit da oltre un mese, con 55 segnalazioni e 29 pull request non integrate, e sono comparsi i primi fork di comunità (Danleo93, casungo, atasc) che ricompilano il pacchetto per conto proprio. Il sorgente resta MIT mentre i pacchetti delle release e l'immagine Docker sono AGPL-3.0 perché incorporano PyMuPDF.
- **2026-10-02** — Rizzo-PII è indicato come la soluzione in locale per l'anonimizzazione dei dati prima di incollarli in un chatbot: modello italiano open source da circa 300 milioni di parametri, pensato apposta per riconoscere e mascherare i dati personali nei testi in italiano e per girare interamente sul computer dell'utente senza connessione di rete, così il testo non lascia mai la macchina. Regge meglio di un tool da browser il carico di PDF, scansioni e volumi alti di documenti.




## Collegamenti

- [[open-source]]
- [[pii-tracer]]
- [[privacy-filter]]
- [[index]]
