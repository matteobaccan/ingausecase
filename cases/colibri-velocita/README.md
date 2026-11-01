# colibri-velocita

La velocità di Inga e quella di [Colibri](https://github.com/JustVugg/colibri) sullo
stesso file del modello e sulla stessa macchina (un runner di GitHub, solo CPU), con
Colibri compilato lì al commit di [`colibri.txt`](https://github.com/matteobaccan/ingausecase/blob/cases/colibri.txt).

Colibri non ha un comando come `inga bench` o `llama-bench` (il suo `coli bench` dà voti
di qualità, solo per GLM), e allora la misura passa per tutti e due dall'API in
streaming, con le stesse richieste:

- un prompt di circa 512 token (frasi sintetiche, contate una volta con l'usage di
  Inga) che chiede di contare fino a 1000, così la risposta arriva sempre a 128 token;
  3 ripetizioni per motore, ognuna con la prima riga diversa (la cache dei prefissi non
  aiuta), dopo una richiesta di riscaldamento;
- **lettura del prompt:** i token del prompt (usage) sul tempo fino al primo token;
- **generazione:** i 127 token dopo il primo sul tempo dopo il primo;
- in più `tools/benchmark_http_serving.py` di Colibri (lo strumento con cui Colibri
  misura un server OpenAI in streaming) su altri 3 prompt uguali per forma, contro i due
  server: token generati al secondo, dall'inizio alla fine di ogni richiesta.

Voci: i rapporti Inga su Colibri (100 = uguali, sopra 100 Inga è più veloce). Voto: la
media dei rapporti di lettura e generazione. Ogni motore usa i suoi thread (Colibri
quanti ne sceglie da sé, nei dettagli). I tempi comprendono l'HTTP e il template, come
per un client vero; i rapporti si confrontano fra versioni, i tok/s da soli no (i
runner non hanno sempre la stessa CPU).
