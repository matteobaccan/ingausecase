---
title: "OCR locale"
category: trend
tags: [ocr, documenti, open-source, privacy, locale, benchmark]
related_puntate: [20261021]
created: 2026-10-19
updated: 2026-10-31
---

# OCR locale

## Introduzione

Il riconoscimento ottico dei caratteri eseguito sulla macchina che elabora i documenti, senza passare dall'API di un fornitore esterno: la condizione che rende utilizzabili scansioni, contratti e fatture a studi professionali, uffici tecnici e pubbliche amministrazioni. Nel 2026 la classifica OmniDocBench è guidata da tre modelli sotto il miliardo e mezzo di parametri, mentre Tesseract conserva un mestiere preciso sui PDF scansionati senza GPU.

## Evoluzione nel tempo

- La corsa ai modelli giganti si è fermata: PaddleOCR-VL-1.6 (0,9 miliardi di parametri), MinerU2.5-Pro (1,2 miliardi) e GLM-OCR (0,9 miliardi) occupano i primi tre posti di OmniDocBench v1.6 con 96,34, 95,75 e 95,22, davanti a dots.ocr, DeepSeek-OCR 2, MinerU pipeline classica, olmOCR e Marker.
- I modelli da 0,9 miliardi girano su una GPU NVIDIA RTX 30 o successiva e su Apple Silicon tramite MLX-VLM; senza scheda video resta la coppia [[tesseract-ocr|Tesseract]] più OCRmyPDF, che legge oltre cento lingue e produce un PDF ricercabile ma non capisce tabelle né impaginazione.
- Sui server con GPU NVIDIA conviene servire PaddleOCR-VL o MinerU con vLLM, oppure usare olmOCR per le conversioni di massa; per i documenti lunghi letti in un solo passaggio c'è Unlimited-OCR.
- Le licenze pesano in azienda: PaddleOCR, GLM-OCR, Docling e olmOCR sono Apache 2.0 o MIT, mentre MinerU e i pesi di Marker aggiungono soglie di fatturato o di utenti.

## Attori coinvolti

- [[paddleocr-vl-1-6|PaddleOCR-VL-1.6]], 0,9B, 96,34 su OmniDocBench v1.6, licenza Apache 2.0.
- [[mineru|MinerU2.5-Pro]], 1,2B, 95,75, licenza Apache 2.0 con condizioni oltre 100 milioni di utenti attivi mensili o 20 milioni di dollari di ricavi mensili.
- GLM-OCR di Z.ai, 0,9B, 95,22, pesi MIT e codice Apache 2.0.
- [[tesseract-ocr|Tesseract]] e OCRmyPDF, per i PDF scansionati su CPU.
- [[olmocr|olmOCR]], 7B, 85,74 su OmniDocBench ma con requisiti e costi dichiarati con precisione: almeno 12 GB di VRAM, 30 GB di disco e meno di 200 dollari per milione di pagine.
- Docling di IBM, MIT, con il modello Granite-Docling da 258 milioni di parametri.

## Notizie rilevanti

- PaddleOCR-VL-1.6 è arrivato con PaddleOCR 3.6.0 il 28 maggio 2026 e richiede, per vLLM, compute capability 8.0 o superiore e CUDA 12.6, cioè le serie RTX 30, 40 e 50, la A10 e la A100; su T4 e V100 vLLM parte ma rischia timeout e saturazione della memoria. La VRAM minima non è dichiarata.
- MinerU è organizzato a livelli: il basic con ONNX occupa circa 0,8 GB di modelli, chiede 2 GB di RAM e si accontenta di una CPU, mentre standard e advanced richiedono almeno 16 GB di RAM e una GPU con 8 GB di VRAM.
- Tesseract ha oltre 77.000 stelle su GitHub, licenza Apache 2.0 e più di cento lingue senza addestramento aggiuntivo; dalla versione 4 usa una rete LSTM per righe di testo, non ha interfaccia grafica e non legge tabelle, colonne o formule.
- Nessun benchmark misura l'italiano: OmniDocBench valuta il testo solo in cinese e inglese, GLM-OCR non dichiara le lingue e la documentazione di PaddleOCR-VL parla di 109 lingue senza nominare l'italiano. Il test utile è su venti pagine reali, confrontate a mano.
- L'OCR locale non elimina tutti i rischi: il testo estratto finisce spesso in un modello linguistico e va trattato come input non fidato, perché un documento costruito ad hoc può contenere istruzioni nascoste; i modelli generativi, a differenza di Tesseract, possono inoltre inventare parole illeggibili.

## Timeline delle notizie

- **2026-10-19** - La guida ai migliori OCR locali del 2026 indica PaddleOCR-VL-1.6, MinerU2.5-Pro e GLM-OCR per la qualità su documenti complessi e Tesseract con OCRmyPDF per i PDF scansionati senza GPU; nessuno dei benchmark disponibili misura l'italiano e le licenze di MinerU e Marker aggiungono soglie commerciali.
- **2026-10-21** — Compare un modello da un milione di parametri che gira su CPU, supporta il giapponese e converte PDF e immagini in Markdown o JSON con le coordinate, anche con testo verticale, con licenza Apache-2.0.
- **2026-10-30** — [[xiaomi]] ha pubblicato [[xiaomi-ocr-0]], modello da 0,8 miliardi di parametri con licenza Apache 2.0 che restituisce Markdown, tabelle in OTSL, formule in LaTeX e campi JSON e risponde a domande sul contenuto; in locale gira con SGLang, vLLM o Ollama e il pacchetto GGUF della comunità occupa circa 1,8 GB. La scheda dichiara 96,83 su OmniDocBench v1.6, con TeleOCR da 1,2B quattro centesimi sopra, e sulla classifica pubblica di Real5 scende a 92,73 dietro PaddleOCR-VL-1.6.







## Collegamenti

- [[paddleocr-vl-1-6]]
- [[mineru]]
- [[glm-ocr]]
- [[tesseract-ocr]]
- [[olmocr]]
- [[docling]]
- [[ai-locale]]
- [[index]]
