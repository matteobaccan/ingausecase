# ifeval

Richieste con istruzioni verificabili di [IFEval](https://huggingface.co/datasets/google/IFEval)
(Zhou et al. 2023, licenza Apache 2.0): "senza virgole", "almeno 300 parole", "in JSON",
"finisci con questa frase"… poste **a Inga e a llama.cpp** con lo stesso file del
modello, sulla stessa macchina, greedy.

- **Dati:** scaricati a ogni esecuzione da [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json).
- **Richieste:** 30 fisse (seed 10), fra le 464 su 541 che usano solo istruzioni
  controllabili da [`verifiche.py`](https://github.com/matteobaccan/ingausecase/blob/cases/cases/ifeval/verifiche.py).
  Restano fuori quelle che chiedono un numero di frasi o una lingua (servirebbero nltk e
  un riconoscitore della lingua).
- **Voto:** la quota delle istruzioni rispettate da Inga (IFEval "instruction-level,
  strict"). Voci: lo stesso per llama.cpp, la differenza, le richieste con tutte le
  istruzioni rispettate (IFEval "prompt-level") di ognuno, le risposte con lo stesso
  testo.

Le verifiche sono riscritte qui: le parole si contano con un'espressione regolare e non
con il tokenizer di nltk, quindi un conteggio può differire di poco da quello ufficiale.
Valgono le stesse per i due motori, che è il confronto che conta.
