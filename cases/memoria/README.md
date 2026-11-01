# memoria

La memoria fra sessioni di Inga (i progetti: diario, regole, stile) su un test pubblico,
[LongMemEval](https://huggingface.co/datasets/xiaowu0162/longmemeval-cleaned) (Wu et al.,
ICLR 2025, licenza MIT), nella versione "oracle": per ogni domanda solo le sessioni di
chat che servono.

- **Dati:** scaricati a ogni esecuzione da [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json)
  (revisione fissata, sha256 controllato), mai nel repository.
- **Domande** (seed 3, sessioni fino a 25.000 caratteri in tutto): 2 per tipo, cioè un
  fatto detto in una sessione, un conto su più sessioni, il ragionamento sulle date e un
  fatto aggiornato, più 2 domande senza risposta, di due tipi (la risposta giusta è non saperlo).
- **Percorso:** per ogni domanda un progetto nuovo. Ogni sessione viene scritta nella
  memoria dal modello, come alla fine di una chat nella web UI
  (`POST /api/inga/memory/{p}/write`, con la data della sessione come orario). Poi la
  domanda in una chat nuova, in tre modi:
  - **oggi:** il system prompt della chat di un progetto (istruzioni, regole, stile;
    il diario non entra nel prompt);
  - **diario:** lo stesso più i file del diario;
  - **tutta la chat:** le sessioni intere nel prompt, senza memoria (il riferimento).
- **Voto:** le risposte giuste nel modo "oggi". Le voci danno i tre modi, i tipi di
  domanda, quante sessioni il modello ha scritto nel diario e quante risposte contengono
  il testo atteso.
- **Giudice:** lo stesso modello, con le istruzioni di giudizio di LongMemEval (sì/no), sul
  testo della risposta. Le domande senza risposta sono giuste solo con `known: false`.
  LongMemEval usa GPT-4o: con un modello piccolo il giudizio è meno affidabile, quindi va
  letto insieme alla voce "testo atteso contenuto".

Differenze da LongMemEval: le sessioni sono scritte con la data di oggi nel diario e la
loro data originale come orario; lo stile della persona viene svuotato prima di ogni
domanda. Le versioni di Inga senza i progetti danno il caso come saltato.

Sono poche domande (10) perché su un runner di GitHub ogni risposta con qwen3-4b costa
qualche minuto: il voto si muove a passi di 10 punti, quindi una differenza di una
domanda fra due versioni non è un segnale.
