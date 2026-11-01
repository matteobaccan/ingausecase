"""The common loop of the cases that ask the same questions to Inga and to another
engine on the same GGUF file: llama.cpp (llama-server), Colibri (coli serve), or both.

All answer with the same messages, greedy, seed fixed (Inga's server started by the
runner, the others started here). Each case gives its items, how to ask and how to
score; this module asks every engine, prints a line per item and writes the result:
the score of Inga (the case's score), the score of each other engine, the difference
and how many answers are the same text.

With in_sequenza=True the engines run one after the other instead of side by side,
each server stopped before the next starts (Inga too, started here with the case's own
options: the case says "avvia_inga": false in case.json): for models that do not fit
twice in the runner's RAM. `velocita` measures the reading of a prompt and the
generation through the streaming API, the same way for every engine.
"""

import contextlib
import json
import os
import random
import subprocess
import time

import inga_api
import llama

MOTORI = ("llama.cpp", "colibri")


# --------------------------------------------------------------------------- engines

class _Motore:
    nome = ""
    url = None
    versione = None

    def extra(self, think=False):
        return None

    def info(self):
        return {}

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class IngaDelRunner(_Motore):
    """The server the runner started for the case (INGA_URL)."""
    nome = "inga"


class IngaDelCaso(_Motore):
    """inga serve started here, with the runner's options and `argomenti` (by default
    the argomenti_serve of case.json, e.g. --mem-limit), for a case with "avvia_inga":
    false."""
    nome = "inga"

    def __init__(self, argomenti=None, attesa=1800):
        if argomenti is None:
            argomenti = json.loads(os.environ.get("IUC_ARGOMENTI_SERVE") or "[]")
        self.argomenti = list(argomenti)
        self.attesa = attesa
        self.n = 0

    def __enter__(self):
        import runner
        self.n += 1
        work = inga_api.work_dir()
        home = os.path.join(work, f"inga-home-{self.n}")
        os.makedirs(home, exist_ok=True)
        self.srv = runner.Server(os.environ["IUC_INGA"], os.environ["IUC_MODEL_PATH"],
                                 int(os.environ.get("IUC_CTX", "4096")), inga_api.SEED, home,
                                 os.path.join(work, f"inga-serve-{self.n}.log"), self.argomenti)
        try:
            self.secondi_avvio = self.srv.wait(self.attesa)
            self.id = self.srv.model_id()
        except runner.Failure as e:
            self.srv.stop()
            raise RuntimeError(str(e)) from None
        self.url = self.srv.url
        return self

    def extra(self, think=False):
        return {"model": self.id}

    def info(self):
        from colibri import picco_rss
        return {"secondi_avvio": round(self.secondi_avvio, 1), "argomenti": self.argomenti,
                "picco_rss_gb": round(picco_rss(self.srv.proc.pid) / 1e9, 2)}

    def __exit__(self, *exc):
        self.info_finale = self.info()
        self.srv.stop()
        return False


class LlamaCpp(_Motore):
    nome = "llama.cpp"

    def __init__(self, model, ctx):
        self.srv = llama.Server(model, ctx, os.path.join(inga_api.work_dir(), "llama-server.log"))
        self.versione = llama.versione()

    def __enter__(self):
        self.srv.__enter__()
        self.url = self.srv.url
        return self

    def __exit__(self, *exc):
        return self.srv.__exit__(*exc)


class Colibri(_Motore):
    nome = "colibri"

    def __init__(self, model, ctx, ram=None):
        import colibri
        self.srv = colibri.Server(model, ctx, os.path.join(inga_api.work_dir(), "colibri-serve.log"),
                                  ram=ram, work=inga_api.work_dir())
        self.versione = colibri.versione()

    def __enter__(self):
        self.srv.__enter__()
        self.url = self.srv.url
        return self

    def extra(self, think=False):
        return self.srv.extra(think)

    def info(self):
        h = self.srv.health
        return {"secondi_avvio": round(self.srv.secondi_avvio, 1), "ram_gb": self.srv.ram,
                "picco_rss_gb": round(self.srv.picco_rss() / 1e9, 2),
                "thread": (h.get("system") or {}).get("engine_threads"),
                "contesto": h.get("context_tokens")}

    def __exit__(self, *exc):
        self.info_finale = self.info()
        return self.srv.__exit__(*exc)


def manca(nome, model=None):
    """Why the engine cannot run here (None if it can)."""
    if nome == "llama.cpp":
        return None if llama.cartella() else "llama.cpp non c'è (IUC_LLAMA)"
    if nome == "colibri":
        import colibri
        if not colibri.cartella():
            return "Colibri non c'è (IUC_COLIBRI)"
        ok, perche = colibri.supporta(model or os.environ["IUC_MODEL_PATH"])
        return None if ok else perche
    return f"motore sconosciuto: {nome}"


def motore(nome, model, ctx, ram=None):
    if nome == "llama.cpp":
        return LlamaCpp(model, ctx)
    if nome == "colibri":
        return Colibri(model, ctx, ram)
    raise ValueError(nome)


def svuota_cache():
    """Drop the page cache (sudo without a password, as on GitHub's runners), so the
    next engine reads the model from the disk and not from what the previous one left
    in RAM. False if it cannot."""
    try:
        p = subprocess.run(["sudo", "-n", "sh", "-c", "sync; echo 3 > /proc/sys/vm/drop_caches"],
                           capture_output=True, timeout=120)
        return p.returncode == 0
    except (OSError, subprocess.TimeoutExpired):
        return False


# --------------------------------------------------------------------------- speed

_PAROLE = ("river mill boat stone garden window lamp market bridge harbor letter road "
           "forest valley tower clock village winter summer morning evening teacher "
           "farmer painter baker sailor doctor child friend neighbor story song").split()
_VERBI = "carried painted found watched opened closed repaired visited crossed described".split()


def _testo(frasi, seme):
    rng = random.Random(seme)
    out = []
    for i in range(frasi):
        a, b, c = rng.sample(_PAROLE, 3)
        out.append(f"The {a} near the old {b} {rng.choice(_VERBI)} {rng.randint(2, 99)} "
                   f"{c}s before noon.")
    return " ".join(out)


def _messaggi(frasi, r, ripetizioni):
    # la prima riga cambia a ogni ripetizione: niente cache dei prefissi fra una e l'altra
    return [{"role": "user", "content":
             f"Run {r + 1} of {ripetizioni}, code {7919 * (r + 3)}.\n\n"
             f"{_testo(frasi, 1000 + r)}\n\nNow count from 1 to 1000, one number per line, "
             "without any other text."}]


def frasi_per(url, extra, n_prompt=512):
    """How many sentences make a prompt of about n_prompt tokens, measured once on the
    server at url (prompt_tokens of the usage)."""
    _, data, _ = inga_api.chat(_messaggi(40, 0, 1), max_tokens=1, url=url, extra=extra)
    t40 = data["usage"]["prompt_tokens"]
    _, data, _ = inga_api.chat(_messaggi(20, 0, 1), max_tokens=1, url=url, extra=extra)
    t20 = data["usage"]["prompt_tokens"]
    per_frase = max((t40 - t20) / 20, 1.0)
    return max(1, round(40 + (n_prompt - t40) / per_frase))


def velocita(url, extra, frasi, n_gen=128, ripetizioni=3):
    """Reading of the prompt and generation through the streaming API: the prompt
    tokens (usage) over the time to the first token, and the tokens after the first
    over the time after it. One unmeasured request first. Returns the means and each
    repetition."""
    inga_api.stream(_messaggi(10, 99, 1), max_tokens=8, url=url, extra=extra)
    prove = []
    for r in range(ripetizioni):
        x = inga_api.stream(_messaggi(frasi, r, ripetizioni), max_tokens=n_gen, url=url,
                            extra=extra, timeout=3600)
        u = x["usage"] or {}
        pt, ct = u.get("prompt_tokens"), u.get("completion_tokens")
        if not pt or not ct or x["ttft"] is None or ct < 2:
            raise RuntimeError(f"risposta senza usage o senza token: {u} {x['testo'][:200]!r}")
        prove.append({"token_prompt": pt, "token_generati": ct, "ttft": round(x["ttft"], 3),
                      "secondi": round(x["secondi"], 3),
                      "pp": pt / x["ttft"], "tg": (ct - 1) / (x["secondi"] - x["ttft"])})
        print(f"    prova {r + 1}: {pt} token di prompt in {x['ttft']:.2f} s "
              f"({prove[-1]['pp']:.1f} tok/s), {ct} generati, {prove[-1]['tg']:.2f} tok/s", flush=True)
    return {"pp": sum(p["pp"] for p in prove) / len(prove),
            "tg": sum(p["tg"] for p in prove) / len(prove),
            "token_prompt": prove[0]["token_prompt"], "prove": prove}


# --------------------------------------------------------------------------- loop

def caso(nome):
    """The run.py of another case as a module (its scegli, messaggi, voto), to ask the
    same questions in the same way."""
    import importlib.util
    path = os.path.join(os.path.dirname(os.environ["IUC_CASE_DIR"]), nome, "run.py")
    spec = importlib.util.spec_from_file_location(f"caso_{nome.replace('-', '_')}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _chiedi(m, msgs, max_tokens, think):
    try:
        testo, _, sec = inga_api.chat(msgs, max_tokens=max_tokens, url=m.url,
                                      extra=m.extra(think), think=think)
    except (RuntimeError, OSError, ValueError) as e:
        testo, sec = f"[errore: {e}]", 0.0
    return testo, sec


def esegui(nome, elementi, messaggi, voto, max_tokens, dettagli=None, motori=("llama.cpp",),
           in_sequenza=False, inga=None, ram=None, misura=None, think=False, scrivi=True):
    """elementi: list of items; messaggi(item) -> chat messages; voto(item, text) ->
    (score 0..1, short note); max_tokens: a number or max_tokens(item). motori: the
    engines beside Inga (llama.cpp, colibri). in_sequenza: one engine at a time (inga: the IngaDelCaso to use, by default the
    runner's server); ram: Colibri's RAM budget in GB; misura(engine, url, extra) ->
    dict, called once per engine as soon as its server is ready (in dettagli.misure).
    Writes the case's result (unless scrivi=False) and returns it."""

    def fine(r):
        if scrivi:
            inga_api.write_result(r)
        return r

    model = os.environ["IUC_MODEL_PATH"]
    ctx = int(os.environ.get("IUC_CTX", "4096"))
    perche = {m: manca(m, model) for m in motori}
    altri = [m for m in motori if not perche[m]]
    if not altri:
        return fine({"stato": "saltato", "motivo": "; ".join(perche.values())})
    inga = inga or IngaDelRunner()
    tutti = [inga] + [motore(m, model, ctx, ram) for m in altri]
    nomi = ["inga"] + altri
    risposte = {m: [] for m in nomi}
    misure, info, interrotti = {}, {}, {}

    def domande(ms):
        for i, el in enumerate(elementi):
            msgs = messaggi(el)
            mt = max_tokens(el) if callable(max_tokens) else max_tokens
            for m in ms:
                testo, sec = _chiedi(m, msgs, mt, think)
                v, nota = voto(el, testo)
                risposte[m.nome].append({"voto": v, "nota": nota, "secondi": round(sec, 1),
                                         "testo": testo})
            righe = ", ".join(f"{_etichetta(m.nome)} {risposte[m.nome][i]['voto']:.2f} "
                              f"({risposte[m.nome][i]['nota']})" for m in ms)
            if len(ms) > 1:
                righe += ", " + ", ".join(
                    ("stesso testo" if risposte["inga"][i]["testo"].strip() == risposte[m.nome][i]["testo"].strip()
                     else "testi diversi") + ("" if len(ms) == 2 else f" ({_etichetta(m.nome)})")
                    for m in ms[1:])
            print(f"{nome} {i:3d}: {righe}", flush=True)
            for m in ms:
                r = risposte[m.nome][i]
                if r["voto"] < 1:
                    # l'inizio delle risposte sbagliate, per capire se è il modello o la lettura
                    print(f"    {_etichetta(m.nome)}: {r['testo'][:160]!r}", flush=True)

    def misura_su(m):
        if misura:
            print(f"{nome}: misura su {_etichetta(m.nome)}", flush=True)
            misure[m.nome] = misura(m.nome, m.url, m.extra(think))

    try:
        if in_sequenza:
            for m in tutti:
                try:
                    with m:
                        misura_su(m)
                        domande([m])
                        info[m.nome] = m.info()
                except RuntimeError as e:
                    if not risposte[m.nome]:
                        return fine({"stato": "errore", "motivo": f"{_etichetta(m.nome)}: {e}",
                                     "dettagli": {"misure": misure, "motori": info}})
                    interrotti[m.nome] = str(e)
                    print(f"{_etichetta(m.nome)} interrotto dopo {len(risposte[m.nome])} domande: {e}")
        else:
            with contextlib.ExitStack() as stack:
                for m in tutti:
                    try:
                        stack.enter_context(m)
                    except RuntimeError as e:
                        return fine({"stato": "errore", "motivo": f"{_etichetta(m.nome)}: {e}"})
                for m in tutti:
                    misura_su(m)
                try:
                    domande(tutti)
                except RuntimeError as e:
                    if not risposte["inga"]:
                        raise
                    print(f"interrotto dopo {len(risposte['inga'])} domande: {e}")
                for m in tutti:
                    info[m.nome] = m.info()
    except RuntimeError as e:
        return fine({"stato": "errore", "motivo": f"{'/'.join(altri)}: {e}"})

    n = min(len(v) for v in risposte.values())
    if n == 0:
        return fine({"stato": "errore", "motivo": "nessuna risposta", "dettagli": {"misure": misure}})
    righe = []
    for i in range(n):
        riga = {"n": i}
        for m in nomi:
            riga[m] = risposte[m][i]
        uguali = {m: risposte["inga"][i]["testo"].strip() == risposte[m][i]["testo"].strip()
                  for m in altri}
        riga["uguali"] = uguali[altri[0]] if len(altri) == 1 else uguali
        righe.append(riga)
    a = sum(r["voto"] for r in risposte["inga"][:n]) / n
    sec_a = sum(r["secondi"] for r in risposte["inga"][:n])
    voci = {"Inga": a}
    det = dict(dettagli or {}, domande=n)
    for m in altri:
        e = _etichetta(m)
        b = sum(r["voto"] for r in risposte[m][:n]) / n
        voci[e] = b
        voci[f"Inga meno {e}"] = a - b
    for m in altri:
        e = _etichetta(m)
        stesso = sum(risposte["inga"][i]["testo"].strip() == risposte[m][i]["testo"].strip()
                     for i in range(n)) / n
        voci["risposte con lo stesso testo" if len(altri) == 1 else
             f"risposte con lo stesso testo di {e}"] = stesso
    for m in altri:
        sec_b = sum(r["secondi"] for r in risposte[m][:n])
        voci[f"tempo di {_etichetta(m)} su quello di Inga"] = sec_b / sec_a if sec_a else 0.0
    for m, motore_ in zip(nomi, tutti):
        if m == "llama.cpp":
            det["llama_cpp"] = motore_.versione
        elif m == "colibri":
            det["colibri"] = motore_.versione
    det["secondi_inga"] = round(sec_a)
    for m in altri:
        det["secondi_llama" if m == "llama.cpp" else f"secondi_{m}"] = \
            round(sum(r["secondi"] for r in risposte[m][:n]))
    if misure:
        det["misure"] = misure
    if any(info.values()):
        det["motori"] = info
    if interrotti:
        det["interrotti"] = interrotti
    if any(perche.values()):
        det["motori_saltati"] = {m: p for m, p in perche.items() if p}
    det["risposte"] = righe
    return fine({"stato": "ok", "voto": a, "voci": voci, "dettagli": det})


def _etichetta(m):
    return {"inga": "Inga", "colibri": "Colibri"}.get(m, m)
