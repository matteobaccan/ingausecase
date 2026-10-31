"""Caso di prova: una domanda in chat, la risposta non deve essere vuota.

Misura il tempo al primo token (TTFT) e il tempo totale della risposta, in streaming.
"""

import os
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import inga_api  # noqa: E402

DOMANDA = "Qual è la capitale d'Italia? Rispondi con una frase."

text, ttft, total = inga_api.chat_stream(
    [{"role": "user", "content": DOMANDA}], max_tokens=64)
text = text.strip()
ok = bool(text)
print(f"risposta: {text!r}")
print(f"primo token dopo {ttft} s, risposta in {total:.2f} s")
inga_api.write_result({
    "stato": "ok",
    "voto": 1.0 if ok else 0.0,
    "voci": {"risposta non vuota": 1.0 if ok else 0.0},
    "dettagli": {
        "domanda": DOMANDA,
        "risposta": text,
        "contiene_roma": "roma" in text.lower(),
        "secondi_primo_token": round(ttft, 3) if ttft is not None else None,
        "secondi_risposta": round(total, 3),
    },
})
