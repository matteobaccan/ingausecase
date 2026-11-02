"""Confronta i servizi di ricerca web che Inga usa o potrebbe usare.

Per ogni domanda (domande.json, risposte note) chiede a ogni servizio i risultati e misura:
- il tempo della chiamata;
- i caratteri di testo che finirebbero nel prompt (circa 4 caratteri per token);
- se la risposta giusta compare in quel testo (qualità del recupero, non della risposta).

Modalità per i servizi che danno solo snippet (DuckDuckGo, Brave):
- `snippet`: solo titoli e snippet;
- `pagine`: snippet + le prime 3 pagine scaricate, i primi 1500 caratteri di testo (come Inga oggi);
- `pagine-bm25`: come `pagine`, ma da ogni pagina il pezzo di 1500 caratteri più vicino alla domanda.

Le chiavi (facoltative) arrivano dall'ambiente: TAVILY_API_KEY, BRAVE_API_KEY, EXA_API_KEY,
FIRECRAWL_API_KEY. Senza chiave il servizio si salta, tranne Firecrawl che prova la modalità
senza chiave (Keyless). Le chiavi non si stampano mai.

Uso: python ricerca/servizi.py [--out risultati.json] [--md riepilogo.md]
"""

import argparse, html, json, math, os, re, sys, time, urllib.parse
import requests

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
T = 30
PAGE_CHARS = 1500
PAGES = 3
RESULTS = 5
S = requests.Session()
S.headers["User-Agent"] = UA


def text_of(page_html):
    page_html = re.sub(r"(?is)<(script|style|noscript|svg|nav|footer|header)[^>]*>.*?</\1>", " ", page_html)
    t = re.sub(r"(?s)<[^>]+>", " ", page_html)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def words(s):
    return re.findall(r"\w+", s.lower())


def bm25_window(text, query, size=PAGE_CHARS):
    """Il pezzo di `size` caratteri con il punteggio BM25 più alto rispetto alla domanda."""
    if len(text) <= size:
        return text
    q = set(w for w in words(query) if len(w) > 2)
    step = size // 3
    wins = [text[i:i + size] for i in range(0, max(1, len(text) - size + step), step)]
    toks = [words(w) for w in wins]
    n = len(wins)
    avg = sum(len(t) for t in toks) / n or 1
    df = {w: sum(1 for t in toks if w in t) for w in q}
    best, best_s = wins[0], -1.0
    for w, t in zip(wins, toks):
        s = 0.0
        for term in q:
            f = t.count(term)
            if f:
                idf = math.log(1 + (n - df[term] + 0.5) / (df[term] + 0.5))
                s += idf * f * 2.2 / (f + 1.2 * (0.25 + 0.75 * len(t) / avg))
        if s > best_s:
            best, best_s = w, s
    return best


def fetch_pages(urls, query):
    first, bm = [], []
    for u in urls[:PAGES]:
        try:
            r = S.get(u, timeout=15)
            if r.ok and "html" in r.headers.get("content-type", ""):
                t = text_of(r.text)
                first.append(t[:PAGE_CHARS])
                bm.append(bm25_window(t, query))
        except requests.RequestException:
            pass
    return first, bm


# Ogni servizio restituisce (snippet: list[str], urls: list[str], extra: dict modalità -> testo)

def ddg(q):
    r = S.post("https://html.duckduckgo.com/html/", data={"q": q}, timeout=T)
    r.raise_for_status()
    urls, snips = [], []
    for m in re.finditer(r'(?s)class="result__a" href="([^"]+)".*?>(.*?)</a>.*?class="result__snippet"[^>]*>(.*?)</a>', r.text):
        href = html.unescape(m.group(1))
        qs = urllib.parse.parse_qs(urllib.parse.urlparse(href).query)
        url = qs.get("uddg", [href])[0]
        if "duckduckgo.com/y.js" in url:
            continue  # pubblicità
        urls.append(url)
        snips.append(text_of(m.group(2)) + " — " + text_of(m.group(3)))
        if len(urls) >= RESULTS:
            break
    if not urls:
        raise RuntimeError(f"nessun risultato (HTTP {r.status_code}, {len(r.text)} byte: blocco o captcha?)")
    return snips, urls, {}


def wikipedia(q, lang):
    r = S.get(f"https://{lang}.wikipedia.org/w/api.php", params={
        "action": "query", "list": "search", "srsearch": q, "srlimit": 3, "format": "json"}, timeout=T)
    r.raise_for_status()
    hits = r.json()["query"]["search"]
    snips = [h["title"] + " — " + text_of(h["snippet"]) for h in hits]
    titles = [h["title"] for h in hits]
    extra = {}
    if titles:
        e = S.get(f"https://{lang}.wikipedia.org/w/api.php", params={
            "action": "query", "prop": "extracts", "explaintext": 1, "exintro": 1,
            "titles": "|".join(titles[:2]), "format": "json"}, timeout=T).json()
        intro = " ".join(p.get("extract", "")[:PAGE_CHARS] for p in e["query"]["pages"].values())
        extra["intro"] = intro
    return snips, [], extra


def brave(q):
    r = S.get("https://api.search.brave.com/res/v1/web/search", params={"q": q, "count": RESULTS},
              headers={"X-Subscription-Token": os.environ["BRAVE_API_KEY"], "Accept": "application/json"}, timeout=T)
    r.raise_for_status()
    res = r.json().get("web", {}).get("results", [])
    return [x["title"] + " — " + text_of(x.get("description", "")) for x in res], [x["url"] for x in res], {}


def tavily(q):
    r = S.post("https://api.tavily.com/search", json={"query": q, "max_results": RESULTS},
               headers={"Authorization": "Bearer " + os.environ["TAVILY_API_KEY"]}, timeout=T)
    r.raise_for_status()
    res = r.json().get("results", [])
    return [x["title"] + " — " + x.get("content", "") for x in res], [x["url"] for x in res], {}


def exa(q):
    r = S.post("https://api.exa.ai/search", json={"query": q, "numResults": RESULTS,
               "contents": {"highlights": {"numSentences": 3}}},
               headers={"x-api-key": os.environ["EXA_API_KEY"]}, timeout=T)
    r.raise_for_status()
    res = r.json().get("results", [])
    return [(x.get("title") or "") + " — " + " ".join(x.get("highlights") or []) for x in res], [x["url"] for x in res], {}


def firecrawl(q, scrape):
    body = {"query": q, "limit": RESULTS}
    if scrape:
        body = {"query": q, "limit": PAGES, "scrapeOptions": {"formats": ["markdown"], "onlyMainContent": True}}
    h = {"Content-Type": "application/json"}
    if os.environ.get("FIRECRAWL_API_KEY"):
        h["Authorization"] = "Bearer " + os.environ["FIRECRAWL_API_KEY"]
    r = S.post("https://api.firecrawl.dev/v2/search", json=body, headers=h, timeout=90)
    if not r.ok:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:300]}")
    data = r.json().get("data", {})
    res = data.get("web", data) if isinstance(data, dict) else data
    snips = [(x.get("title") or "") + " — " + (x.get("description") or "") for x in res]
    urls = [x.get("url", "") for x in res]
    extra = {}
    if scrape:
        md = [x.get("markdown") or "" for x in res]
        extra["pagine"] = " ".join(m[:PAGE_CHARS] for m in md)
        extra["pagine-bm25"] = " ".join(bm25_window(re.sub(r"\s+", " ", m), q) for m in md)
    return snips, urls, extra


def norm(s):
    s = s.lower()
    s = re.sub(r"(?<=\d)[.,   ](?=\d{3}\b)", "", s)  # 299.792.458 -> 299792458
    return s


def found(text, answers):
    t = norm(text)
    return any(re.search(r"(?<!\w)" + re.escape(norm(a)) + r"(?!\w)", t) for a in answers)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="ricerca-risultati.json")
    ap.add_argument("--md", default="ricerca-riepilogo.md")
    args = ap.parse_args()
    qs = json.load(open(os.path.join(os.path.dirname(__file__), "domande.json"), encoding="utf-8"))

    services = [("duckduckgo", lambda q, l: ddg(q), True),
                ("wikipedia", lambda q, l: wikipedia(q, l), False)]
    if os.environ.get("BRAVE_API_KEY"): services.append(("brave", lambda q, l: brave(q), True))
    if os.environ.get("TAVILY_API_KEY"): services.append(("tavily", lambda q, l: tavily(q), False))
    if os.environ.get("EXA_API_KEY"): services.append(("exa", lambda q, l: exa(q), False))
    services.append(("firecrawl", lambda q, l: firecrawl(q, False), False))
    services.append(("firecrawl-scrape", lambda q, l: firecrawl(q, True), False))

    rows = []  # {servizio, modalita, domanda, ok, chars, secondi, errore}
    for qi, item in enumerate(qs):
        q, ans, lang = item["domanda"], item["risposte"], item.get("lingua", "en")
        for name, fn, pages in services:
            t0 = time.monotonic()
            try:
                snips, urls, extra = fn(q, lang)
                dt = time.monotonic() - t0
                st = " ".join(snips)
                if name != "firecrawl-scrape":
                    rows.append(dict(servizio=name, modalita="snippet", domanda=qi, ok=found(st, ans), chars=len(st), secondi=dt))
                for mode, txt in extra.items():
                    rows.append(dict(servizio=name, modalita=mode, domanda=qi, ok=found(st + " " + txt, ans), chars=len(st) + len(txt), secondi=dt))
                if pages and urls:
                    t1 = time.monotonic()
                    first, bm = fetch_pages(urls, q)
                    dp = dt + time.monotonic() - t1
                    for mode, parts in (("pagine", first), ("pagine-bm25", bm)):
                        txt = st + " " + " ".join(parts)
                        rows.append(dict(servizio=name, modalita=mode, domanda=qi, ok=found(txt, ans), chars=len(txt), secondi=dp))
            except Exception as e:  # noqa: BLE001 - si registra e si va avanti
                msg = str(e).replace(os.environ.get("TAVILY_API_KEY", "\0"), "***")
                rows.append(dict(servizio=name, modalita="errore", domanda=qi, ok=False, chars=0,
                                 secondi=time.monotonic() - t0, errore=msg[:300]))
                print(f"[{name}] domanda {qi}: {msg[:200]}", file=sys.stderr)
            time.sleep(1.0)
        print(f"domanda {qi + 1}/{len(qs)} fatta", file=sys.stderr)

    json.dump(rows, open(args.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    groups = {}
    for r in rows:
        groups.setdefault((r["servizio"], r["modalita"]), []).append(r)
    out = [f"# Servizi di ricerca: {len(qs)} domande con risposta nota\n",
           "Trovata = la risposta giusta compare nel testo che andrebbe nel prompt (più alto è meglio).",
           "Token ≈ caratteri / 4 (più basso è meglio). Secondi = mediana per domanda (più basso è meglio).\n",
           "| Servizio | Modalità | Trovata ↑ | Token medi ↓ | Secondi (mediana) ↓ | Errori |",
           "|---|---|---|---|---|---|"]
    errs = {}
    for (s, m), g in groups.items():
        if m == "errore":
            errs[s] = g
    for (s, m), g in sorted(groups.items()):
        if m == "errore":
            continue
        secs = sorted(r["secondi"] for r in g)
        out.append(f"| {s} | {m} | {sum(r['ok'] for r in g)}/{len(qs)} | {round(sum(r['chars'] for r in g) / len(g) / 4)} "
                   f"| {secs[len(secs) // 2]:.2f} | {len(errs.get(s, []))} |")
    for s in errs:
        if not any(k[0] == s and k[1] != "errore" for k in groups):
            out.append(f"| {s} | — | 0/{len(qs)} | — | — | {len(errs[s])} |")
    if errs:
        out.append("\n## Primi errori\n")
        for s, g in errs.items():
            out.append(f"- **{s}**: {g[0].get('errore', '')}")
    open(args.md, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
