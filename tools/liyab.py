"""Liyab beside Inga, for the cases that compare the two on the same GGUF file.

Liyab (https://github.com/andrei-borcea/liyab, Apache-2.0) is a C++20 engine for GGUF
files made for phones and Macs, which streams the weights of a model larger than the RAM.
Its local API lives in its Flutter app; on a server it runs through `liyab-cli`, which
takes a raw text (no chat template) and, with `--json`, prints one line after loading and
one line per generation with its own times (prompt tokens, time to the first token,
decode time, tokens per second, peak resident memory) and the reply. The workflows build
it at the commit of liyab.txt for the runner's CPU (.github/actions/liyab) and put the
folder of `liyab-cli` in IUC_LIYAB; without it, `cartella()` is None and the comparing
cases are skipped.

To give both engines the same text, the cases render the chat themselves with the model's
ChatML layout (Qwen3, the model of the cases) and pass it raw to `liyab-cli`, while Inga
gets the same messages through its chat API (its template renders the same ChatML).
"""

import json
import os
import subprocess
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cartella():
    d = os.environ.get("IUC_LIYAB")
    return d if d and os.path.isfile(os.path.join(d, "liyab-cli")) else None


def versione():
    with open(os.path.join(ROOT, "liyab.txt"), encoding="utf-8") as f:
        return f.read().strip()


def picco_inga():
    """The peak resident memory (VmHWM) of the `inga serve` the runner started
    (IUC_INGA_PID), and its children, in MiB; None without it."""
    pid = os.environ.get("IUC_INGA_PID")
    if not pid:
        return None
    import colibri
    return round(colibri.picco_rss(int(pid)) / 2**20, 1)


def chatml(messages):
    """Qwen3's ChatML for `messages`, ending with the assistant's turn opened (no
    thinking block: the instruct models of the cases do not think)."""
    out = []
    for m in messages:
        out.append(f"<|im_start|>{m['role']}\n{m['content']}<|im_end|>\n")
    out.append("<|im_start|>assistant\n")
    return "".join(out)


def genera(model, testo, n, ctx=4096, extra=(), timeout=3600):
    """One `liyab-cli --json` run on `testo`, greedy: the load line, the turn line (its
    stats) and the reply without the end-of-turn token, and the wall-clock seconds."""
    cmd = [os.path.join(cartella(), "liyab-cli"), "-m", model, "-p", testo, "-n", str(n),
           "--temp", "0", "--ctx", str(ctx), "--threads", str(os.cpu_count() or 4),
           "--json", *extra]
    t0 = time.monotonic()
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    sec = time.monotonic() - t0
    righe = [json.loads(r) for r in p.stdout.splitlines() if r.startswith("{")]
    carico = next((r for r in righe if "load_ms" in r), None)
    turno = next((r for r in righe if "turn" in r), None)
    if p.returncode != 0 or turno is None:
        raise RuntimeError(f"liyab-cli è uscito con {p.returncode}: {(p.stderr or p.stdout)[-800:]}")
    risposta = turno.get("text", "")
    for fine in ("<|im_end|>", "<|endoftext|>"):
        risposta = risposta.split(fine)[0]
    return {"carico": carico, "turno": turno, "risposta": risposta.strip(), "secondi": sec,
            "stderr": p.stderr[-2000:]}
