# gsm8k

Problemi di aritmetica a parole di [GSM8K](https://huggingface.co/datasets/openai/gsm8k)
(Cobbe et al. 2021, licenza MIT), posti **a Inga e a llama.cpp** con lo stesso file del
modello, sulla stessa macchina, greedy.

- **Dati:** il test di GSM8K, scaricato a ogni esecuzione da [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json)
  (revisione fissata, sha256 controllato).
- **Domande:** 30 fisse (seed 8). Il modello ragiona in breve e chiude con
  `Answer: <numero>`. È giusta se il numero è quello di GSM8K.
- **Voto:** le risposte giuste di Inga. Voci: Inga, llama.cpp, la differenza, le
  risposte con lo stesso testo (greedy, le due dovrebbero coincidere quasi sempre), il
  tempo di llama.cpp su quello di Inga.

Serve a tre cose: vedere se Inga risponde come llama.cpp (template, campionamento,
calcoli), confrontare la velocità su risposte vere e scegliere il modello (lo stesso
caso con `--model`). I numeri non sono quelli pubblicati sulle schede dei modelli (altri
prompt, piena precisione).
