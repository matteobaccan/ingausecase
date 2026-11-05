# q6k

Il secondo kernel Q6_K di generazione di Inga (`debug.q6k_kernel=v2`, spento di default,
sul ramo `exp/0.45-q6k` di Inga) contro il primo, sulla stessa macchina e nello stesso
processo.

Il Q6_K è circa il 29 % dei byte letti per token in Qwen3-4B Q4_K_M (l'uscita, `attn_v` e
`ffn_down` di metà degli strati). Il secondo kernel fa una moltiplicazione ogni 32 valori
invece di due e toglie lo scarto di 32 una volta per blocco, come llama.cpp e Liyab: sulla
macchina di sviluppo (4 vCPU senza SMT, AVX-512) il token intero è andato da 1,01 a 1,05
volte più veloce, con AVX2 nel rumore. Qui si misura su un runner con SMT, dove con 4 thread
Inga era più lenta di llama.cpp
([thread](https://github.com/matteobaccan/ingausecase/blob/cases/cases/thread/README.md)).

- Inga: `inga bench -p 0 -n 128 -r 5 -t T --ab debug.q6k_kernel=v2`, con 2 e 4 thread
  (Qwen3-4B Q4_K_M): le due varianti a ripetizioni alternate nello stesso processo.

Voci: il rapporto v2 / v1 con 2 e con 4 thread. Voto: quello con 4 thread. Il JSON tiene
l'uscita di `lscpu` e le righe della tabella di `--ab`. Va lanciato con `prova` su un ramo di
Inga che abbia la chiave (`exp/0.45-q6k` o più recente).
