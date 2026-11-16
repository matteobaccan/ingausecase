# Risultati di Inga 0.46.6

Eseguito con `inga 0.46.6`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.46.5).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | 91.7 | 0.0 | 3:20 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| canale-http | **90.7** | 82.7 | +8.1 | 32:06 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | **162.4** | 161.0 | +1.3 | 18:36 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | 82.5 | 82.5 | 0.0 | 16:08 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 2:26 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | 76.7 | 0.0 | 16:19 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| densa | 99.6 | **101.5** | -1.9 | 13:03 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 15:38 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 82.5 | 82.5 | 0.0 | 2:23 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | 80.0 | 80.0 | 0.0 | 19:22 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | 80.6 | **83.9** | -3.3 | 42:37 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-cli | **279.5** | 246.2 | +33.3 | 6:50 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-confronto | 274.7 | **339.2** | -64.5 | 8:28 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-qualita | 82.5 | 82.5 | 0.0 | 19:04 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-velocita | **179.7** | 173.4 | +6.2 | 3:17 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | 20.0 | 20.0 | 0.0 | 25:41 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 93.1 | 93.1 | 0.0 | 6:57 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:02 | Qwen3-0.6B-Q8_0.gguf | ok |
| q6k | **100.2** | 100.0 | +0.2 | 5:07 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| rag-recupero | 67.8 | **70.8** | -3.0 | 8:42 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-rgb | 85.0 | 85.0 | 0.0 | 39:23 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| thread | **140.3** | 104.4 | +35.9 | 7:10 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | 60.0 | 60.0 | 0.0 | 46:55 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | **106.9** | 105.4 | +1.5 | 9:57 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 91.7 | 91.7 | 0.0 |
| llama.cpp | ↑ | **93.3** | 91.7 | +1.7 |
| Inga meno llama.cpp | ↑ | -1.7 | 0.0 | -1.7 |
| risposte con lo stesso testo | ≈ | 95.0 | 96.7 | -1.7 |
| tempo di llama.cpp su quello di Inga | ↑ | **125.1** | **138.0** | -12.9 |

### canale-http — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **166.9** | **161.4** | +5.6 |
| qwen3-0.6b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **263.2** | **253.5** | +9.8 |
| qwen3-0.6b: generazione a d=2048, split-KV su spento | ↑ | 78.1 | **101.5** | -23.4 |
| qwen3-0.6b: generazione a d=4096, split-KV su spento | ↑ | 76.8 | **100.8** | -23.9 |
| qwen3-0.6b: generazione bench, tok/s | ↑ | 4654.1 | **5117.7** | -463.7 |
| qwen3-0.6b: prompt bench, tok/s | ↑ | **66344.7** | 39061.5 | +27283.2 |
| qwen3-0.6b: generazione bench_d, tok/s | ↑ | **4011.1** | 3877.4 | +133.8 |
| qwen3-0.6b: generazione bench_d su bench | ↑ | 86.2 | 75.8 | +10.4 |
| qwen3-0.6b: prompt bench_d, tok/s | ↑ | **49495.8** | 30630.3 | +18865.6 |
| qwen3-0.6b: generazione bench_t, tok/s | ↑ | 4736.9 | **5191.4** | -454.5 |
| qwen3-0.6b: generazione bench_t su bench | ↑ | **101.8** | **101.4** | +0.3 |
| qwen3-0.6b: prompt bench_t, tok/s | ↑ | **61811.3** | 37015.5 | +24795.8 |
| qwen3-0.6b: generazione run, tok/s | ↑ | **3930.0** | 3923.3 | +6.7 |
| qwen3-0.6b: generazione run su bench | ↑ | 84.4 | 76.7 | +7.8 |
| qwen3-0.6b: prompt run, tok/s | ↑ | **64740.0** | 39086.7 | +25653.3 |
| qwen3-0.6b: generazione run_corto, tok/s | ↑ | 4276.7 | **4826.7** | -550.0 |
| qwen3-0.6b: generazione run_corto su bench | ↑ | 91.9 | 94.3 | -2.4 |
| qwen3-0.6b: prompt run_corto, tok/s | ↑ | **57930.0** | 41576.7 | +16353.3 |
| qwen3-0.6b: generazione api, tok/s | ↑ | **4093.3** | 4023.0 | +70.3 |
| qwen3-0.6b: generazione api su bench | ↑ | 88.0 | 78.6 | +9.3 |
| qwen3-0.6b: generazione api, il motore, tok/s | ↑ | **4126.3** | 4055.2 | +71.1 |
| qwen3-0.6b: generazione api, il motore su bench | ↑ | 88.7 | 79.2 | +9.4 |
| qwen3-0.6b: prompt api, tok/s | ↑ | **65200.3** | 37784.0 | +27416.3 |
| qwen3-0.6b: generazione stream, tok/s | ↑ | **4043.1** | 3951.0 | +92.1 |
| qwen3-0.6b: generazione stream su bench | ↑ | 86.9 | 77.2 | +9.7 |
| qwen3-0.6b: generazione stream, il motore, tok/s | ↑ | **4074.6** | 3981.4 | +93.2 |
| qwen3-0.6b: generazione stream, il motore su bench | ↑ | 87.5 | 77.8 | +9.8 |
| qwen3-0.6b: prompt stream, tok/s | ↑ | **64174.4** | 38890.7 | +25283.7 |
| qwen3-0.6b: generazione stream_meno, tok/s | ↑ | **4118.2** | 4028.9 | +89.3 |
| qwen3-0.6b: generazione stream_meno su bench | ↑ | 88.5 | 78.7 | +9.8 |
| qwen3-0.6b: generazione stream_meno, il motore, tok/s | ↑ | **4150.1** | 4059.6 | +90.5 |
| qwen3-0.6b: generazione stream_meno, il motore su bench | ↑ | 89.2 | 79.3 | +9.8 |
| qwen3-0.6b: prompt stream_meno, tok/s | ↑ | **63726.6** | 38775.2 | +24951.4 |
| qwen3-4b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **115.1** | **119.0** | -3.9 |
| qwen3-4b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **157.5** | **165.5** | -8.1 |
| qwen3-4b: generazione a d=2048, split-KV su spento | ↑ | 92.8 | **100.3** | -7.5 |
| qwen3-4b: generazione bench, tok/s | ↑ | 863.1 | **1150.6** | -287.5 |
| qwen3-4b: prompt bench, tok/s | ↑ | **10483.5** | 6408.2 | +4075.2 |
| qwen3-4b: generazione bench_d, tok/s | ↑ | 836.3 | **1043.1** | -206.8 |
| qwen3-4b: generazione bench_d su bench | ↑ | 96.9 | 90.7 | +6.2 |
| qwen3-4b: prompt bench_d, tok/s | ↑ | **9330.7** | 5717.4 | +3613.4 |
| qwen3-4b: generazione bench_t, tok/s | ↑ | 1049.1 | **1182.9** | -133.8 |
| qwen3-4b: generazione bench_t su bench | ↑ | **121.5** | **102.8** | +18.7 |
| qwen3-4b: prompt bench_t, tok/s | ↑ | **9731.9** | 6014.7 | +3717.1 |
| qwen3-4b: generazione run, tok/s | ↑ | 793.3 | **983.3** | -190.0 |
| qwen3-4b: generazione run su bench | ↑ | 91.9 | 85.5 | +6.5 |
| qwen3-4b: prompt run, tok/s | ↑ | **10266.7** | 6330.0 | +3936.7 |
| qwen3-4b: generazione run_corto, tok/s | ↑ | 813.3 | **963.3** | -150.0 |
| qwen3-4b: generazione run_corto su bench | ↑ | 94.2 | 83.7 | +10.5 |
| qwen3-4b: prompt run_corto, tok/s | ↑ | **9113.3** | 6303.3 | +2810.0 |
| qwen3-4b: generazione api, tok/s | ↑ | 817.1 | **1015.0** | -197.9 |
| qwen3-4b: generazione api su bench | ↑ | 94.7 | 88.2 | +6.5 |
| qwen3-4b: generazione api, il motore, tok/s | ↑ | 823.6 | **1023.1** | -199.5 |
| qwen3-4b: generazione api, il motore su bench | ↑ | 95.4 | 88.9 | +6.5 |
| qwen3-4b: prompt api, tok/s | ↑ | **10189.2** | 6270.2 | +3919.0 |
| qwen3-4b: generazione stream, tok/s | ↑ | 816.6 | **1014.2** | -197.6 |
| qwen3-4b: generazione stream su bench | ↑ | 94.6 | 88.1 | +6.5 |
| qwen3-4b: generazione stream, il motore, tok/s | ↑ | 823.1 | **1022.2** | -199.2 |
| qwen3-4b: generazione stream, il motore su bench | ↑ | 95.4 | 88.8 | +6.5 |
| qwen3-4b: prompt stream, tok/s | ↑ | **10229.9** | 6254.3 | +3975.6 |
| qwen3-4b: generazione stream_meno, tok/s | ↑ | 974.9 | **1054.2** | -79.3 |
| qwen3-4b: generazione stream_meno su bench | ↑ | **113.0** | 91.6 | +21.3 |
| qwen3-4b: generazione stream_meno, il motore, tok/s | ↑ | 982.5 | **1062.5** | -79.9 |
| qwen3-4b: generazione stream_meno, il motore su bench | ↑ | **113.8** | 92.3 | +21.5 |
| qwen3-4b: prompt stream_meno, tok/s | ↑ | **10256.4** | 6271.8 | +3984.6 |

### colibri-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | ↑ | **162.4** | **145.8** | +16.7 |
| generazione (128 token), Inga su Colibri | ↑ | **162.3** | **176.3** | -14.0 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Colibri | ↑ | 100.0 | 100.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 70.0 | 60.0 | +10.0 |

### colibri-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **82.5** | 82.5 | 0.0 |
| Colibri | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Colibri | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 42.5 | 42.5 | 0.0 |
| tempo di Colibri su quello di Inga | ↑ | 100.0 | **147.7** | -47.7 |
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
| da 2 a 4 thread (default) | ↑ | 100.1 | **101.2** | -1.1 |
| debug.cpu_task_kb=64 con 2 thread, sul default | ↑ | **92.8** | 91.4 | +1.4 |
| debug.cpu_tasks_per_thread=1 con 2 thread, sul default | ↑ | 99.4 | **99.7** | -0.3 |
| debug.cpu_task_kb=64 con 4 thread, sul default | ↑ | **95.7** | 94.0 | +1.7 |
| debug.cpu_tasks_per_thread=1 con 4 thread, sul default | ↑ | 99.6 | **100.1** | -0.5 |
| debug.weights_thp con 2 thread, sul default | ↑ | 99.9 | **100.4** | -0.5 |
| debug.weights_thp con 4 thread, sul default | ↑ | 98.8 | **101.5** | -2.7 |

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
| Inga | ↑ | 80.0 | 80.0 | 0.0 |
| llama.cpp | ↑ | **83.3** | 83.3 | 0.0 |
| Inga meno llama.cpp | ↑ | -3.3 | -3.3 | 0.0 |
| risposte con lo stesso testo | ≈ | 36.7 | 36.7 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | **100.4** | **110.6** | -10.2 |

### ifeval — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 80.6 | **83.9** | -3.3 |
| llama.cpp | ↑ | **83.9** | 80.0 | +3.9 |
| Inga meno llama.cpp | ↑ | -3.3 | **3.9** | -7.2 |
| risposte con lo stesso testo | ≈ | 10.0 | 13.3 | -3.3 |
| tempo di llama.cpp su quello di Inga | ↑ | **109.5** | **118.3** | -8.7 |
| richieste con tutte le istruzioni, Inga | ↑ | 73.3 | **76.7** | -3.3 |
| richieste con tutte le istruzioni, llama.cpp | ↑ | **76.7** | 70.0 | +6.7 |

### liyab-cli — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **442.8** | **375.9** | +66.9 |
| generazione (128 token), Inga su Liyab senza bozze | ↑ | **116.2** | **116.5** | -0.2 |
| generazione (128 token), Inga su Liyab con le sue bozze | ↑ | **116.2** | **116.7** | -0.5 |
| generazione, Inga (tok/s) | ↑ | 901.1 | **1382.6** | -481.4 |
| generazione, Liyab senza bozze (tok/s) | ↑ | 775.3 | **1187.2** | -411.9 |
| generazione, Liyab con le sue bozze (tok/s) | ↑ | 775.6 | **1185.0** | -409.4 |
| picco di memoria residente, Inga (MiB) | ↓ | 285730.0 | **285650.0** | +80.0 |
| picco di memoria residente, Liyab (MiB) | ↓ | 250640.0 | 250640.0 | 0.0 |
| picco di memoria, Inga su Liyab | ↓ | 114.0 | 114.0 | 0.0 |

### liyab-confronto — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: prompt, Inga API su Liyab | ↑ | **366.3** | **418.9** | -52.6 |
| qwen3-0.6b: generazione, Inga API su Liyab | ↑ | **373.5** | **444.5** | -71.0 |
| qwen3-0.6b: prompt, Inga bench su Liyab | ↑ | **368.6** | **421.6** | -53.1 |
| qwen3-0.6b: generazione, Inga bench su Liyab | ↑ | **439.6** | **575.0** | -135.4 |
| qwen3-0.6b: generazione, Inga API su Inga bench | ↑ | 85.0 | 77.3 | +7.7 |
| qwen3-0.6b: picco di RAM, Inga API (MiB) | ↑ | **108403.3** | 107130.0 | +1273.3 |
| qwen3-0.6b: picco di RAM, Inga bench (MiB) | ↑ | **129033.3** | 129006.7 | +26.7 |
| qwen3-0.6b: picco di RAM, Liyab (MiB) | ↑ | 69926.7 | **69933.3** | -6.7 |
| qwen3-4b: prompt, Inga API su Liyab | ↑ | **256.2** | **373.7** | -117.5 |
| qwen3-4b: generazione, Inga API su Liyab | ↑ | **102.8** | **119.6** | -16.8 |
| qwen3-4b: prompt, Inga bench su Liyab | ↑ | **260.3** | **385.9** | -125.6 |
| qwen3-4b: generazione, Inga bench su Liyab | ↑ | **112.9** | **134.2** | -21.3 |
| qwen3-4b: generazione, Inga API su Inga bench | ↑ | 91.0 | 89.1 | +1.9 |
| qwen3-4b: picco di RAM, Inga API (MiB) | ↑ | **276886.7** | 276570.0 | +316.7 |
| qwen3-4b: picco di RAM, Inga bench (MiB) | ↑ | **285753.3** | 285683.3 | +70.0 |
| qwen3-4b: picco di RAM, Liyab (MiB) | ↑ | **250640.0** | 250633.3 | +6.7 |

### liyab-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.5 | 82.5 | 0.0 |
| Liyab | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Liyab | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 57.5 | 55.0 | +2.5 |
| tempo di Liyab su quello di Inga | ↑ | **126.8** | **117.4** | +9.4 |
| picco di memoria residente, Inga (MiB) | ↑ | **366500.0** | 364160.0 | +2340.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | **248590.0** | 248580.0 | +10.0 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Liyab | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | 75.0 | 75.0 | 0.0 |
| GSM8K, Liyab | ↑ | 70.0 | 70.0 | 0.0 |

### liyab-velocita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **255.7** | **248.4** | +7.4 |
| generazione (128 token), Inga su Liyab | ↑ | **103.6** | 98.5 | +5.1 |
| lettura del prompt, Inga (tok/s) | ↑ | **6448.7** | 6232.7 | +216.0 |
| lettura del prompt, Liyab (tok/s) | ↑ | **2521.5** | 2509.6 | +11.9 |
| generazione, Inga (tok/s) | ↑ | **1025.8** | 1002.8 | +22.9 |
| generazione, Liyab (tok/s) | ↑ | 990.1 | **1017.7** | -27.5 |
| picco di memoria residente, Inga (MiB) | ↑ | 303040.0 | **304440.0** | -1400.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | **250830.0** | 250810.0 | +20.0 |

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
| generazione con 2 thread, kernel Q6_K v2 su v1 | ↑ | 99.7 | 100.0 | -0.3 |
| generazione con 4 thread, kernel Q6_K v2 su v1 | ↑ | **100.2** | 100.0 | +0.2 |

### rag-recupero — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| nDCG@10 | ↑ | 67.8 | **70.8** | -3.0 |
| recall@10 | ↑ | 90.0 | **91.7** | -1.7 |
| recall@5 | ↑ | 75.8 | **82.4** | -6.5 |
| MRR@10 | ↑ | 60.5 | **63.8** | -3.3 |

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
| generazione con 2 thread, Inga su llama.cpp | ↑ | **113.9** | **129.4** | -15.5 |
| generazione con 2 thread, Inga su Liyab | ↑ | **187.2** | **151.7** | +35.4 |
| generazione con 4 thread, Inga su llama.cpp | ↑ | **140.3** | **104.4** | +35.9 |
| generazione con 4 thread, Inga su Liyab | ↑ | **144.3** | **121.8** | +22.4 |
| Inga con 4 thread su Inga con 2 | ↑ | **133.8** | 93.8 | +40.0 |
| llama.cpp con 4 thread su llama.cpp con 2 | ↑ | **108.6** | **116.2** | -7.6 |
| Inga senza -t su llama.cpp con 4 thread | ↑ | **107.3** | **107.9** | -0.6 |

### tokensave — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste con tokensave | ↑ | 60.0 | 60.0 | 0.0 |
| giuste senza strumenti | ↑ | 10.0 | **15.0** | -5.0 |
| giuste con il codice nel prompt | ↑ | **90.0** | 90.0 | 0.0 |
| domande con almeno una chiamata a tokensave | ≈ | 95.0 | 95.0 | 0.0 |
| token del prompt per domanda, con tokensave su codice nel prompt | ↓ | **72.7** | **70.3** | +2.4 |
| token generati per domanda, con tokensave su senza strumenti | ↓ | 137.5 | 112.1 | +25.4 |

### velocita — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | ↑ | **106.4** | 85.7 | +20.8 |
| generazione (tg128), Inga su llama.cpp | ↑ | **107.4** | **125.2** | -17.8 |
| perplexity, Inga su llama.cpp | ↓ | **99.9** | **99.9** | 0.0 |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''

Macchina: x86_64, 4 CPU, Linux-7.0.0-1014-aws-x86_64-with-glibc2.39.
