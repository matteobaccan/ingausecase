# Risultati di Inga 0.47.0

Eseguito con `inga 0.47.0`, seed 42, temperatura 0. Voti in percentuale; il confronto è con la versione precedente presente in `results/` (0.46.6).

Come leggere i numeri: ↑ più alto è meglio (un voto arriva al massimo a 100), ↓ più basso è meglio, ≈ solo descrittivo. Le voci "A su B" sono un rapporto (100 = pari) e "A meno B" una differenza (0 = pari). In **neretto**: nei rapporti e nelle differenze, i valori dal lato buono della parità (sopra con ↑, sotto con ↓); nelle voci che misurano due motori o due modi, il migliore fra loro; altrimenti il migliore fra questa versione e la precedente.

| Caso (↑ più alto è meglio) | Voto | Voto precedente | Differenza | Tempo (m:s) | Modello | Stato |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| arc | 91.7 | 91.7 | 0.0 | 3:13 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| canale-http | 86.5 | **90.7** | -4.2 | 44:03 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-moe | 149.0 | **162.4** | -13.3 | 23:27 | Qwen3-30B-A3B-Q4_K_M.gguf | ok |
| colibri-qualita | 82.5 | 82.5 | 0.0 | 14:04 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| colibri-velocita | - | - | - | 2:14 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | errore |
| contratti | 76.7 | 76.7 | 0.0 | 16:01 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| densa | **100.0** | 99.6 | +0.4 | 19:43 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| documenti | 100.0 | 100.0 | 0.0 | 11:43 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| email | 82.5 | 82.5 | 0.0 | 2:04 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| gsm8k | **83.3** | 80.0 | +3.3 | 18:08 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| ifeval | 80.6 | 80.6 | 0.0 | 38:07 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-cli | **285.7** | 279.5 | +6.1 | 6:48 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-confronto | **292.6** | 274.7 | +17.9 | 8:05 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-qualita | 82.5 | 82.5 | 0.0 | 18:38 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| liyab-velocita | 127.3 | **179.7** | -52.4 | 4:30 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| memoria | 20.0 | 20.0 | 0.0 | 23:36 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| pdf | 93.1 | 93.1 | 0.0 | 6:14 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| prova | 100.0 | 100.0 | 0.0 | 0:02 | Qwen3-0.6B-Q8_0.gguf | ok |
| q6k | 99.4 | **100.2** | -0.8 | 3:03 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| rag-recupero | **68.4** | 67.8 | +0.6 | 4:40 | Qwen3-0.6B-Q8_0.gguf | ok |
| rag-rgb | 85.0 | 85.0 | 0.0 | 26:48 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| thread | 98.6 | **140.3** | -41.7 | 4:11 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| tokensave | 60.0 | 60.0 | 0.0 | 28:44 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |
| velocita | **159.3** | 106.9 | +52.4 | 16:17 | Qwen3-4B-Instruct-2507-Q4_K_M.gguf | ok |

## Voci di ogni caso

### arc — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 91.7 | 91.7 | 0.0 |
| llama.cpp | ↑ | **93.3** | 93.3 | 0.0 |
| Inga meno llama.cpp | ↑ | -1.7 | -1.7 | 0.0 |
| risposte con lo stesso testo | ≈ | 95.0 | 95.0 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | **148.3** | **125.1** | +23.2 |

### canale-http — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **176.6** | **166.9** | +9.7 |
| qwen3-0.6b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **292.4** | **263.2** | +29.1 |
| qwen3-0.6b: generazione a d=2048, split-KV su spento | ↑ | **101.1** | 78.1 | +23.0 |
| qwen3-0.6b: generazione a d=4096, split-KV su spento | ↑ | **100.7** | 76.8 | +23.9 |
| qwen3-0.6b: generazione bench, tok/s | ↑ | 4475.7 | **4654.1** | -178.4 |
| qwen3-0.6b: prompt bench, tok/s | ↑ | 14841.2 | **66344.7** | -51503.4 |
| qwen3-0.6b: generazione bench_d, tok/s | ↑ | 3588.5 | **4011.1** | -422.6 |
| qwen3-0.6b: generazione bench_d su bench | ↑ | 80.2 | 86.2 | -6.0 |
| qwen3-0.6b: prompt bench_d, tok/s | ↑ | 13032.9 | **49495.8** | -36462.9 |
| qwen3-0.6b: generazione bench_t, tok/s | ↑ | **4762.8** | 4736.9 | +25.9 |
| qwen3-0.6b: generazione bench_t su bench | ↑ | **106.4** | **101.8** | +4.6 |
| qwen3-0.6b: prompt bench_t, tok/s | ↑ | 14416.9 | **61811.3** | -47394.4 |
| qwen3-0.6b: generazione run, tok/s | ↑ | 3406.7 | **3930.0** | -523.3 |
| qwen3-0.6b: generazione run su bench | ↑ | 76.1 | 84.4 | -8.3 |
| qwen3-0.6b: prompt run, tok/s | ↑ | 14883.3 | **64740.0** | -49856.7 |
| qwen3-0.6b: generazione run_corto, tok/s | ↑ | **4543.3** | 4276.7 | +266.7 |
| qwen3-0.6b: generazione run_corto su bench | ↑ | **101.5** | 91.9 | +9.6 |
| qwen3-0.6b: prompt run_corto, tok/s | ↑ | 15713.3 | **57930.0** | -42216.7 |
| qwen3-0.6b: generazione api, tok/s | ↑ | 3685.2 | **4093.3** | -408.1 |
| qwen3-0.6b: generazione api su bench | ↑ | 82.3 | 88.0 | -5.6 |
| qwen3-0.6b: generazione api, il motore, tok/s | ↑ | 3715.4 | **4126.3** | -410.9 |
| qwen3-0.6b: generazione api, il motore su bench | ↑ | 83.0 | 88.7 | -5.6 |
| qwen3-0.6b: prompt api, tok/s | ↑ | 14829.7 | **65200.3** | -50370.7 |
| qwen3-0.6b: generazione stream, tok/s | ↑ | 3629.5 | **4043.1** | -413.6 |
| qwen3-0.6b: generazione stream su bench | ↑ | 81.1 | 86.9 | -5.8 |
| qwen3-0.6b: generazione stream, il motore, tok/s | ↑ | 3657.7 | **4074.6** | -416.9 |
| qwen3-0.6b: generazione stream, il motore su bench | ↑ | 81.7 | 87.5 | -5.8 |
| qwen3-0.6b: prompt stream, tok/s | ↑ | 14854.9 | **64174.4** | -49319.5 |
| qwen3-0.6b: generazione stream_meno, tok/s | ↑ | 3714.2 | **4118.2** | -404.0 |
| qwen3-0.6b: generazione stream_meno su bench | ↑ | 83.0 | 88.5 | -5.5 |
| qwen3-0.6b: generazione stream_meno, il motore, tok/s | ↑ | 3742.9 | **4150.1** | -407.2 |
| qwen3-0.6b: generazione stream_meno, il motore su bench | ↑ | 83.6 | 89.2 | -5.5 |
| qwen3-0.6b: prompt stream_meno, tok/s | ↑ | 14867.2 | **63726.6** | -48859.4 |
| qwen3-4b: generazione a d=512, attenzione f16 su quella per posizione | ↑ | **122.0** | **115.1** | +6.9 |
| qwen3-4b: generazione a d=2048, attenzione f16 su quella per posizione | ↑ | **172.4** | **157.5** | +14.9 |
| qwen3-4b: generazione a d=2048, split-KV su spento | ↑ | 100.0 | 92.8 | +7.2 |
| qwen3-4b: generazione bench, tok/s | ↑ | **992.5** | 863.1 | +129.3 |
| qwen3-4b: prompt bench, tok/s | ↑ | 3253.6 | **10483.5** | -7229.9 |
| qwen3-4b: generazione bench_d, tok/s | ↑ | **924.4** | 836.3 | +88.1 |
| qwen3-4b: generazione bench_d su bench | ↑ | 93.1 | 96.9 | -3.8 |
| qwen3-4b: prompt bench_d, tok/s | ↑ | 3032.5 | **9330.7** | -6298.2 |
| qwen3-4b: generazione bench_t, tok/s | ↑ | **1056.3** | 1049.1 | +7.2 |
| qwen3-4b: generazione bench_t su bench | ↑ | **106.4** | **121.5** | -15.1 |
| qwen3-4b: prompt bench_t, tok/s | ↑ | 3167.6 | **9731.9** | -6564.3 |
| qwen3-4b: generazione run, tok/s | ↑ | **913.3** | 793.3 | +120.0 |
| qwen3-4b: generazione run su bench | ↑ | 92.0 | 91.9 | +0.1 |
| qwen3-4b: prompt run, tok/s | ↑ | 3213.3 | **10266.7** | -7053.3 |
| qwen3-4b: generazione run_corto, tok/s | ↑ | **973.3** | 813.3 | +160.0 |
| qwen3-4b: generazione run_corto su bench | ↑ | 98.1 | 94.2 | +3.8 |
| qwen3-4b: prompt run_corto, tok/s | ↑ | 3056.7 | **9113.3** | -6056.7 |
| qwen3-4b: generazione api, tok/s | ↑ | **913.4** | 817.1 | +96.2 |
| qwen3-4b: generazione api su bench | ↑ | 92.0 | 94.7 | -2.6 |
| qwen3-4b: generazione api, il motore, tok/s | ↑ | **920.6** | 823.6 | +97.0 |
| qwen3-4b: generazione api, il motore su bench | ↑ | 92.8 | 95.4 | -2.7 |
| qwen3-4b: prompt api, tok/s | ↑ | 3239.7 | **10189.2** | -6949.5 |
| qwen3-4b: generazione stream, tok/s | ↑ | **912.4** | 816.6 | +95.7 |
| qwen3-4b: generazione stream su bench | ↑ | 91.9 | 94.6 | -2.7 |
| qwen3-4b: generazione stream, il motore, tok/s | ↑ | **919.5** | 823.1 | +96.4 |
| qwen3-4b: generazione stream, il motore su bench | ↑ | 92.6 | 95.4 | -2.7 |
| qwen3-4b: prompt stream, tok/s | ↑ | 3241.4 | **10229.9** | -6988.5 |
| qwen3-4b: generazione stream_meno, tok/s | ↑ | 949.2 | **974.9** | -25.8 |
| qwen3-4b: generazione stream_meno su bench | ↑ | 95.6 | **113.0** | -17.3 |
| qwen3-4b: generazione stream_meno, il motore, tok/s | ↑ | 956.6 | **982.5** | -25.9 |
| qwen3-4b: generazione stream_meno, il motore su bench | ↑ | 96.4 | **113.8** | -17.4 |
| qwen3-4b: prompt stream_meno, tok/s | ↑ | 3234.2 | **10256.4** | -7022.2 |

### colibri-moe — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Colibri | ↑ | **153.9** | **162.4** | -8.5 |
| generazione (128 token), Inga su Colibri | ↑ | **144.1** | **162.3** | -18.2 |
| risposte giuste, Inga | ↑ | 100.0 | 100.0 | 0.0 |
| risposte giuste, Colibri | ↑ | 100.0 | 100.0 | 0.0 |
| risposte con lo stesso testo | ≈ | 60.0 | 70.0 | -10.0 |

### colibri-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | **82.5** | 82.5 | 0.0 |
| Colibri | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Colibri | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 42.5 | 42.5 | 0.0 |
| tempo di Colibri su quello di Inga | ↑ | **124.2** | 100.0 | +24.2 |
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
| da 2 a 4 thread (default) | ↑ | **115.2** | 100.1 | +15.0 |
| debug.cpu_task_kb=64 con 2 thread, sul default | ↑ | 92.0 | **92.8** | -0.8 |
| debug.cpu_tasks_per_thread=1 con 2 thread, sul default | ↑ | **99.8** | 99.4 | +0.4 |
| debug.cpu_task_kb=64 con 4 thread, sul default | ↑ | 94.3 | **95.7** | -1.4 |
| debug.cpu_tasks_per_thread=1 con 4 thread, sul default | ↑ | **99.9** | 99.6 | +0.3 |
| debug.weights_thp con 2 thread, sul default | ↑ | **100.2** | 99.9 | +0.4 |
| debug.weights_thp con 4 thread, sul default | ↑ | **100.0** | 98.8 | +1.2 |

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
| tempo di llama.cpp su quello di Inga | ↑ | **119.9** | **100.4** | +19.5 |

### ifeval — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 80.6 | 80.6 | 0.0 |
| llama.cpp | ↑ | **83.9** | 83.9 | 0.0 |
| Inga meno llama.cpp | ↑ | -3.3 | -3.3 | 0.0 |
| risposte con lo stesso testo | ≈ | 10.0 | 10.0 | 0.0 |
| tempo di llama.cpp su quello di Inga | ↑ | **131.0** | **109.5** | +21.5 |
| richieste con tutte le istruzioni, Inga | ↑ | 73.3 | 73.3 | 0.0 |
| richieste con tutte le istruzioni, llama.cpp | ↑ | **76.7** | 76.7 | 0.0 |

### liyab-cli — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **433.6** | **442.8** | -9.2 |
| generazione (128 token), Inga su Liyab senza bozze | ↑ | **137.7** | **116.2** | +21.5 |
| generazione (128 token), Inga su Liyab con le sue bozze | ↑ | **141.9** | **116.2** | +25.7 |
| generazione, Inga (tok/s) | ↑ | **1060.3** | 901.1 | +159.2 |
| generazione, Liyab senza bozze (tok/s) | ↑ | 770.0 | **775.3** | -5.3 |
| generazione, Liyab con le sue bozze (tok/s) | ↑ | 747.2 | **775.6** | -28.4 |
| picco di memoria residente, Inga (MiB) | ↓ | 289890.0 | **285730.0** | +4160.0 |
| picco di memoria residente, Liyab (MiB) | ↓ | 250650.0 | **250640.0** | +10.0 |
| picco di memoria, Inga su Liyab | ↓ | 115.7 | 114.0 | +1.7 |

### liyab-confronto — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| qwen3-0.6b: prompt, Inga API su Liyab | ↑ | **373.2** | **366.3** | +6.9 |
| qwen3-0.6b: generazione, Inga API su Liyab | ↑ | **429.7** | **373.5** | +56.2 |
| qwen3-0.6b: prompt, Inga bench su Liyab | ↑ | **373.3** | **368.6** | +4.8 |
| qwen3-0.6b: generazione, Inga bench su Liyab | ↑ | **427.0** | **439.6** | -12.5 |
| qwen3-0.6b: generazione, Inga API su Inga bench | ↑ | **100.6** | 85.0 | +15.7 |
| qwen3-0.6b: picco di RAM, Inga API (MiB) | ↑ | 106176.7 | **108403.3** | -2226.7 |
| qwen3-0.6b: picco di RAM, Inga bench (MiB) | ↑ | **129106.7** | 129033.3 | +73.3 |
| qwen3-0.6b: picco di RAM, Liyab (MiB) | ↑ | **69930.0** | 69926.7 | +3.3 |
| qwen3-4b: prompt, Inga API su Liyab | ↑ | **255.1** | **256.2** | -1.1 |
| qwen3-4b: generazione, Inga API su Liyab | ↑ | **112.4** | **102.8** | +9.6 |
| qwen3-4b: prompt, Inga bench su Liyab | ↑ | **259.7** | **260.3** | -0.6 |
| qwen3-4b: generazione, Inga bench su Liyab | ↑ | **128.7** | **112.9** | +15.7 |
| qwen3-4b: generazione, Inga API su Inga bench | ↑ | 87.3 | 91.0 | -3.7 |
| qwen3-4b: picco di RAM, Inga API (MiB) | ↑ | **281650.0** | 276886.7 | +4763.3 |
| qwen3-4b: picco di RAM, Inga bench (MiB) | ↑ | **289906.7** | 285753.3 | +4153.3 |
| qwen3-4b: picco di RAM, Liyab (MiB) | ↑ | 250640.0 | 250640.0 | 0.0 |

### liyab-qualita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| Inga | ↑ | 82.5 | 82.5 | 0.0 |
| Liyab | ↑ | 80.0 | 80.0 | 0.0 |
| Inga meno Liyab | ↑ | **2.5** | **2.5** | 0.0 |
| risposte con lo stesso testo | ≈ | 55.0 | 57.5 | -2.5 |
| tempo di Liyab su quello di Inga | ↑ | **161.6** | **126.8** | +34.8 |
| picco di memoria residente, Inga (MiB) | ↑ | **369230.0** | 366500.0 | +2730.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | 248590.0 | 248590.0 | 0.0 |
| ARC, Inga | ↑ | 90.0 | 90.0 | 0.0 |
| ARC, Liyab | ↑ | 90.0 | 90.0 | 0.0 |
| GSM8K, Inga | ↑ | 75.0 | 75.0 | 0.0 |
| GSM8K, Liyab | ↑ | 70.0 | 70.0 | 0.0 |

### liyab-velocita — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (~512 token), Inga su Liyab | ↑ | **157.5** | **255.7** | -98.3 |
| generazione (128 token), Inga su Liyab | ↑ | 97.1 | **103.6** | -6.5 |
| lettura del prompt, Inga (tok/s) | ↑ | 3212.1 | **6448.7** | -3236.6 |
| lettura del prompt, Liyab (tok/s) | ↑ | 2039.9 | **2521.5** | -481.7 |
| generazione, Inga (tok/s) | ↑ | 804.6 | **1025.8** | -221.1 |
| generazione, Liyab (tok/s) | ↑ | 828.5 | **990.1** | -161.7 |
| picco di memoria residente, Inga (MiB) | ↑ | **331220.0** | 303040.0 | +28180.0 |
| picco di memoria residente, Liyab (MiB) | ↑ | 250820.0 | **250830.0** | -10.0 |

### memoria — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| giuste, diario | ↑ | 40.0 | 40.0 | 0.0 |
| giuste, tutta la chat | ↑ | 70.0 | 70.0 | 0.0 |
| testo atteso contenuto, oggi | ↑ | 20.0 | 20.0 | 0.0 |
| testo atteso contenuto, diario | ↑ | 40.0 | 40.0 | 0.0 |
| testo atteso contenuto, tutta la chat | ↑ | 60.0 | 60.0 | 0.0 |
| abstention, diario | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, diario | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, diario | ↑ | 100.0 | 100.0 | 0.0 |
| single-session-user, diario | ↑ | 0.0 | 0.0 | 0.0 |
| temporal-reasoning, diario | ↑ | 0.0 | 0.0 | 0.0 |
| abstention, oggi | ↑ | 100.0 | 100.0 | 0.0 |
| knowledge-update, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| multi-session, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| single-session-user, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| temporal-reasoning, oggi | ↑ | 0.0 | 0.0 | 0.0 |
| sessioni scritte nel diario | ↑ | 87.5 | 87.5 | 0.0 |

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
| generazione con 2 thread, kernel Q6_K v2 su v1 | ↑ | **100.3** | 99.7 | +0.6 |
| generazione con 4 thread, kernel Q6_K v2 su v1 | ↑ | 99.4 | **100.2** | -0.8 |

### rag-recupero — ↑ più alto è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| nDCG@10 | ↑ | **68.4** | 67.8 | +0.6 |
| recall@10 | ↑ | 90.0 | 90.0 | 0.0 |
| recall@5 | ↑ | 75.8 | 75.8 | 0.0 |
| MRR@10 | ↑ | **61.4** | 60.5 | +0.8 |

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
| generazione con 2 thread, Inga su llama.cpp | ↑ | 97.5 | **113.9** | -16.4 |
| generazione con 2 thread, Inga su Liyab | ↑ | **127.8** | **187.2** | -59.4 |
| generazione con 4 thread, Inga su llama.cpp | ↑ | 98.6 | **140.3** | -41.7 |
| generazione con 4 thread, Inga su Liyab | ↑ | **125.1** | **144.3** | -19.1 |
| Inga con 4 thread su Inga con 2 | ↑ | 97.9 | **133.8** | -35.9 |
| llama.cpp con 4 thread su llama.cpp con 2 | ↑ | 96.8 | **108.6** | -11.8 |
| Inga senza -t su llama.cpp con 4 thread | ↑ | **105.7** | **107.3** | -1.6 |

### tokensave — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| giuste con tokensave | ↑ | 60.0 | 60.0 | 0.0 |
| giuste senza strumenti | ↑ | 15.0 | 10.0 | +5.0 |
| giuste con il codice nel prompt | ↑ | **90.0** | 90.0 | 0.0 |
| domande con almeno una chiamata a tokensave | ≈ | 95.0 | 95.0 | 0.0 |
| token del prompt per domanda, con tokensave su codice nel prompt | ↓ | **70.6** | **72.7** | -2.2 |
| token generati per domanda, con tokensave su senza strumenti | ↓ | 116.5 | 137.5 | -21.0 |

### velocita — ↑ più alto è meglio; le voci ↓, più basso è meglio

| Voce | Meglio | Valore | Valore precedente | Differenza |
| --- | :---: | ---: | ---: | ---: |
| lettura del prompt (pp512), Inga su llama.cpp | ↑ | **188.6** | **106.4** | +82.2 |
| generazione (tg128), Inga su llama.cpp | ↑ | **130.0** | **107.4** | +22.6 |
| perplexity, Inga su llama.cpp | ↓ | **99.9** | **99.9** | 0.0 |

## Casi saltati o in errore

- colibri-velocita: RuntimeError: risposta senza usage o senza token: {'prompt_tokens': 512, 'completion_tokens': 0, 'total_tokens': 512} ''

Macchina: x86_64, 4 CPU, Linux-7.0.0-1017-azure-x86_64-with-glibc2.39.
