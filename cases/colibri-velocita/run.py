"""Caso colibri-velocita: la velocità di Inga e di Colibri sullo stesso file del modello,
sulla stessa macchina, misurata allo stesso modo per tutti e due.

Colibri non ha un comando come `inga bench` o `llama-bench` (il suo `coli bench` dà voti
di qualità, e solo per GLM): la misura passa dall'API in streaming dei due server, con
le stesse richieste. Un prompt di circa P token (frasi sintetiche, quante ne servono:
contate una volta con l'usage di Inga) che chiede di contare fino a 1000, così la
risposta arriva sempre a N token; R ripetizioni per motore, ognuna con una prima riga
diversa (niente cache dei prefissi), dopo una richiesta di riscaldamento.

- lettura del prompt: i token del prompt (usage) sul tempo fino al primo token;
- generazione: i token dopo il primo sul tempo dopo il primo.

In più, `tools/benchmark_http_serving.py` di Colibri (lo strumento che Colibri usa per
misurare un server OpenAI in streaming) su altri R prompt fatti allo stesso modo, contro i
due server: token generati al secondo dall'inizio alla fine della richiesta. Il server di
Inga è quello avviato dal runner; quello di Colibri resta acceso accanto (il modello sta
due volte in RAM, come nel caso velocita con llama.cpp). Voto: la media dei due rapporti Inga su
Colibri (1 = come Colibri).
"""

import json
import os
import subprocess
import sys

sys.path.insert(0, os.environ["IUC_TOOLS"])
import colibri  # noqa: E402
import confronto  # noqa: E402
import inga_api  # noqa: E402

P, N, R = 512, 128, 3


def benchmark_http(url, modello, frasi, nome):
    """benchmark_http_serving.py di Colibri sui prompt delle R ripetizioni."""
    work = inga_api.work_dir()
    carico = os.path.join(work, "carico.jsonl")
    with open(carico, "w", encoding="utf-8") as f:
        # altri prompt che quelli della misura (la cache dei prefissi non li conosce)
        for r in range(R):
            f.write(json.dumps({"messages": confronto._messaggi(frasi, R + r, 2 * R)}) + "\n")
    out = os.path.join(work, f"benchmark-http-{nome}.json")
    cmd = [sys.executable, os.path.join(colibri.cartella(), "tools", "benchmark_http_serving.py"),
           "--base-url", url + "/v1", "--model", modello, "--workload", carico, "--output", out,
           "--concurrency", "1", "--repeats", "1", "--max-tokens", str(N), "--temperature", "0",
           "--timeout", "1200"]
    print("$ " + " ".join(cmd), flush=True)
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=7200)
    if not os.path.exists(out):
        raise RuntimeError(f"benchmark_http_serving.py è uscito con {p.returncode}: {(p.stderr or p.stdout)[-800:]}")
    with open(out, encoding="utf-8") as f:
        s = json.load(f)["summary"] or {}
    return {"token_al_secondo": s.get("successful_completion_tokens_per_second"),
            "primo_output_p50": (s.get("successful_first_output_seconds") or {}).get("p50"),
            "riuscite": s.get("succeeded"), "fallite": s.get("failed")}


def main():
    perche = confronto.manca("colibri")
    if perche:
        inga_api.write_result({"stato": "saltato", "motivo": perche})
        return
    model, ctx = os.environ["IUC_MODEL_PATH"], int(os.environ.get("IUC_CTX", "2048"))
    out = {}
    try:
        frasi = confronto.frasi_per(None, None, P)
        print(f"Inga: {frasi} frasi per un prompt di circa {P} token", flush=True)
        out["inga"] = confronto.velocita(None, None, frasi, N, R)
        out["inga_http"] = benchmark_http(inga_api.base_url(), os.environ.get("INGA_MODEL", ""),
                                          frasi, "inga")
        with confronto.Colibri(model, ctx) as c:
            print(f"Colibri: pronto in {c.srv.secondi_avvio:.0f} s", flush=True)
            out["colibri"] = confronto.velocita(c.url, c.extra(), frasi, N, R)
            out["colibri_http"] = benchmark_http(c.url, colibri.MODEL_ID, frasi, "colibri")
            out["colibri_motore"] = c.info()
    except (RuntimeError, OSError, ValueError, KeyError, subprocess.TimeoutExpired) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"{type(e).__name__}: {e}", "dettagli": out})
        return
    pp = out["inga"]["pp"] / out["colibri"]["pp"]
    tg = out["inga"]["tg"] / out["colibri"]["tg"]
    voci = {f"lettura del prompt (~{P} token), Inga su Colibri": pp,
            f"generazione ({N} token), Inga su Colibri": tg}
    a, b = out["inga_http"]["token_al_secondo"], out["colibri_http"]["token_al_secondo"]
    if a and b:
        voci["token al secondo dall'inizio alla fine (benchmark_http_serving di Colibri), Inga su Colibri"] = a / b
    print(f"prompt: Inga {out['inga']['pp']:.1f}, Colibri {out['colibri']['pp']:.1f} tok/s ({pp:.2f}x); "
          f"generazione: Inga {out['inga']['tg']:.2f}, Colibri {out['colibri']['tg']:.2f} tok/s ({tg:.2f}x)")
    inga_api.write_result({
        "stato": "ok",
        "voto": (pp + tg) / 2,
        "voci": voci,
        "dettagli": dict(out, frasi=frasi, token_generati=N, ripetizioni=R, colibri=colibri.versione(),
                         cpu=os.cpu_count()),
    })


if __name__ == "__main__":
    main()
