---
title: "Disinformazione AI"
category: trend
tags: [disinformazione, geopolitica, influenza, openai, sicurezza]
related_puntate: []
created: 2026-09-27
updated: 2026-10-30
sources: [raw/pillitteri/pillitteri20260826-openai-rete-russa-chatgpt-cremlino.md, raw/pillitteri/pillitteri20260928-bixonimania-malattia-finta-ai.md, raw/pillitteri/pillitteri20260930-newsguard-russia-imita-bbc-euronews-disinformazione.md, raw/controrumore/controrumore20261010-diario-ai-lai-decide-ma-chi-ne-risponde.md, raw/controrumore/controrumore20261024-diario-ai-sicurezza-regole-e-nuovi.md, raw/controrumore/controrumore20261030-diario-ai-fiducia-denaro-e-controlli.md]
---

# Disinformazione AI

## Introduzione

Operazioni di influenza in cui l'AI è l'ingranaggio, non il prodotto: reti di account e siti costruiti per fabbricare l'apparenza di un'autorità accademica e diffondere narrazioni politiche, smascherate dai laboratori di threat intelligence. Il tratto comune è che l'inganno non sta nel testo generato ma nell'infrastruttura che il testo serve a promuovere.

## Attori coinvolti

- [[openai]]
- [[deepfake]]
- [[sicurezza-ai]]

## Timeline delle notizie

- **2026-08-26** — Il 25 agosto 2026 OpenAI bandisce un gruppo di account ChatGPT quasi certamente gestiti dalla Russia, usati per gonfiare il finto centro studi International Burke Institute e diffondere narrazioni favorevoli a Mosca in Occidente. Su 36 articoli attribuiti ai presunti esperti dell'IBI tra settembre 2025 e maggio 2026, 34 erano copiati da altre fonti, a volte con firme false; il dominio, registrato a febbraio 2025, si presentava con un indirizzo in Israele e citava Francis Fukuyama e Noam Chomsky. [Fonte: raw/pillitteri/pillitteri20260826-openai-rete-russa-chatgpt-cremlino.md]
- **2026-08-26** — Gli operatori scrivevano i prompt in russo e facevano generare al modello commenti in inglese da pubblicare su X, LinkedIn, Facebook, Substack e Telegram, con l'istruzione esplicita di nascondere ogni indizio linguistico dell'origine russa; poiché OpenAI vieta l'accesso dalla Russia, il gruppo si collegava via VPN. La firma dell'operazione era un indice di sovranità pubblicato dal finto think tank, che lodava la Russia e attaccava Francia, Germania, Unione Europea e Stati Uniti. [Fonte: raw/pillitteri/pillitteri20260826-openai-rete-russa-chatgpt-cremlino.md]
- **2026-08-26** — Un dettaglio ha tradito la rete: in un articolo sulla Germania compariva l'espressione "the Svetofor coalition", dove svetofor è la traduzione russa di semaforo, cioè l'Ampelkoalition tedesca, una resa innaturale per un anglofono. I canali Telegram collegati contavano dai 10.000 ai 20.000 iscritti ciascuno, mentre l'audience complessiva resta limitata alla fascia bassa della Categoria 3 della Brookings Breakout Scale. [Fonte: raw/pillitteri/pillitteri20260826-openai-rete-russa-chatgpt-cremlino.md]

- **2026-09-28** — Il caso della **bixonimania**: il 16 marzo 2024 una ricercatrice dell'Università di Göteborg ha inventato una sindrome oculare e nei mesi successivi ha caricato due preprint su Preprints.org che dichiaravano apertamente di essere falsi. Poche settimane dopo [[copilot|Microsoft Copilot]] la descriveva come "una condizione intrigante e relativamente rara", [[gemini]] attribuiva il disturbo all'esposizione alla luce blu consigliando un oculista e [[perplexity]] ne stimava la prevalenza in circa un caso ogni 90.000 persone. Il meccanismo è la ricerca online in tempo reale: bastava che il preprint comparisse tra i primi risultati perché il riassunto lo trattasse come una fonte valida, perché il modello non valuta la plausibilità del contenuto ma prevede la continuazione statisticamente coerente di un documento che, nella forma, assomiglia a un paper medico. [Fonte: raw/pillitteri/pillitteri20260928-bixonimania-malattia-finta-ai.md]
- **2026-09-28** — Il passaggio più preoccupante non riguarda i chatbot ma la letteratura scientifica: nel novembre 2024 tre dermatologi hanno pubblicato sulla rivista peer-reviewed Cureus, edita da Springer Nature, uno studio sulle occhiaie che citava la bixonimania come forma emergente reale, e la rivista ha ritirato il paper il 30 marzo 2026 parlando di "tre riferimenti irrilevanti, incluso uno a una malattia fittizia"; Preprints.org ha rimosso i due preprint il 10 aprile 2026, catalogandoli come contenuto fabbricato. È il fenomeno che i ricercatori chiamano **citation laundering**: un'allucinazione generata dall'AI passa attraverso una ricerca bibliografica assistita dall'AI, un autore umano la trascrive senza aprire il documento originale e da lì acquisisce l'autorità formale di una fonte peer-reviewed. [Fonte: raw/pillitteri/pillitteri20260928-bixonimania-malattia-finta-ai.md]
- **2026-09-30** — NewsGuard conta 906 articoli e servizi falsi attribuiti a 163 testate reali di 21 paesi da tre operazioni di influenza russe dall'inizio dell'invasione dell'Ucraina: nel primo semestre 2026 i falsi firmati con il nome di una testata vera passano da 44 a 421, un aumento dell'850%, con Euronews la più imitata (82) e l'uso di loghi, grafica e perfino indirizzi web copiati. [Fonte: raw/pillitteri/pillitteri20260930-newsguard-russia-imita-bbc-euronews-disinformazione.md]
- **2026-10-10** — Un'inchiesta di The Atlantic documenta come alcuni chatbot possano essere indotti a produrre immagini, documenti e video falsi su presunte frodi elettorali: nei test del Brennan Center i ricercatori hanno aggirato diverse protezioni, a volte combinando modelli diversi. Il rischio documentato riguarda la diffusione di falsi indizi e la fiducia nelle elezioni, non una capacità di alterare il conteggio delle schede. [Fonte: raw/controrumore/controrumore20261010-diario-ai-lai-decide-ma-chi-ne-risponde.md]
- **2026-10-24** — Un articolo di The Atlantic raccoglie casi delle elezioni di midterm statunitensi in cui risposte AI e riepiloghi online hanno indirizzato elettori verso informazioni o raccolte fondi errate: una rilevazione di settembre indica che il 4% degli intervistati aveva chiesto informazioni elettorali a un chatbot nel mese precedente e quasi il 40% aveva consultato i riepiloghi AI di Google Search. I test citati hanno riscontrato errori fattuali e fonti inaffidabili, ma risalgono ad agosto e non specificano il modello valutato, quindi non definiscono l'affidabilità attuale dei singoli servizi. [Fonte: raw/controrumore/controrumore20261024-diario-ai-sicurezza-regole-e-nuovi.md]
- **2026-10-30** — Associated Press riferisce che video manipolati con AI hanno diffuso false dichiarazioni attribuite a ex collaboratori di due candidati democratici al Senato statunitense: analisi forensi e collegamenti online sostengono l'ipotesi di un legame con una rete russa, ma l'attribuzione resta probabilistica e non prova un'operazione statale in ogni sua parte. Le copie dei filmati sono rimaste disponibili anche dopo la sospensione di alcuni account e non sono misurati né la diffusione complessiva né gli effetti sul voto. [Fonte: raw/controrumore/controrumore20261030-diario-ai-fiducia-denaro-e-controlli.md]













## Collegamenti

- [[openai]]
- [[deepfake]]
- [[ai-slop]]
- [[sicurezza-ai]]
- [[index]]
