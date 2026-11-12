# Risultati di Inga 0.46.5

Eseguito con `inga 0.46.5`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.46.0).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | 91.7 | 0.0 | 4:34 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| canale-http | **82.7** | 78.5 | +4.1 | 32:30 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | 161.0 | **184.1** | -23.1 | 18:29 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | 82.5 | 82.5 | 0.0 | 17:13 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 3:51 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | 76.7 | 0.0 | 15:50 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| densa | **101.5** | 100.1 | +1.4 | 18:36 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 10:45 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 82.5 | 82.5 | 0.0 | 1:39 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | 80.0 | **83.3** | -3.3 | 14:06 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | **83.9** | 80.6 | +3.3 | 33:33 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-cli | **246.2** | 179.9 | +66.3 | 4:48 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-confronto | **339.2** | 246.9 | +92.2 | 6:11 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-moe | 211.4 | **235.1** | -23.7 | 49:10 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| liyab-qualita | 82.5 | 82.5 | 0.0 | 16:39 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-velocita | **173.4** | 142.3 | +31.1 | 3:20 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | 20.0 | 20.0 | 0.0 | 52:36 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 93.1 | 93.1 | 0.0 | 9:56 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:02 | Qwen3-0.6B-Q8_0.gguf | ok |
| q6k | 100.0 | **100.1** | -0.1 | 4:17 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| rag-recupero | 70.8 | 70.8 | 0.0 | 8:43 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-rgb | 85.0 | 85.0 | 0.0 | 22:50 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| thread | **104.4** | 92.5 | +11.9 | 5:45 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | **60.0** | 45.0 | +15.0 | 31:16 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | 105.4 | **109.5** | -4.1 | 10:49 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 91.7 | 91.7 | 0.0 |
| llama.cpp | ↑ | 91.7 | 91.7 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | 0.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 96.7 | 96.7 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | **138.0** | **137.5** | +0.4 |

### canale-http — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **161.4** | **185.3** | -23.9 |
| qwen3-0.6b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **253.5** | **307.9** | -54.5 |
| qwen3-0.6b: generazione a d=2048, split-KV su spento | ↑ | **101.5** | **101.0** | +0.5 |
| qwen3-0.6b: generazione a d=4096, split-KV su spento | ↑ | **100.8** | **100.4** | +0.4 |
| qwen3-0.6b: generazione bench, tok/s | ↑ | 5117.7 | **5361.3** | -243.6 |
| qwen3-0.6b: prompt bench, tok/s | ↑ | **39061.5** | 15121.0 | +23940.4 |
| qwen3-0.6b: generazione bench_d, tok/s | ↑ | 3877.4 | **4182.1** | -304.7 |
| qwen3-0.6b: generazione bench_d su bench | ↑ | 75.8 | 78.0 | -2.2 |
| qwen3-0.6b: prompt bench_d, tok/s | ↑ | **30630.3** | 13391.0 | +17239.3 |
| qwen3-0.6b: generazione bench_t, tok/s | ↑ | 5191.4 | **5505.7** | -314.2 |
| qwen3-0.6b: generazione bench_t su bench | ↑ | **101.4** | **102.7** | -1.3 |
| qwen3-0.6b: prompt bench_t, tok/s | ↑ | **37015.5** | 14615.8 | +22399.7 |
| qwen3-0.6b: generazione run, tok/s | ↑ | **3923.3** | 3776.7 | +146.7 |
| qwen3-0.6b: generazione run su bench | ↑ | 76.7 | 70.4 | +6.2 |
| qwen3-0.6b: prompt run, tok/s | ↑ | **39086.7** | 15220.0 | +23866.7 |
| qwen3-0.6b: generazione run_corto, tok/s | ↑ | 4826.7 | **4833.3** | -6.7 |
| qwen3-0.6b: generazione run_corto su bench | ↑ | 94.3 | 90.2 | +4.2 |
| qwen3-0.6b: prompt run_corto, tok/s | ↑ | **41576.7** | 16390.0 | +25186.7 |
| qwen3-0.6b: generazione api, tok/s | ↑ | **4023.0** | 3849.8 | +173.2 |
| qwen3-0.6b: generazione api su bench | ↑ | 78.6 | 71.8 | +6.8 |
| qwen3-0.6b: generazione api, il motore, tok/s | ↑ | **4055.2** | 3880.2 | +175.0 |
| qwen3-0.6b: generazione api, il motore su bench | ↑ | 79.2 | 72.4 | +6.9 |
| qwen3-0.6b: prompt api, tok/s | ↑ | **37784.0** | 15228.9 | +22555.1 |
| qwen3-0.6b: generazione stream, tok/s | ↑ | **3951.0** | 3826.5 | +124.5 |
| qwen3-0.6b: generazione stream su bench | ↑ | 77.2 | 71.4 | +5.8 |
| qwen3-0.6b: generazione stream, il motore, tok/s | ↑ | **3981.4** | 3856.3 | +125.1 |
| qwen3-0.6b: generazione stream, il motore su bench | ↑ | 77.8 | 71.9 | +5.9 |
| qwen3-0.6b: prompt stream, tok/s | ↑ | **38890.7** | 15271.1 | +23619.5 |
| qwen3-0.6b: generazione stream_meno, tok/s | ↑ | **4028.9** | 3829.8 | +199.1 |
| qwen3-0.6b: generazione stream_meno su bench | ↑ | 78.7 | 71.4 | +7.3 |
| qwen3-0.6b: generazione stream_meno, il motore, tok/s | ↑ | **4059.6** | 3859.1 | +200.5 |
| qwen3-0.6b: generazione stream_meno, il motore su bench | ↑ | 79.3 | 72.0 | +7.3 |
| qwen3-0.6b: prompt stream_meno, tok/s | ↑ | **38775.2** | 15264.9 | +23510.3 |
| qwen3-4b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **119.0** | **130.1** | -11.1 |
| qwen3-4b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **165.5** | **188.7** | -23.1 |
| qwen3-4b: generazione a d=2048, split-KV su spento | ↑ | **100.3** | **100.3** | 0.0 |
| qwen3-4b: generazione bench, tok/s | ↑ | 1150.6 | **1290.6** | -140.0 |
| qwen3-4b: prompt bench, tok/s | ↑ | **6408.2** | 3298.9 | +3109.3 |
| qwen3-4b: generazione bench_d, tok/s | ↑ | 1043.1 | **1160.0** | -116.9 |
| qwen3-4b: generazione bench_d su bench | ↑ | 90.7 | 89.9 | +0.8 |
| qwen3-4b: prompt bench_d, tok/s | ↑ | **5717.4** | 3043.5 | +2673.8 |
| qwen3-4b: generazione bench_t, tok/s | ↑ | 1182.9 | **1314.0** | -131.1 |
| qwen3-4b: generazione bench_t su bench | ↑ | **102.8** | **101.8** | +1.0 |
| qwen3-4b: prompt bench_t, tok/s | ↑ | **6014.7** | 3182.1 | +2832.7 |
| qwen3-4b: generazione run, tok/s | ↑ | 983.3 | **1100.0** | -116.7 |
| qwen3-4b: generazione run su bench | ↑ | 85.5 | 85.2 | +0.2 |
| qwen3-4b: prompt run, tok/s | ↑ | **6330.0** | 3266.7 | +3063.3 |
| qwen3-4b: generazione run_corto, tok/s | ↑ | 963.3 | **1213.3** | -250.0 |
| qwen3-4b: generazione run_corto su bench | ↑ | 83.7 | 94.0 | -10.3 |
| qwen3-4b: prompt run_corto, tok/s | ↑ | **6303.3** | 3073.3 | +3230.0 |
| qwen3-4b: generazione api, tok/s | ↑ | 1015.0 | **1111.2** | -96.2 |
| qwen3-4b: generazione api su bench | ↑ | 88.2 | 86.1 | +2.1 |
| qwen3-4b: generazione api, il motore, tok/s | ↑ | 1023.1 | **1120.0** | -97.0 |
| qwen3-4b: generazione api, il motore su bench | ↑ | 88.9 | 86.8 | +2.1 |
| qwen3-4b: prompt api, tok/s | ↑ | **6270.2** | 3271.3 | +2998.9 |
| qwen3-4b: generazione stream, tok/s | ↑ | 1014.2 | **1106.1** | -91.9 |
| qwen3-4b: generazione stream su bench | ↑ | 88.1 | 85.7 | +2.4 |
| qwen3-4b: generazione stream, il motore, tok/s | ↑ | 1022.2 | **1114.8** | -92.6 |
| qwen3-4b: generazione stream, il motore su bench | ↑ | 88.8 | 86.4 | +2.5 |
| qwen3-4b: prompt stream, tok/s | ↑ | **6254.3** | 3262.4 | +2992.0 |
| qwen3-4b: generazione stream_meno, tok/s | ↑ | 1054.2 | **1132.4** | -78.2 |
| qwen3-4b: generazione stream_meno su bench | ↑ | 91.6 | 87.7 | +3.9 |
| qwen3-4b: generazione stream_meno, il motore, tok/s | ↑ | 1062.5 | **1141.3** | -78.8 |
| qwen3-4b: generazione stream_meno, il motore su bench | ↑ | 92.3 | 88.4 | +3.9 |
| qwen3-4b: prompt stream_meno, tok/s | ↑ | **6271.8** | 3270.2 | +3001.6 |

### colibri-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | ↑ | **145.8** | **166.7** | -20.9 |
| generazione (128 token), Inga su Colibri | ↑ | **176.3** | **201.5** | -25.2 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Colibri | ↑ | 100.0 | 100.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 60.0 | 60.0 | 0.0 |

### colibri-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **82.5** | 82.5 | 0.0 |
| Colibri | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Colibri | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 42.5 | 47.5 | -5.0 |
| tempo di Colibri su quello di Inga | ↑ | **147.7** | **145.7** | +2.0 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Colibri | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | **75.0** | 75.0 | 0.0 |
| GSM8K, Colibri | ↑ | 70.0 | 70.0 | 0.0 |

### contratti — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta | ↑ | 93.3 | 93.3 | 0.0 |
| articolo giusto | ↑ | 60.0 | 60.0 | 0.0 |
| citazione fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| estratti dal distrattore | ↓ | 27.7 | 27.7 | 0.0 |

### densa — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| da 2 a 4 thread (default) | ↑ | 101.2 | **106.8** | -5.5 |
| debug.cpu_task_kb=64 con 2 thread, sul default | ↑ | 91.4 | 91.4 | 0.0 |
| debug.cpu_tasks_per_thread=1 con 2 thread, sul default | ↑ | 99.7 | **99.9** | -0.2 |
| debug.cpu_task_kb=64 con 4 thread, sul default | ↑ | **94.0** | 93.0 | +1.0 |
| debug.cpu_tasks_per_thread=1 con 4 thread, sul default | ↑ | 100.1 | 100.1 | 0.0 |
| debug.weights_thp con 2 thread, sul default | ↑ | **100.4** | 99.8 | +0.6 |
| debug.weights_thp con 4 thread, sul default | ↑ | **101.5** | 98.5 | +3.0 |

### documenti — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta | ↑ | 100.0 | 100.0 | 0.0 |
| pagina giusta | ↑ | 100.0 | 100.0 | 0.0 |
| pagina giusta fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| estratti dal distrattore | ↓ | 1.7 | 1.7 | 0.0 |

### email — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| urgenza | ↑ | 75.0 | 75.0 | 0.0 |
| reparto | ↑ | 90.0 | 90.0 | 0.0 |
| entrambi giusti | ↑ | 67.5 | 67.5 | 0.0 |

### gsm8k — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 80.0 | **83.3** | -3.3 |
| llama.cpp | ↑ | **83.3** | 83.3 | 0.0 |
| Inga meno llama.cpp | ↑ | -3.3 | 0.0 | -3.3 |
| risposte con lo stesso testo | ≈ | 36.7 | 40.0 | -3.3 |
| tempo di llama.cpp su quello di Inga | ↑ | **110.6** | **100.4** | +10.3 |

### ifeval — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **83.9** | 80.6 | +3.3 |
| llama.cpp | ↑ | 80.0 | **85.6** | -5.6 |
| Inga meno llama.cpp | ↑ | **3.9** | -5.0 | +8.9 |
| risposte con lo stesso testo | ≈ | 13.3 | 10.0 | +3.3 |
| tempo di llama.cpp su quello di Inga | ↑ | **118.3** | 90.5 | +27.8 |
| richieste con tutte le istruzioni, Inga | ↑ | **76.7** | 73.3 | +3.3 |
| richieste con tutte le istruzioni, llama.cpp | ↑ | 70.0 | **80.0** | -10.0 |

### liyab-cli — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **375.9** | **246.7** | +129.3 |
| generazione (128 token), Inga su Liyab senza bozze | ↑ | **116.5** | **113.1** | +3.4 |
| generazione (128 token), Inga su Liyab con le sue bozze | ↑ | **116.7** | **115.4** | +1.3 |
| generazione, Inga (tok/s) | ↑ | **1382.6** | 1170.5 | +212.0 |
| generazione, Liyab senza bozze (tok/s) | ↑ | **1187.2** | 1035.4 | +151.8 |
| generazione, Liyab con le sue bozze (tok/s) | ↑ | **1185.0** | 1014.2 | +170.8 |
| picco di memoria residente, Inga (MiB) | ↓ | **285650.0** | 285660.0 | -10.0 |
| picco di memoria residente, Liyab (MiB) | ↓ | **250640.0** | 250660.0 | -20.0 |
| picco di memoria, Inga su Liyab | ↓ | 114.0 | 114.0 | 0.0 |

### liyab-confronto — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: prompt, Inga API su Liyab | ↑ | **418.9** | **341.4** | +77.5 |
| qwen3-0.6b: generazione, Inga API su Liyab | ↑ | **444.5** | **297.1** | +147.4 |
| qwen3-0.6b: prompt, Inga bench su Liyab | ↑ | **421.6** | **340.4** | +81.2 |
| qwen3-0.6b: generazione, Inga bench su Liyab | ↑ | **575.0** | **376.7** | +198.3 |
| qwen3-0.6b: generazione, Inga API su Inga bench | ↑ | 77.3 | 78.9 | -1.6 |
| qwen3-0.6b: picco di RAM, Inga API (MiB) | ↑ | **107130.0** | 105860.0 | +1270.0 |
| qwen3-0.6b: picco di RAM, Inga bench (MiB) | ↑ | **129006.7** | 129003.3 | +3.3 |
| qwen3-0.6b: picco di RAM, Liyab (MiB) | ↑ | 69933.3 | 69933.3 | 0.0 |
| qwen3-4b: prompt, Inga API su Liyab | ↑ | **373.7** | **251.5** | +122.3 |
| qwen3-4b: generazione, Inga API su Liyab | ↑ | **119.6** | 97.8 | +21.7 |
| qwen3-4b: prompt, Inga bench su Liyab | ↑ | **385.9** | **253.0** | +132.8 |
| qwen3-4b: generazione, Inga bench su Liyab | ↑ | **134.2** | **107.0** | +27.2 |
| qwen3-4b: generazione, Inga API su Inga bench | ↑ | 89.1 | 91.4 | -2.3 |
| qwen3-4b: picco di RAM, Inga API (MiB) | ↑ | **276570.0** | 274660.0 | +1910.0 |
| qwen3-4b: picco di RAM, Inga bench (MiB) | ↑ | **285683.3** | 285636.7 | +46.7 |
| qwen3-4b: picco di RAM, Liyab (MiB) | ↑ | 250633.3 | **250636.7** | -3.3 |

### liyab-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **162.3** | **179.0** | -16.7 |
| generazione (128 token), Inga su Liyab | ↑ | **260.4** | **291.2** | -30.8 |
| lettura del prompt, Inga (tok/s) | ↑ | 2422.2 | **2673.7** | -251.5 |
| lettura del prompt, Liyab (tok/s) | ↑ | 1492.1 | **1493.4** | -1.3 |
| generazione, Inga (tok/s) | ↑ | 737.6 | **829.9** | -92.4 |
| generazione, Liyab (tok/s) | ↑ | 283.2 | **285.0** | -1.8 |
| picco di RAM, Inga (MiB) | ↑ | 1475330.0 | **1478200.0** | -2870.0 |
| picco di RAM, Liyab (MiB) | ↑ | **774530.0** | 774090.0 | +440.0 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Liyab | ↑ | 10.0 | 10.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 0.0 | 0.0 | 0.0 |

### liyab-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.5 | 82.5 | 0.0 |
| Liyab | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Liyab | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 55.0 | 55.0 | 0.0 |
| tempo di Liyab su quello di Inga | ↑ | **117.4** | **115.1** | +2.3 |
| picco di memoria residente, Inga (MiB) | ↑ | 364160.0 | **364540.0** | -380.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | 248580.0 | 248580.0 | 0.0 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Liyab | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | 75.0 | 75.0 | 0.0 |
| GSM8K, Liyab | ↑ | 70.0 | 70.0 | 0.0 |

### liyab-velocita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **248.4** | **156.9** | +91.4 |
| generazione (128 token), Inga su Liyab | ↑ | 98.5 | **127.7** | -29.2 |
| lettura del prompt, Inga (tok/s) | ↑ | **6232.7** | 3258.0 | +2974.7 |
| lettura del prompt, Liyab (tok/s) | ↑ | **2509.6** | 2076.3 | +433.3 |
| generazione, Inga (tok/s) | ↑ | 1002.8 | **1098.4** | -95.6 |
| generazione, Liyab (tok/s) | ↑ | **1017.7** | 859.9 | +157.8 |
| picco di memoria residente, Inga (MiB) | ↑ | **304440.0** | 303800.0 | +640.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | 250810.0 | **250820.0** | -10.0 |

### memoria — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| giuste, diario | ↑ | 30.0 | **40.0** | -10.0 |
| giuste, tutta la chat | ↑ | 70.0 | 70.0 | 0.0 |
| testo atteso contenuto, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| testo atteso contenuto, diario | ↑ | 30.0 | **40.0** | -10.0 |
| testo atteso contenuto, tutta la chat | ↑ | 60.0 | 60.0 | 0.0 |
| abstention, diario | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, diario | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, diario | ↑ | 50.0 | **100.0** | -50.0 |
| single-session-user, diario | ↑ | 0.0 | 0.0 | 0.0 |
| temporal-reasoning, diario | ↑ | 0.0 | 0.0 | 0.0 |
| abstention, oggi | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| single-session-user, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| temporal-reasoning, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| sessioni scritte nel diario | ↑ | **93.8** | 87.5 | +6.2 |

### pdf — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| campo numero | ↑ | 100.0 | 100.0 | 0.0 |
| campo data | ↑ | 100.0 | 100.0 | 0.0 |
| campo fornitore | ↑ | 85.0 | 85.0 | 0.0 |
| campo partita_iva | ↑ | 85.0 | 85.0 | 0.0 |
| campo imponibile | ↑ | 100.0 | 100.0 | 0.0 |
| campo iva | ↑ | 100.0 | 100.0 | 0.0 |
| campo totale | ↑ | 100.0 | 100.0 | 0.0 |
| campo righe | ↑ | 75.0 | 75.0 | 0.0 |
| righe singole | ↑ | 90.0 | 90.0 | 0.0 |

### prova — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta non vuota | ↑ | 100.0 | 100.0 | 0.0 |

### q6k — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| generazione con 2 thread, kernel Q6_K v2 su v1 | ↑ | 100.0 | 100.0 | 0.0 |
| generazione con 4 thread, kernel Q6_K v2 su v1 | ↑ | 100.0 | **100.1** | -0.1 |

### rag-recupero — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| nDCG@10 | ↑ | 70.8 | 70.8 | 0.0 |
| recall@10 | ↑ | 91.7 | 91.7 | 0.0 |
| recall@5 | ↑ | 82.4 | 82.4 | 0.0 |
| MRR@10 | ↑ | 63.8 | 63.8 | 0.0 |

### rag-rgb — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta con rumore | ↑ | 100.0 | 100.0 | 0.0 |
| rifiuto senza la risposta | ↑ | 70.0 | 70.0 | 0.0 |
| passaggio giusto fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| risposte date con rumore | ↑ | 100.0 | 100.0 | 0.0 |

### thread — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| generazione con 2 thread, Inga su llama.cpp | ↑ | **129.4** | 83.6 | +45.8 |
| generazione con 2 thread, Inga su Liyab | ↑ | **151.7** | **100.7** | +51.0 |
| generazione con 4 thread, Inga su llama.cpp | ↑ | **104.4** | 92.5 | +11.9 |
| generazione con 4 thread, Inga su Liyab | ↑ | **121.8** | **108.5** | +13.3 |
| Inga con 4 thread su Inga con 2 | ↑ | 93.8 | **110.3** | -16.5 |
| llama.cpp con 4 thread su llama.cpp con 2 | ↑ | **116.2** | 99.7 | +16.5 |
| Inga senza -t su llama.cpp con 4 thread | ↑ | **107.9** | 85.4 | +22.6 |

### tokensave — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste con tokensave | ↑ | 60.0 | 45.0 | +15.0 |
| giuste senza strumenti | ↑ | 15.0 | 15.0 | 0.0 |
| giuste con il codice nel prompt | ↑ | **90.0** | 90.0 | 0.0 |
| domande con almeno una chiamata a tokensave | ≈ | 95.0 | 95.0 | 0.0 |
| token del prompt per domanda, con tokensave su codice nel prompt | ↓ | **70.3** | **71.8** | -1.5 |
| token generati per domanda, con tokensave su senza strumenti | ↓ | 112.1 | **99.2** | +13.0 |

### velocita — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | ↑ | 85.7 | **124.1** | -38.4 |
| generazione (tg128), Inga su llama.cpp | ↑ | **125.2** | 95.0 | +30.2 |
| perplexity, Inga su llama.cpp | ↓ | **99.9** | **100.0** | -0.1 |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
