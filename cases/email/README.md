# Email

Smistamento di email e ticket (caso aziendale 4): 40 messaggi sintetici in italiano,
scritti a mano e fissi ([`messaggi.json`](messaggi.json): `testo`, `urgenza`,
`reparto`), con persone e aziende inventate. Inga classifica ogni messaggio con
l'output strutturato (`response_format` con uno schema JSON i cui campi sono `enum`):

- `urgenza`: `alta`, `media`, `bassa`;
- `reparto`: `amministrazione`, `assistenza_tecnica`, `commerciale`, `logistica`,
  `risorse_umane`.

Le regole date al modello sono nel messaggio di sistema di [`run.py`](run.py).

Come si dà il voto: la media dell'accuratezza su urgenza e su reparto (voto esatto,
nessun punteggio parziale). Le voci del risultato riportano le due accuratezze e la
quota di messaggi con entrambe giuste; i dettagli hanno la confusione (le coppie
`atteso -> dato` sbagliate, con quante volte) e l'elenco dei messaggi sbagliati.

L'urgenza ha una parte di giudizio: le etichette seguono le regole del messaggio di
sistema, e un cambio di voto va letto come tendenza tra versioni.
