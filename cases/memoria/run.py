"""Caso memoria: domande sulle chat passate (LongMemEval) con la memoria dei progetti.

Dati: LongMemEval (Wu et al., ICLR 2025, licenza MIT), la versione "oracle" (per ogni
domanda solo le sessioni di chat che servono), scaricata a ogni esecuzione (dati.json).
Un sottoinsieme fisso (seed): PER_TIPO domande per ognuno dei tipi in TIPI e una
domanda "senza risposta" (abstention: la risposta giusta è non saperlo) per tre tipi,
con sessioni fino a MAX_CARATTERI caratteri in tutto.

Per ogni domanda, il percorso della web UI: un progetto nuovo
(POST /api/inga/projects), ogni sessione scritta nella memoria dal modello come alla
fine di una chat (POST /api/inga/memory/{p}/write, con la data della sessione come
orario), poi la domanda in una chat nuova del progetto. Tre modi:
- oggi: il system prompt della chat di un progetto (GET /api/inga/memory/{p}/context:
  istruzioni, regole e stile; il diario non c'è);
- diario: lo stesso più i file del diario (come sarebbe con il diario nel contesto);
- tutta la chat: le sessioni intere nel prompt, senza memoria (il riferimento).
Il voto di ogni risposta lo dà lo stesso modello, con le istruzioni di giudizio di
LongMemEval (sì/no), sul testo della risposta; le domande senza risposta sono giuste
solo con known: false.
Prima di ogni domanda lo stile della persona (my-style, comune a tutti i progetti) viene
svuotato, perché una domanda non veda i fatti di un'altra.
"""

import json
import os
import random
import re
import sys
from urllib.parse import quote

sys.path.insert(0, os.environ["IUC_TOOLS"])
import dati  # noqa: E402
import inga_api  # noqa: E402

TIPI = ["single-session-user", "multi-session", "temporal-reasoning", "knowledge-update"]
PER_TIPO = 3
MAX_CARATTERI = 25000
SEED = 3
MODI = ["oggi", "diario", "tutta la chat"]

SISTEMA = (
    "The current date is {date}. You are talking with a person you have talked with "
    "before. Answer their question about themselves or about your earlier conversations "
    "using only what is written below. If it is not written there, set known to false and "
    "say you do not know; do not guess."
)
SCHEMA = {
    "type": "object",
    "properties": {"answer": {"type": "string", "maxLength": 400}, "known": {"type": "boolean"}},
    "required": ["answer", "known"],
}
GIUDICE = (
    "I will give you a question, a correct answer, and a response from a model. Say yes "
    "if the response contains the correct answer or is equivalent to it, or contains all "
    "the steps that lead to it. Say no if it gives only part of the information the "
    "answer needs, or a different answer.{extra}\n\nQuestion: {q}\n\nCorrect answer: {a}"
    "\n\nModel response: {r}\n\nIs the model response correct?"
)
EXTRA = {
    "temporal-reasoning": " Do not penalize off-by-one errors in a number of days, weeks or months.",
    "knowledge-update": " If the response gives older information along with the updated answer, "
                        "it is correct as long as the updated answer is the correct one.",
}


def norm(s):
    return re.sub(r"[\s.,'’\-()]", "", str(s).casefold())


def scegli(righe):
    rng = random.Random(SEED)
    corte = [r for r in righe
             if sum(len(t["content"]) for s in r["haystack_sessions"] for t in s) <= MAX_CARATTERI]
    out = []
    for tipo in TIPI:
        c = [r for r in corte if r["question_type"] == tipo and not r["question_id"].endswith("_abs")]
        rng.shuffle(c)
        out += c[:PER_TIPO]
    # le domande senza risposta: una per tipo, finché ce ne sono
    for tipo in ["single-session-user", "multi-session", "knowledge-update"][:PER_TIPO]:
        c = [r for r in corte if r["question_type"] == tipo and r["question_id"].endswith("_abs")]
        rng.shuffle(c)
        out += c[:1]
    return out


def trascrizione(q):
    parti = []
    for data, sessione in sorted(zip(q["haystack_dates"], q["haystack_sessions"]), key=lambda x: x[0]):
        righe = [f"{'Person' if t['role'] == 'user' else 'Assistant'}: {t['content']}" for t in sessione]
        parti.append(f"### Conversation of {data}\n" + "\n".join(righe))
    return "Earlier conversations, in full:\n\n" + "\n\n".join(parti)


def diario(pid):
    files = inga_api.get(f"/api/inga/memory/{quote(pid)}/files").get("files") or []
    testi = []
    for f in files:
        path = f.get("path", "")
        if path.startswith("diary/") and path.endswith(".md"):
            testi.append(inga_api.get(f"/api/inga/memory/{quote(pid)}/files?path={quote(path)}")["text"])
    return "\n\n".join(testi)


def rispondi(q, memoria):
    sistema = SISTEMA.format(date=q["question_date"])
    if memoria.strip():
        sistema += "\n\n" + memoria
    else:
        sistema += "\n\n(Nothing is written about earlier conversations.)"
    msgs = [{"role": "system", "content": sistema}, {"role": "user", "content": q["question"]}]
    try:
        dato, _, sec = inga_api.chat(msgs, schema=SCHEMA, max_tokens=250)
        return dato, sec
    except (ValueError, RuntimeError) as e:
        print(f"  risposta non valida: {e}")
        return {}, 0.0


def giudica(q, dato):
    if q["question_id"].endswith("_abs"):
        return dato.get("known") is False
    if not str(dato.get("answer", "")).strip():
        return False
    prompt = GIUDICE.format(extra=EXTRA.get(q["question_type"], ""), q=q["question"],
                            a=q["answer"], r=dato.get("answer", ""))
    schema = {"type": "object", "properties": {"correct": {"type": "boolean"}}, "required": ["correct"]}
    try:
        v, _, _ = inga_api.chat([{"role": "user", "content": prompt}], schema=schema, max_tokens=20)
        return bool(v.get("correct"))
    except (ValueError, RuntimeError):
        return False


def main():
    try:
        inga_api.get("/api/inga/projects")
    except inga_api.NonDisponibile as e:
        inga_api.write_result({"stato": "saltato", "motivo": f"questa versione non ha i progetti: {e}"})
        return
    try:
        with open(dati.file("longmemeval-oracle"), encoding="utf-8") as f:
            righe = json.load(f)
    except dati.Cambiato as e:
        inga_api.write_result({"stato": "errore", "motivo": str(e)})
        return
    except OSError as e:
        inga_api.write_result({"stato": "saltato", "motivo": f"LongMemEval non si scarica: {e}"})
        return
    domande = scegli(righe)
    modello = os.environ.get("INGA_MODEL", "")
    giuste = {m: 0 for m in MODI}
    esatte = {m: 0 for m in MODI}
    per_tipo = {}
    sessioni = scritte = regole = 0
    out = []
    for q in domande:
        tipo = "abstention" if q["question_id"].endswith("_abs") else q["question_type"]
        inga_api.put("/api/inga/memory/my-style/files", {"path": "style.md", "text": ""})
        pid = inga_api.post("/api/inga/projects", {"name": f"lme {q['question_id']}"})["id"]
        scrittura = []
        for data, sid, sessione in sorted(zip(q["haystack_dates"], q["haystack_session_ids"],
                                              q["haystack_sessions"]), key=lambda x: x[:2]):
            msgs = [{"role": t["role"], "content": t["content"]} for t in sessione]
            r = inga_api.post(f"/api/inga/memory/{quote(pid)}/write",
                              {"model": modello, "chat": {"id": sid, "title": "", "span": data,
                                                          "messages": msgs}}, timeout=1800)
            sessioni += 1
            scritte += not r.get("nothing")
            regole += sum(len(w.get("rules") or []) for w in r.get("wrote") or [])
            scrittura.append({"data": data, "scritto": not r.get("nothing"), "perché": r.get("why"),
                              "writer": r.get("writer")})
        contesto = inga_api.get(f"/api/inga/memory/{quote(pid)}/context").get("text") or ""
        testo_diario = diario(pid)
        memorie = {
            "oggi": contesto,
            "diario": (contesto + "\n\n" if contesto else "")
                      + ("Inga's diary of the earlier conversations:\n\n" + testo_diario if testo_diario else ""),
            "tutta la chat": trascrizione(q),
        }
        riga = {"id": q["question_id"], "tipo": tipo, "domanda": q["question"], "attesa": q["answer"],
                "scrittura": scrittura, "contesto": contesto, "diario": testo_diario}
        for m in MODI:
            dato, sec = rispondi(q, memorie[m])
            ok = giudica(q, dato)
            ex = (dato.get("known") is False) if tipo == "abstention" else \
                norm(q["answer"]) in norm(dato.get("answer", ""))
            giuste[m] += ok
            esatte[m] += ex
            per_tipo.setdefault((m, tipo), []).append(ok)
            riga[m] = {"risposta": dato.get("answer"), "known": dato.get("known"), "giusta": ok,
                       "esatta": ex, "secondi": round(sec, 1)}
        print(f"{q['question_id']} ({tipo}): " + ", ".join(
            f"{m} {'ok' if riga[m]['giusta'] else 'NO'}" for m in MODI)
            + f"; scritte {sum(s['scritto'] for s in scrittura)}/{len(scrittura)} sessioni", flush=True)
        out.append(riga)
    n = len(domande)
    voci = {f"giuste, {m}": giuste[m] / n for m in MODI}
    voci.update({f"testo atteso contenuto, {m}": esatte[m] / n for m in MODI})
    for (m, tipo), v in sorted(per_tipo.items()):
        if m != "tutta la chat":
            voci[f"{tipo}, {m}"] = sum(v) / len(v)
    voci["sessioni scritte nel diario"] = scritte / sessioni if sessioni else 0.0
    inga_api.write_result({
        "stato": "ok",
        "voto": giuste["oggi"] / n,
        "voci": voci,
        "dettagli": {"domande": n, "seed": SEED, "sessioni": sessioni, "regole_scritte": regole,
                     "giudice": f"lo stesso modello ({modello})", "risposte": out},
    })


if __name__ == "__main__":
    main()
