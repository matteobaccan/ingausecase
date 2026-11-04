# canale-http

**Quanto costa il canale HTTP di Inga**, misurando lo stesso modello sullo stesso runner e nello stesso job in cinque modi, con lo stesso prompt del caso liyab-velocita (circa 512 token, chiede di contare fino a 1000) e 128 token generati, 3 giri a ordine ruotato dopo una prova non misurata per ogni modo:

| modo | come | che cosa misura |
|---|---|---|
| `bench` | `inga bench -p 512 -n 128 -r 1 --json` | il motore da solo, prompt casuale, generazione da contesto vuoto |
| `bench_d` | `inga bench -p 512 -n 128 -d 512` | il motore da solo, con 512 token già nella cache prima di ogni prova (non misurati): la generazione dopo un prompt lungo quanto quello dei casi |
| `bench_t` | `inga bench -p 512 -n 128 -t 3` | il motore da solo con processori − 1 thread (il default è uno per core fisico: 2 su un runner a 4 vCPU con SMT) |
| `run_corto` | `inga run <modello> -p "una frase" -n 128` | la sessione completa senza server e senza la cache lunga |
| `run` | `inga run <modello> -p TESTO -n 128` | il motore con la sessione completa (template, prompt vero), senza server; la riga delle statistiche su stderr |
| `api` | `inga serve` + `/v1/chat/completions` senza streaming | il client (token della risposta sul tempo oltre il primo token) e il motore (`inga_timings.predicted_per_second`) |
| `stream` | la stessa richiesta in streaming | il client (token dopo il primo sul tempo dopo il primo) e il motore |
| `stream_meno` | in streaming, `--threads-decode` = processori − 1 | come sopra, con un core libero per il thread che scrive sulla rete |

Il caso nasce dai risultati di [`liyab-confronto`](../liyab-confronto) su Inga 0.43.0: la generazione dall'API in streaming era 0,58× quella di `inga bench` per Qwen3-0.6B (25,8 contro 44,7 tok/s) e 0,80× per Qwen3-4B (9,1 contro 11,3), con la lettura del prompt uguale: un costo fisso per token. I tempi del motore accanto a quelli del client dicono se il costo sta dentro il processo (contesa dei core fra i thread di generazione e il thread della rete, lavoro del server per token) o nel canale (relay, JSON, scrittura sul socket); `run` dice quanto pesa la sessione completa rispetto a `bench`; `stream_meno` prova la cura più semplice.

Prima esecuzione (Inga 0.43.0, 4 vCPU, i cinque modi iniziali): il canale HTTP non costa niente, il client vede la stessa velocità del motore (Qwen3-0.6B: 21,9 tok/s in streaming contro 22,1 del motore; `inga run -p` 21,3) e lo scarto è tutto fra `bench` (34,2) e la sessione vera; `--threads-decode 3` batte il default (23,2 contro 21,9; sul 4B 7,5 contro 6,2). Da qui `bench_d`, `bench_t` e `run_corto`: separano la cache lunga dal lavoro per token della sessione.

Seconda esecuzione (0.43.0, altro runner a 4 vCPU): `bench` 47,0 tok/s, `bench -d 512` 29,1, `run` 28,2, API 27,2, `run` con prompt corto 41,9 (Qwen3-0.6B); sul 4B 12,0 / 9,8 / 9,3 / 9,7 / 10,0. Lo scarto è l'attenzione in generazione sulla cache lunga; 3 thread contro 2 non cambiano niente su questo runner. Da qui, per ogni modello, `inga bench --profile -d 0` e `-d 512`: il tempo per operazione per token (nei dettagli, `profili`).

Voto: la media, sui due modelli, della generazione in streaming vista dal client sulla generazione di `bench` (1 = il canale non costa niente). I dettagli in [`run.py`](run.py).
