---
title: "Stampa 3D e IA"
category: trend
tags: [stampa-3d, cad, hardware, agent-skills, open-source]
related_puntate: []
created: 2026-09-25
updated: 2026-09-25
---

# Stampa 3D e IA

## Introduzione

Per iniziare con la stampa 3D nel 2026 bastano una stampante a filamento con calibrazione automatica, che parte da circa 200 euro, e due programmi gratuiti: uno slicer come Bambu Studio o OrcaSlicer e un CAD come Tinkercad. Il resto si impara stampando, e l'intelligenza artificiale accorcia proprio la parte più ostica, cioè il disegno dei pezzi: cinque anni fa la prima settimana se ne andava a livellare il piatto con un foglio di carta, oggi una Bambu Lab A1 mini si monta in una ventina di minuti e si calibra da sola.

## Hardware e software

- La scelta per chi inizia è quasi sempre il filamento (FDM), che costa meno e perdona gli errori, mentre la resina (MSLA) vince sul dettaglio delle miniature al prezzo di un flusso di lavoro fatto di guanti in nitrile, lavaggio in alcol isopropilico e polimerizzazione sotto lampada UV.
- Le fasce indicative del mercato europeo a settembre 2026, IVA inclusa: Creality Ender-3 V3 SE sotto i 200 euro per il budget minimo, Bambu Lab A1 mini intorno ai 200 per il primo acquisto, A1 Combo o P1S intorno ai 400 per il multicolore o per una CoreXY chiusa, P2S Combo intorno ai 750 per l'uso intenso, Prusa Core One da 1.349 per laboratori e riparabilità con firmware aperto, Elegoo Saturn 4 Ultra 16K intorno ai 490 per le miniature.
- Ogni stampa passa da tre stadi — modello, slicing, G-code — e tutti i programmi necessari sono gratuiti: Bambu Studio, OrcaSlicer e PrusaSlicer fra gli slicer, Tinkercad, Autodesk Fusion, FreeCAD 1.1, OpenSCAD e Blender fra i CAD.
- Un dettaglio da mettere nel conto prima di comprare: da inizio 2025 il firmware Bambu Lab filtra i comandi inviati da programmi di terze parti, quindi chi vuole comandare la stampante da uno script, da Home Assistant o da un agente deve attivare la modalità LAN con l'opzione sviluppatore e rinunciare all'accesso remoto via cloud; Prusa, con firmware aperto, non pone questo vincolo.

## L'IA nella stampa 3D

- L'IA entra in tre punti diversi, che conviene tenere separati: genera modelli da una foto o da una frase, scrive il codice di pezzi tecnici con misure precise e sorveglia la stampa mentre è in corso.
- Sul primo fronte, dal 17 marzo 2026 Meshy è integrato nel MakerLab di MakerWorld e converte una foto in un modello 3D con le texture, con un'opzione che traduce i colori in zone assegnate alle bobine dell'AMS e un export 3MF pronto per la stampa multicolore al costo di due crediti a esportazione; lo stesso lavoro lo fanno [[tripo]], che a settembre ha raccolto 446 milioni di dollari lanciando P2.0, e Rodin di Hyper3D, mentre in locale restano i progetti open source Hunyuan3D-2 di Tencent (14.965 stelle) e TRELLIS di Microsoft (13.700, licenza MIT), entrambi con almeno 16 GB di memoria video consigliata.
- Qui sta l'equivoco più comune fra chi inizia: i generatori image-to-3D producono una mesh, cioè una superficie di migliaia di triangoli senza quote, e un supporto con due fori per viti M4 a 40 millimetri di distanza esce con i fori dove capita; i pezzi funzionali richiedono un modello parametrico, e proprio lì i modelli linguistici danno il meglio, perché OpenSCAD, CadQuery e build123d descrivono il pezzo con righe di codice che un agente come [[claude-code]] o [[codex]] scrive, esegue, guarda e corregge.
- Il terzo uso è il più concreto per chi stampa ogni giorno: le telecamere delle stampanti recenti analizzano ogni strato e fermano il lavoro quando qualcosa va storto, con la P2S che riconosce il classico "spaghetti" — il filamento aggrovigliato nel vuoto quando il pezzo si stacca — le sbavature fra un pezzo e l'altro e gli oggetti dimenticati sul piatto, e per le macchine senza telecamera c'è Obico, piattaforma open source (1.908 stelle) che aggiunge il rilevamento dei guasti alle stampanti con OctoPrint, Klipper o Duet.

## Skill per la progettazione parametrica

- Le skill trasformano una richiesta in italiano — "un coperchio a incastro per questa scatola da 80 per 60 millimetri" — in un modello parametrico, controllano che il risultato sia stampabile ed esportano il file per lo slicer, e Claude Code e Codex condividono il formato aperto [[agent-skills]] documentato su agentskills.io.
- I progetti più solidi a settembre 2026: cad-skill di flowful-ai per Claude Code con motore CadQuery (581 stelle, licenza PolyForm Noncommercial che ne vieta l'uso commerciale, richiede Python fra 3.10 e 3.12), openscad-agent (129 stelle), codex-cad di Alexander Koller per Codex con CadQuery e FreeCAD (licenza MIT, verifica di stampabilità con Bambu Studio), build123d-mcp come server MCP per Claude Code, Codex CLI e Cursor (94 stelle, Apache-2.0), mcp-3D-printer-server per il controllo delle stampanti (238 stelle, GPL-2.0) e blender-mcp (29.314 stelle, MIT).
- Un dato che misura l'effetto del ponte MCP: secondo l'autore di build123d-mcp, sulla classifica pubblica CADGenBench di giugno 2026 lo stesso modello linguistico è passato da un punteggio di 0,360 a 0,457 usando il server, con i modelli validi saliti dall'88 al 100 per cento.
- L'avvertenza che vale più di tutte: un agente sbaglia le misure con la stessa sicurezza con cui le azzecca, quindi prima di stampare un pezzo che deve accoppiarsi con un oggetto reale conviene controllare le quote nell'anteprima e confrontarle con un calibro, e non lasciare che un agente avvii da solo una stampa su una macchina che nessuno sorveglia.

## Timeline delle notizie

- **2026-09-25** — La guida mette in fila hardware, software, corsi gratuiti e strumenti IA per chi parte da zero nella stampa 3D nel 2026: circa 250 euro fra stampante entry level, prima bobina di PLA e calibro digitale, tutti i programmi necessari gratuiti dallo slicer al CAD, e l'IA che si occupa della parte più ostica, cioè il disegno dei pezzi. La skill più popolare per far progettare pezzi a Claude Code, cad-skill di flowful-ai, conta 581 stelle su GitHub, mentre i generatori image-to-3D come Meshy e [[tripo]] restano utili per le forme organiche e inadatti ai pezzi funzionali, che richiedono quote esatte.

## Collegamenti

- [[agent-skills]]
- [[agenti-ai]]
- [[claude-code]]
- [[codex]]
- [[formazione-ai]]
- [[tripo]]
- [[index]]
