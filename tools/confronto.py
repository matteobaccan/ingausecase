"""The common loop of the cases that ask the same questions to Inga and to llama.cpp.

Both answer with the same messages, greedy, seed fixed, on the same GGUF file (Inga's
server started by the runner, llama-server started here). Each case gives its items,
how to ask and how to score; this module asks both, prints a line per item and writes
the result: the score of Inga (the case's score), the score of llama.cpp, the
difference and how many answers are the same text.
"""

import os

import inga_api
import llama


def esegui(nome, elementi, messaggi, voto, max_tokens, dettagli=None):
    """elementi: list of items; messaggi(item) -> chat messages; voto(item, text) ->
    (score 0..1, short note). Writes the case's result."""
    if not llama.cartella():
        inga_api.write_result({"stato": "saltato", "motivo": "llama.cpp non c'è (IUC_LLAMA)"})
        return
    model = os.environ["IUC_MODEL_PATH"]
    ctx = int(os.environ.get("IUC_CTX", "4096"))
    log = os.path.join(inga_api.work_dir(), "llama-server.log")
    righe = []
    try:
        with llama.Server(model, ctx, log) as srv:
            for i, el in enumerate(elementi):
                msgs = messaggi(el)
                riga = {"n": i}
                for motore, url in (("inga", None), ("llama.cpp", srv.url)):
                    try:
                        testo, _, sec = inga_api.chat(msgs, max_tokens=max_tokens, url=url)
                    except (RuntimeError, OSError, ValueError) as e:
                        testo, sec = f"[errore: {e}]", 0.0
                    v, nota = voto(el, testo)
                    riga[motore] = {"voto": v, "nota": nota, "secondi": round(sec, 1), "testo": testo}
                riga["uguali"] = riga["inga"]["testo"].strip() == riga["llama.cpp"]["testo"].strip()
                print(f"{nome} {i:3d}: Inga {riga['inga']['voto']:.2f} ({riga['inga']['nota']}), "
                      f"llama.cpp {riga['llama.cpp']['voto']:.2f} ({riga['llama.cpp']['nota']}), "
                      f"{'stesso testo' if riga['uguali'] else 'testi diversi'}", flush=True)
                righe.append(riga)
    except RuntimeError as e:
        if not righe:
            inga_api.write_result({"stato": "errore", "motivo": f"llama.cpp: {e}"})
            return
        print(f"llama-server interrotto dopo {len(righe)} domande: {e}")
    n = len(righe)
    a = sum(r["inga"]["voto"] for r in righe) / n
    b = sum(r["llama.cpp"]["voto"] for r in righe) / n
    stesso = sum(r["uguali"] for r in righe) / n
    sec_a = sum(r["inga"]["secondi"] for r in righe)
    sec_b = sum(r["llama.cpp"]["secondi"] for r in righe)
    inga_api.write_result({
        "stato": "ok",
        "voto": a,
        "voci": {"Inga": a, "llama.cpp": b, "Inga meno llama.cpp": a - b,
                 "risposte con lo stesso testo": stesso,
                 "tempo di llama.cpp su quello di Inga": sec_b / sec_a if sec_a else 0.0},
        "dettagli": dict(dettagli or {}, domande=n, llama_cpp=llama.versione(),
                         secondi_inga=round(sec_a), secondi_llama=round(sec_b), risposte=righe),
    })
