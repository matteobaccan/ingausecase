# Contratti

Domande con risposta nota su un contratto collettivo: il **CCNL Commercio, Terziario,
Distribuzione e Servizi di Conflavoro PMI** (firmato con Confsal, Confsal
Federlavoratori e Fesica il 19 maggio 2026, in vigore dal 01/06/2026 al 31/05/2029; 96
pagine). Il PDF non stampa un codice CNEL, quindi qui non ne è indicato nessuno; non è
il CCNL Terziario di Confcommercio.

Il testo **non** è nel repository: il PDF si scarica a ogni esecuzione dall'URL di
[`fonti.json`](../../fonti.json) (chiave `ccnl`) e si controlla con il suo sha256; se il
file scaricato è cambiato, il caso lo dice e si ferma in errore, senza dare voti su un
testo diverso da quello su cui le domande sono state verificate. La cache di GitHub
tiene il PDF, con la chiave fatta da URL e sha256 (vedi [`tools/`](../../tools)).

## Il distrattore

Nella stessa collezione del contratto c'è la **Divina Commedia** (chiave
`divina-commedia` di `fonti.json`, testo di pubblico dominio, 475 pagine): la risposta
deve venire dal contratto, e gli estratti della Commedia (che parla anche di San
Francesco, di mesi e di numeri) vanno ignorati.

## Come funziona

Il caso usa le **collezioni di documenti di Inga**, non un recupero fatto in proprio:

1. il runner avvia `inga serve` con il modello di chat (`qwen3-4b`) e, accanto, un
   piccolo modello di embedding multilingue (`minilm-multilingue` di
   [`models.json`](../../models.json), 118M parametri, controllato con lo sha256) e lo
   sceglie come modello di embedding del server;
2. [`run.py`](run.py) aggiunge i due PDF alla collezione `contratti` con
   `POST /api/inga/documents`: Inga li legge con il suo lettore di PDF, li divide in
   chunk e li indicizza con i vettori e con BM25 (se Inga rifiutasse un PDF, il caso
   manda il testo estratto da pypdf, pagina per pagina, e lo scrive nel risultato);
3. ogni domanda nomina la collezione (`"inga_documents": [{"collection":
   "contratti"}]`): Inga cerca gli estratti più vicini (ricerca ibrida) e li mette nel
   prompt, entro un terzo del contesto di 8192 token. La risposta è strutturata:
   `risposta` e `sorgente` (il numero dell'articolo; la chiave viene dopo `risposta`
   in ordine alfabetico, l'ordine in cui Inga le scrive, così l'articolo si sceglie
   dopo aver scritto la risposta).

## Le domande

Le 15 domande di [`domande.json`](domande.json) sono state verificate sul testo del
PDF (sha256 di `fonti.json`): ognuna ha le risposte accettate (`risposte`), l'articolo
(`articolo`, come è stampato), la pagina (`pagina`) e una frase esatta del testo che la
prova (`citazione`). Ci sono domande facili (ferie, comporto, quattordicesima) e
difficili (prova per livello, orario dei distributori di carburante, preavviso per
livello e anzianità, part-time sopra i 30 dipendenti, il santo del 4 ottobre).

## Come si dà il voto

Per ogni domanda: la risposta deve contenere il dato atteso (uno dei testi di
`risposte`, confrontati senza maiuscole, spazi e punteggiatura) e l'articolo citato
deve essere quello atteso; il voto è la media delle due cose. Le voci riportano anche
due misure della ricerca, che non entrano nel voto: quante volte la `citazione` era in
un estratto del contratto, e quale parte degli estratti veniva dalla Divina Commedia.
