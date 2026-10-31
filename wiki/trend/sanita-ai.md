---
title: "Sanità AI"
category: trend
tags: [sanita, salute, assicurazioni, documentazione, agenti]
related_puntate: [20260928, 20261021]
created: 2026-09-28
updated: 2026-10-31
---

# Sanità AI

## Introduzione

Il punto in cui l'intelligenza artificiale entra nella pratica clinica, nella documentazione delle cartelle e nella catena amministrativa che porta dal referto al rimborso. Il tema ricorrente è che il primo effetto misurabile non è una cura migliore ma una codifica più aggressiva.

## Attori coinvolti

- [[veeva]]
- [[anthropic]]
- [[claude-opus-5-5]]

## Timeline delle notizie

- **2026-09-26** — La Blue Cross Blue Shield Association stima in circa 942 milioni di dollari la spesa sanitaria aggiuntiva generata tra il 2023 e il 2025 dalla codifica assistita dall'AI, che classifica più pazienti ospedalieri come clinicamente complessi senza un aumento corrispondente delle cure erogate; l'associazione aggiunge che gli assicuratori stanno ampliando i controlli automatizzati su fatture e pagamenti. È un'analisi prodotta dagli assicuratori, non una revisione indipendente delle cartelle cliniche. Il dettaglio dell'analisi: 653 milioni dei 942 derivano da diagnosi secondarie fatturate con maggiore frequenza, e tra i pazienti sottoposti a interventi intestinali maggiori le diagnosi di ostruzione parziale sono salite del 55 per cento e quelle di eccesso di acido nell'organismo del 33 per cento tra il primo trimestre 2023 e il quarto trimestre 2025; circa 55.000 ricoveri sono stati spostati a un gradino DRG superiore, per un costo medio di 11.900 dollari a salto, in una scala che va da un peso tariffario di 1,68 senza complicazioni a 2,40 con complicazione (+42 per cento) fino a 4,60 con complicazione maggiore (+173 per cento). I nomi ricorrenti tra i fornitori sono SmarterDx, che lavora a percentuale sul ricavo aggiuntivo trovato, Pieces Technologies, che integra la generazione della nota clinica con la logica tariffaria, e Abridge. L'American Hospital Association respinge la lettura e attribuisce la crescita della codifica all'invecchiamento della popolazione e alle malattie croniche, con un case-mix index salito di circa il 5 per cento tra il 2019 e il 2024 e la codifica di massima complessita' passata dal 10,2 al 22,7 per cento; nessuna delle due associazioni ha pubblicato dati a livello di singolo paziente.
- **2026-09-28** — Gli ambient AI scribe — sistemi che ascoltano la visita e redigono la nota clinica per l'approvazione del medico — sono in diffusione nelle grandi strutture: Downstate li ha usati in oltre 900 incontri e Permanente e Intermountain riportano risparmi di tempo significativi. Il cambiamento che pesa è il passaggio successivo, perché le note approvate confluiscono sempre più spesso nei flussi di codifica e fatturazione.
- **2026-09-28** — Veeva ha annunciato Study Builder Agent, un agente che configura il sistema di raccolta e controllo dati di uno studio clinico partendo dal protocollo, generando moduli EDC, visite, regole di controllo, listing e dati di test dagli standard dell'organizzazione: l'azienda promette configurazioni in circa un giorno, ma non ha pubblicato implementazioni clienti e l'accesso per gli early adopter è previsto a dicembre 2026.
- **2026-09-28** — Su Hugging Face è comparso un dataset medico sintetico con 2.194 malattie simulate da Claude Opus 5.5: i dialoghi durano in media trentatré turni tra sintomi, esami, trattamento e follow-up, e ogni paziente nasconde di proposito un'informazione o mente, lasciando al medico il compito di scoprirlo.

- **2026-09-28** — Il 19 agosto 2026 la FDA ha autorizzato [[aletta]] di [[vitestro]], primo robot capace di individuare una vena, inserire l'ago e prelevare il sangue senza intervento manuale diretto, con procedura De Novo e classificazione dei sistemi robotici per il prelievo venoso come dispositivi di Classe II. Nello studio ADOPT su 1.633 pazienti in tre ospedali olandesi il successo al primo tentativo è del 94,5 per cento quando il sistema individua una vena idonea, con eventi avversi lievi nello 0,6 per cento delle procedure e un tasso di emolisi dello 0,3 per cento contro l'intervallo di laboratorio dello 0,7-3,2 per cento; la supervisione di un flebotomista formato resta obbligatoria, ma un solo operatore può seguire fino a tre dispositivi insieme.
- **2026-09-29** — Gli scribi AI ambientali passano dalla trascrizione alla documentazione che alimenta anche coding e fatturazione: un ospedale di Brooklyn sperimenta Sunrise Thread AI con cinquanta medici e oltre novecento visite già documentate, mentre altre organizzazioni riportano riduzioni del tempo dedicato alle note, con benefici non uniformi ma un'AI ormai dentro la catena clinico-amministrativa.
- **2026-09-29** — Roche delinea un percorso verso laboratori scientifici autonomi: cicli chiusi in cui l'AI contribuisce a scegliere gli esperimenti, sistemi automatizzati li eseguono e i risultati alimentano le iterazioni successive, per aumentare il numero di esperimenti e standardizzare la raccolta dei dati.
- **2026-09-30** — Il segretario alla Salute Robert F. Kennedy Jr. vuole unire le cartelle cliniche degli americani e renderle ricercabili dall'AI per la ricerca su malattie croniche e possibili legami con vaccini, alimenti, sostanze chimiche e stile di vita, citando Medicare, Medicaid e i dati dei CDC; non ha dettagliato le tutele sulla privacy.
- **2026-10-05** — Lo Utah firma con Nolla Health la prima autorizzazione statale americana a far emettere a un'AI una prescrizione iniziale e non un semplice rinnovo, limitata ai farmaci topici per l'acne da lieve a moderata e vincolata a tre fasi di supervisione medica che si allentano solo al raggiungimento di soglie di concordanza e senza eventi avversi gravi.



- **2026-10-06** — Il 72 per cento dei responsabili sanitari intervistati da Imprivata afferma che strumenti o agenti AI vengono distribuiti senza approvazione formale dell'IT: il 28 per cento dichiara di avere già agenti in produzione e il 44 per cento di sperimentarli. Il rischio è maggiore rispetto al software tradizionale perché questi sistemi possono avviare workflow e attraversare cartelle cliniche, fatturazione e comunicazioni; gli esperti indicano inventari, credenziali limitate nel tempo, autorizzazioni granulari, controlli contro prompt injection e tracciamento verificabile delle azioni.
- **2026-10-07** — Nolla Health avvia in Utah un programma in cui un sistema AI valuta casi di acne lieve o moderata e genera una prescrizione iniziale, con controlli clinici destinati a diminuire gradualmente; il progetto apre interrogativi su responsabilità, accesso alle cure e monitoraggio, e il banco di prova sarà la capacità del sistema di riconoscere i casi fuori perimetro e trasferirli a un professionista.
- **2026-10-08** — OpenAI usa una rete di centinaia di medici in diversi Paesi per valutare le risposte sanitarie di ChatGPT: entro luglio sono state esaminate oltre 700.000 risposte in 49 lingue, considerando triage, incertezza, domande di approfondimento e appropriatezza dei suggerimenti, in un ambito dove risposte plausibili ma errate hanno conseguenze rilevanti.

- **2026-10-08** — Google riferisce che squadre dell'Organizzazione mondiale della sanità e partner nella Repubblica Democratica del Congo hanno usato Earth AI per analizzare un focolaio di Ebola: combinando dati geospaziali, immagini satellitari e mobilità gli strumenti avrebbero identificato in pochi minuti 48 insediamenti e oltre 45.500 persone a rischio, indirizzando laboratori mobili e sorveglianza.

- **2026-10-08** — Il governo statunitense, Meta, Google DeepMind e Isomorphic Labs partecipano a un'iniziativa Biohub da 1,8 miliardi di dollari per creare grandi dataset biologici aperti destinati ai modelli AI, con dati su come cellule e sistemi reagiscono alle perturbazioni, un primo corpus atteso entro circa un anno e l'obiettivo di migliorare le previsioni sperimentali nell'arco di cinque anni.
- **2026-10-09** — Aziende specializzate in AI stanno simulando studi clinici su pazienti virtuali per stimare quali farmaci abbiano maggiori probabilità di fallire prima delle costose sperimentazioni umane: Reuters cita BioinvestGPT, il cui sviluppatore sostiene di aver previsto l'esito negativo di uno studio Novartis, e QuantHealth, che dichiara simulazioni completabili in circa un mese; le prove disponibili provengono soprattutto dai fornitori e richiederanno confronti prospettici e validazione indipendente.

- **2026-10-09** — Biohub, Dipartimento dell'Energia, National Institutes of Health, Meta, Google DeepMind e Isomorphic Labs annunciano impegni per 1,8 miliardi di dollari in fondi, dati, calcolo e tecniche di misurazione: la Virtual Biology Initiative raccoglierà osservazioni standardizzate sulle reazioni delle cellule per addestrare modelli predittivi e scegliere meglio gli esperimenti da eseguire, con le risorse accessibili alla comunità scientifica dopo una fase iniziale privilegiata per alcuni finanziatori.
- **2026-10-13** — Scarlet raccoglie 50 milioni di dollari in una Series B per ampliare valutazione e certificazione di software e dispositivi medici AI, adattando le procedure regolatorie ai ritmi di aggiornamento del software, più rapidi di quelli dei dispositivi tradizionali, e per l'espansione internazionale. Il finanziamento è confermato ma non dimostra ancora una riduzione effettiva dei tempi di certificazione o una maggiore qualità delle verifiche.
- **2026-10-15** — Negli Stati Uniti strumenti AI valutano la probabilità che i pazienti paghino le fatture mediche e personalizzano messaggi, conversazioni e piani di rateizzazione, con chatbot e assistenti vocali integrati nella fatturazione ospedaliera: Cedar dichiara oltre 600.000 conversazioni gestite dal proprio assistente e un aumento del 21% dei pagamenti nel breve periodo, dati aziendali che non dimostrano maggiore accessibilità delle cure e sollevano questioni di riservatezza.

- **2026-10-15** — Uno studio retrospettivo in trenta terapie intensive neonatali di venti Paesi ha adattato un modello AI per localizzare il tubo endotracheale nelle radiografie dei neonati: ogni centro ha aggiornato il sistema con cinquanta immagini locali trasferendo al successivo i parametri e non le radiografie, e l'errore medio è sceso a 0,67 centimetri contro 1,29 dell'adattamento separato e 4,30 del modello adulto non adattato.

- **2026-10-15** — Un rapporto del Peterson Health Technology Institute sostiene che negli Stati Uniti i sistemi di pagamento e rimborso possono ostacolare le applicazioni AI capaci di migliorare direttamente le cure: gli strumenti amministrativi trovano più facilmente clienti e ritorni misurabili, mentre quelli clinici affrontano verifiche, responsabilità e incertezza sui finanziamenti, e il rapporto propone incentivi legati ai benefici per pazienti e operatori.
- **2026-10-15** — Edward Kang, 17 anni, vince il secondo posto e 175.000 dollari alla Regeneron Science Talent Search 2026 con RetinaMind, prototipo di IA che analizza immagini del fondo oculare e restituisce tre percentuali di confidenza per neurotipico, autismo e ADHD: sotto c'è un insieme di reti neurali convoluzionali che combinano le previsioni con voto e media, più una mappa GradCAM che evidenzia le zone pesate di più dal modello, e il lavoro estende uno studio del 2021 dell'Università Cinese di Hong Kong che aveva riferito sensibilità del 96 per cento e specificità del 91 per cento su poche decine di bambini. L'accuratezza del circa 89 per cento riferita alla stampa non ha ancora una pubblicazione sottoposta a revisione paritaria, non si conoscono il dataset di addestramento né la separazione fra dati di addestramento e verifica né sensibilità e specificità per classe, e lo stesso Kang parla di proof of concept che non distingue la gravità. Non esiste una versione pubblica né un'approvazione regolatoria, la diagnosi di autismo e ADHD resta affidata a valutazioni cliniche e comportamentali come DSM, ADOS e scale di Conners, e i ricercatori avvertono che le differenze retiniche potrebbero riflettere condizioni neurologiche in generale invece di questi disturbi.
- **2026-10-17** — [[colossal-biosciences|Colossal Biosciences]] presenta GenoMorph, piattaforma AI che analizza dati genetici e di sviluppo per individuare sequenze legate a caratteristiche fisiche di specie estinte, partendo dal becco e dal cranio del dodo, con circa 2.300 possibili bersagli genetici selezionati; l'annuncio non significa che il dodo sia stato riportato in vita.
- **2026-10-21** — [[profluent]] annuncia [[omnii-1]] e sostiene che i primi batteriofagi generati dall'AI sono stati somministrati a un paziente umano con infezione antibiotico-resistente: è il primo caso dichiarato di questo tipo.
- **2026-10-21** — Tre anni di benchmark di [[stanford|Stanford HAI]] mostrano che i punteggi nei test di conoscenza non bastano nei flussi di lavoro sanitari: in PhysicianBench la prestazione migliore è il 46 per cento dei compiti e in HealthAdminBench il 36, con difficoltà nel collegare informazioni tra documenti e applicazioni.

- **2026-10-21** — Strumenti AI di Mass General Brigham analizzano fotografie del volto per stimare l'età biologica e segnali associati alla sopravvivenza oncologica: in una coorte separata di oltre 38.000 persone un'età biologica stimata superiore a quella anagrafica era associata a un maggiore rischio di morte, ma gli autori precisano che l'associazione non dimostra un miglioramento delle cure e chiedono verifiche su popolazioni più rappresentative.

- **2026-10-21** — [[openai]] acquisisce [[orchestra-bio]] e intende integrarne piattaforma e team nella suite [[gpt-rosalind]]: il software aiuta i gruppi biofarmaceutici a coordinare studi, scadenze e campagne e può segnalare problemi operativi, lasciando alle persone le decisioni successive.

- **2026-10-21** — In 64 ore Claude ha generato oltre 318.000 progetti di proteine leganti per cinque tossine di scorpione: 211 testati da Adaptyv Bio e Twist Bioscience, 17 passati ai criteri di legame stabiliti da [[anthropic]], un risultato preliminare che non dimostra che neutralizzino il veleno o siano sicure come trattamento.
- **2026-10-21** — [[astrazeneca]] e [[oracle]] prevedono di usare AI e dati sanitari deidentificati per individuare pazienti per le sperimentazioni, sostenere la diagnosi precoce e monitorare la sicurezza dei farmaci, con un primo programma sull'ipertensione non controllata ad Abu Dhabi insieme a M42 e un accordo che resta non vincolante.
- **2026-10-21** — [[tairex]] presenta a Pechino [[mhac]], il sistema che porta in ambulatorio i medici IA addestrati in Agent Hospital: 54 agenti specializzati affiancano il dottore, mostrano i pareri su una schermata unica e segnalano dove non coincidono, mentre le correzioni del medico tornano al sistema per il fine-tuning e la decisione resta umana. L'azienda dichiara oltre il 96 per cento su MedQA e circa il 30 per cento di guadagno di efficienza nella prova al Beijing Tsinghua Changgung Hospital, in 18 reparti con più di 40 medici, senza test indipendenti né indicazione di cosa sia stato misurato.



- **2026-10-22** — [[sophont]] ha presentato [[holon-s1]], modello di ricerca che analizza comuni vetrini patologici colorati per stimare l'attività di geni e percorsi biologici nei tumori, ricavando ipotesi molecolari da immagini già presenti negli archivi ospedalieri quando mancano misure genomiche. Non è un test diagnostico: i risultati sono dell'azienda e servono verifiche indipendenti su riproducibilità e generalizzazione.
- **2026-10-23** — Lo Utah amplia i piloti AI supervisionati su rinnovo delle prescrizioni, prime prescrizioni per l'acne e fisioterapia virtuale: le aziende partecipanti devono avere un'assicurazione di responsabilità dedicata, non possono rinunciare alla responsabilità e i piloti futuri richiederanno valutatori indipendenti. Resta aperto chi risponda del danno al paziente, ed è il nodo su cui lavorano i regolatori.



- **2026-10-24** — Uno studio su Science ha misurato MAI-DxO di Microsoft, che coordina agenti per interrogare un paziente simulato, chiedere esami e formulare diagnosi, sui casi complessi del New England Journal of Medicine: 83% di accuratezza contro il 36% di medici generalisti e internisti singoli con materiali di riferimento. Il confronto non includeva specialisti dei casi difficili e riguardava simulazioni, non visite reali, e Microsoft avvierà valutazioni ospedaliere con Beth Israel Deaconess.
- **2026-10-26** — Phylo ha annunciato un accordo con Bayer per usare Biomni Lab in workflow di scoperta di farmaci che riuniscono letteratura scientifica, dati biomedici e metodi analitici: secondo Phylo gli agenti riducono il lavoro manuale e registrano fonti, metodi ed esecuzioni perché i ricercatori possano esaminare i passaggi. L'annuncio non specifica dimensione, calendario o risultati già ottenuti.
- **2026-10-26** — Una rete convoluzionale di dieci anni, piccola e specializzata, riconosce le lesioni cutanee molto meglio di [[gpt-6-astra]] e di Fable 5.1 secondo i risultati pubblicati dal laboratorio Lynch.
- **2026-10-27** — Il Johns Hopkins Bayview Medical Center sta avvisando 3.182 pazienti che i loro dati possono essere finiti su uno strumento di IA pubblico non autorizzato: il 21 settembre un membro del personale ha caricato per errore un foglio di calcolo con nomi, date di ricovero, numeri di cartella, reparto, farmaci e nomi dei medici, senza numeri di previdenza sociale né dati finanziari. L'ospedale ha fatto cancellare richiesta, conversazione e documento dalla cronologia, ha chiesto alla società di eliminare i dati e rafforza formazione e restrizioni sugli strumenti non approvati, mentre non è noto se i dati possano essere finiti nell'addestramento; le linee guida interne del maggio 2025 vietavano già quel tipo di caricamento.
- **2026-10-28** — Il Centre for Artificial Intelligence and Robotics dell'Accademia cinese delle scienze ha presentato a Hong Kong CARES 4.0, agente clinico multimodale costruito sul framework Harness e su modelli addestrati su TC, RM, ecografia, endoscopia ed EEG, che segue il paziente dai sintomi alla diagnosi, riassume l'uso delle apparecchiature e prepara bozze di report scientifici. Secondo il direttore Liu Hongbin è in prova in più di trenta ospedali, senza studi di accuratezza pubblicati e con la decisione che resta al medico; in broncoscopia il sistema segnala quando la sonda si avvicina a vasi, arterie o nervi.
- **2026-10-29** — Uno studio su cinque modelli linguistici e 177.120 casi clinici sintetici, pubblicato su Nature Health, ha rilevato forte convergenza sulle marche commerciali di farmaci anche quando era indicato lo stesso principio attivo: in media il prodotto più consigliato raccoglieva il 97,5 per cento delle prime scelte per coppia farmaco-malattia. Nel sottoinsieme con dati di costo gli autori stimano che 38 principi attivi avrebbero generato una spesa simulata più alta, per 55,6 milioni di dollari annui; i casi erano sintetici, quindi lo studio misura raccomandazioni dei modelli e non prescrizioni o esiti reali.
- **2026-10-30** — Un sondaggio del Pew Research Center su 3.488 adulti statunitensi rileva maggiore disponibilità verso l'AI per traduzioni e appuntamenti, ma disagio diffuso su diagnosi e trattamenti: il 60 per cento si dichiara a disagio con l'AI in queste decisioni, il 47 per cento accetterebbe una diagnosi assistita se un professionista controllasse il risultato e appena il 3 per cento approva una decisione autonoma. La rilevazione misura opinioni dichiarate, non esperienze cliniche o esiti sanitari osservati.
- **2026-10-31** — [[formation-bio]] ha annunciato un fondo con 600 milioni di dollari di impegni di capitale per acquisire o prendere in licenza da dieci a quindici programmi farmacologici nei prossimi tre-cinque anni, ciascuno gestito in una società separata con una piattaforma AI e infrastrutture condivise per sviluppo clinico, regolazione e produzione. L'azienda punta a traguardi clinici in due-quattro anni dall'acquisizione, obiettivi dichiarati per cui restano necessari studi su sicurezza ed efficacia.
































































## Collegamenti

- [[veeva]]
- [[claude-opus-5-5]]
- [[economia-ai]]
- [[regolamentazione]]
[[healthleap]]
- [[scarlet]]
- [[index]]
- [[palantir]]
