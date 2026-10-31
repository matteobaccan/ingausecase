# PDF

Estrazione di dati da PDF (caso aziendale 7). [`genera.py`](genera.py) crea a ogni
esecuzione, con un seed fisso, 20 documenti sintetici in italiano (fatture in due
impaginazioni e ordini d'acquisto) come PDF di testo, e la loro verità in
`verita.json`; i PDF non sono nel repository. Nomi di aziende, indirizzi e partite IVA
sono inventati (le partite IVA hanno solo la cifra di controllo giusta).

[`run.py`](run.py) estrae il testo di ogni PDF con pypdf e chiede a Inga, con l'output
strutturato (`response_format` con uno schema JSON), questi campi: `numero`, `data`
(AAAA-MM-GG), `fornitore`, `partita_iva` (del fornitore, non del cliente),
`imponibile`, `iva`, `totale`, `righe` (descrizione, quantità, prezzo unitario,
importo).

Come si dà il voto: campi esatti sul totale dei campi (8 per documento, 160 in tutto).
Gli importi valgono se uguali al centesimo, i testi dopo aver tolto maiuscole, spazi e
punteggiatura (`S.r.l.` = `Srl`), la partita IVA sulle sole cifre; `righe` vale solo se
tutte le righe sono giuste e nello stesso numero. Le voci del risultato danno
l'accuratezza di ogni campo e quella delle righe prese una per una; i dettagli elencano
i campi sbagliati con il valore atteso e quello dato.
