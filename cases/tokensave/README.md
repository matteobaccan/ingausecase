# tokensave

Inga come **host MCP**: un modello locale risponde a domande su un codice vero con gli
strumenti di [tokensave](https://github.com/aovestdipaperino/tokensave) (licenza MIT), un
server MCP che indicizza il progetto con tree-sitter (simboli, chiamate, eredità) e
risponde con `tokensave_search`, `tokensave_callers`, `tokensave_context`, ...

- **Programma:** tokensave 7.16.0, il binario della release per Linux x86_64 (voce
  `tokensave-linux` di [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json):
  URL, sha256, dimensione; lo sha256 è anche quello di `SHA256SUMS` della release).
  Gira con la sua home nella cartella di lavoro, senza contatore mondiale
  (`disable-upload-counter`), senza controllo della versione e senza indicizzare da sé.
- **Progetto:** [itsdangerous](https://github.com/pallets/itsdangerous) 2.2.0 (BSD-3-Clause,
  commit `096c8d4` in [`domande.json`](domande.json)), clonato a ogni esecuzione e
  indicizzato con `tokensave init`; se il tag non è più a quel commit, il caso si ferma.
- **Host MCP:** il runner scrive [`mcp.json`](mcp.json) nella home di Inga (`{lavoro}` è
  la cartella di lavoro) e avvia `inga serve --mcp ... --allow-mcp-commands
  --mcp-auto-approve ...` (`case.json`: `mcp`, `argomenti_serve`); gli altri casi restano
  con `--no-mcp`. Il caso approva il comando del server (`POST /api/inga/mcp/servers`) e
  si collega (`POST /api/inga/mcp/connect`). Le chiamate approvate sono solo quelle degli
  strumenti in lettura: una chiamata a un altro (le modifiche ai file) è rifiutata e
  Inga lo dice al modello.
- **Domande:** 20, con le risposte verificate leggendo quel commit (`verifica` dice
  dove): quale file definisce una classe, cosa solleva una funzione, quali classi ne
  ereditano un'altra, chi chiama una funzione, quante eccezioni ci sono. Una risposta è
  giusta se contiene la stringa attesa (una di `una`, o tutte quelle di `tutte`), a
  parole intere.

Ogni domanda in tre modi, a temperatura 0, un modo alla volta (la cache dei prefissi
riprende il prompt di sistema):

1. **con tokensave:** la richiesta chiede gli strumenti del server (`"inga_mcp":
   ["tokensave"]`); Inga li offre al modello, esegue le chiamate e gli ridà i risultati
   fino alla risposta; le chiamate sono in `inga_mcp_calls`;
2. **senza strumenti:** il modello risponde con quello che sa (la base);
3. **codice nel prompt:** i sorgenti di `src/itsdangerous` (circa 42 KB) nel prompt di
   sistema, l'alternativa senza strumenti a cui tokensave vuole risparmiare token.

**Voto:** le risposte giuste con tokensave. Voci: le giuste in ogni modo, le domande con
almeno una chiamata a tokensave, e i rapporti dei token per domanda (dall'usage
dell'API): del prompt con tokensave su quelli col codice nel prompt, dei generati con
tokensave su quelli senza strumenti. I numeri assoluti per domanda
(token del prompt, generati, chiamate, chiamate rifiutate, secondi) sono nei dettagli
(`per_domanda`), con ogni risposta e le sue chiamate.

Come contano i token: con gli strumenti `prompt_tokens` è il prompt dell'**ultimo** giro
(le definizioni degli strumenti, la domanda, le chiamate e i loro risultati), non la
somma dei giri; `completion_tokens` è la somma dei token generati in tutti i giri. Le
definizioni dei 12 strumenti che tokensave mostra all'inizio (gli altri si chiedono con
`tokensave_more`) pesano qualche migliaio di token in ogni richiesta con gli strumenti.

Se il modello non chiama gli strumenti (un modello troppo piccolo), il caso gira lo
stesso e lo dice (`nota` nei dettagli). Se l'host MCP di Inga non avvia tokensave o non
si collega, il caso va in errore con il motivo che Inga dà.
