"""Caso liyab-velocita: la velocità di Inga e di Liyab sullo stesso file del modello,
sulla stessa macchina.

Liyab non ha un server fuori dalla sua app: si misura con `liyab-cli --json`, che dice i
suoi tempi (token del prompt, tempo al primo token, tempo della generazione, picco di
memoria residente). Il prompt è lo stesso del caso colibri-velocita (circa P token di
frasi sintetiche, che chiede di contare fino a 1000, così la risposta arriva sempre a N
token), con una prima riga diversa a ogni ripetizione: a Inga dall'API in streaming, a
Liyab lo stesso testo già passato dal ChatML di Qwen3. Una prova non misurata prima, per
tutti e due (per Liyab porta il file nella cache delle pagine: ogni prova è un processo).

- lettura del prompt: i token del prompt sul tempo fino al primo token;
- generazione: i token dopo il primo sul tempo dopo il primo.

Voto: la media dei due rapporti Inga su Liyab (1 = come Liyab). Le misure dei due motori
non vengono dallo stesso orologio (lo streaming HTTP per Inga, le statistiche di
liyab-cli per Liyab, che non contano il caricamento del modello): lo dice il risultato.
"""

import os
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import inga_api  # noqa: E402
import liyab  # noqa: E402

P, N, R = 512, 128, 3


def velocita_liyab(model, ctx, frasi):
    liyab.genera(model, liyab.chatml(confronto._messaggi(10, 99, 1)), 8, ctx)
    prove = []
    for r in range(R):
        g = liyab.genera(model, liyab.chatml(confronto._messaggi(frasi, r, R)), N, ctx)
        t = g["turno"]
        pt, ct = t["prompt_tokens"], t["generated_tokens"]
        if not pt or ct < 2 or not t["ttft_ms"] or not t["decode_ms"]:
            raise RuntimeError(f"liyab-cli senza token o senza tempi: {t}")
        prove.append({"token_prompt": pt, "token_generati": ct, "ttft": t["ttft_ms"] / 1000,
                      "decode_s": t["decode_ms"] / 1000, "tokens_per_second": t["tokens_per_second"],
                      "bozze_proposte": t.get("draft_tokens_proposed"),
                      "bozze_accettate": t.get("draft_tokens_accepted"),
                      "picco_rss_mib": t.get("peak_rss_mib"), "secondi_processo": round(g["secondi"], 2),
                      "pp": pt / (t["ttft_ms"] / 1000), "tg": (ct - 1) / (t["decode_ms"] / 1000)})
        print(f"    prova {r + 1}: {pt} token di prompt, primo token in {t['ttft_ms'] / 1000:.2f} s "
              f"({prove[-1]['pp']:.1f} tok/s), {ct} generati, {prove[-1]['tg']:.2f} tok/s "
              f"(liyab: {t['tokens_per_second']:.2f}), picco {t.get('peak_rss_mib')} MiB", flush=True)
    return {"pp": sum(p["pp"] for p in prove) / R, "tg": sum(p["tg"] for p in prove) / R,
            "token_prompt": prove[0]["token_prompt"], "prove": prove}


def main():
    if not liyab.cartella():
        inga_api.write_result({"stato": "saltato", "motivo": "Liyab non c'è (IUC_LIYAB)"})
        return
    model, ctx = os.environ["IUC_MODEL_PATH"], int(os.environ.get("IUC_CTX", "4096"))
    out = {}
    try:
        frasi = confronto.frasi_per(None, None, P)
        print(f"Inga: {frasi} frasi per un prompt di circa {P} token", flush=True)
        out["inga"] = confronto.velocita(None, None, frasi, N, R)
        print("Liyab:", flush=True)
        out["liyab"] = velocita_liyab(model, ctx, frasi)
    except (RuntimeError, OSError, ValueError, KeyError, subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    pp = out["inga"]["pp"] / out["liyab"]["pp"]
    tg = out["inga"]["tg"] / out["liyab"]["tg"]
    print(f"prompt: Inga {out['inga']['pp']:.1f}, Liyab {out['liyab']['pp']:.1f} tok/s ({pp:.2f}x); "
          f"generazione: Inga {out['inga']['tg']:.2f}, Liyab {out['liyab']['tg']:.2f} tok/s ({tg:.2f}x)")
    inga_api.write_result({
        "stato": "ok",
        "voto": (pp + tg) / 2,
        "voci": {f"lettura del prompt (~{P} token), Inga su Liyab": pp,
                 f"generazione ({N} token), Inga su Liyab": tg,
                 "lettura del prompt, Inga (tok/s)": out["inga"]["pp"],
                 "lettura del prompt, Liyab (tok/s)": out["liyab"]["pp"],
                 "generazione, Inga (tok/s)": out["inga"]["tg"],
                 "generazione, Liyab (tok/s)": out["liyab"]["tg"]},
        "dettagli": dict(out, frasi=frasi, token_generati=N, ripetizioni=R, liyab=liyab.versione(),
                         cpu=os.cpu_count(),
                         misura="Inga: API in streaming; Liyab: statistiche di liyab-cli --json"),
    })


if __name__ == "__main__":
    main()
