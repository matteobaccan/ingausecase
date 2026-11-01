# velocita

Inga contro llama.cpp sullo stesso file del modello e sulla stessa macchina (un runner
di GitHub, solo CPU), con llama.cpp compilato lì per quella CPU, alla versione di
[`llama-cpp.txt`](https://github.com/matteobaccan/ingausecase/blob/cases/llama-cpp.txt).

- **Velocità:** `inga bench -p 512 -n 128 -r 3` e `llama-bench -p 512 -n 128 -r 3`, con
  tutti i thread. Voci: la lettura del prompt (pp512) e la generazione (tg128) di Inga
  divise per quelle di llama.cpp (100 = uguali, sopra 100 Inga è più veloce).
- **Perplexity:** `inga perplexity` e `llama-perplexity` sul test di wikitext-2 (lo stesso
  file che usa llama.cpp, da [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json)),
  40 pezzi da 512 token. Voce: quella di Inga divisa per quella di llama.cpp; deve stare
  vicina a 100 (la rotazione notturna di Inga chiede l'1 %).
- **Voto:** la media dei due rapporti di velocità.

I tok/s di ognuno sono nei dettagli del JSON. I runner di GitHub non hanno sempre la
stessa CPU: i rapporti, misurati sulla stessa macchina nello stesso job, si confrontano
fra versioni; i tok/s da soli no.
