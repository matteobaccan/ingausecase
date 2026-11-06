# Risultati di Inga 0.45.0

Eseguito con `inga 0.45.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.44.0).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | 91.7 | 0.0 | 5:14 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| canale-http | **79.1** | 78.9 | +0.2 | 40:21 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | **158.1** | 155.5 | +2.6 | 20:51 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | **82.5** | 80.0 | +2.5 | 17:36 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 3:19 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | 76.7 | 0.0 | 10:23 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| densa | 99.5 | - | - | 18:38 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 29:27 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | **82.5** | 81.2 | +1.2 | 2:59 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | 80.0 | **83.3** | -3.3 | 17:47 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | **83.9** | 82.2 | +1.7 | 30:20 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-cli | **248.5** | 142.5 | +106.0 | 7:48 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-confronto | 259.8 | **294.3** | -34.5 | 8:27 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-moe | **266.5** | 246.9 | +19.6 | 53:49 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| liyab-qualita | 82.5 | 82.5 | 0.0 | 18:30 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-velocita | **140.7** | 136.6 | +4.1 | 4:21 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | 20.0 | 20.0 | 0.0 | 49:15 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | **93.1** | 92.5 | +0.6 | 11:04 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:02 | Qwen3-0.6B-Q8_0.gguf | ok |
| q6k | 99.1 | - | - | 4:15 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| rag-recupero | 70.6 | **70.8** | -0.2 | 5:40 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-rgb | **85.0** | 82.5 | +2.5 | 41:16 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| thread | 90.4 | **132.3** | -42.0 | 5:09 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | 45.0 | **55.0** | -10.0 | 22:35 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | 121.1 | **129.3** | -8.2 | 9:02 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 91.7 | 91.7 | 0.0 |
| llama.cpp | ↑ | 91.7 | 91.7 | 0.0 |
| Inga meno llama.cpp | ↑ | 0.0 | 0.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 96.7 | 95.0 | +1.7 |
| tempo di llama.cpp su quello di Inga | ↑ | **143.3** | **139.2** | +4.1 |

### canale-http — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **187.9** | **183.0** | +4.9 |
| qwen3-0.6b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **315.3** | **289.8** | +25.5 |
| qwen3-0.6b: generazione a d=2048, split-KV su spento | ↑ | **101.1** | **100.6** | +0.5 |
| qwen3-0.6b: generazione a d=4096, split-KV su spento | ↑ | **101.0** | 99.6 | +1.4 |
| qwen3-0.6b: generazione bench, tok/s | ↑ | **5284.9** | 4768.8 | +516.0 |
| qwen3-0.6b: prompt bench, tok/s | ↑ | 15030.0 | **15203.8** | -173.8 |
| qwen3-0.6b: generazione bench_d, tok/s | ↑ | **4166.1** | 3814.4 | +351.8 |
| qwen3-0.6b: generazione bench_d su bench | ↑ | 78.8 | 80.0 | -1.2 |
| qwen3-0.6b: prompt bench_d, tok/s | ↑ | **13386.8** | 13369.5 | +17.3 |
| qwen3-0.6b: generazione bench_t, tok/s | ↑ | **5368.1** | 4943.2 | +424.9 |
| qwen3-0.6b: generazione bench_t su bench | ↑ | **101.6** | **103.7** | -2.1 |
| qwen3-0.6b: prompt bench_t, tok/s | ↑ | 14462.1 | **14541.5** | -79.4 |
| qwen3-0.6b: generazione run, tok/s | ↑ | **3730.0** | 3470.0 | +260.0 |
| qwen3-0.6b: generazione run su bench | ↑ | 70.6 | 72.8 | -2.2 |
| qwen3-0.6b: prompt run, tok/s | ↑ | **15123.3** | 15066.7 | +56.7 |
| qwen3-0.6b: generazione run_corto, tok/s | ↑ | **4780.0** | 4376.7 | +403.3 |
| qwen3-0.6b: generazione run_corto su bench | ↑ | 90.4 | 91.8 | -1.3 |
| qwen3-0.6b: prompt run_corto, tok/s | ↑ | 16223.3 | **16330.0** | -106.7 |
| qwen3-0.6b: generazione api, tok/s | ↑ | **3832.1** | 3355.4 | +476.7 |
| qwen3-0.6b: generazione api su bench | ↑ | 72.5 | 70.4 | +2.1 |
| qwen3-0.6b: generazione api, il motore, tok/s | ↑ | **3862.8** | 3382.2 | +480.6 |
| qwen3-0.6b: generazione api, il motore su bench | ↑ | 73.1 | 70.9 | +2.2 |
| qwen3-0.6b: prompt api, tok/s | ↑ | 15191.1 | **15195.5** | -4.4 |
| qwen3-0.6b: generazione stream, tok/s | ↑ | **3819.3** | 3368.1 | +451.2 |
| qwen3-0.6b: generazione stream su bench | ↑ | 72.3 | 70.6 | +1.6 |
| qwen3-0.6b: generazione stream, il motore, tok/s | ↑ | **3849.1** | 3394.5 | +454.6 |
| qwen3-0.6b: generazione stream, il motore su bench | ↑ | 72.8 | 71.2 | +1.7 |
| qwen3-0.6b: prompt stream, tok/s | ↑ | **15212.7** | 15205.7 | +7.1 |
| qwen3-0.6b: generazione stream_meno, tok/s | ↑ | **3826.6** | 3378.9 | +447.7 |
| qwen3-0.6b: generazione stream_meno su bench | ↑ | 72.4 | 70.9 | +1.6 |
| qwen3-0.6b: generazione stream_meno, il motore, tok/s | ↑ | **3855.9** | 3404.6 | +451.2 |
| qwen3-0.6b: generazione stream_meno, il motore su bench | ↑ | 73.0 | 71.4 | +1.6 |
| qwen3-0.6b: prompt stream_meno, tok/s | ↑ | **15160.8** | 15128.6 | +32.2 |
| qwen3-4b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **130.8** | **126.6** | +4.2 |
| qwen3-4b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **189.6** | **180.7** | +8.9 |
| qwen3-4b: generazione a d=2048, split-KV su spento | ↑ | **100.4** | **100.2** | +0.2 |
| qwen3-4b: generazione bench, tok/s | ↑ | **1290.6** | 1140.6 | +150.0 |
| qwen3-4b: prompt bench, tok/s | ↑ | 3257.4 | **3272.6** | -15.2 |
| qwen3-4b: generazione bench_d, tok/s | ↑ | **1164.8** | 1038.4 | +126.3 |
| qwen3-4b: generazione bench_d su bench | ↑ | 90.3 | 91.0 | -0.8 |
| qwen3-4b: prompt bench_d, tok/s | ↑ | 3029.3 | **3053.9** | -24.5 |
| qwen3-4b: generazione bench_t, tok/s | ↑ | **1309.8** | 1159.3 | +150.5 |
| qwen3-4b: generazione bench_t su bench | ↑ | **101.5** | **101.6** | -0.1 |
| qwen3-4b: prompt bench_t, tok/s | ↑ | **3190.1** | 3171.3 | +18.8 |
| qwen3-4b: generazione run, tok/s | ↑ | **1110.0** | 990.0 | +120.0 |
| qwen3-4b: generazione run su bench | ↑ | 86.0 | 86.8 | -0.8 |
| qwen3-4b: prompt run, tok/s | ↑ | 3220.0 | **3243.3** | -23.3 |
| qwen3-4b: generazione run_corto, tok/s | ↑ | **1220.0** | 1080.0 | +140.0 |
| qwen3-4b: generazione run_corto su bench | ↑ | 94.5 | 94.7 | -0.2 |
| qwen3-4b: prompt run_corto, tok/s | ↑ | **3096.7** | 3073.3 | +23.3 |
| qwen3-4b: generazione api, tok/s | ↑ | **1113.1** | 978.8 | +134.3 |
| qwen3-4b: generazione api su bench | ↑ | 86.2 | 85.8 | +0.4 |
| qwen3-4b: generazione api, il motore, tok/s | ↑ | **1121.9** | 986.5 | +135.4 |
| qwen3-4b: generazione api, il motore su bench | ↑ | 86.9 | 86.5 | +0.4 |
| qwen3-4b: prompt api, tok/s | ↑ | **3262.5** | 3251.8 | +10.7 |
| qwen3-4b: generazione stream, tok/s | ↑ | **1108.3** | 994.3 | +114.0 |
| qwen3-4b: generazione stream su bench | ↑ | 85.9 | 87.2 | -1.3 |
| qwen3-4b: generazione stream, il motore, tok/s | ↑ | **1117.0** | 1002.1 | +114.9 |
| qwen3-4b: generazione stream, il motore su bench | ↑ | 86.5 | 87.9 | -1.3 |
| qwen3-4b: prompt stream, tok/s | ↑ | **3261.0** | 3237.6 | +23.4 |
| qwen3-4b: generazione stream_meno, tok/s | ↑ | **1128.6** | 1013.9 | +114.7 |
| qwen3-4b: generazione stream_meno su bench | ↑ | 87.4 | 88.9 | -1.4 |
| qwen3-4b: generazione stream_meno, il motore, tok/s | ↑ | **1137.5** | 1021.9 | +115.6 |
| qwen3-4b: generazione stream_meno, il motore su bench | ↑ | 88.1 | 89.6 | -1.5 |
| qwen3-4b: prompt stream_meno, tok/s | ↑ | **3252.0** | 3241.0 | +10.9 |

### colibri-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | ↑ | **141.9** | **144.4** | -2.5 |
| generazione (128 token), Inga su Colibri | ↑ | **174.2** | **166.5** | +7.7 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Colibri | ↑ | 100.0 | 100.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 70.0 | 70.0 | 0.0 |

### colibri-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **82.5** | 80.0 | +2.5 |
| Colibri | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Colibri | ↑ | **2.5** | 0.0 | +2.5 |
| risposte con lo stesso testo | ≈ | 47.5 | 45.0 | +2.5 |
| tempo di Colibri su quello di Inga | ↑ | **144.3** | **134.7** | +9.5 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Colibri | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | **75.0** | 70.0 | +5.0 |
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
| da 2 a 4 thread (default) | ↑ | 107.0 | - | - |
| debug.cpu_task_kb=64 con 2 thread, sul default | ↑ | 91.7 | - | - |
| debug.cpu_tasks_per_thread=1 con 2 thread, sul default | ↑ | 99.8 | - | - |
| debug.cpu_task_kb=64 con 4 thread, sul default | ↑ | 93.5 | - | - |
| debug.cpu_tasks_per_thread=1 con 4 thread, sul default | ↑ | 99.4 | - | - |
| debug.weights_thp con 2 thread, sul default | ↑ | 99.5 | - | - |
| debug.weights_thp con 4 thread, sul default | ↑ | 99.5 | - | - |

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
| urgenza | ↑ | **75.0** | 72.5 | +2.5 |
| reparto | ↑ | 90.0 | 90.0 | 0.0 |
| entrambi giusti | ↑ | **67.5** | 65.0 | +2.5 |

### gsm8k — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 80.0 | **83.3** | -3.3 |
| llama.cpp | ↑ | **83.3** | 83.3 | 0.0 |
| Inga meno llama.cpp | ↑ | -3.3 | 0.0 | -3.3 |
| risposte con lo stesso testo | ≈ | 36.7 | 40.0 | -3.3 |
| tempo di llama.cpp su quello di Inga | ↑ | 96.8 | 95.9 | +0.9 |

### ifeval — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **83.9** | 82.2 | +1.7 |
| llama.cpp | ↑ | 80.0 | **85.6** | -5.6 |
| Inga meno llama.cpp | ↑ | **3.9** | -3.3 | +7.2 |
| risposte con lo stesso testo | ≈ | 13.3 | 10.0 | +3.3 |
| tempo di llama.cpp su quello di Inga | ↑ | **106.0** | 91.9 | +14.0 |
| richieste con tutte le istruzioni, Inga | ↑ | **76.7** | 76.7 | 0.0 |
| richieste con tutte le istruzioni, llama.cpp | ↑ | 70.0 | **80.0** | -10.0 |

### liyab-cli — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **367.1** | **155.6** | +211.5 |
| generazione (128 token), Inga su Liyab senza bozze | ↑ | **129.8** | **129.5** | +0.4 |
| generazione (128 token), Inga su Liyab con le sue bozze | ↑ | **140.1** | **130.1** | +10.1 |
| generazione, Inga (tok/s) | ↑ | 965.9 | **1147.4** | -181.4 |
| generazione, Liyab senza bozze (tok/s) | ↑ | 744.0 | **886.3** | -142.2 |
| generazione, Liyab con le sue bozze (tok/s) | ↑ | 689.3 | **882.0** | -192.7 |
| picco di memoria residente, Inga (MiB) | ↓ | 285580.0 | **285530.0** | +50.0 |
| picco di memoria residente, Liyab (MiB) | ↓ | **250650.0** | 250660.0 | -10.0 |
| picco di memoria, Inga su Liyab | ↓ | 113.9 | 113.9 | 0.0 |

### liyab-confronto — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: prompt, Inga API su Liyab | ↑ | **338.6** | **415.1** | -76.5 |
| qwen3-0.6b: generazione, Inga API su Liyab | ↑ | **346.3** | **280.2** | +66.1 |
| qwen3-0.6b: prompt, Inga bench su Liyab | ↑ | **340.2** | **415.4** | -75.3 |
| qwen3-0.6b: generazione, Inga bench su Liyab | ↑ | **450.5** | **342.4** | +108.2 |
| qwen3-0.6b: generazione, Inga API su Inga bench | ↑ | 76.9 | 81.8 | -5.0 |
| qwen3-0.6b: picco di RAM, Inga API (MiB) | ↑ | **107450.0** | 104900.0 | +2550.0 |
| qwen3-0.6b: picco di RAM, Inga bench (MiB) | ↑ | **128913.3** | 128836.7 | +76.7 |
| qwen3-0.6b: picco di RAM, Liyab (MiB) | ↑ | 69933.3 | 69933.3 | 0.0 |
| qwen3-4b: prompt, Inga API su Liyab | ↑ | **250.9** | **369.3** | -118.4 |
| qwen3-4b: generazione, Inga API su Liyab | ↑ | **103.3** | **112.4** | -9.0 |
| qwen3-4b: prompt, Inga bench su Liyab | ↑ | **254.3** | **370.0** | -115.7 |
| qwen3-4b: generazione, Inga bench su Liyab | ↑ | **115.5** | **121.6** | -6.1 |
| qwen3-4b: generazione, Inga API su Inga bench | ↑ | 89.5 | 92.4 | -2.9 |
| qwen3-4b: picco di RAM, Inga API (MiB) | ↑ | **274660.0** | 273700.0 | +960.0 |
| qwen3-4b: picco di RAM, Inga bench (MiB) | ↑ | **285596.7** | 285566.7 | +30.0 |
| qwen3-4b: picco di RAM, Liyab (MiB) | ↑ | 250633.3 | 250633.3 | 0.0 |

### liyab-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **205.4** | **194.3** | +11.0 |
| generazione (128 token), Inga su Liyab | ↑ | **327.7** | **299.5** | +28.2 |
| lettura del prompt, Inga (tok/s) | ↑ | **3087.2** | 2922.4 | +164.8 |
| lettura del prompt, Liyab (tok/s) | ↑ | 1503.3 | **1503.9** | -0.6 |
| generazione, Inga (tok/s) | ↑ | **962.9** | 879.3 | +83.6 |
| generazione, Liyab (tok/s) | ↑ | **293.9** | 293.6 | +0.3 |
| picco di RAM, Inga (MiB) | ↑ | **1496320.0** | 1366620.0 | +129700.0 |
| picco di RAM, Liyab (MiB) | ↑ | 774450.0 | **774470.0** | -20.0 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Liyab | ↑ | 10.0 | 10.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 0.0 | 0.0 | 0.0 |

### liyab-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.5 | 82.5 | 0.0 |
| Liyab | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Liyab | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 57.5 | 62.5 | -5.0 |
| tempo di Liyab su quello di Inga | ↑ | **130.1** | **117.8** | +12.3 |
| picco di memoria residente, Inga (MiB) | ↑ | 364440.0 | **366330.0** | -1890.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | **248590.0** | 248570.0 | +20.0 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Liyab | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | 75.0 | 75.0 | 0.0 |
| GSM8K, Liyab | ↑ | 70.0 | 70.0 | 0.0 |

### liyab-velocita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **158.5** | **157.0** | +1.5 |
| generazione (128 token), Inga su Liyab | ↑ | **122.9** | **116.2** | +6.6 |
| lettura del prompt, Inga (tok/s) | ↑ | 3199.0 | **3254.9** | -55.8 |
| lettura del prompt, Liyab (tok/s) | ↑ | 2017.9 | **2072.6** | -54.7 |
| generazione, Inga (tok/s) | ↑ | **1032.6** | 1012.2 | +20.4 |
| generazione, Liyab (tok/s) | ↑ | 840.2 | **870.7** | -30.5 |
| picco di memoria residente, Inga (MiB) | ↑ | **303930.0** | 302610.0 | +1320.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | 250820.0 | **250830.0** | -10.0 |

### memoria — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| giuste, diario | ↑ | 30.0 | 30.0 | 0.0 |
| giuste, tutta la chat | ↑ | 70.0 | 70.0 | 0.0 |
| testo atteso contenuto, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| testo atteso contenuto, diario | ↑ | 30.0 | 30.0 | 0.0 |
| testo atteso contenuto, tutta la chat | ↑ | 60.0 | 60.0 | 0.0 |
| abstention, diario | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, diario | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, diario | ↑ | 50.0 | 50.0 | 0.0 |
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
| campo righe | ↑ | **75.0** | 70.0 | +5.0 |
| righe singole | ↑ | **90.0** | 88.0 | +2.0 |

### prova — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta non vuota | ↑ | 100.0 | 100.0 | 0.0 |

### q6k — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| generazione con 2 thread, kernel Q6_K v2 su v1 | ↑ | **100.3** | - | - |
| generazione con 4 thread, kernel Q6_K v2 su v1 | ↑ | 99.1 | - | - |

### rag-recupero — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| nDCG@10 | ↑ | 70.6 | **70.8** | -0.2 |
| recall@10 | ↑ | 91.7 | 91.7 | 0.0 |
| recall@5 | ↑ | 82.4 | 82.4 | 0.0 |
| MRR@10 | ↑ | 63.6 | **63.8** | -0.2 |

### rag-rgb — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| risposta giusta con rumore | ↑ | 100.0 | 100.0 | 0.0 |
| rifiuto senza la risposta | ↑ | **70.0** | 65.0 | +5.0 |
| passaggio giusto fra gli estratti | ↑ | 100.0 | 100.0 | 0.0 |
| risposte date con rumore | ↑ | 100.0 | 100.0 | 0.0 |

### thread — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| generazione con 2 thread, Inga su llama.cpp | ↑ | 84.6 | **106.9** | -22.3 |
| generazione con 2 thread, Inga su Liyab | ↑ | **100.0** | **180.2** | -80.2 |
| generazione con 4 thread, Inga su llama.cpp | ↑ | 90.4 | **132.3** | -42.0 |
| generazione con 4 thread, Inga su Liyab | ↑ | **102.8** | **145.6** | -42.7 |
| Inga con 4 thread su Inga con 2 | ↑ | **109.5** | **140.8** | -31.3 |
| llama.cpp con 4 thread su llama.cpp con 2 | ↑ | **102.6** | **113.8** | -11.2 |
| Inga senza -t su llama.cpp con 4 thread | ↑ | 86.6 | 93.9 | -7.3 |

### tokensave — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste con tokensave | ↑ | 45.0 | **55.0** | -10.0 |
| giuste senza strumenti | ↑ | 15.0 | 10.0 | +5.0 |
| giuste con il codice nel prompt | ↑ | **90.0** | 90.0 | 0.0 |
| domande con almeno una chiamata a tokensave | ≈ | 95.0 | 100.0 | -5.0 |
| token del prompt per domanda, con tokensave su codice nel prompt | ↓ | **71.8** | **72.6** | -0.8 |
| token generati per domanda, con tokensave su senza strumenti | ↓ | **99.2** | 136.8 | -37.7 |

### velocita — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | ↑ | **150.9** | **159.4** | -8.5 |
| generazione (tg128), Inga su llama.cpp | ↑ | 91.2 | 99.1 | -7.9 |
| perplexity, Inga su llama.cpp | ↓ | **99.9** | **99.8** | 0.0 |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
