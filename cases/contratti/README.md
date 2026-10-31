# Contratti

Domande con risposta nota su un contratto collettivo: il CCNL Terziario, Distribuzione
e Servizi (Confcommercio, codice CNEL H011). Il testo **non** è nel repository: si
scarica a ogni esecuzione dall'URL di [`fonte.json`](fonte.json), l'unico valore da
impostare.

[`run.py`](run.py) estrae il testo del PDF con pypdf e lo divide per articoli
(`Art. N`). Il contratto è troppo lungo per il contesto di un modello piccolo, quindi
per ogni domanda prende i 4 articoli più vicini per parole in comune (BM25, nel
caso stesso, senza embedding) e li dà a Inga come documenti (`inga_documents`), ognuno
col suo numero; la risposta è strutturata (`risposta` e `articolo`, scelto fra i 4).

Come si dà il voto: per ogni domanda verificata, la risposta deve contenere il dato
atteso (uno dei testi di `risposte`, confrontati senza maiuscole, spazi e
punteggiatura) e l'articolo citato deve essere quello atteso; il voto è la media delle
due cose. Le voci riportano anche quante volte l'articolo atteso era fra i 4 recuperati
(la qualità del recupero, che non dipende da Inga).

## Stato: saltato

Il caso oggi si salta, con il motivo nel risultato e nel riepilogo:

- da questa macchina di sviluppo non si raggiungono né il sito del CNEL né quelli delle
  parti firmatarie, quindi l'URL ufficiale del PDF non è stato verificato e in
  `fonte.json` è `null`;
- le 12 domande di [`domande.json`](domande.json) sono solo le tracce: `risposte` è
  vuoto, `articolo` è `null` e `verificata` è `false`. Vanno completate leggendo il
  testo scaricato (il dato atteso e il numero dell'articolo) e segnate
  `"verificata": true`; il caso usa solo le domande verificate.

Con l'URL impostato e almeno una domanda verificata il caso parte da solo.
