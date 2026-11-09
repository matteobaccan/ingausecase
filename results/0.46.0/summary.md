# Risultati di Inga 0.46.0

Eseguito con `inga 0.46.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.45.0).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | 91.7 | 0.0 | 4:13 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| canale-http | 78.5 | **79.1** | -0.5 | 40:28 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | **184.1** | 158.1 | +26.0 | 25:14 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | 82.5 | 82.5 | 0.0 | 18:02 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 2:52 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | 76.7 | 0.0 | 16:44 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| densa | **100.1** | 99.5 | +0.6 | 17:46 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 17:35 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 82.5 | 82.5 | 0.0 | 1:27 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | **83.3** | 80.0 | +3.3 | 13:10 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | 80.6 | **83.9** | -3.3 | 29:53 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-cli | 179.9 | **248.5** | -68.6 | 5:58 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-confronto | 246.9 | **259.8** | -12.8 | 9:14 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-moe | 235.1 | **266.5** | -31.4 | 54:33 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| liyab-qualita | 82.5 | 82.5 | 0.0 | 16:23 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-velocita | **142.3** | 140.7 | +1.6 | 4:14 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | 20.0 | 20.0 | 0.0 | 32:02 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 93.1 | 93.1 | 0.0 | 6:42 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:02 | Qwen3-0.6B-Q8_0.gguf | ok |
| q6k | **100.1** | 99.1 | +1.0 | 4:09 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| rag-recupero | **70.8** | 70.6 | +0.2 | 8:42 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-rgb | 85.0 | 85.0 | 0.0 | 70:48 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| thread | **92.5** | 90.4 | +2.1 | 4:57 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | 45.0 | 45.0 | 0.0 | 23:06 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | 109.5 | **121.1** | -11.6 | 28:45 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 91.7 | 91.7 | 0.0 |
| llama.cpp | ↑ | 91.7 | 91.7 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | 0.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 96.7 | 96.7 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | **137.5** | **143.3** | -5.8 |

### canale-http — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **185.3** | **187.9** | -2.6 |
| qwen3-0.6b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **307.9** | **315.3** | -7.4 |
| qwen3-0.6b: generazione a d=2048, split-KV su spento | ↑ | **101.0** | **101.1** | -0.1 |
| qwen3-0.6b: generazione a d=4096, split-KV su spento | ↑ | **100.4** | **101.0** | -0.7 |
| qwen3-0.6b: generazione bench, tok/s | ↑ | **5361.3** | 5284.9 | +76.5 |
| qwen3-0.6b: prompt bench, tok/s | ↑ | **15121.0** | 15030.0 | +91.0 |
| qwen3-0.6b: generazione bench_d, tok/s | ↑ | **4182.1** | 4166.1 | +16.0 |
| qwen3-0.6b: generazione bench_d su bench | ↑ | 78.0 | 78.8 | -0.8 |
| qwen3-0.6b: prompt bench_d, tok/s | ↑ | **13391.0** | 13386.8 | +4.1 |
| qwen3-0.6b: generazione bench_t, tok/s | ↑ | **5505.7** | 5368.1 | +137.6 |
| qwen3-0.6b: generazione bench_t su bench | ↑ | **102.7** | **101.6** | +1.1 |
| qwen3-0.6b: prompt bench_t, tok/s | ↑ | **14615.8** | 14462.1 | +153.7 |
| qwen3-0.6b: generazione run, tok/s | ↑ | **3776.7** | 3730.0 | +46.7 |
| qwen3-0.6b: generazione run su bench | ↑ | 70.4 | 70.6 | -0.1 |
| qwen3-0.6b: prompt run, tok/s | ↑ | **15220.0** | 15123.3 | +96.7 |
| qwen3-0.6b: generazione run_corto, tok/s | ↑ | **4833.3** | 4780.0 | +53.3 |
| qwen3-0.6b: generazione run_corto su bench | ↑ | 90.2 | 90.4 | -0.3 |
| qwen3-0.6b: prompt run_corto, tok/s | ↑ | **16390.0** | 16223.3 | +166.7 |
| qwen3-0.6b: generazione api, tok/s | ↑ | **3849.8** | 3832.1 | +17.7 |
| qwen3-0.6b: generazione api su bench | ↑ | 71.8 | 72.5 | -0.7 |
| qwen3-0.6b: generazione api, il motore, tok/s | ↑ | **3880.2** | 3862.8 | +17.4 |
| qwen3-0.6b: generazione api, il motore su bench | ↑ | 72.4 | 73.1 | -0.7 |
| qwen3-0.6b: prompt api, tok/s | ↑ | **15228.9** | 15191.1 | +37.7 |
| qwen3-0.6b: generazione stream, tok/s | ↑ | **3826.5** | 3819.3 | +7.1 |
| qwen3-0.6b: generazione stream su bench | ↑ | 71.4 | 72.3 | -0.9 |
| qwen3-0.6b: generazione stream, il motore, tok/s | ↑ | **3856.3** | 3849.1 | +7.2 |
| qwen3-0.6b: generazione stream, il motore su bench | ↑ | 71.9 | 72.8 | -0.9 |
| qwen3-0.6b: prompt stream, tok/s | ↑ | **15271.1** | 15212.7 | +58.4 |
| qwen3-0.6b: generazione stream_meno, tok/s | ↑ | **3829.8** | 3826.6 | +3.2 |
| qwen3-0.6b: generazione stream_meno su bench | ↑ | 71.4 | 72.4 | -1.0 |
| qwen3-0.6b: generazione stream_meno, il motore, tok/s | ↑ | **3859.1** | 3855.9 | +3.3 |
| qwen3-0.6b: generazione stream_meno, il motore su bench | ↑ | 72.0 | 73.0 | -1.0 |
| qwen3-0.6b: prompt stream_meno, tok/s | ↑ | **15264.9** | 15160.8 | +104.1 |
| qwen3-4b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **130.1** | **130.8** | -0.7 |
| qwen3-4b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **188.7** | **189.6** | -0.9 |
| qwen3-4b: generazione a d=2048, split-KV su spento | ↑ | **100.3** | **100.4** | -0.1 |
| qwen3-4b: generazione bench, tok/s | ↑ | **1290.6** | 1290.6 | 0.0 |
| qwen3-4b: prompt bench, tok/s | ↑ | **3298.9** | 3257.4 | +41.5 |
| qwen3-4b: generazione bench_d, tok/s | ↑ | 1160.0 | **1164.8** | -4.7 |
| qwen3-4b: generazione bench_d su bench | ↑ | 89.9 | 90.3 | -0.4 |
| qwen3-4b: prompt bench_d, tok/s | ↑ | **3043.5** | 3029.3 | +14.2 |
| qwen3-4b: generazione bench_t, tok/s | ↑ | **1314.0** | 1309.8 | +4.2 |
| qwen3-4b: generazione bench_t su bench | ↑ | **101.8** | **101.5** | +0.3 |
| qwen3-4b: prompt bench_t, tok/s | ↑ | 3182.1 | **3190.1** | -8.0 |
| qwen3-4b: generazione run, tok/s | ↑ | 1100.0 | **1110.0** | -10.0 |
| qwen3-4b: generazione run su bench | ↑ | 85.2 | 86.0 | -0.8 |
| qwen3-4b: prompt run, tok/s | ↑ | **3266.7** | 3220.0 | +46.7 |
| qwen3-4b: generazione run_corto, tok/s | ↑ | 1213.3 | **1220.0** | -6.7 |
| qwen3-4b: generazione run_corto su bench | ↑ | 94.0 | 94.5 | -0.5 |
| qwen3-4b: prompt run_corto, tok/s | ↑ | 3073.3 | **3096.7** | -23.3 |
| qwen3-4b: generazione api, tok/s | ↑ | 1111.2 | **1113.1** | -1.9 |
| qwen3-4b: generazione api su bench | ↑ | 86.1 | 86.2 | -0.1 |
| qwen3-4b: generazione api, il motore, tok/s | ↑ | 1120.0 | **1121.9** | -1.9 |
| qwen3-4b: generazione api, il motore su bench | ↑ | 86.8 | 86.9 | -0.1 |
| qwen3-4b: prompt api, tok/s | ↑ | **3271.3** | 3262.5 | +8.9 |
| qwen3-4b: generazione stream, tok/s | ↑ | 1106.1 | **1108.3** | -2.1 |
| qwen3-4b: generazione stream su bench | ↑ | 85.7 | 85.9 | -0.2 |
| qwen3-4b: generazione stream, il motore, tok/s | ↑ | 1114.8 | **1117.0** | -2.2 |
| qwen3-4b: generazione stream, il motore su bench | ↑ | 86.4 | 86.5 | -0.2 |
| qwen3-4b: prompt stream, tok/s | ↑ | **3262.4** | 3261.0 | +1.3 |
| qwen3-4b: generazione stream_meno, tok/s | ↑ | **1132.4** | 1128.6 | +3.8 |
| qwen3-4b: generazione stream_meno su bench | ↑ | 87.7 | 87.4 | +0.3 |
| qwen3-4b: generazione stream_meno, il motore, tok/s | ↑ | **1141.3** | 1137.5 | +3.9 |
| qwen3-4b: generazione stream_meno, il motore su bench | ↑ | 88.4 | 88.1 | +0.3 |
| qwen3-4b: prompt stream_meno, tok/s | ↑ | **3270.2** | 3252.0 | +18.2 |

### colibri-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | ↑ | **166.7** | **141.9** | +24.8 |
| generazione (128 token), Inga su Colibri | ↑ | **201.5** | **174.2** | +27.2 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Colibri | ↑ | 100.0 | 100.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 60.0 | 70.0 | -10.0 |

### colibri-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **82.5** | 82.5 | 0.0 |
| Colibri | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Colibri | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 47.5 | 47.5 | 0.0 |
| tempo di Colibri su quello di Inga | ↑ | **145.7** | **144.3** | +1.4 |
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
| da 2 a 4 thread (default) | ↑ | 106.8 | **107.0** | -0.2 |
| debug.cpu_task_kb=64 con 2 thread, sul default | ↑ | 91.4 | **91.7** | -0.3 |
| debug.cpu_tasks_per_thread=1 con 2 thread, sul default | ↑ | **99.9** | 99.8 | +0.1 |
| debug.cpu_task_kb=64 con 4 thread, sul default | ↑ | 93.0 | **93.5** | -0.5 |
| debug.cpu_tasks_per_thread=1 con 4 thread, sul default | ↑ | **100.1** | 99.4 | +0.7 |
| debug.weights_thp con 2 thread, sul default | ↑ | **99.8** | 99.5 | +0.3 |
| debug.weights_thp con 4 thread, sul default | ↑ | 98.5 | **99.5** | -1.0 |

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
| Inga | ↑ | **83.3** | 80.0 | +3.3 |
| llama.cpp | ↑ | 83.3 | 83.3 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | -3.3 | +3.3 |
| risposte con lo stesso testo | ≈ | 40.0 | 36.7 | +3.3 |
| tempo di llama.cpp su quello di Inga | ↑ | **100.4** | 96.8 | +3.6 |

### ifeval — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 80.6 | **83.9** | -3.3 |
| llama.cpp | ↑ | **85.6** | 80.0 | +5.6 |
| Inga meno llama.cpp | ↑ | -5.0 | **3.9** | -8.9 |
| risposte con lo stesso testo | ≈ | 10.0 | 13.3 | -3.3 |
| tempo di llama.cpp su quello di Inga | ↑ | 90.5 | **106.0** | -15.5 |
| richieste con tutte le istruzioni, Inga | ↑ | 73.3 | **76.7** | -3.3 |
| richieste con tutte le istruzioni, llama.cpp | ↑ | **80.0** | 70.0 | +10.0 |

### liyab-cli — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **246.7** | **367.1** | -120.4 |
| generazione (128 token), Inga su Liyab senza bozze | ↑ | **113.1** | **129.8** | -16.8 |
| generazione (128 token), Inga su Liyab con le sue bozze | ↑ | **115.4** | **140.1** | -24.7 |
| generazione, Inga (tok/s) | ↑ | **1170.5** | 965.9 | +204.6 |
| generazione, Liyab senza bozze (tok/s) | ↑ | **1035.4** | 744.0 | +291.3 |
| generazione, Liyab con le sue bozze (tok/s) | ↑ | **1014.2** | 689.3 | +324.9 |
| picco di memoria residente, Inga (MiB) | ↓ | 285660.0 | **285580.0** | +80.0 |
| picco di memoria residente, Liyab (MiB) | ↓ | 250660.0 | **250650.0** | +10.0 |
| picco di memoria, Inga su Liyab | ↓ | 114.0 | 113.9 | 0.0 |

### liyab-confronto — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: prompt, Inga API su Liyab | ↑ | **341.4** | **338.6** | +2.8 |
| qwen3-0.6b: generazione, Inga API su Liyab | ↑ | **297.1** | **346.3** | -49.2 |
| qwen3-0.6b: prompt, Inga bench su Liyab | ↑ | **340.4** | **340.2** | +0.2 |
| qwen3-0.6b: generazione, Inga bench su Liyab | ↑ | **376.7** | **450.5** | -73.9 |
| qwen3-0.6b: generazione, Inga API su Inga bench | ↑ | 78.9 | 76.9 | +2.0 |
| qwen3-0.6b: picco di RAM, Inga API (MiB) | ↑ | 105860.0 | **107450.0** | -1590.0 |
| qwen3-0.6b: picco di RAM, Inga bench (MiB) | ↑ | **129003.3** | 128913.3 | +90.0 |
| qwen3-0.6b: picco di RAM, Liyab (MiB) | ↑ | 69933.3 | 69933.3 | 0.0 |
| qwen3-4b: prompt, Inga API su Liyab | ↑ | **251.5** | **250.9** | +0.6 |
| qwen3-4b: generazione, Inga API su Liyab | ↑ | 97.8 | **103.3** | -5.5 |
| qwen3-4b: prompt, Inga bench su Liyab | ↑ | **253.0** | **254.3** | -1.3 |
| qwen3-4b: generazione, Inga bench su Liyab | ↑ | **107.0** | **115.5** | -8.5 |
| qwen3-4b: generazione, Inga API su Inga bench | ↑ | 91.4 | 89.5 | +1.9 |
| qwen3-4b: picco di RAM, Inga API (MiB) | ↑ | 274660.0 | 274660.0 | 0.0 |
| qwen3-4b: picco di RAM, Inga bench (MiB) | ↑ | **285636.7** | 285596.7 | +40.0 |
| qwen3-4b: picco di RAM, Liyab (MiB) | ↑ | **250636.7** | 250633.3 | +3.3 |

### liyab-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **179.0** | **205.4** | -26.3 |
| generazione (128 token), Inga su Liyab | ↑ | **291.2** | **327.7** | -36.5 |
| lettura del prompt, Inga (tok/s) | ↑ | 2673.7 | **3087.2** | -413.5 |
| lettura del prompt, Liyab (tok/s) | ↑ | 1493.4 | **1503.3** | -9.9 |
| generazione, Inga (tok/s) | ↑ | 829.9 | **962.9** | -133.0 |
| generazione, Liyab (tok/s) | ↑ | 285.0 | **293.9** | -8.9 |
| picco di RAM, Inga (MiB) | ↑ | 1478200.0 | **1496320.0** | -18120.0 |
| picco di RAM, Liyab (MiB) | ↑ | 774090.0 | **774450.0** | -360.0 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Liyab | ↑ | 10.0 | 10.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 0.0 | 0.0 | 0.0 |

### liyab-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.5 | 82.5 | 0.0 |
| Liyab | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Liyab | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 55.0 | 57.5 | -2.5 |
| tempo di Liyab su quello di Inga | ↑ | **115.1** | **130.1** | -15.0 |
| picco di memoria residente, Inga (MiB) | ↑ | **364540.0** | 364440.0 | +100.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | 248580.0 | **248590.0** | -10.0 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Liyab | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | 75.0 | 75.0 | 0.0 |
| GSM8K, Liyab | ↑ | 70.0 | 70.0 | 0.0 |

### liyab-velocita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **156.9** | **158.5** | -1.6 |
| generazione (128 token), Inga su Liyab | ↑ | **127.7** | **122.9** | +4.8 |
| lettura del prompt, Inga (tok/s) | ↑ | **3258.0** | 3199.0 | +59.0 |
| lettura del prompt, Liyab (tok/s) | ↑ | **2076.3** | 2017.9 | +58.4 |
| generazione, Inga (tok/s) | ↑ | **1098.4** | 1032.6 | +65.8 |
| generazione, Liyab (tok/s) | ↑ | **859.9** | 840.2 | +19.6 |
| picco di memoria residente, Inga (MiB) | ↑ | 303800.0 | **303930.0** | -130.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | 250820.0 | 250820.0 | 0.0 |

### memoria — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| giuste, diario | ↑ | **40.0** | 30.0 | +10.0 |
| giuste, tutta la chat | ↑ | 70.0 | 70.0 | 0.0 |
| testo atteso contenuto, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| testo atteso contenuto, diario | ↑ | **40.0** | 30.0 | +10.0 |
| testo atteso contenuto, tutta la chat | ↑ | 60.0 | 60.0 | 0.0 |
| abstention, diario | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, diario | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, diario | ↑ | **100.0** | 50.0 | +50.0 |
| single-session-user, diario | ↑ | 0.0 | 0.0 | 0.0 |
| temporal-reasoning, diario | ↑ | 0.0 | 0.0 | 0.0 |
| abstention, oggi | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| single-session-user, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| temporal-reasoning, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| sessioni scritte nel diario | ↑ | 87.5 | **93.8** | -6.2 |

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
| generazione con 2 thread, kernel Q6_K v2 su v1 | ↑ | 100.0 | **100.3** | -0.3 |
| generazione con 4 thread, kernel Q6_K v2 su v1 | ↑ | **100.1** | 99.1 | +1.0 |

### rag-recupero — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| nDCG@10 | ↑ | **70.8** | 70.6 | +0.2 |
| recall@10 | ↑ | 91.7 | 91.7 | 0.0 |
| recall@5 | ↑ | 82.4 | 82.4 | 0.0 |
| MRR@10 | ↑ | **63.8** | 63.6 | +0.2 |

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
| generazione con 2 thread, Inga su llama.cpp | ↑ | 83.6 | 84.6 | -1.0 |
| generazione con 2 thread, Inga su Liyab | ↑ | **100.7** | **100.0** | +0.7 |
| generazione con 4 thread, Inga su llama.cpp | ↑ | 92.5 | 90.4 | +2.1 |
| generazione con 4 thread, Inga su Liyab | ↑ | **108.5** | **102.8** | +5.6 |
| Inga con 4 thread su Inga con 2 | ↑ | **110.3** | **109.5** | +0.8 |
| llama.cpp con 4 thread su llama.cpp con 2 | ↑ | 99.7 | **102.6** | -2.9 |
| Inga senza -t su llama.cpp con 4 thread | ↑ | 85.4 | 86.6 | -1.2 |

### tokensave — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste con tokensave | ↑ | 45.0 | 45.0 | 0.0 |
| giuste senza strumenti | ↑ | 15.0 | 15.0 | 0.0 |
| giuste con il codice nel prompt | ↑ | **90.0** | 90.0 | 0.0 |
| domande con almeno una chiamata a tokensave | ≈ | 95.0 | 95.0 | 0.0 |
| token del prompt per domanda, con tokensave su codice nel prompt | ↓ | **71.8** | **71.8** | 0.0 |
| token generati per domanda, con tokensave su senza strumenti | ↓ | **99.2** | **99.2** | 0.0 |

### velocita — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | ↑ | **124.1** | **150.9** | -26.9 |
| generazione (tg128), Inga su llama.cpp | ↑ | 95.0 | 91.2 | +3.8 |
| perplexity, Inga su llama.cpp | ↓ | **100.0** | **99.9** | +0.1 |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
