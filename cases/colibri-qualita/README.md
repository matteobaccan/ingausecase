# colibri-qualita

Le stesse domande **a Inga e a [Colibri](https://github.com/JustVugg/colibri)** (il
motore in C, licenza Apache-2.0, che legge dal disco gli esperti delle mixture of
experts), con lo stesso file GGUF, sulla stessa macchina, greedy. Colibri è compilato
sul runner per la sua CPU al commit di [`colibri.txt`](https://github.com/matteobaccan/ingausecase/blob/cases/colibri.txt)
(`.github/actions/colibri`); il GGUF passa da `coli import` (una cartella che punta al
file, nulla è copiato o riquantizzato) e da `coli serve`, l'API compatibile con OpenAI.

- **Domande:** le prime 20 di quelle fisse del caso [`arc`](../arc) (ARC-Challenge) e le
  prime 20 del caso [`gsm8k`](../gsm8k), dagli stessi dati di [`dati.json`](https://github.com/matteobaccan/ingausecase/blob/cases/dati.json),
  poste e valutate come in quei casi.
- **Voto:** le risposte giuste di Inga. Voci: Inga e Colibri in tutto e per test, la
  differenza, le risposte con lo stesso testo, il tempo di Colibri su quello di Inga.
- **Architetture:** Colibri non ha tutte quelle di Inga (la sua `docs/gguf.md`: qwen3,
  qwen3moe, qwen35, lfm3, olmoe, ...; qui si compilano i motori `qwen36` e `olmoe`): con
  un modello che non ha, il caso si dà come saltato e dice perché.

Colibri ignora `seed` (lo dice la sua API): a temperatura 0 non serve. Il ragionamento è
spento per tutti e due (`enable_thinking` false: per Inga in `chat_template_kwargs`,
per Colibri nel corpo della richiesta, dove lo legge).
