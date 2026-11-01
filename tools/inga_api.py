"""Small client for the OpenAI-compatible API of `inga serve`, shared by the cases.

Only the standard library. Every request is deterministic: temperature 0 and a
fixed seed (the SEED environment variable, 42 by default).

A case's run.py imports it with:

    import os, sys
    sys.path.insert(0, os.environ["IUC_TOOLS"])
    import inga_api
"""

import json
import os
import time
import urllib.error
import urllib.request

SEED = int(os.environ.get("SEED", "42"))


def base_url():
    return os.environ["INGA_URL"].rstrip("/")


def case_dir():
    return os.environ["IUC_CASE_DIR"]


def work_dir():
    """A scratch folder for this case (generated files, downloads); not committed."""
    d = os.environ["IUC_WORK_DIR"]
    os.makedirs(d, exist_ok=True)
    return d


def write_result(result):
    """Write the case's score JSON where the runner expects it.

    result: {"stato": "ok" | "saltato", "voto": 0..1, "voci": {name: 0..1},
             "motivo": "...", "dettagli": {...}}
    """
    with open(os.environ["IUC_RESULT"], "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


def _post(path, body, timeout, url=None):
    req = urllib.request.Request(
        (url or base_url()).rstrip("/") + path,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        return urllib.request.urlopen(req, timeout=timeout)
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:2000]
        raise RuntimeError(f"POST {path}: HTTP {e.code}: {detail}") from None


def chat(messages, schema=None, max_tokens=1024, timeout=1800, think=False, extra=None, url=None):
    """One chat completion. Returns (content, response_json, seconds).

    schema: a JSON schema dict; the answer is then constrained by
    response_format json_schema and the parsed object is in content.
    url: another OpenAI-compatible server (llama-server) instead of INGA_URL.
    """
    body = {
        "model": os.environ.get("INGA_MODEL", ""),
        "messages": messages,
        "temperature": 0,
        "seed": SEED,
        "max_tokens": max_tokens,
        "stream": False,
        "chat_template_kwargs": {"enable_thinking": bool(think)},
    }
    if schema is not None:
        body["response_format"] = {
            "type": "json_schema",
            "json_schema": {"name": "risposta", "schema": schema, "strict": True},
        }
    if extra:
        body.update(extra)
    t0 = time.monotonic()
    with _post("/v1/chat/completions", body, timeout, url) as r:
        data = json.loads(r.read().decode("utf-8"))
    seconds = time.monotonic() - t0
    content = data["choices"][0]["message"].get("content") or ""
    if schema is not None:
        content = json.loads(content)
    return content, data, seconds


def chat_stream(messages, max_tokens=256, timeout=600, think=False):
    """A streamed chat completion. Returns (text, ttft_seconds, total_seconds)."""
    r = stream(messages, max_tokens=max_tokens, timeout=timeout, think=think)
    return r["testo"], r["ttft"], r["secondi"]


def stream(messages, max_tokens=256, timeout=600, think=False, url=None, extra=None):
    """A streamed chat completion, with the usage the server reports at the end
    (stream_options.include_usage). url and extra as in chat (another server, more
    fields of the body). Returns {"testo", "ttft" (seconds to the first piece of
    text), "secondi" (to the end), "usage" (or None), "pezzi" (pieces received)}."""
    body = {
        "model": os.environ.get("INGA_MODEL", ""),
        "messages": messages,
        "temperature": 0,
        "seed": SEED,
        "max_tokens": max_tokens,
        "stream": True,
        "stream_options": {"include_usage": True},
        "chat_template_kwargs": {"enable_thinking": bool(think)},
    }
    if extra:
        body.update(extra)
    t0 = time.monotonic()
    ttft = None
    parts = []
    usage = None
    with _post("/v1/chat/completions", body, timeout, url) as r:
        for raw in r:
            line = raw.decode("utf-8", "replace").strip()
            if not line.startswith("data:"):
                continue
            payload = line[5:].strip()
            if payload == "[DONE]":
                break
            try:
                chunk = json.loads(payload)
            except ValueError:
                continue
            if chunk.get("usage"):
                usage = chunk["usage"]
            for ch in chunk.get("choices") or []:
                delta = ch.get("delta") or {}
                # il primo token generato può essere anche ragionamento
                piece = delta.get("content") or delta.get("reasoning_content")
                if piece:
                    if ttft is None:
                        ttft = time.monotonic() - t0
                    if delta.get("content"):
                        parts.append(delta["content"])
    return {"testo": "".join(parts), "ttft": ttft, "secondi": time.monotonic() - t0,
            "usage": usage, "pezzi": len(parts)}


def add_document(collection, name, text=None, pdf_path=None, timeout=3600):
    """Add a file to one of Inga's collections of documents (POST /api/inga/documents):
    Inga reads it (a PDF with its own reader), cuts it into chunks and embeds them with
    the server's embedding model. Returns Inga's answer (chunks, pages, ...).

    Needs a case with "modello_embedding" in case.json (the runner then serves the
    embedding model beside the chat model and chooses it)."""
    body = {"collection": collection, "name": name}
    if pdf_path is not None:
        import base64
        with open(pdf_path, "rb") as f:
            body["data"] = "data:application/pdf;base64," + base64.b64encode(f.read()).decode("ascii")
    else:
        body["text"] = text
    with _post("/api/inga/documents", body, timeout) as r:
        return json.loads(r.read().decode("utf-8"))


class NonDisponibile(Exception):
    """The server has no such route (an older version of Inga): the case is skipped."""


def _call(method, path, body=None, timeout=600):
    data = None if body is None else json.dumps(body).encode("utf-8")
    req = urllib.request.Request(base_url() + path, data=data, method=method,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8") or "null")
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")[:2000]
        if e.code == 404:
            raise NonDisponibile(f"{method} {path}: HTTP 404 (questa versione di Inga non lo ha)") from None
        raise RuntimeError(f"{method} {path}: HTTP {e.code}: {detail}") from None


def get(path, timeout=600):
    return _call("GET", path, timeout=timeout)


def post(path, body, timeout=600):
    return _call("POST", path, body, timeout=timeout)


def put(path, body, timeout=600):
    return _call("PUT", path, body, timeout=timeout)


def search_documents(collection, query, k=10):
    """The passages Inga finds for `query` in a collection (GET /api/inga/documents/search,
    the same search the chat uses with inga_documents), best first."""
    from urllib.parse import urlencode
    q = urlencode({"q": query, "collection": collection, "k": k})
    return get("/api/inga/documents/search?" + q).get("passages") or []
