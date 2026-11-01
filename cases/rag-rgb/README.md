# rag-rgb

Due abilità del RAG su un test pubblico,
[RGB](https://github.com/chen700564/RGB) (Chen et al., AAAI 2024; file `en_refine.json`,
licenza CC BY-NC-SA 4.0, solo uso non commerciale): domande su notizie 2022–2023 con
passaggi che contengono la risposta e passaggi sullo stesso tema che non la contengono.

- **Dati:** scaricati a ogni esecuzione da [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json)
  (sha256 controllato), mai nel repository.
- **Rumore** (20 domande, seed 5): 3 passaggi giusti e 3 sbagliati per domanda, tutti in
  una collezione (le altre domande fanno da rumore in più). Giusta se la risposta
  contiene il dato atteso (come RGB: ogni parte, in una delle sue
  varianti).
- **Rifiuto** (20 altre domande): solo passaggi senza la risposta. Giusta se dice che negli
  estratti non c'è (`found: false`) senza darla lo
  stesso: un rifiuto che poi scrive la risposta, presa da quello che il modello sa, è
  sbagliato.
- **Voto:** la media delle due. Voci: le due, quante volte il passaggio giusto era fra gli
  estratti dati al modello, quante risposte date con il rumore.

Le domande sono in inglese, come in RGB. Il caso usa la ricerca della chat
(`inga_documents`), quindi gira anche sulle versioni di Inga senza la ricerca diretta.
