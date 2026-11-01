# Documenti

Domande su una base di documenti (caso aziendale 1): 15 domande sulle pagine della
[wiki](../../wiki) di AINews, ciascuna con il dato atteso e la pagina che lo contiene
([`domande.json`](domande.json); ogni risposta è stata controllata nella sua pagina).

## Come funziona

Il caso usa le **collezioni di documenti di Inga** (la funzione "chat con i documenti"):
il runner avvia `inga serve` con il modello di chat (`qwen3-4b`) e, accanto, il piccolo
modello di embedding multilingue `minilm-multilingue` di
[`models.json`](../../models.json), e lo sceglie come modello di embedding del server.
[`run.py`](run.py) mette nella collezione `wiki`, con `POST /api/inga/documents`:

- le 15 pagine con le risposte;
- 45 altre pagine della wiki, di tutte le cartelle, scelte con un seed fisso fra quelle
  che non contengono nessuna delle risposte attese;
- la **Divina Commedia** (chiave `divina-commedia` di [`fonti.json`](../../fonti.json):
  il PDF si scarica a ogni esecuzione, non è nel repository, si controlla con il suo
  sha256 e lo legge Inga stessa), un testo lungo che non c'entra.

Ogni domanda nomina la collezione (`"inga_documents": [{"collection": "wiki"}]`): Inga
cerca gli estratti più vicini (ricerca ibrida, vettori e BM25) fra tutte le 61
sorgenti e li mette nel prompt, entro un terzo del contesto di 8192 token. Il modello
deve quindi trovare la parte giusta, non più leggere tre pagine date. La risposta è
strutturata: `risposta` (una frase) e `sorgente`, il numero `[n]` dell'estratto da cui
viene, come Inga numera gli estratti nel prompt; la pagina citata è quella di
quell'estratto (dal campo `inga_documents` della risposta). La chiave `sorgente` viene
dopo `risposta` in ordine alfabetico, l'ordine in cui Inga scrive le chiavi: il modello
sceglie l'estratto dopo aver scritto la risposta.

Fino alla 0.40.0 il caso dava a Inga, per ogni domanda, la pagina giusta e due altre
pagine intere: il voto della 0.40.0 (100) non è confrontabile con quelli di oggi.

## Come si dà il voto

La media di due cose, contate su tutte le domande: la risposta contiene il dato atteso
(uno dei testi di `risposte`, confrontati senza maiuscole, spazi e punteggiatura) e la
pagina citata è quella giusta. Le voci riportano anche, fuori dal voto, quante volte la
pagina giusta era fra gli estratti e quale parte degli estratti veniva dalla Divina
Commedia.
