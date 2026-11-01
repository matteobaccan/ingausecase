# arc

Domande di scienze a scelta multipla di
[ARC-Challenge](https://huggingface.co/datasets/allenai/ai2_arc) (Clark et al. 2018,
licenza CC BY-SA 4.0), poste **a Inga e a llama.cpp** con lo stesso file del modello,
sulla stessa macchina, greedy.

- **Dati:** il test di ARC-Challenge, scaricato a ogni esecuzione da
  [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json).
- **Domande:** 60 fisse (seed 9). La risposta è `Answer: <lettera>`; giusta se è quella
  di ARC.
- **Voto e voci:** come [`gsm8k`](https://github.com/matteobaccan/ingausecase/tree/cases/cases/gsm8k).

Risposte brevi (al massimo 256 token, per i modelli che ragionano prima di rispondere):
misura soprattutto la lettura del prompt e la conoscenza del modello. La lettera è
l'ultimo `Answer: X`, altrimenti `answer is X`, altrimenti una lettera da sola all'inizio.
