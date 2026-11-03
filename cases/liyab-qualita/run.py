"""Caso liyab-qualita: le stesse domande a Inga e a Liyab, sullo stesso file del modello.

ARC domande di ARC-Challenge e GSM domande di GSM8K (le prime delle domande fisse dei
casi arc e gsm8k, dati.json), fatte e valutate come in quei casi, greedy: a Inga dalla sua
API di chat, a Liyab con `liyab-cli` sullo stesso testo già passato dal ChatML di Qwen3
(liyab-cli prende testo grezzo). Un processo di liyab-cli per domanda: il suo
caricamento non entra nei tempi (si usano i suoi). Voto: la parte di risposte giuste di
Inga; le voci dicono anche quella di Liyab, per test e in tutto, e quante risposte hanno
lo stesso testo.
"""

import os
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import confronto  # noqa: E402
import dati  # noqa: E402
import inga_api  # noqa: E402
import liyab  # noqa: E402

ARC, GSM = 20, 20


def main():
    if not liyab.cartella():
        inga_api.write_result({"stato": "saltato", "motivo": "Liyab non c'è (IUC_LIYAB)"})
        return
    model, ctx = os.environ["IUC_MODEL_PATH"], int(os.environ.get("IUC_CTX", "4096"))
    arc, gsm = confronto.caso("arc"), confronto.caso("gsm8k")
    casi = {"ARC": (arc, 256), "GSM8K": (gsm, 512)}
    try:
        elementi = ([{"test": "ARC", "el": e} for e in arc.scegli(ARC)]
                    + [{"test": "GSM8K", "el": e} for e in gsm.scegli(GSM)])
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    righe = []
    picco_liyab = 0
    for i, x in enumerate(elementi):
        mod, max_tok = casi[x["test"]]
        msgs = mod.messaggi(x["el"])
        try:
            ti, _, si = inga_api.chat(msgs, max_tokens=max_tok)
        except (RuntimeError, OSError, ValueError) as e:
            ti, si = f"[errore: {e}]", 0.0
        try:
            g = liyab.genera(model, liyab.chatml(msgs), max_tok, ctx)
            tl, sl = g["risposta"], (g["turno"]["ttft_ms"] + g["turno"]["decode_ms"]) / 1000
            picco_liyab = max(picco_liyab, g["turno"].get("peak_rss_mib") or 0)
        except (RuntimeError, OSError, ValueError, subprocess.TimeoutExpired) as e:
            tl, sl = f"[errore: {e}]", 0.0
        # voto() dà (punteggio, spiegazione), come negli altri casi
        vi, vl = mod.voto(x["el"], ti), mod.voto(x["el"], tl)
        vi, vl = (vi[0] if isinstance(vi, tuple) else vi), (vl[0] if isinstance(vl, tuple) else vl)
        righe.append({"test": x["test"], "inga": {"testo": ti, "voto": vi, "secondi": round(si, 2)},
                      "liyab": {"testo": tl, "voto": vl, "secondi": round(sl, 2)}})
        print(f"  {i + 1}/{len(elementi)} {x['test']}: Inga {vi}, Liyab {vl}", flush=True)
    n = len(righe)
    gi = sum(r["inga"]["voto"] for r in righe) / n
    gl = sum(r["liyab"]["voto"] for r in righe) / n
    ti_tot = sum(r["inga"]["secondi"] for r in righe) or 1
    voci = {"Inga": gi, "Liyab": gl, "Inga meno Liyab": gi - gl,
            "risposte con lo stesso testo": sum(r["inga"]["testo"].strip() == r["liyab"]["testo"].strip()
                                                for r in righe) / n,
            "tempo di Liyab su quello di Inga": sum(r["liyab"]["secondi"] for r in righe) / ti_tot,
            "picco di memoria residente, Inga (MiB)": liyab.picco_inga(),
            "picco di memoria residente, Liyab (MiB)": picco_liyab or None}
    for test in casi:
        mie = [r for r in righe if r["test"] == test]
        for m, nome in (("inga", "Inga"), ("liyab", "Liyab")):
            voci[f"{test}, {nome}"] = sum(r[m]["voto"] for r in mie) / len(mie)
    errori = sum(r["liyab"]["testo"].startswith("[errore") for r in righe)
    inga_api.write_result({"stato": "ok" if errori < n else "errore",
                           "motivo": None if errori < n else righe[0]["liyab"]["testo"][:600],
                           "voto": gi, "voci": voci,
                           "dettagli": {"risposte": righe, "liyab": liyab.versione(), "errori_liyab": errori}})


if __name__ == "__main__":
    main()
