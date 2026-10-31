---
title: "Mercato dei dati rubati"
category: trend
tags: [dark-web, infostealer, privacy, data-breach, sicurezza]
related_puntate: []
created: 2026-09-25
updated: 2026-10-27
sources: [raw/pillitteri/pillitteri20260830-anthropic-sessioni-claude-rubate-infostealer.md, raw/pillitteri/pillitteri20260904-patenti-dark-web-idscan.md, raw/pillitteri/pillitteri20260923-crif-dark-web-italia-terza-infostealer-2026.md, raw/pillitteri/pillitteri20260923-revolut-hacker-riscatto-clienti-leak-site.md, raw/pillitteri/pillitteri20260925-agenti-ia-rubano-600000-carte-credito-gambit.md, raw/pillitteri/pillitteri20261002-reddit-chiude-rss-scraping-ia.md, raw/controrumore/controrumore20261019-diario-ai-regole-investimenti-e-nuovi.md, raw/controrumore/controrumore20261021-diario-ai-regole-salute-e-infrastrutture.md, raw/controrumore/controrumore20261027-diario-ai-la-spesa-ai-accelera-tra.md]
---

# Mercato dei dati rubati

## Introduzione

Quadro del circuito clandestino in cui finiscono credenziali, documenti e sessioni sottratti agli utenti, e delle conseguenze pratiche per chi ne resta coinvolto. Il baricentro si è spostato dal danno una tantum alla raccolta di identità digitali: un infostealer non porta via una singola password ma l'intero profilo di navigazione, con credenziali, indirizzi IP, sistema operativo e sessioni già autenticate. [Fonte: raw/pillitteri/pillitteri20260923-crif-dark-web-italia-terza-infostealer-2026.md]

## Evoluzione nel tempo

- La merce è diventata il cookie di sessione di un servizio AI a pagamento: man mano che gli abbonamenti AI diventano un costo reale in bolletta, la sessione acquista un valore che prima non aveva, e chi vende infostealer lo ha capito prima di molti utenti. [Fonte: raw/pillitteri/pillitteri20260830-anthropic-sessioni-claude-rubate-infostealer.md]
- Il furto di identità documentale non si risolve cambiando una password: a differenza di una credenziale, la patente, la data di nascita e il volto restano gli stessi per anni e chi li possiede può riutilizzarli a lungo per frodi e aperture di conti fraudolente. [Fonte: raw/pillitteri/pillitteri20260904-patenti-dark-web-idscan.md]
- Più cresce l'obbligo di verificare l'identità, più gli archivi di scansioni diventano bersagli grossi: in Europa il regolamento eIDAS e i sistemi di verifica dell'età moltiplicano i punti in cui un cittadino deve caricare un documento, e nel Regno Unito l'Online Safety Act ha reso obbligatoria la verifica dell'età per numerosi siti. [Fonte: raw/pillitteri/pillitteri20260904-patenti-dark-web-idscan.md]
- L'estorsione si sposta dalla banca ai singoli: quando l'azienda rifiuta di pagare, gli attaccanti aprono un sito di leak e chiedono il riscatto direttamente alle persone i cui dati sono stati rubati. [Fonte: raw/pillitteri/pillitteri20260923-revolut-hacker-riscatto-clienti-leak-site.md]

## Attori coinvolti

- CRIF, il gruppo italiano dei servizi di informazione creditizia, che con l'Osservatorio Cyber monitora i dati personali in circolazione nei mercati clandestini e li incrocia con quelli dei propri utenti. [Fonte: raw/pillitteri/pillitteri20260923-crif-dark-web-italia-terza-infostealer-2026.md]
- IDScan.net, società di verifica dell'identità con sede in Louisiana con oltre 21 milioni di verifiche al mese in più di 20.000 sedi: la tecnologia scansiona i documenti anche con luce infrarossa e ultravioletta, la stessa che le banche usano per distinguere una patente vera da una falsa. Tra i clienti Hertz, Target, FedEx, Motorola Solutions, Caesars Entertainment e oltre mille dispensari di cannabis in 19 stati americani. [Fonte: raw/pillitteri/pillitteri20260904-patenti-dark-web-idscan.md]
- Nexus, il servizio comparso il 31 agosto 2026 su un forum criminale russo che funzionava come motore di ricerca a pagamento sui documenti: si digitava un nome e si otteneva la fototessera, la scansione fronte e retro, il numero della patente, la data di nascita e l'indirizzo. [Fonte: raw/pillitteri/pillitteri20260904-patenti-dark-web-idscan.md]
- Le sei famiglie di infostealer citate nella notifica di [[anthropic]]: Vidar, Lumma (LummaC2), StealC, RedLine e Acreed per Windows, Atomic Stealer (AMOS) per macOS. [Fonte: raw/pillitteri/pillitteri20260830-anthropic-sessioni-claude-rubate-infostealer.md]
- Il gruppo IAmNotAVillain, che ha aperto un leak site sulla rete Tor dopo aver sottratto a Revolut i dati di circa 680 clienti usando una PEC istituzionale italiana. [Fonte: raw/pillitteri/pillitteri20260923-revolut-hacker-riscatto-clienti-leak-site.md]
- Le autorità intervenute: l'FBI con la sede di New Orleans sul caso IDScan.net, il Garante per la protezione dei dati personali con una nota del 18 settembre 2026 e un canale aperto con l'autorità lituana competente su Revolut, la Procura di Reggio Calabria che indaga per accesso abusivo e la Financial Conduct Authority britannica. [Fonte: raw/pillitteri/pillitteri20260923-revolut-hacker-riscatto-clienti-leak-site.md]

## Notizie rilevanti

- Cambiare password dopo un alert serve, ma con un infostealer non basta: se il malware ha rubato i cookie di sessione l'attaccante può restare dentro l'account anche con la password nuova finché la sessione non viene chiusa, quindi il primo passo è disconnettere tutti i dispositivi dal servizio coinvolto. [Fonte: raw/pillitteri/pillitteri20260923-crif-dark-web-italia-terza-infostealer-2026.md]
- Le combinazioni contano più dei dati singoli: nel 99,8% dei casi il numero della carta di credito viaggia con il codice di sicurezza e la data di scadenza, username e password stanno insieme nel 96% dei casi ed email e password nel 95,9%. [Fonte: raw/pillitteri/pillitteri20260923-crif-dark-web-italia-terza-infostealer-2026.md]
- Le categorie di account più colpite sono i servizi e gli abbonamenti digitali (26,6%), i social network (20,8%) e forum e siti web (16,3%): profili che molti utenti aprono una volta e non controllano più, spesso con una password riusata altrove. [Fonte: raw/pillitteri/pillitteri20260923-crif-dark-web-italia-terza-infostealer-2026.md]
- La leva dell'estorsione ai clienti è il denaro e non la vergogna come nel caso Vastaamo del 2020: i clienti Revolut presi di mira detengono criptovalute in quantità, e un indirizzo di casa accanto a uno storico Bitcoin è il kit di partenza per il wrench attack, l'estorsione fisica contro chi custodisce asset digitali. [Fonte: raw/pillitteri/pillitteri20260923-revolut-hacker-riscatto-clienti-leak-site.md]
- Il caso IDScan.net è stato ricostruito dai timestamp: ogni documento era corredato fino a sei immagini e un timestamp al secondo, e il ricercatore Zach Edwards ha ritrovato la propria scansione con un orario che combaciava con la sua visita a un dispensario di Las Vegas durante DEFCON, mentre altri timestamp corrispondevano al secondo ai noleggi auto Hertz. [Fonte: raw/pillitteri/pillitteri20260904-patenti-dark-web-idscan.md]

## Timeline delle notizie

- **2026-08-30** — [[anthropic]] sloggia una parte degli utenti da [[claude]] e cancella la carta di pagamento salvata sui loro account: un infostealer ha copiato i cookie di sessione sui computer degli utenti e un attore malevolo li ha riusati per entrare negli account e bruciarne l'abbonamento, come l'azienda scrive nella notifica parlando di furto delle sessioni di login e non di credenziali indovinate. L'autenticazione a due fattori non protegge da questo scenario, perché la sessione rubata è già un login andato a buon fine. L'ordine delle mosse indicato è rimuovere il malware, mettere in sicurezza la casella email e solo dopo reinserire la carta. [Fonte: raw/pillitteri/pillitteri20260830-anthropic-sessioni-claude-rubate-infostealer.md]
- **2026-09-04** — Brian Krebs trova la propria patente della Virginia offerta come campione gratuito su Nexus, il catalogo da oltre 153 milioni di patenti di guida statunitensi e canadesi, più di 10 milioni di carte d'identità, circa 3 milioni di documenti di viaggio e 579.000 tessere sanitarie, quasi 170 milioni di documenti riconducibili a una sola azienda di verifica dell'identità. Il servizio sparisce due giorni dopo, ma i dati restano in circolazione e l'FBI apre un'indagine formale; al 7 settembre risultano almeno quattro class action depositate contro IDScan.net, che continua a parlare di potenziale incidente di sicurezza senza confermare la violazione. [Fonte: raw/pillitteri/pillitteri20260904-patenti-dark-web-idscan.md]
- **2026-09-21** — L'Osservatorio Cyber di CRIF presenta il dato del primo semestre 2026: 2,5 miliardi di dati unici in circolazione sul dark web, con l'Italia terza al mondo dopo Stati Uniti e Francia per account rubati dagli infostealer, sesta sulle email compromesse e quarta in Europa, ventiduesima nel mondo sulle carte di credito. Il 32,3% degli utenti italiani monitorati ha ricevuto almeno un alert nel semestre, con la Lombardia al 15,7%, il Lazio al 12,3% e la Sicilia all'11,3%, e le fasce più esposte sono i 51-60 anni e i 41-50. [Fonte: raw/pillitteri/pillitteri20260923-crif-dark-web-italia-terza-infostealer-2026.md]
- **2026-09-23** — IAmNotAVillain apre un leak site su Tor e chiede il riscatto direttamente ai correntisti Revolut: i nuovi estratti riguardano una decina di clienti di cui sono stati pubblicati volto, documento d'identità e informazioni bancarie, e il gruppo dice di voler vendere l'intero archivio per circa 300.000 dollari, un decimo dei tre milioni di dollari chiesti alla banca e lasciati scadere. [Fonte: raw/pillitteri/pillitteri20260923-revolut-hacker-riscatto-clienti-leak-site.md]
- **2026-09-25** — Nel caso degli agenti IA che hanno violato 27 aziende, le oltre 600.000 carte di credito ancora valide vengono da due sole di quelle aziende e per il 79 per cento (488.372) sono emesse negli Stati Uniti; dietro ci sono Emirati Arabi al 2,2 per cento, Arabia Saudita all'1,1, Regno Unito all'1 e Nuova Zelanda allo 0,9, mentre per il restante 16 per cento circa non esiste una ripartizione pubblica e Italia e Francia non compaiono nell'elenco diffuso. Non c'è nessun elenco pubblico delle carte coinvolte, quindi nessuno può sapere se la propria è nel lotto, e gli skimmer restano installati su oltre cento siti di cui non si conosce la geografia: la contromisura per chi compra online resta controllare gli addebiti e usare carte virtuali sui siti meno noti. [Fonte: raw/pillitteri/pillitteri20260925-agenti-ia-rubano-600000-carte-credito-gambit.md]
- **2026-10-02** — Reddit motiva la chiusura dell'RSS con la lotta allo scraping non autorizzato ma continua a monetizzare gli stessi dati con accordi di licensing diretti con le aziende di IA: Google e OpenAI hanno già intese commerciali con la piattaforma che restano invariate dopo l'annuncio, e nel secondo trimestre 2026 la voce «altri ricavi» di Reddit, che include proprio questi accordi di licenza, è cresciuta del 24% su base annua arrivando a 43 milioni di dollari. La lettura è che lo scraping gratuito via RSS o API pubblica sottrae valore a un dato che Reddit preferisce vendere sotto contratto, e che chi vuole i dati per addestrare o alimentare un modello dovrà passare da un accordo commerciale. [Fonte: raw/pillitteri/pillitteri20261002-reddit-chiude-rss-scraping-ia.md]
- **2026-10-19** — [[meta]] ha eliminato dai termini per gli account business una clausola che sembrava autorizzare l'uso di URL, pagine e domini per addestrare prodotti, dopo le proteste di editori e proprietari di siti: l'azienda sostiene che riguardava pubblicità e prodotti commerciali e che la rimozione non cambia le modalità dei crawler, ma non chiarisce in generale quali siti vengano raccolti né le basi d'uso dei contenuti. [Fonte: raw/controrumore/controrumore20261019-diario-ai-regole-investimenti-e-nuovi.md]
- **2026-10-21** — Gli Stati Uniti sanzionano cinque entità cinesi legate all'ex ingegnere Google Linwei Ding, condannato per aver sottratto informazioni riservate su infrastrutture per l'AI: fra i designati la società fondata da Ding e quattro realtà dell'incubatore pechinese MiraclePlus. [Fonte: raw/controrumore/controrumore20261021-diario-ai-regole-salute-e-infrastrutture.md]

- **2026-10-21** — Internet Archive difende il valore pubblico della memoria online: il fondatore Brewster Kahle sostiene che bloccare la Wayback Machine per fermare la raccolta delle aziende AI colpisce giornalisti, ricercatori e tribunali senza impedire l'acquisizione da altri canali. [Fonte: raw/controrumore/controrumore20261021-diario-ai-regole-salute-e-infrastrutture.md]
- **2026-10-27** — [[micro1]] offre alle aziende da 100.000 a due milioni di dollari per licenziare email, messaggi Slack, documenti e presentazioni da usare nell'addestramento, con un piano di investimenti da un miliardo nell'acquisto di dati aziendali: il mercato dei dati arriva così agli archivi interni, dove stanno procedure e decisioni che non si trovano altrove. Restano aperti consenso dei lavoratori, privacy, segreti commerciali e distribuzione del valore. [Fonte: raw/controrumore/controrumore20261027-diario-ai-la-spesa-ai-accelera-tra.md]













## Collegamenti

- [[anthropic]]
- [[claude]]
- [[crashstealer]]
- [[cybersicurezza]]
- [[malware-slop]]
- [[privacy-online]]
- [[regolamentazione]]
- [[reddit]]
- [[index]]
