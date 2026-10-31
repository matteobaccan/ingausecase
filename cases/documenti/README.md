# Documenti

Domande su una base di documenti (caso aziendale 1): 15 domande sulle pagine della
[wiki](../../wiki) di AINews, ciascuna con il dato atteso e la pagina che lo contiene
([`domande.json`](domande.json); ogni risposta è stata controllata nella sua pagina).

Per ogni domanda Inga riceve tre pagine intere come documenti, con il campo
`inga_documents` della richiesta (la funzione "chat con i documenti" di Inga): la
pagina giusta e due pagine della stessa cartella, scelte con un seed fisso fra quelle
che non contengono il dato atteso, in ordine mescolato. **Niente recupero per
embedding (RAG)**: le tre pagine stanno nel terzo del contesto (16384 token) e Inga le
mette intere nel prompt; il risultato registra, per ogni domanda, il modo usato da Inga
(`whole` o `excerpts`). Così il caso misura la lettura e la citazione, non la qualità
di un modello di embedding; un caso con le collezioni e un modello di embedding si può
aggiungere dopo.

La risposta è strutturata: `risposta` (una frase) e `pagina` (una delle tre, con un
`enum`).

Come si dà il voto: la media di due cose, contate su tutte le domande: la risposta
contiene il dato atteso (uno dei testi di `risposte`, confrontati senza maiuscole,
spazi e punteggiatura) e la pagina citata è quella giusta.
