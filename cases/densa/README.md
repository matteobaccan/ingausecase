# densa

La generazione di un modello denso (Qwen3-4B-Instruct-2507 Q4_K_M) sulla CPU di Inga, su un
runner con SMT (4 vCPU, 2 core). Nel caso
[q6k](https://github.com/matteobaccan/ingausecase/blob/cases/cases/q6k/README.md) Inga è
passata da 2 a 4 thread guadagnando solo il 4 % (llama.cpp il 31 % nel caso
[thread](https://github.com/matteobaccan/ingausecase/blob/cases/cases/thread/README.md)):
qui si cerca dove si perde.

- **Scala**: `inga bench -p 0 -n 128 -r 3 -t T --json` con 1, 2, 3 e 4 thread.
- **Divisione del lavoro fra i thread**, con 2 e 4 thread:
  `inga bench -p 0 -n 128 -r 5 -t T --ab CHIAVE=VALORE`, le due varianti nello stesso
  processo a ripetizioni alternate (gli stessi bit: cambia solo chi calcola quali righe):
  - `debug.cpu_task_kb=16` e `=256`: i KiB di pesi di un compito (64 di default);
  - `debug.cpu_tasks_per_thread=1`: una sola fetta di righe per thread, come divide
    llama.cpp (8 compiti per thread di default);
  - `debug.cpu_spin_us=0`: i thread senza lavoro dormono subito invece di girare per
    5 ms (sull'SMT un thread che gira toglie risorse al suo gemello).
- **Pagine grandi per i pesi** (`debug.weights_thp`): il file letto in memoria anonima
  con `MADV_HUGEPAGE` invece di essere mappato. Si legge al caricamento, quindi niente
  `--ab`: esecuzioni alternate senza e con `--set debug.weights_thp=true` (ABAB, `-r 3`),
  con 2 e 4 thread; durante quelle con la chiave il caso legge `AnonHugePages` del
  processo da `/proc`, per sapere se il kernel ha dato davvero pagine da 2 MiB.
- **Profilo**: `inga bench -p 0 -n 64 -r 1 -t T --profile` con 2 e 4 thread, il tempo per
  tipo di operazione per token.

Voci: la scala da 2 a 4 thread e il rapporto variante / default di ogni chiave con 2 e 4
thread. Voto: il rapporto migliore con 4 thread (sopra 1, più veloce del default). Il JSON
tiene `lscpu`, il kernel e lo stato delle pagine grandi trasparenti. Va lanciato con
`prova` su un ramo di Inga che abbia le chiavi (`exp/0.45` o più recente).
