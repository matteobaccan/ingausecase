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
import re
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


def con_time(cmd, timeout=3600):
    """cmd under /usr/bin/time -v: stdout, stderr and the peak resident memory in MiB (the
    same measure for every engine)."""
    p = subprocess.run(["/usr/bin/time", "-v", *cmd], capture_output=True, text=True, timeout=timeout)
    m = re.search(r"Maximum resident set size \(kbytes\):\s*(\d+)", p.stderr)
    if p.returncode != 0:
        raise RuntimeError(f"{os.path.basename(cmd[0])} è uscito con {p.returncode}: {p.stderr[-1200:]}")
    return p.stdout, p.stderr, (round(int(m.group(1)) / 1024, 1) if m else None)


def misura(model, testo, n, ctx=4096, extra=(), timeout=3600):
    """One `liyab-cli --json` run under /usr/bin/time: prompt and decode speed from its
    own stats (prompt tokens over the time to the first token, the tokens after the first
    over the decode time), the reply and the peak resident memory."""
    cmd = [os.path.join(cartella(), "liyab-cli"), "-m", model, "-p", testo, "-n", str(n),
           "--temp", "0", "--ctx", str(ctx), "--threads", str(os.cpu_count() or 4), "--json", *extra]
    so, _, picco = con_time(cmd, timeout)
    t = next(json.loads(x) for x in so.splitlines() if x.startswith("{") and '"turn"' in x)
    pt, ct = t["prompt_tokens"], t["generated_tokens"]
    risposta = t.get("text", "")
    for fine in ("<|im_end|>", "<|endoftext|>"):
        risposta = risposta.split(fine)[0]
    return {"token_prompt": pt, "token_generati": ct, "picco_mib": picco,
            "bozze": [t.get("draft_tokens_proposed"), t.get("draft_tokens_accepted")],
            "pp": pt / (t["ttft_ms"] / 1000) if t["ttft_ms"] else None,
            "tg": (ct - 1) / (t["decode_ms"] / 1000) if ct > 1 and t["decode_ms"] else None,
            "risposta": risposta.strip(), "turno": t}
