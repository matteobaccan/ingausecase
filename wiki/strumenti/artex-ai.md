---
title: "ARTEX AI"
category: strumento
tags: [cybersecurity, agenti, open-source, pentest, cina]
related_puntate: []
created: 2026-10-06
updated: 2026-10-31
sources: [raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md, raw/pillitteri/pillitteri20261022-artex-ai-giappone-gmo-aziende.md, raw/pillitteri/pillitteri20261026-connectwise-cloud-backup-violato-tenant-microsoft-365.md, raw/controrumore/controrumore20261031-diario-ai-agenti-mercati-e-nuove.md]
---

# ARTEX AI

## Introduzione

Sistema open source di penetration test autonomo costruito su modelli linguistici con un'architettura multi-agente: cerca i bersagli, individua le vulnerabilità, pianifica il percorso d'attacco, lancia gli strumenti di sicurezza e verifica da solo i risultati. Il progetto è su GitHub dal 26 luglio 2026, pubblicato dall'account Autumn-27 con licenza AGPL-3.0 e descrizione in cinese, ed è indicato come il vincitore della sfida «Agent+» del Baidu Security Response Center su circa 150 squadre. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]

## Funzionalità principali

- Ciclo d'attacco autonomo: ricerca dei bersagli, individuazione delle vulnerabilità, pianificazione del percorso, lancio degli strumenti di sicurezza e verifica dei risultati senza un operatore che guidi ogni passaggio. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- Architettura multi-agente sopra modelli linguistici, con il ciclo sopra descritto ripetuto fino a esaurimento delle ipotesi. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- La descrizione del repository è in cinese (AI 自主渗透测试系统, «sistema di penetration test autonomo») e la licenza è AGPL-3.0. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]

## Casi d'uso

- Test di sicurezza autorizzati sui propri sistemi o su quelli di un cliente, che è lo scopo dichiarato di un tool di penetration test. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- Uso offensivo documentato: secondo la stampa coreana è stato usato contro almeno sette istituti finanziari sudcoreani — Shinhan, KB Kookmin, Hana, BNK Busan, Yegaram Savings Bank, Welcome Savings Bank e Hyundai Capital — tra fine settembre e i primi di ottobre 2026, con i dati di circa 68.000 persone portati via (nomi, telefoni, numero di registrazione del residente, reddito annuo e plafond del prestito). [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- Il tempo di rilevamento conta più del resto: Shinhan se n'è accorta dopo 15 ore, Hana dopo 41 e KB Kookmin dopo 67, mentre le tre banche insieme avevano speso 124 miliardi di won (circa 92 milioni di dollari) in sicurezza l'anno precedente. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- Il punto d'ingresso sono stati i sistemi ai margini — portali per dipendenti e intermediari, reti degli appaltatori — non il cuore dei pagamenti, e nessuna delle ricostruzioni descrive una vulnerabilità inedita: la novità sta nella velocità e nella scala di un agente che prova e riprova senza stancarsi. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]

## Repository

- Account Autumn-27 su GitHub dal 26 luglio 2026, licenza AGPL-3.0: al 6 ottobre 2026 il repository conta 1.655 stelle e 376 fork. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- La traccia dell'uso è arrivata il 2 ottobre dalla stringa «ARTEX, console di penetration test autonomo» letta da Moon Jong-hyun del Genians Security Center nel titolo HTML di server collegati ad attacchi di credential stuffing, e poi confermata dal Korea Financial Security Institute rifacendo il percorso dai log di Shinhan e dagli indirizzi IP degli aggressori. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]

## Azienda / autore

- Autore indicato come Autumn-27, vincitore secondo la stampa coreana della sfida «Agent+» del Baidu Security Response Center. Un funzionario di governo, citato dall'Herald Business, ha chiarito che l'AI è stata usata ma non ha agito da sola: «Un hacker ha usato l'AI come strumento». [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]

## Limiti e avvertenze

- Usare il tool contro sistemi altrui senza permesso configura un accesso abusivo a sistema informatico, che in Italia è reato (articolo 615-ter del codice penale); la licenza AGPL-3.0 non cambia il perimetro d'uso legittimo. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- Un tool con la documentazione in cinese dice quale software è stato usato e poco altro: la Financial Supervisory Service ha mappato 33 indirizzi IP (28 unici) in 12 paesi, con il gruppo più numeroso negli Stati Uniti e presenze anche in Giappone, Hong Kong, Singapore, Vietnam, Thailandia, Malaysia, Spagna, Lettonia e Svezia, e Park Sang-won del Financial Security Institute ha spiegato che è impossibile risalire a chi sono partendo dal solo indirizzo. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- Il termine di paragone più vicino è il caso Gambit Security, dove tre framework già pronti e modelli commerciali avevano portato la spesa media a 25,46 dollari per bersaglio: il costo di una prova scende vicino a zero e un buco che prima restava aperto per anni tende a essere trovato in pochi giorni. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]

## Timeline delle notizie

- **2026-10-06** — Hacker non identificati hanno violato almeno sette istituti finanziari sudcoreani tra fine settembre e i primi di ottobre 2026 usando ARTEX AI, tool cinese open source di penetration test autonomo, portando via i dati di circa 68.000 persone; il Korea Financial Security Institute ha confermato l'uso del tool ricostruendolo dai log della Shinhan e dagli indirizzi IP degli aggressori. Un funzionario di governo ha precisato che l'AI è stata usata come strumento da un hacker e non ha agito da sola, mentre la Financial Supervisory Service ha girato a circa 500 aziende l'elenco degli indirizzi sospetti imponendo controlli d'emergenza e il presidente Lee Jae Myung ha ordinato un'indagine. Al 6 ottobre il repository conta 1.655 stelle e 376 fork. [Fonte: raw/pillitteri/pillitteri20261006-artex-ai-attacco-banche-sudcoreane.md]
- **2026-10-22** — GMO Cybersecurity by Ierae conferma che ARTEX compare nell'infrastruttura usata contro circa 20 aziende giapponesi, nove delle quali nello stesso settore: otto hanno annunciato fughe di dati tra settembre e ottobre, ma la società non dimostra che tutte e venti siano state violate. Sugli altri sei server citati nel rapporto non è confermato l'uso di ARTEX, e i modelli indicati da CrowdStrike per la Corea (DeepSeek v4.1-flash, GLM-5.3, Grok 4.6 e Claude Code) non risultano legati ai casi giapponesi. [Fonte: raw/pillitteri/pillitteri20261022-artex-ai-giappone-gmo-aziende.md]
- **2026-10-26** — Microsoft attribuisce a Storm-0940 l'abuso di questo framework, in uso dall'inizio di settembre 2026, nell'attacco a ConnectWise e nei tentativi su oltre 2.250 tenant Microsoft 365 condotti con le identità applicative rubate: nel rapporto del 21 ottobre il gruppo è passato in più casi dal primo contatto ai privilegi elevati in meno di tre ore. Lo strumento lascia scegliere qualsiasi modello collegato, altri gruppi lo usano in varie parti del mondo e vederlo nei log non basta a indicare l'autore. [Fonte: raw/pillitteri/pillitteri20261026-connectwise-cloud-backup-violato-tenant-microsoft-365.md]
- **2026-10-31** — CrowdStrike attribuisce a un operatore associato a VAPOR PANDA una campagna condotta dal 17 ottobre con questo agente open source, DeepSeek e un altro modello commerciale contro oltre 200 organizzazioni in almeno 14 Paesi, con accessi successivi allo sfruttamento confermati in nove organizzazioni e l'uso di una backdoor. Il framework lascia scegliere qualsiasi modello collegato e i conteggi vengono dall'analisi della sola CrowdStrike. [Fonte: raw/controrumore/controrumore20261031-diario-ai-agenti-mercati-e-nuove.md]










## Collegamenti

- [[cybersicurezza]]
- [[agenti-ai]]
- [[bug-hunting-ai]]
- [[deepseek]]
- [[index]]
