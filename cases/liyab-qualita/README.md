# liyab-qualita

Le stesse domande **a Inga e a [Liyab](https://github.com/andrei-borcea/liyab)** sullo stesso file GGUF, greedy: le prime 20 domande fisse del caso [`arc`](../arc) e le prime 20 del caso [`gsm8k`](../gsm8k), poste e valutate come in quei casi. Inga dalla sua API di chat; Liyab con `liyab-cli`, che prende testo grezzo: lo stesso dialogo passato dal ChatML di Qwen3 dal caso. Voto: le risposte giuste di Inga; voci: Inga e Liyab in tutto e per test, la differenza, le risposte con lo stesso testo, il tempo di Liyab su quello di Inga.

Liyab è compilato sul runner per la sua CPU al commit di [`liyab.txt`](https://github.com/matteobaccan/ingausecase/blob/cases/liyab.txt) (`.github/actions/liyab`: CMake, Release, Clang, solo CPU con i kernel AVX2 scelti a runtime). Per i suoi autori la build Linux è ancora da validare: se non compila, il caso si dà come saltato.
