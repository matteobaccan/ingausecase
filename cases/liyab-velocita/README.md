# liyab-velocita

La velocità **di Inga e di [Liyab](https://github.com/andrei-borcea/liyab)** (il motore C++20 per GGUF, licenza Apache-2.0, pensato per telefono e Mac) sullo stesso file GGUF e sulla stessa macchina: un prompt di circa 512 token che chiede di contare fino a 1000, 128 token generati, 3 ripetizioni dopo una prova non misurata. Inga dall'API in streaming (i token del prompt sul tempo al primo token, quelli dopo il primo sul tempo dopo il primo); Liyab con `liyab-cli --json`, dalle sue statistiche (`prompt_tokens`, `ttft_ms`, `generated_tokens`, `decode_ms`), che non contano il caricamento del modello. Voto: la media dei rapporti Inga su Liyab.

Liyab è compilato sul runner per la sua CPU al commit di [`liyab.txt`](https://github.com/matteobaccan/ingausecase/blob/cases/liyab.txt) (`.github/actions/liyab`: CMake, Release, Clang, solo CPU con i kernel AVX2 scelti a runtime). Per i suoi autori la build Linux è ancora da validare: se non compila, il caso si dà come saltato.
