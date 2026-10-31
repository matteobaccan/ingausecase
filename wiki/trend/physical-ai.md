---
title: "Physical AI"
category: trend
tags: [physical-ai, robotica, agenti]
related_puntate: [20261015]
created: 2026-09-19
updated: 2026-10-31
sources: [raw/pillitteri/pillitteri20260619-project-fetch-fase-2-claude-opus-robot-dog.md, raw/pillitteri/pillitteri20260731-gemini-robotics-2-controllo-corpo-intero.md, raw/pillitteri/pillitteri20260919-openai-robotica-27-assunzioni-stipendi.md, raw/controrumore/controrumore20260919-diario-ai-lai-fa-gia-paura-al-lavoro.md, raw/pillitteri/pillitteri20260812-robot-cani-luna-base-cinese-ilrs.md, raw/pillitteri/pillitteri20260923-nvidia-halos-sicurezza-ia-fisica.md, raw/pillitteri/pillitteri20260812-byd-xiao-di-robot-umanoidi-concessionaria.md, raw/pillitteri/pillitteri20260821-unitree-superman-umanoide-batte-bolt.md, raw/pillitteri/pillitteri20260822-robot-umanoidi-cina-redditivita.md, raw/pillitteri/pillitteri20260926-scuola-robot-hangzhou-primi-diplomi.md, raw/pillitteri/pillitteri20260928-fda-aletta-robot-prelievo-sangue.md, raw/tldr/tldr20261001.md, raw/pillitteri/pillitteri20260817-honor-robot-phone-gimbal-robotico.md, raw/controrumore/controrumore20261005-diario-ai-quando-lai-diventa-un-problema.md, raw/controrumore/controrumore20261006-diario-ai-lai-entra-nella-sfera-privata.md, raw/controrumore/controrumore20261009-diario-ai-gpt-6-cambia-forma-a-chatgpt.md, raw/pillitteri/pillitteri20260703-ubtech-u1-robot-umanoide-compagnia.md, raw/pillitteri/pillitteri20260804-unitree-as2-w-robot-quadrupede-ruote.md, raw/pillitteri/pillitteri20260830-robot-sesso-cinese-somnia-lab-video-mocap.md, raw/pillitteri/pillitteri20261011-figure-helix-2-5-robot-umanoide-faccende-casa.md, raw/pillitteri/pillitteri20261011-lutech-luca-robot-umanoide-fabbriche-italiane.md, raw/pillitteri/pillitteri20261011-robot-xrobotdoll-emozioni-video-virale.md, raw/pillitteri/pillitteri20261012-tesla-optimus-vendita-2027-prezzo-preordini.md, raw/tldr/tldr20261014.md, raw/pillitteri/pillitteri20261014-gemini-4-argon-robot-cornhole-pagoda-blender.md, raw/puntate/ainews20261015.md, raw/controrumore/controrumore20261015-diario-ai-sicurezza-lavoro-e-nuove.md, raw/pillitteri/pillitteri20261014-robco-unicorno-miliardo-dollari.md, raw/controrumore/controrumore20261016-diario-ai-lintelligenza-artificiale.md, raw/controrumore/controrumore20261017-diario-ai-regole-agenti-e-nuovi-costi.md, raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md, raw/pillitteri/pillitteri20261019-neo1-robot-umanoide-4-metri-cina.md, raw/pillitteri/pillitteri20261019-vangrid-cos-e-come-funziona.md, raw/controrumore/controrumore20261020-diario-ai-rischi-costi-e-nuove-regole.md, raw/controrumore/controrumore20261021-diario-ai-regole-salute-e-infrastrutture.md, raw/pillitteri/pillitteri20261022-huang-microduck-robot-gtc-berlino-rtx-spark.md, raw/controrumore/controrumore20261023-diario-ai-agenti-sotto-osservazione.md, raw/pillitteri/pillitteri20261024-unitree-h2-x-robot-solleva-auto-salta-4-metri.md, raw/myclaw/myclaw20261023-agents-plan-factory-production.md, raw/tldr/tldr20261027.md, raw/pillitteri/pillitteri20261027-boston-dynamics-cani-robot-spot-ice-dipendenti.md, raw/pillitteri/pillitteri20261027-farfalla-robotica-ia-ali-npj-robotics.md, raw/pillitteri/pillitteri20261027-genie-4-google-deepmind-world-model.md, raw/controrumore/controrumore20261031-diario-ai-agenti-mercati-e-nuove.md]
---

# Physical AI

## Introduzione

L'intelligenza artificiale che esce dallo schermo e controlla oggetti che si muovono nello spazio: bracci industriali, robot quadrupedi e umanoidi, veicoli autonomi. Il collo di bottiglia storico è il divario tra ciò che un modello sa fare in simulazione e ciò che funziona davvero nel mondo reale, e la domanda che attraversa il filone è dove si sposti quel collo di bottiglia man mano che i modelli migliorano. [Fonte: raw/pillitteri/pillitteri20260619-project-fetch-fase-2-claude-opus-robot-dog.md] Nella definizione più larga di [[nvidia]] rientrano anche telecamere intelligenti e macchine che non si spostano ma interpretano lo spazio, mentre il termine embodied AI usato da Crunchbase resta più legato al robot. [Fonte: raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md]

## Evoluzione nel tempo

- Il confine si è spostato dal scrivere il software di controllo alla manipolazione fisica fine: programmare sensori, visione e pianificazione è ormai rapidissimo, mentre la regolazione in tempo reale di un oggetto reale resta il limite. È la differenza tra il ciclo "inquadra il problema ed esegui" e il ciclo "percepisci e adatta in tempo reale", il controllo a ciclo chiuso. [Fonte: raw/pillitteri/pillitteri20260619-project-fetch-fase-2-claude-opus-robot-dog.md]
- I soldi sono arrivati prima dei risultati misurabili: al 22 giugno 2026 le startup di robotica avevano già raccolto 18,8 miliardi di dollari, contro i 15 dell'intero 2025 e i 14,1 del picco precedente nel 2021, secondo Crunchbase, con round da 1,4 miliardi per Skild AI guidato da SoftBank e fino a 1,4 per Neura Robotics con Tether in testa. [Fonte: raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md]
- Il collo di bottiglia si è spostato sui dati di interazione fisica, che in rete non esistono nella quantità necessaria: i dataset di teleoperazione sono oltre 100.000 volte più piccoli di quelli con cui si addestrano i modelli linguistici, perciò nascono aziende che li producono, li vendono o li fanno raccogliere dagli smartphone delle persone, mentre Open X-Embodiment ha mostrato che i dati di robot diversi messi insieme valgono più della loro somma. [Fonte: raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md]
- I world model restano un contenitore di approcci diversi - simulazione della fisica con Cosmos 3, spazi navigabili con Genie 3, ricostruzione 3D con Atlas di World Labs, rappresentazioni astratte con i JEPA di AMI Labs - e nessuna famiglia chiude da sola il problema. [Fonte: raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md]
- La catena di [[nvidia]] resta il riferimento per costruire un sistema di physical AI: un computer per addestrare i modelli di fondazione, uno per simulare con Omniverse, Cosmos, Isaac Lab e Isaac Sim, e uno a bordo del robot con Jetson Thor. [Fonte: raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md]

## Attori coinvolti

- [[anthropic]]
- [[gemini-robotics-2]]
- [[google-deepmind]]
- [[nvidia]]
- [[openai]]
- [[tesla]]
- [[figure-ai]]
- [[1x-technologies]]
- [[unitree]]
- [[world-labs]]
- [[ami-labs]]
- [[vangrid]]

## Timeline delle notizie

- **2026-07-03** — UBTECH presenta il 30 giugno a Shenzhen l'umanoide U1, venduto sotto il marchio consumer UWORLD: pelle in silicone, contatto visivo e risposte con mezzo secondo di ritardo, nasce per fare compagnia a chi vive da solo, con l'U1 Lite a 119.800 yuan (circa 15.500 euro) e oltre 13.361 ordini in meno di un mese di prevendita su JD.com. [Fonte: raw/pillitteri/pillitteri20260703-ubtech-u1-robot-umanoide-compagnia.md]

- **2026-08-04** — Unitree Robotics presenta l'AS2-W Super Athlete, un quadrupede con quattro ruote motorizzate su gambe articolate: 25 kg di peso, 16 kg di carico continuo, oltre 30 km di autonomia a vuoto e una struttura che regge fino a 150 kg statici, sei volte il proprio peso, ripreso mentre risale pareti rocciose e scende gradini senza rallentare. [Fonte: raw/pillitteri/pillitteri20260804-unitree-as2-w-robot-quadrupede-ruote.md]

- **2026-08-30** — Il video virale presentato come "il robot del sesso cinese" non mostra nessun robot ma solo una sessione di motion capture; dietro c'è Somnia Lab, che con quei dati vuole costruire il robot da compagnia Model L, in preordine su somnia.love con consegna promessa per fine 2027, intorno al cui nome è già nata una truffa cripto. [Fonte: raw/pillitteri/pillitteri20260830-robot-sesso-cinese-somnia-lab-video-mocap.md]

- **2026-10-11** — Il video del robot XRobotDoll non mostra emozioni ma un meccanismo di espressioni su comando: una testa in silicone muove sopracciglia, occhi e bocca quando un uomo le chiede a voce di essere felice, arrabbiata, triste o sorpresa. [Fonte: raw/pillitteri/pillitteri20261011-robot-xrobotdoll-emozioni-video-virale.md]

- **2026-10-11** — Con Figure Helix 2.5, Figure AI ha mandato l'umanoide Figure 03 a fare le faccende in 30 abitazioni mai viste della Bay Area, senza raccogliere dati sul posto: 237 prove completate su 420 (il 56%) contro il 9% di un modello identico addestrato da zero. [Fonte: raw/pillitteri/pillitteri20261011-figure-helix-2-5-robot-umanoide-faccende-casa.md]

- **2026-10-11** — Lutech presenta l'8 ottobre a Milano L.u.c.a. (Lutech hUmanoid Collaborative Assistant), il suo primo robot umanoide per le fabbriche italiane dalla logistica alla produzione, destinato alle mansioni più rischiose; sullo sfondo pesa il regolamento UE sulle macchine applicabile dal 20 gennaio 2027. [Fonte: raw/pillitteri/pillitteri20261011-lutech-luca-robot-umanoide-fabbriche-italiane.md]

- **2026-08-17** — Honor apre il 12 agosto 2026 i preordini dell'Honor Robot Phone, primo smartphone con un gimbal meccanico motorizzato integrato nel corpo: il braccio Titanium Agile a quattro gradi di libertà si dispiega in 0,8 secondi, il motore in titanio pesa 2,6 grammi e ruota fino a 360 gradi al secondo, con due sensori da 200 megapixel sviluppati con Arri. In YOYO Robot Mode il gimbal muove il telefono come un piccolo robot da scrivania, con oltre cento movimenti facciali, seguendo il soggetto e riconoscendo la provenienza della voce. [Fonte: raw/pillitteri/pillitteri20260817-honor-robot-phone-gimbal-robotico.md]

- **2026-09-19** — [[openai]] porta a ventisette le posizioni aperte nella robotica, contro le undici di maggio, con stipendi base fino a 500.000 dollari e una combinazione di ruoli su attuatori, elettronica e firmware, simulazione, raccolta dati, inferenza e machine learning che disegna una piattaforma robotica proprietaria invece del solo software di controllo da montare su macchine altrui: il ruolo meglio pagato è un ingegnere di machine learning per i sistemi dati distribuiti, perché a decidere il ritmo del miglioramento sono le pipeline che alimentano i cicli di addestramento, non il braccio meccanico. [[sam-altman]] conferma che l'azienda costruirà "sicuramente un umanoide" e altre forme fisiche, precisando che la sfida decisiva resta l'intelligenza e non il telaio, mentre la sequenza raccontata dai media punta prima a robot per data center e ambienti controllati. [Fonte: raw/pillitteri/pillitteri20260919-openai-robotica-27-assunzioni-stipendi.md]
- **2026-06-19** — Project Fetch, la seconda fase dello studio del Frontier Red Team di [[anthropic]] pubblicata il 18 giugno 2026, misura l'uplift di [[claude-opus-4-7]] su un robot quadrupede commerciale: il modello da solo completa quattro compiti in nove minuti e trentacinque secondi contro i 361 minuti (sei ore) della squadra di ricercatori senza AI e i 181 minuti della squadra che lo usava come copilota, cioè 37,7 e 18,9 volte più veloce, con 1.045 righe di codice contro le 10.309 scritte dagli umani. La persona resta nel ciclo solo per collegare il portatile, approvare i comandi e azionare il controller a mano, e il modello non riesce a riportare indietro una palla da spiaggia: il riconoscimento dell'oggetto e la pianificazione funzionano, manca la spinta precisa. [Fonte: raw/pillitteri/pillitteri20260619-project-fetch-fase-2-claude-opus-robot-dog.md]
- **2026-06-19** — Gli autori descrivono un percorso a tre stadi — i modelli aiutano gli umani, gli umani aiutano i modelli, i modelli fanno da soli — e avvertono che «sarebbe imprudente escludere» che la stessa traiettoria si ripeta anche sull'hardware, dopo che il salto da Opus 4.1 a Opus 4.7 è avvenuto in pochi mesi. Lo studio non dimostra che un robot guidato da Claude sia pronto per un magazzino o per una casa. [Fonte: raw/pillitteri/pillitteri20260619-project-fetch-fase-2-claude-opus-robot-dog.md]
- **2026-07-31** — [[google-deepmind]] pubblica [[gemini-robotics-2]], tre modelli che portano sotto un'unica policy addestrata il controllo di un umanoide intero: il VLA che muove il corpo, ER 2 come cervello di alto livello e On-Device 2 sul computer di bordo. Lo stesso checkpoint pilota tre configurazioni hardware diverse e i tassi di successo pubblicati mostrano dove il limite resta: 92% nello svitare una lampadina contro il 36% nell'avvitarla e il 32% nell'usare la paletta per la polvere. [Fonte: raw/pillitteri/pillitteri20260731-gemini-robotics-2-controllo-corpo-intero.md]

- **2026-09-19** — Spirit AI prevede entro meta 2027 un salto nelle capacita dei robot umanoidi paragonabile al momento ChatGPT, con circa 1.000 contractor per dati reali e decine di umanoidi Moz1 operativi presso CATL e JD.com. [Fonte: raw/controrumore/controrumore20260919-diario-ai-lai-fa-gia-paura-al-lavoro.md]
- **2026-08-12** — L'8 agosto 2026 la China Academy of Space Technology pubblica un documento tecnico su come robot quadrupedi potrebbero lavorare fianco a fianco con gli astronauti alla futura base lunare cinese: lo scenario è di tre astronauti e due robot cani operativi al polo sud della Luna, presso la International Lunar Research Station, che Pechino punta a completare nella configurazione base intorno al 2035. Il cuore dello studio è la divisione dei ruoli, con la decisione guidata dall'astronauta e i robot autonomi che portano a termine il lavoro fisico. [Fonte: raw/pillitteri/pillitteri20260812-robot-cani-luna-base-cinese-ilrs.md]

- **2026-09-23** — [[nvidia]] presenta [[halos]] come sistema di sicurezza full stack dell'IA fisica, che raccoglie in un'unica catena le prove di sicurezza di hardware, software, simulazione e aggiornamenti e le fa ispezionare da un laboratorio accreditato prima della certificazione finale: il laboratorio però lavora sulla documentazione di prodotto e non su prove fisiche, e il suo esito non vale come certificato del veicolo o del robot finito, il che lascia aperto il divario tra tracciabilità dei documenti e verifica sul campo. [Fonte: raw/pillitteri/pillitteri20260923-nvidia-halos-sicurezza-ia-fisica.md]

- **2026-08-12** — BYD porta il robot umanoide Xiao Di nelle concessionarie: alto 1,61 metri, visione a 360 gradi, mani con 31 gradi di libertà e traduzione in tempo reale tra sei dialetti cinesi e sei lingue, con l'obiettivo di due o tre unità per ciascuno degli oltre 3.000 punti vendita. [Fonte: raw/pillitteri/pillitteri20260812-byd-xiao-di-robot-umanoidi-concessionaria.md]
- **2026-08-21** — Unitree mostra Superman, prototipo umanoide con gambe da 85 centimetri che dichiara 12,66 metri al secondo e un salto da 2 metri, numeri da video non verificati da terzi. [Fonte: raw/pillitteri/pillitteri20260821-unitree-superman-umanoide-batte-bolt.md]
- **2026-08-22** — La Cina domina le spedizioni di robot umanoidi ma non ancora i conti: nel primo semestre 2026 il mondo ha ricevuto circa 19.100 unità (quasi il quadruplo dell'anno prima), oltre il 97 per cento con marchio cinese, con Agibot a circa 9.700 unità e le prime cinque aziende (Agibot, Unitree, Galbot, UBTech, Leju Robotics) all'86 per cento. I produttori però perdono marginalità: UBTech ha visto l'utile rettificato del primo trimestre calare del 53 per cento a fronte di ricavi su del 68. [Fonte: raw/pillitteri/pillitteri20260822-robot-umanoidi-cina-redditivita.md]

- **2026-09-26** — La scuola dei robot di Hangzhou consegna il 17 settembre i primi quattro "diplomi": due robot guida, uno per le ispezioni e un pianista hanno concluso oltre due mesi di addestramento e sono stati assegnati ai loro posti di lavoro, tra cui uno stabilimento Nestlé a Tianjin; il momento solenne è l'assegnazione di un codice (fùmǎ) che certifica la maturità del prodotto. [Fonte: raw/pillitteri/pillitteri20260926-scuola-robot-hangzhou-primi-diplomi.md]

- **2026-09-28** — Con [[aletta]], autorizzato dalla FDA il 19 agosto 2026, l'automazione robotica entra in una delle procedure manuali più diffuse in medicina: il dispositivo di [[vitestro]] cerca la vena con luce infrarossa e ultrasuoni, controlla il flusso con un modulo Doppler prima di avvicinare l'ago e si ferma se non trova un vaso adatto, con un sensore di movimento che sgancia l'ago se il paziente si muove. La FDA ha autorizzato il 19 agosto 2026 il primo sistema di questo tipo, e il quadro in cui si colloca è quello di tutta la physical AI sanitaria: NVIDIA ha aperto un laboratorio dedicato alla sicurezza dei sistemi di intelligenza artificiale fisica applicati ad auto e robot mentre Google porta avanti il controllo del corpo intero nei robot umanoidi. [Fonte: raw/pillitteri/pillitteri20260928-fda-aletta-robot-prelievo-sangue.md]
- **2026-10-01** — Una ricerca di Anthropic misura che i robot sanno già svolgere il 74% dei compiti dei lavori fisici statunitensi, ma sono economicamente convenienti solo per lo 0,3% a causa dei costi elevati. [Fonte: raw/tldr/tldr20261001.md]
- **2026-10-05** — L'esercito statunitense istituisce l'Army Futures and Autonomous Systems Command, insieme a una nuova figura responsabile degli acquisti per l'autonomia: la struttura integra tecnologie autonome in formazioni, acquisti e addestramento, con interventi su aviazione e altri sistemi. [Fonte: raw/controrumore/controrumore20261005-diario-ai-quando-lai-diventa-un-problema.md]
- **2026-10-06** — [[safeworld]] esce dallo stealth con oltre 12 milioni di dollari per strumenti indipendenti di valutazione della sicurezza dei robot controllati da modelli generativi: replica ambienti reali in simulatori, inserisce il software effettivo del robot e prova migliaia di incontri con modelli umani, tra angoli ciechi, cadute e distanze di arresto. L'obiettivo è una certificazione adatta a sistemi probabilistici in ambienti non strutturati, verificando quanto le simulazioni siano rappresentative delle condizioni reali. [Fonte: raw/controrumore/controrumore20261006-diario-ai-lai-entra-nella-sfera-privata.md]
- **2026-10-09** — H-JEPA, metodo basato su modelli predittivi gerarchici, ha aumentato nei test simulati Visual AntMaze il tasso di successo dal 18 al 73 per cento rispetto a un sistema JEPA non gerarchico, separando azioni immediate e pianificazione di lungo periodo nello spazio delle rappresentazioni latenti e riducendo il calcolo necessario; gli autori riportano risultati anche su video reali del dataset DROID, senza ancora dimostrare affidabilità per robot autonomi in ambienti operativi. [Fonte: raw/controrumore/controrumore20261009-diario-ai-gpt-6-cambia-forma-a-chatgpt.md]
- **2026-10-12** — La finestra commerciale di Optimus resta appesa a un giudizio: a Musk serve un robot di altissima affidabilità e sicurezza per vendere al pubblico entro fine 2027, e le vendite esterne a clienti industriali sarebbero al più presto dal secondo semestre 2027 secondo una presentazione interna a JPMorgan. Prezzo e preordini non esistono, mentre i primi impieghi indicati sono lavori ripetitivi e rischiosi in fabbrica, non la casa. [Fonte: raw/pillitteri/pillitteri20261012-tesla-optimus-vendita-2027-prezzo-preordini.md]
- **2026-10-14** — Physical Intelligence apre la beta della Pi API, che porta i suoi modelli fondativi robotici a addestramento e inferenza: l'utente carica i dati, avvia il fine-tuning su calcolo gestito e recupera i modelli da un gateway ospitato per l'inferenza, mentre l'infrastruttura ML e i pipeline di dati restano al provider. [Fonte: raw/tldr/tldr20261014.md]
- **2026-10-14** — Due demo di Gemini 4 Argon: il robot umanoide Apollo di Apptronik impara a giocare a cornhole guardando un solo video di una persona, e il modello costruisce da zero in Blender un complesso di templi con una pagoda; per nessuna delle due Google pubblica tempi, costi o numero di tentativi. [Fonte: raw/pillitteri/pillitteri20261014-gemini-4-argon-robot-cornhole-pagoda-blender.md]
- **2026-10-14** — RobCo, startup di Monaco di Baviera che costruisce bracci robotici modulari per le fabbriche, supera il miliardo di dollari di valutazione il 5 ottobre 2026, il doppio dei circa 500 milioni di gennaio, in un'operazione che unisce nuovo capitale e una vendita di azioni da parte dei dipendenti. I bracci si montano come mattoncini, si programmano senza scrivere codice e imparano un compito guardandolo dimostrare, con un modello in abbonamento (robotics-as-a-service) che mette hardware e software sulla stessa piattaforma; la società serve soprattutto medie imprese manifatturiere e i tre fondatori, Roman Hölzl, Paul Maroldt e Constantin Dresel, erano ricercatori della cattedra di robotica e intelligenza artificiale dell'Università tecnica di Monaco. [Fonte: raw/pillitteri/pillitteri20261014-robco-unicorno-miliardo-dollari.md]



- **2026-10-15** — RoboParty presenta RP1, piattaforma robotica umanoide completamente open source con CAD meccanico, progetto degli attuatori, sistemi elettrici, firmware, driver, modelli di simulazione e strumenti di addestramento, che ha dimostrato camminata continua, recupero da disturbi e tracciamento del movimento umano. [Fonte: raw/puntate/ainews20261015.md]

- **2026-10-15** — In Cina crescono i lavori di raccolta dati per l'addestramento dei robot: persone con sensori ripetono gesti come piegare vestiti, lavare piatti e afferrare oggetti centinaia di volte al giorno, con compensi indicativi da 4.000 a 6.000 yuan al mese. [Fonte: raw/controrumore/controrumore20261015-diario-ai-sicurezza-lavoro-e-nuove.md]
- **2026-10-16** — La cinese [[dexforce]] addestra umanoidi con ambienti virtuali e dati sintetici per la manipolazione, puntando a fabbriche, uffici e case senza atlete dimostrative. Round da un miliardo di yuan, verifiche indipendenti in attesa. [Fonte: raw/controrumore/controrumore20261016-diario-ai-lintelligenza-artificiale.md]
- **2026-10-17** — Aziende di robotica pagano persone, con compensi da uno a trenta dollari l'ora, per registrare attività quotidiane con videocamere indossabili e sensori, trasformando i movimenti umani in dati di addestramento per robot. [Fonte: raw/controrumore/controrumore20261017-diario-ai-regole-agenti-e-nuovi-costi.md]

- **2026-10-19** — Al 22 giugno 2026 le startup di robotica avevano già raccolto 18,8 miliardi di dollari, contro i 15 dell'intero 2025 e i 14,1 del picco precedente nel 2021 secondo Crunchbase, con round da 1,4 miliardi per Skild AI guidato da SoftBank e fino a 1,4 per Neura Robotics con Tether in testa. Il collo di bottiglia resta il dato sull'interazione fisica: secondo The Robot Report i dataset di teleoperazione sono oltre 100.000 volte più piccoli di quelli linguistici, e XDOF (uscita allo scoperto a giugno con 70 milioni, autrice del dataset open source ABC-130K da 130.000 traiettorie) propone una piramide che parte dai video egocentrici, mentre Open X-Embodiment ha mostrato che i dati di robot diversi messi insieme valgono più della loro somma. [Fonte: raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md]

- **2026-10-19** — [[nvidia]] descrive la physical AI come una pipeline a tre computer: DGX per addestrare i modelli di fondazione, Omniverse e Cosmos per simulare con Isaac Lab e Isaac Sim, Jetson Thor a bordo del robot. Al GTC di marzo 2026 Isaac GR00T N1.7 è in accesso anticipato con licenza commerciale e GR00T N2 è annunciato per fine anno con «più del doppio» dei successi rispetto ai migliori modelli VLA, risultato dichiarato su un modello non ancora disponibile; i world model restano invece un contenitore di approcci diversi, tra Cosmos 3 (32 e 8 miliardi di parametri), Street View collegato a Genie 3 con 280 miliardi di immagini, Atlas di World Labs, i JEPA di AMI Labs con 1,03 miliardi raccolti e Project Prometheus da 12 miliardi, e nessuno chiude da solo il problema. [Fonte: raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md]

- **2026-10-19** — Lo stato dell'arte misurato: Figure 03 completa 237 prove su 420 (il 56%) in 30 case sconosciute, Tesla Optimus resta senza prezzo e senza preordini con vendita promessa entro fine 2027, 1X NEO è in prevendita a 20.000 dollari con una mano a 25 gradi di libertà e la papera open source Microduck parte da 399 dollari. In Europa RobCo supera il miliardo di valutazione, Lutech ha presentato L.u.c.a. e Neura Robotics con l'Università Tecnica di Monaco apre il TUM RoboGym da 2.300 metri quadri; dal 20 gennaio 2027 il Regolamento macchine (UE) 2023/1230 sostituisce la direttiva 2006/42/CE e va letto insieme all'AI Act, mentre Halos di NVIDIA resta un controllo documentale e non una certificazione del prodotto finito. [Fonte: raw/pillitteri/pillitteri20261019-physical-ai-cos-e-come-funziona.md]

- **2026-10-19** — NeodraDynamics Robotics, startup di Pechino nata nel 2024 e guidata dal fondatore Yang Tao, presenta alla China International Industry Fair Neo1, un umanoide alto circa 4 metri e pesante 1,2 tonnellate che dichiara 500 kg di carico con due braccia, 41 gradi di libertà (39 mossi da attuatori idraulici lineari e 2 elettrici ai polsi) e un micro cilindro idraulico digitale da 1,1 kg capace, secondo l'azienda, di muovere 1.000 kg con ripetibilità al micrometro. I numeri vengono solo dal produttore: nessun terzo ha visto la macchina lavorare, le due precisioni diffuse (±0,05 mm a settembre, circa ±0,005 mm a ottobre) differiscono di dieci volte e i documenti non spiegano perché, non è chiaro se Neo1 cammini e prezzo, autonomia, clienti e data di vendita non sono stati comunicati. [Fonte: raw/pillitteri/pillitteri20261019-neo1-robot-umanoide-4-metri-cina.md]

- **2026-10-19** — [[vangrid]] è la startup olandese che paga chi filma luoghi con lo smartphone e consegna modelli 3D alle aziende che addestrano robot: al 19 ottobre l'explorer pubblico conta 1.304.193 catture, 2.644.152 eventi e 458.021 wallet attivi (che non sono persone né dispositivi) e la bacheca 620.030 dollari di bounty accettati su 636.514 finanziati (942 su 973, con tempo mediano di accettazione di circa 6 ore), con premi in USDC su Base e dalla fine di settembre su Arc e una commissione del 10%. Il seed da 9 milioni annunciato il 6 agosto è una dichiarazione del CEO riportata da The Block senza conferme indipendenti, i punti PTC non hanno valore monetario e non si convertono in $VAN secondo il whitepaper, e l'ancoraggio on-chain prova esistenza, ordine e integrità della ripresa ma non che la scena sia quella dichiarata. [Fonte: raw/pillitteri/pillitteri20261019-vangrid-cos-e-come-funziona.md]
- **2026-10-20** — Un dirigente di Siemens indica l'AI come leva per portare l'automazione manifatturiera dal 30-40% al 70-80% e collega l'obiettivo a incrementi di produttività annui del 7-9%, con 500 milioni di euro di investimenti a Erlangen entro il 2030 e la collaborazione con Nvidia su gemelli digitali e physical AI. [Fonte: raw/controrumore/controrumore20261020-diario-ai-rischi-costi-e-nuove-regole.md]
- **2026-10-21** — [[eka-robotics]] raccoglie 150 milioni di dollari in Series A a 1,45 miliardi di valutazione post-money per robot che manipolano oggetti con modelli di AI fisica, sensori di forza e simulazioni, dichiarando oltre il 95 per cento di prese riuscite e circa 1.500 oggetti movimentati all'ora; i piloti industriali sono in corso e TechCrunch non presenta quei dati come benchmark indipendente. [Fonte: raw/controrumore/controrumore20261021-diario-ai-regole-salute-e-infrastrutture.md]
- **2026-10-21** — Unitree pubblica il video di H2-X, l'umanoide che salta da una piattaforma di 4 metri, sfonda a calci la portiera di un'auto e ne solleva il muso per liberare un manichino, presentato come robot da guardia e da soccorso con circa 8 ore di autonomia dichiarata a robot fermo; il filmato supera 9,7 milioni di visualizzazioni in due giorni e porta in sovrimpressione la precisazione che non c'è accelerazione. [Fonte: raw/pillitteri/pillitteri20261024-unitree-h2-x-robot-solleva-auto-salta-4-metri.md]



- **2026-10-22** — La dimostrazione di NVIDIA a Berlino mostra la catena di addestramento di un robot: l'agente AI prepara il percorso, il robot viene simulato in Isaac Sim, i lavori partono verso il cloud e la policy appresa torna sul portatile per la valutazione prima di essere caricata sull'hardware fisico. Il portatile quindi non addestra da solo, e la demo non misura il passaggio dalla simulazione al pavimento vero. [Fonte: raw/pillitteri/pillitteri20261022-huang-microduck-robot-gtc-berlino-rtx-spark.md]
- **2026-10-23** — Nvidia pubblica su Hugging Face SimReady Central, libreria gratuita con oltre duemila asset OpenUSD per simulazioni robotiche e gemelli digitali di fabbrica: può ridurre il lavoro per preparare scenari e dati sintetici, ma non prova che i robot generalizzino meglio nel mondo reale. [Fonte: raw/controrumore/controrumore20261023-diario-ai-agenti-sotto-osservazione.md]
- **2026-10-23** — Nella fabbrica Siemens di Erlangen un agente AI costruisce scenari di produzione all'arrivo degli ordini, valutando capacità, materiali e date di consegna, e li fa provare ai pianificatori sul gemello digitale dell'impianto prima di scegliere. Il sistema gira in prova dentro la produzione reale, non in un laboratorio, e l'azienda stima risparmi fino al 20 per cento. [Fonte: raw/myclaw/myclaw20261023-agents-plan-factory-production.md]
- **2026-10-27** — Un test su nove modelli multimodali e sei compiti con bracci robotici reali, condotto fra luglio e ottobre, rileva una capacità che raddoppia circa ogni 54 giorni, con il miglior tasso di esecuzione cresciuto di 4,4 volte e il costo per sotto-compito sceso di 6,2 volte. I modelli sono limitati soprattutto da efficienza e precisione, non dal ragionamento; le misure arrivano da un'analisi pubblicata su LessWrong e non da una valutazione indipendente. [Fonte: raw/tldr/tldr20261027.md]
- **2026-10-27** — Il Dipartimento della Sicurezza Interna ha assegnato il 25 settembre un contratto da 1,3 milioni di dollari a Radeco per quattro Spot di Boston Dynamics trasformati in Cerberus, destinati all'ICE, con il costruttore nel ruolo di supporto tecnico; più di 300 dipendenti su circa 1.400 avevano firmato a inizio settembre una petizione contro la vendita, e l'azienda ha confermato di procedere. Il caso sposta il dibattito della robotica commerciale dal prodotto al cliente: le condizioni di vendita vietano l'uso come arma ma non l'impiego come occhio mobile con zoom e termocamera, e la distinzione fra indagini transnazionali ed espulsioni vale meno di quanto l'azienda sostenga. [Fonte: raw/pillitteri/pillitteri20261027-boston-dynamics-cani-robot-spot-ice-dipendenti.md]
- **2026-10-27** — Uno studio dell'Università di Scienza e Tecnologia di Pechino, pubblicato in accesso libero su npj Robotics il 7 ottobre, addestra una rete neurale su 95 voli di una farfalla robotica da 48,3 grammi e usa un agente di reinforcement learning per scegliere la forma di 19 coppie di ali: l'aumento del 339 per cento riguarda un indice degli autori, angolo di salita diviso frequenza di battito, non la portanza in newton, e l'angolo di salita passa da 7,9 a 33,6 gradi. Contro la migliore ala a parametro singolo il vantaggio scende a +59 per cento sull'angolo e +19 per cento sulla velocità, e le ali ottime stanno al bordo dell'intervallo provato, quindi il metodo conta più del numero. [Fonte: raw/pillitteri/pillitteri20261027-farfalla-robotica-ia-ali-npj-robotics.md]
- **2026-10-28** — Nella demo di [[genie-4]] il robot umanoide Apollo di Apptronik gioca a dama mentre Gemini 3.8 Flash fa da agente guida, osserva la scena, scompone l'obiettivo in passi, controlla i fotogrammi e corregge il piano, con Gemini 4 Argon e Gemini Robotics nello stesso ciclo di simulazione. Google presenta il world model come campo di prova per robot e agenti, dove un robot virtuale può imparare un compito senza rompere niente. [Fonte: raw/pillitteri/pillitteri20261027-genie-4-google-deepmind-world-model.md]
- **2026-10-31** — [[walmart]] e [[symbotic]] hanno ampliato l'accordo per automatizzare altri 25 centri di distribuzione statunitensi, con un impegno iniziale di circa 6 miliardi di dollari distribuito su più anni e il software AI del fornitore a coordinare il movimento delle merci. La cifra non rappresenta ricavi già contabilizzati e i benefici attesi su scorte, servizio e dipendenti non sono ancora misurati indipendentemente. [Fonte: raw/controrumore/controrumore20261031-diario-ai-agenti-mercati-e-nuove.md]
- **2026-10-31** — La Casa Bianca ha definito le importazioni di robotica e macchinari industriali una possibile minaccia alla sicurezza nazionale e ha disposto negoziati con i partner commerciali senza applicare nuovi dazi nell'immediato; la proclamazione riguarda anche robot autonomi e umanoidi e richiama dipendenze produttive e possibili vulnerabilità dei sistemi stranieri. Tariffe, quote o altre restrizioni restano opzioni future. [Fonte: raw/controrumore/controrumore20261031-diario-ai-agenti-mercati-e-nuove.md]
































































## Collegamenti

- [[anthropic]]
- [[claude-opus-4-7]]
- [[gemini-robotics-2]]
- [[google-deepmind]]
- [[openai]]
- [[sam-altman]]
- [[world-models]]
[[jumper]]
- [[index]]
- [[rp1]]
- [[dexforce]]
- [[cosmos-3]]
- [[ami-labs]]
- [[vangrid]]
- [[figure-ai]]
- [[1x-technologies]]
- [[unitree]]
- [[siemens]]
