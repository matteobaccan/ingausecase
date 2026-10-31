---
title: "AI in Auto"
category: trend
tags: [auto, carplay, assistenti, integrazione, apple, software-defined, auto-elettrica, general-motors, mercedes]
related_puntate: []
created: 2026-09-15
updated: 2026-10-31
---

# AI in Auto

## Introduzione

L'arrivo dei chatbot conversazionali nel cruscotto, reso possibile da iOS 26.4: con quell'aggiornamento [[apple]] ha aperto Apple CarPlay alle AI di terze parti e nel giro di pochi mesi lo schermo dell'auto ha ospitato cinque assistenti. La regola comune imposta da Apple è che l'esperienza sia esclusivamente vocale, senza testo sullo schermo, immagini o cronologia, per limitare le distrazioni alla guida.

Sotto il cruscotto, intanto, si gioca l'altra metà della partita: l'auto come piattaforma software, dove a decidere il comportamento del veicolo è il codice e non la meccanica. È il filone delle fonti non-AI di Pillitteri su auto elettriche e architetture di bordo, ripreso qui per quello che serve al tema: centraline, aggiornamenti a distanza, livelli di assistenza, ecosistemi e barriere commerciali.

## Evoluzione nel tempo

- **31 marzo 2026** — [[openai]] rilascia l'integrazione ufficiale di ChatGPT Voice Mode per CarPlay, primo chatbot AI sulla piattaforma automobilistica di Apple; funziona anche con il piano gratuito e l'attivazione passa da una nuova chat vocale sull'icona ChatGPT della dashboard.
- **Settembre 2026** — [[anthropic]] porta [[claude]] su CarPlay nella versione recente dell'app per iPhone, senza comunicato ufficiale: è il quinto chatbot dopo [[chatgpt]], Perplexity, [[grok]] e Meta AI.
- **14 settembre 2026** — iOS 27 porta su CarPlay il refresh più corposo dal 2014, con diciotto sfondi nuovi, il MiniPlayer ancorato in alto a destra, la barra di avanzamento nella schermata Now Playing e, per la prima volta, i video sullo schermo dell'auto quando è ferma; CarPlay Ultra resta legata a pochi modelli.
- Le architetture elettriche si accentrano e cambiano ciò che il software può fare. Sulla Ferrari Luce una nuova Vehicle Control Unit governa da sola powertrain, dinamica, recupero di energia e sospensioni attive su tre tensioni (800 V per i quattro motori, 48 V per le sospensioni, 12 V per gli ausiliari) rileggendo sensori e ridistribuendo coppia 200 volte al secondo, e i paddle al volante non simulano marce ma modulano cinque livelli di coppia e cinque di freno rigenerativo; il suono non viene sintetizzato ma rivelato da un accelerometro che amplifica le vibrazioni meccaniche, e il cockpit firmato LoveFrom rinuncia al maxi-touchscreen con la tesi che il touch obbliga a distogliere lo sguardo.
- Il fossato competitivo resta il software di guida, non l'hardware. La Leapmotor B05 monta l'architettura LEAP 3.5 con 28 centraline al posto delle 42 della generazione precedente, meno di 1,5 chilometri di cablaggio e celle integrate nella scocca (Cell-to-Chassis 2.0+, 34.500 Nm per grado), ma si ferma a un Qualcomm Snapdragon 8155 del 2019 sull'infotainment e a 21 ADAS di livello 2 SAE, mentre [[tesla]] progetta il silicio in casa (AI4+ con 64 GB complessivi, AI5 da 2.000-2.500 TOPS atteso in volume nel 2027). Il vero motivo per cui l'auto cinese costa meno non è tecnico: è l'assemblaggio a Figueruelas, in Spagna, che la tiene fuori dai dazi sulle elettriche cinesi.
- Il pendolo fra software di bordo proprietario e telefono in tasca oscilla in entrambe le direzioni. General Motors nel 2023 aveva annunciato di togliere il mirroring dalle proprie elettriche e nell'autunno 2026 è tornata sui pickup a benzina con CarPlay e Android Auto in picture-in-picture, mentre Mercedes sulla nuova Classe C ha fatto la scelta opposta e ha portato nell'abitacolo un assistente che coordina ChatGPT, Gemini e Bing.
- L'assistente multi-agente non fa lavorare i modelli insieme sulla stessa risposta: il sistema instrada la domanda in base al tema — ChatGPT per la conoscenza generale, Gemini per navigazione e luoghi, Bing per meteo, notizie e quotazioni — e lascia al cloud l'elaborazione, quindi le funzioni AI dipendono da una connessione dati attiva, dalla copertura del servizio Paese per Paese e dall'accordo con i fornitori, con il contenuto delle richieste vocali che esce dall'abitacolo.

## Attori coinvolti

- [[apple]] — padrona della piattaforma, decide template e vincoli.
- [[anthropic]] — con [[claude]], quinta AI ammessa sul cruscotto.
- [[openai]] — con [[chatgpt]], la prima ad arrivare.
- [[xiaomi]] — l'auto come nodo di un ecosistema che lega telefono e casa intelligente, con l'ingresso in Europa annunciato per il 2027.
- General Motors e Mercedes-Benz — i due lati opposti della stessa partita sull'abitacolo, la marcia indietro sul mirroring da una parte e l'assistente multi-fornitore dall'altra: nessuna delle due ha una pagina in wiki.
- Ferrari e Leapmotor — i due estremi del ragionamento sul software di bordo, rispettivamente il controllo di dinamica di una sportiva da 550.000 euro e la riduzione dei costi di una berlina da 26.900 euro; nessuna delle due ha una pagina in wiki.

## Notizie rilevanti

- Chi controlla gli aggiornamenti controlla il ciclo di vita del veicolo, e insieme la sua superficie di attacco: un'auto che riceve codice via rete espone canale di aggiornamento, gateway telematico e chiave digitale, tanto che nell'Unione europea il Regolamento UN R156 impone un sistema certificato di gestione degli aggiornamenti con l'identificativo RXSWIN.
- L'ingresso cinese in Europa passa dai dazi prima che dalla tecnologia: l'Unione applica alle elettriche cinesi dazi compensativi dal 7,8% al 35,3% sopra al 10% di dazio base (fino a circa il 45% per i produttori meno collaborativi), un nuovo entrante come Xiaomi ricadrebbe nella fascia dei cooperanti intorno al 20% e la produzione locale resta un'ipotesi per la fase successiva al debutto. Il fianco delicato è anche un altro: un ecosistema che unisce microfoni, telecamere, posizione dell'auto e abitudini domestiche sotto HyperOS concentra dati su cui in Europa valgono GDPR e regole sui veicoli connessi.
- Sul fronte dell'adozione, la ricarica privata diventa politica industriale: il bonus colonnine domestiche riapre con l'80% del costo di acquisto e installazione fino a 1.500 euro per i privati e 8.000 per i condomini, 15 milioni stanziati per il 2026 e domande dalle 12:00 del 22 settembre 2026 alle 12:00 del 31 gennaio 2027 sulla piattaforma di Invitalia, con SPID, CIE o CNS e una PEC attiva., che Apple non concede a nessuno tranne alla propria Siri: le app di terze parti vanno aperte con un tocco sullo schermo dell'auto prima di poterci parlare, il che ne riduce l'uso reale alla guida. Claude, in particolare, non comanda né l'auto né l'iPhone: non cambia la musica, non imposta la navigazione e non manda messaggi, resta una voce con cui ragionare e recuperare il filo di una conversazione iniziata sul telefono.
- Il contesto in cui tutto questo avviene è un sistema di bordo che dipende anche dal processore del cruscotto, con differenze di fluidità evidenti tra le generazioni di SoC.

## Timeline delle notizie

- **2026-04-07** — ChatGPT arriva su Apple CarPlay con iOS 26.4: è il primo chatbot AI sulla piattaforma, con esperienza solo vocale e requisiti iPhone con iOS 26.4 o successivo e app aggiornata.
- **2026-09-07** — Claude sbarca su CarPlay: schermata di conversazione a mani libere, continuità con le chat iniziate su iPhone, nessuna wake word e nessun controllo su auto o telefono.
- **2026-09-15** — iOS 27 rinnova CarPlay con sfondi, MiniPlayer, barra di avanzamento e video a veicolo fermo: i miglioramenti toccano la parte che si usa ogni giorno (mappe, musica, messaggi) e le app devono essere ricompilate per sfruttarli.
- **2026-05-28** — Ferrari Luce: la prima elettrica del Cavallino viene presentata il 25 maggio alla Vela di Calatrava di Roma con quattro motori indipendenti (1.050 CV, anteriori a 30.000 giri e 140 Nm, posteriori a 25.500 giri e 355 Nm, 0-100 in 2,5 secondi su 2.260 kg), oltre sessanta brevetti, ricarica fino a 350 kW sulla batteria da 122 kWh e 550.000 euro di partenza, con consegne europee nel quarto trimestre 2026 e statunitensi nel secondo trimestre 2027. Il titolo perde quasi otto punti percentuali nelle ore successive al reveal, mentre la vettura costruisce il discorso sulla centralina che aggiorna i parametri duecento volte al secondo, sul suono rivelato dall'accelerometro posteriore e sugli interni LoveFrom di Jony Ive e Marc Newson senza maxi-touchscreen.
- **2026-08-04** — Leapmotor B05 contro Tesla Model 3, settemila euro di differenza spiegati a livelli: ordini aperti in Europa dal 23 aprile 2026 a 26.900 euro contro i 34.015 della Model 3 Standard, e il divario non lo fa la batteria ma il rame, con LEAP 3.5 che porta le centraline da 42 a 28 e il cablaggio sotto 1,5 chilometri. La B05 si ferma al livello 2 SAE con 21 ADAS e 14 sensori e monta un computer centrale Snapdragon a doppio SA8797P solo sull'ammiraglia D19, mentre Tesla gioca la partita dell'omologazione europea di FSD Supervised e del silicio proprietario.
- **2026-09-05** — [[xiaomi]] conferma all'IFA di Berlino l'ingresso nel mercato automobilistico europeo nel 2027 con la Germania apripista (mercati con guida a destra nel 2028, Francia e Italia dopo senza data), dopo la firma di memorandum con otto gruppi di concessionari tedeschi tra cui Emil Frey Germany e LUEG Mobility: una rete fisica invece della vendita diretta di [[tesla]], con SU7 e YU7 in testa, oltre 500.000 consegne della serie SU7 in 28,5 mesi e il giro del Nürburgring in 7 minuti e 4,957 secondi per la SU7 Ultra. L'argomento dichiarato non è l'auto ma l'ecosistema Human x Car x Home sotto HyperOS, e a Monaco di Baviera lavora dal 2025 un centro di sviluppo con ex BMW come Rudolf Dittrich e Claus-Dieter Groll.
- **2026-09-16** — Il bonus colonnine domestiche riapre lo sportello (fonte non-AI, ripresa qui per l'adozione dell'elettrico): contributo a fondo perduto dell'80% su acquisto, messa in opera e spese tecniche di colonnine e wallbox, con tetto di 1.500 euro per le persone fisiche e 8.000 per i condomini; domande dalle 12:00 del 22 settembre 2026 alle 12:00 del 31 gennaio 2027 per gli impianti completati tra il 26 giugno e il 31 dicembre 2026, solo online su Invitalia.
- **2026-08-18** — Mercedes presenta la nuova Classe C restyling con **MBUX di quarta generazione** e un assistente vocale multi-agente: ChatGPT risponde alle domande di conoscenza generale, Google Gemini copre navigazione e luoghi — con Google Maps e un Automotive AI Agent su Vertex AI — e Microsoft Bing porta la ricerca web su meteo, notizie e quotazioni, con il sistema che sceglie a chi girare la domanda e mantiene il contesto su più battute. La carrozzeria cambia poco, il software molto: sotto MBUX gira **MB.OS** con gli aggiornamenti over-the-air, il volante reintroduce i comandi fisici e la gamma adotta il mild-hybrid a 48 volt. Ordini in Germania dal 18 agosto 2026 a 41.045 euro netti per la C 200 (48.844 IVA inclusa), listino italiano non ancora comunicato, Stati Uniti nella prima metà del 2027; le funzioni AI richiedono una connessione dati attiva e il contenuto delle richieste vocali viene elaborato sui server dei fornitori.
- **2026-09-16** — CarPlay e Android Auto tornano sui pickup di General Motors entro la fine del 2026, sui modelli 2027 di Chevrolet Silverado 1500 e GMC Sierra 1500: non a tutto schermo ma dentro una scheda in picture-in-picture accanto ai dati nativi del mezzo, con superfici che superano i 60 pollici, i comandi fisici mantenuti e un menu a tendina per privacy e microfono di bordo. È la marcia indietro rispetto alla decisione del 2023 di togliere la proiezione dello smartphone dalle elettriche per spingere il sistema proprietario, e il gruppo l'ha costruita insieme ad Apple e Google; sul fronte assistenza alla guida il sistema Super Cruise, che permette la guida a mani libere sulle autostrade mappate, riceve una grafica che mostra a schermo gli oggetti rilevati intorno al mezzo. Nel quadro della pagina resta il contesto delle AI entrate su CarPlay con iOS 27, [[chatgpt]] e [[claude]] compresi.
- **2026-08-22** — A giugno 2026 i ricercatori di Kaspersky trovano il primo malware documentato per le auto connesse: non colpisce la centralina che governa freni e motore ma l'head unit Android che gestisce navigatore, radio e schermo touch, e viaggia dentro il normale aggiornamento del firmware. Il ricercatore Dmitry Kalinin isola un downloader multi-stadio, con un primo pezzo che si chiama JarService, poi un loader che parla con i server dei criminali e infine il modulo che genera il guadagno vero, con obiettivi di frode pubblicitaria e proxy-botnet. Il caso è un precedente perché il bersaglio è scelto: il codice non è un virus da telefono capitato dentro una macchina, è pensato per starci.
- **2026-10-16** — Una guida mette in fila gli ADAS: le sei funzioni più diffuse (frenata automatica d'emergenza, cruise control adattivo, mantenimento di corsia, avviso di angolo cieco, riconoscimento dei segnali, monitoraggio dell'attenzione) e i tre passi di ogni sistema (percepire con telecamere, radar a onde millimetriche, ultrasuoni e lidar, decidere con la sensor fusion, agire su freni e sterzo). Dal 7 luglio 2024 una parte dei sistemi è obbligatoria su ogni auto nuova immatricolata nell'UE (regolamento 2019/2144, GSR 2), con l'obbligo partito il 6 luglio 2022 per i modelli di nuova omologazione; [[tesla]] usa le sole telecamere (vision only), mentre i robotaxi di [[waymo]] montano telecamere, radar e lidar insieme. Ogni funzione ha un ODD (ambito di impiego previsto) fuori dal quale si disattiva e la guida torna alla persona.
- **2026-10-16** — La Tesla Roadster Rocket presentata il 15 ottobre 2026 si solleva con dieci propulsori a gas freddo collegati a 600 litri di aria compressa ricaricabili, in tre versioni (Performance "road ready", Thrust "race ready", Rocket "air ready", quest'ultima solo su invito) e con produzione indicata da Elon Musk al 2028. Un'auto Tesla è già stata presa da remoto mentre andava, nel 2016: i ricercatori del Keen Security Lab di [[tencent]] arrivarono da remoto al CAN bus di una Model S partendo dal browser di bordo agganciato a un hotspot Wi-Fi malevolo, e da circa 19 chilometri di distanza manipolarono i freni; Tesla chiuse la falla con l'aggiornamento 7.1 entro dieci giorni. Dal 2021 i regolamenti ONU R155 e R156 obbligano i costruttori a un sistema certificato di cybersicurezza e di gestione degli aggiornamenti, in UE per tutti i veicoli nuovi da luglio 2024; per la Roadster, prototipo da dimostrazione, l'omologazione per la strada resta incerta.
- **2026-10-24** — Gemini arriva su CarPlay il 21 ottobre non come app a comando vocale ma dentro Google Maps, ed è la prima delle AI ammesse da Apple che entra da un'app di navigazione invece che dalla categoria aperta con iOS 26.4. È confermata negli Stati Uniti, Mobiflip la vede già attiva in Germania, mentre per l'Italia Google non ha dato date e la guida italiana dice ancora il contrario.
- **2026-10-31** — [[rivian]] ha ampliato la collaborazione con Volkswagen concedendo in licenza elementi della tecnologia del proprio assistente vocale AI, dopo aver introdotto Rivian Assistant sui modelli R1 e R2 e aver collegato l'iniziativa alla propria piattaforma software per veicoli. Nel trimestre i ricavi software e servizi dell'azienda sono cresciuti del 45% a 605 milioni di dollari, un dato che include più attività e non permette di misurare i ricavi dell'assistente.













## Collegamenti

- [[anthropic]]
- [[apple]]
- [[chatgpt]]
- [[claude]]
- [[grok]]
- [[guida-autonoma]]
- [[openai]]
- [[tesla]]
- [[voce-ai]]
- [[xiaomi]]
- [[index]]
