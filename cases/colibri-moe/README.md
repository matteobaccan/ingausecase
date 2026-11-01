# colibri-moe

Una mixture of experts **più grande della RAM che le si dà**, con Inga e con
[Colibri](https://github.com/JustVugg/colibri): tutti e due tengono in RAM la parte
densa e leggono dal disco gli esperti che non ci stanno. Lo stesso GGUF,
[Qwen3-30B-A3B Q4_K_M](https://huggingface.co/unsloth/Qwen3-30B-A3B-GGUF) (18,6 GB, 128
esperti per strato, 8 attivi; sha256 in [`models.json`](https://github.com/matteobaccan/ingausecase/blob/cases/models.json)),
sulla stessa macchina (un runner di GitHub: 4 CPU, 16 GB di RAM), con lo stesso budget
di RAM: 8 GB.

- **Inga:** `inga serve --mem-limit 8G` (gli strati o gli esperti che non ci stanno si
  leggono dal disco mentre il modello gira).
- **Colibri:** `coli serve --ram 8` (RAM_GB: il budget con cui il motore dimensiona la
  sua cache di esperti), dopo `coli import` del GGUF.
- **Un motore alla volta:** il modello non sta due volte nella RAM del runner, quindi il
  runner non avvia Inga (`"avvia_inga": false`): lo avvia il caso, lo ferma, poi avvia
  Colibri. Prima di ogni misura la cache delle pagine del sistema si svuota (`sudo`, che
  i runner hanno: `cache_svuotata` nei dettagli), così nessuno legge il file dalla RAM
  lasciata dall'altro.
- **Velocità:** come in [`colibri-velocita`](../colibri-velocita): prompt di circa 512
  token, 128 generati, 3 ripetizioni, dall'API in streaming. Voci: i rapporti Inga su
  Colibri della lettura e della generazione; voto: la loro media.
- **Risposte:** 6 domande di ARC-Challenge e 4 problemi di GSM8K (i primi dei casi
  [`arc`](../arc) e [`gsm8k`](../gsm8k)), valutati come lì. Voci: le giuste di ognuno e
  quelle con lo stesso testo.
- **Memoria:** il picco della memoria residente (VmHWM) del processo e dei figli, nei
  dettagli, con i secondi di avvio.

**Cosa non misura.** Il budget è quello che ogni motore si dà da sé, non un limite del
sistema: nessuno dei due è chiuso in un cgroup, e la cache delle pagine del kernel può
tenere in RAM parte del file oltre gli 8 GB (16 GB in tutto sul runner), per tutti e due
allo stesso modo; quanto il disco del runner (una SSD di rete) pesa sulla velocità non si
separa dal resto. I due motori non contano la memoria allo stesso modo (`--mem-limit` di
Inga e `--ram` di Colibri sono il budget di ognuno, con le sue regole: il picco di RSS
nei dettagli dice quanto hanno usato). Non è la velocità con tutto il modello in RAM, né
quella con una GPU, né un confronto di qualità (10 domande sono poche): dice se Inga
regge il confronto con un motore fatto apposta per gli esperti dal disco, sullo stesso
file e con la stessa memoria. Con un modello che Colibri non ha (`--model`), il caso si
dà come saltato; con un modello piccolo (`--model qwen3-0.6b`) gira tutto in RAM e prova
solo il percorso del caso.

Il disco del runner non basta per il modello: il caso chiede 26 GB (`disco_gb` in
`case.json`) e i workflow tolgono prima gli SDK che i casi non usano (dotnet, Android,
GHC, CodeQL). Il modello è più grande della cache di GitHub (10 GB): si scarica a ogni
esecuzione.
