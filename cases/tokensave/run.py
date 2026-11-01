"""Caso tokensave: Inga come host MCP, con gli strumenti di tokensave su un codice vero.

tokensave (https://github.com/aovestdipaperino/tokensave, MIT) è un server MCP che
indicizza un progetto con tree-sitter (simboli, chiamate, eredità) e risponde con
strumenti come tokensave_search, tokensave_callers, tokensave_context. Il programma è
quello della release fissata in dati.json (tokensave-linux, sha256 controllato); il
progetto è itsdangerous al commit di domande.json, indicizzato con `tokensave init`.

Il runner scrive mcp.json di questo caso nella home di Inga ({lavoro} = la cartella di
lavoro) e avvia `inga serve` con il suo host MCP (--allow-mcp-commands e
--mcp-auto-approve dei soli strumenti in lettura, case.json). Qui il comando del server
si approva (POST /api/inga/mcp/servers) e ci si collega; poi ogni domanda di
domande.json, a temperatura 0, in tre modi:

- con tokensave: la richiesta chiede gli strumenti del server ("inga_mcp":
  ["tokensave"]), Inga li offre al modello, esegue le chiamate approvate e ridà i
  risultati, fino alla risposta; le chiamate sono in inga_mcp_calls;
- senza strumenti: la stessa domanda, il modello risponde con quello che sa;
- codice nel prompt: i sorgenti del pacchetto (src/itsdangerous) nel prompt di sistema,
  l'alternativa ingenua agli strumenti.

Per ogni modo: le risposte giuste (domande.json: una delle stringhe di `una`, o tutte
quelle di `tutte`) e i token dell'usage di ogni risposta. Con gli strumenti
prompt_tokens è il prompt dell'ultimo giro (definizioni degli strumenti, domanda,
chiamate e risultati), completion_tokens la somma dei token generati in tutti i giri.
Voto: le risposte giuste con tokensave.
"""

import json
import os
import re
import subprocess
import sys
import tarfile

sys.path.insert(0, os.environ["IUC_TOOLS"])
import dati  # noqa: E402
import inga_api  # noqa: E402

SERVER = "tokensave"
MAX_TOKENS = 1024
SISTEMA = ("You answer questions about the source code of the Python library itsdangerous "
           "2.2.0 (the package src/itsdangerous). Answer briefly, naming the exact files, "
           "classes, functions or values asked.")
CON = " Look the answer up in the code with the tokensave tools before answering."
SENZA = " Answer from what you know about this library."
CODICE = " Its source code follows.\n\n"


def esegui(cmd, env=None, cwd=None, timeout=600):
    print("$ " + " ".join(cmd), flush=True)
    p = subprocess.run(cmd, capture_output=True, text=True, env=env, cwd=cwd, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError(f"{os.path.basename(cmd[0])} {cmd[1] if len(cmd) > 1 else ''} è uscito "
                           f"con {p.returncode}: {(p.stderr or p.stdout)[-1500:]}")
    return p.stdout


def prepara(progetto):
    """Il programma di tokensave e il progetto indicizzato, nella cartella di lavoro
    (dove li aspetta mcp.json)."""
    work = inga_api.work_dir()
    cartella = os.path.join(work, "tokensave")
    exe = os.path.join(cartella, "tokensave")
    os.makedirs(cartella, exist_ok=True)
    with tarfile.open(dati.file("tokensave-linux")) as t:
        m = next(x for x in t.getmembers() if os.path.basename(x.name) == "tokensave" and x.isfile())
        with t.extractfile(m) as src, open(exe, "wb") as out:
            out.write(src.read())
    os.chmod(exe, 0o755)
    sorgente = os.path.join(work, "progetto")
    if not os.path.isdir(sorgente):
        esegui(["git", "clone", "-q", "--depth", "1", "--branch", progetto["tag"], progetto["repo"], sorgente])
    head = esegui(["git", "-C", sorgente, "rev-parse", "HEAD"]).strip()
    if head != progetto["commit"]:
        raise dati.Cambiato(f"{progetto['repo']} {progetto['tag']} è al commit {head}, "
                            f"domande.json dice {progetto['commit']}: le risposte vanno ricontrollate")
    # la home di tokensave nella cartella di lavoro: niente contatore mondiale, niente
    # controllo della versione, niente indicizzazione da sola
    home = os.path.join(work, "tokensave-home")
    os.makedirs(home, exist_ok=True)
    env = dict(os.environ, HOME=home, TOKENSAVE_UPDATE_CHECK="0", TOKENSAVE_AUTO_INIT="0")
    esegui([exe, "disable-upload-counter"], env=env)
    esegui([exe, "init", sorgente, "--cpu-usage", "balanced", "--no-git-hook"], env=env)
    try:
        stato = json.loads(esegui([exe, "status", sorgente, "--json"], env=env))
    except ValueError:
        stato = {}
    versione = esegui([exe, "--version"], env=env).strip()
    return sorgente, versione, stato


def collega():
    """Approva il comando del server (le chiamate le approva --mcp-auto-approve) e si
    collega. Restituisce il server come lo vede Inga, o solleva RuntimeError con il
    motivo che Inga dà."""
    inga_api.post("/api/inga/mcp/servers", {"server": SERVER, "approve": True})
    try:
        s = inga_api.post("/api/inga/mcp/connect", {"server": SERVER}, timeout=300)
    except RuntimeError as e:
        s = inga_api.get("/api/inga/mcp")
        srv = next((x for x in s.get("servers") or [] if x.get("name") == SERVER), {})
        raise RuntimeError(f"{e}; stato: {srv.get('state')}, {srv.get('reason')}, {srv.get('notes')}") from None
    srv = next((x for x in s.get("servers") or [] if x.get("name") == SERVER), None)
    if not srv or srv.get("state") != "connected" or not srv.get("tools"):
        raise RuntimeError(f"il server MCP {SERVER} non è collegato: {srv}")
    return srv


def codice(sorgente, cartella):
    parti = []
    base = os.path.join(sorgente, cartella)
    for nome in sorted(os.listdir(base)):
        if nome.endswith(".py"):
            with open(os.path.join(base, nome), encoding="utf-8") as f:
                parti.append(f"### {cartella}/{nome}\n```python\n{f.read()}```\n")
    return "\n".join(parti)


def _cerca(s, testo):
    p = re.escape(s.lower())
    if re.match(r"\w", s):
        p = r"(?<![\w-])" + p
    if re.search(r"\w$", s):
        p += r"(?![\w-])"
    return re.search(p, testo.lower()) is not None


def giusta(d, testo):
    testo = testo.replace("`", "").replace("*", "")
    if "tutte" in d:
        return all(_cerca(s, testo) for s in d["tutte"])
    return any(_cerca(s, testo) for s in d["una"])


def chiedi(d, sistema, extra=None):
    msgs = [{"role": "system", "content": sistema}, {"role": "user", "content": d["domanda"]}]
    try:
        testo, data, sec = inga_api.chat(msgs, max_tokens=MAX_TOKENS, extra=extra, timeout=3600)
    except (RuntimeError, OSError, ValueError) as e:
        return {"giusta": False, "testo": f"[errore: {e}]", "secondi": 0.0, "token_prompt": 0,
                "token_generati": 0, "chiamate": []}
    msg = data["choices"][0]["message"]
    u = data.get("usage") or {}
    chiamate = [{"strumento": c.get("tool"), "argomenti": c.get("arguments"), "stato": c.get("stage"),
                 "motivo": c.get("reason")} for c in msg.get("inga_mcp_calls") or []]
    return {"giusta": giusta(d, testo), "testo": testo, "secondi": round(sec, 1),
            "token_prompt": u.get("prompt_tokens", 0), "token_generati": u.get("completion_tokens", 0),
            "token_in_cache": (u.get("prompt_tokens_details") or {}).get("cached_tokens"),
            "chiamate": chiamate}


def main():
    with open(os.path.join(inga_api.case_dir(), "domande.json"), encoding="utf-8") as f:
        cfg = json.load(f)
    progetto, domande = cfg["progetto"], cfg["domande"]
    try:
        sorgente, versione, stato = prepara(progetto)
        srv = collega()
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    except (RuntimeError, OSError, subprocess.TimeoutExpired, inga_api.NonDisponibile) as e:
        inga_api.write_result({"stato": "errore", "motivo": f"tokensave tramite l'host MCP di Inga: {e}"})
        return
    strumenti = [t.get("name") for t in srv.get("tools") or []]
    print(f"{versione}: collegato in {(srv.get('server') or {}).get('connect_secs')} s, "
          f"{len(strumenti)} strumenti offerti: {', '.join(strumenti)}", flush=True)

    modi = {
        "con tokensave": (SISTEMA + CON, {"inga_mcp": [SERVER]}),
        "senza strumenti": (SISTEMA + SENZA, None),
        "codice nel prompt": (SISTEMA + CODICE + codice(sorgente, progetto["sorgenti"]), None),
    }
    # un modo alla volta: il prompt di sistema resta lo stesso per tutte le domande e
    # Inga lo riprende dalla cache dei prefissi (il codice nel prompt è lungo)
    risposte = {m: [] for m in modi}
    for m, (sistema, extra) in modi.items():
        for i, d in enumerate(domande):
            r = chiedi(d, sistema, extra)
            risposte[m].append(r)
            fatte = [c for c in r["chiamate"] if c["stato"] == "done"]
            print(f"{m} {i:2d} {d['id']}: {'giusta' if r['giusta'] else 'sbagliata'}, "
                  f"{r['token_prompt']}+{r['token_generati']} token, {r['secondi']} s"
                  + (f", chiamate {len(fatte)} ({', '.join(c['strumento'] or '?' for c in fatte)})"
                     if extra else ""), flush=True)
            if not r["giusta"]:
                print(f"    {r['testo'][:160]!r}", flush=True)
            for c in r["chiamate"]:
                if c["stato"] != "done":
                    print(f"    chiamata {c['strumento']} {c['stato']}: {c['motivo']}", flush=True)

    n = len(domande)

    def media(m, k):
        return sum(r[k] for r in risposte[m]) / n

    giuste = {m: sum(r["giusta"] for r in risposte[m]) / n for m in modi}
    chiamate = [sum(c["stato"] == "done" for c in r["chiamate"]) for r in risposte["con tokensave"]]
    rifiutate = sum(sum(c["stato"] != "done" for c in r["chiamate"]) for r in risposte["con tokensave"])
    per_domanda = {m: {"token_prompt": round(media(m, "token_prompt")),
                       "token_generati": round(media(m, "token_generati")),
                       "secondi": round(media(m, "secondi"), 1)} for m in modi}
    per_domanda["con tokensave"]["chiamate"] = round(sum(chiamate) / n, 2)
    per_domanda["con tokensave"]["chiamate_rifiutate"] = round(rifiutate / n, 2)

    def rapporto(a, b, k):
        return per_domanda[a][k] / per_domanda[b][k] if per_domanda[b][k] else 0.0

    voci = {
        "giuste con tokensave": giuste["con tokensave"],
        "giuste senza strumenti": giuste["senza strumenti"],
        "giuste con il codice nel prompt": giuste["codice nel prompt"],
        "domande con almeno una chiamata a tokensave": sum(c > 0 for c in chiamate) / n,
        "token del prompt per domanda, con tokensave su codice nel prompt":
            rapporto("con tokensave", "codice nel prompt", "token_prompt"),
        "token generati per domanda, con tokensave su senza strumenti":
            rapporto("con tokensave", "senza strumenti", "token_generati"),
    }
    nota = None
    if not any(chiamate):
        nota = ("il modello non ha chiamato nessuno strumento di tokensave (troppo piccolo, o non "
                "chiama strumenti nel formato che Inga legge): con tokensave ha risposto senza "
                "guardare il codice")
        print("NOTA: " + nota, flush=True)
    for m in modi:
        print(f"{m}: giuste {giuste[m]:.2f}, per domanda {per_domanda[m]}", flush=True)
    inga_api.write_result({
        "stato": "ok",
        "voto": giuste["con tokensave"],
        "voci": voci,
        "dettagli": {"tokensave": versione, "progetto": progetto, "indice": stato,
                     "strumenti_offerti": strumenti, "per_domanda": per_domanda, "nota": nota,
                     "domande": n, "risposte": [
                         dict(id=d["id"], **{m: risposte[m][i] for m in modi})
                         for i, d in enumerate(domande)]},
    })


if __name__ == "__main__":
    main()
