"""The checks of IFEval's instructions, written again here (no nltk, no langdetect).

Each check takes the answer and the instruction's kwargs and says whether the
instruction is followed, as IFEval's "strict" checks do. Words are counted with a
regular expression instead of nltk's tokenizer, so a count can differ by a few from
the official one: the same check scores both engines, which is what the case compares.
The instructions that need nltk's sentence splitter or a language detector
(length_constraints:number_sentences, language:response_language) are not here: the
case leaves out the prompts that use them.
"""

import json
import re


def _confronta(n, relazione, soglia):
    return n < soglia if relazione == "less than" else n >= soglia


def _parole(t):
    return re.findall(r"\b\w+\b", t)


def no_comma(r, k):
    return "," not in r


def number_words(r, k):
    return _confronta(len(_parole(r)), k["relation"], k["num_words"])


def forbidden_words(r, k):
    return not any(re.search(r"\b" + re.escape(w) + r"\b", r, re.I) for w in k["forbidden_words"])


def highlighted(r, k):
    n = sum(1 for h in re.findall(r"\*[^\n\*]*\*", r) if h.strip("*").strip())
    n += sum(1 for h in re.findall(r"\*\*[^\n\*]*\*\*", r) if h.removeprefix("**").removesuffix("**").strip())
    return n >= k["num_highlights"]


def frequency(r, k):
    n = len(re.findall(re.escape(k["keyword"]), r, re.I))
    return _confronta(n, k["relation"], k["frequency"])


def repeat_prompt(r, k):
    return r.strip().lower().startswith(k["prompt_to_repeat"].strip().lower())


def quotation(r, k):
    t = r.strip()
    return len(t) > 1 and t[0] == '"' and t[-1] == '"'


def lowercase(r, k):
    return r == r.lower()


def existence(r, k):
    return all(re.search(w, r, re.I) for w in k["keywords"])


def title(r, k):
    return any(t.strip("<>").strip() for t in re.findall(r"<<[^\n]+>>", r))


def letter_frequency(r, k):
    n = r.lower().count(k["letter"].lower())
    return _confronta(n, k["let_relation"], k["let_frequency"])


def bullets(r, k):
    n = len(re.findall(r"^\s*\*[^\*].*$", r, re.M)) + len(re.findall(r"^\s*-.*$", r, re.M))
    return n == k["num_bullets"]


def placeholders(r, k):
    return len(re.findall(r"\[.*?\]", r)) >= k["num_placeholders"]


def paragraphs(r, k):
    parti = re.split(r"\s?\*\*\*\s?", r)
    n = len(parti)
    for i, p in enumerate(parti):
        if not p.strip():
            if i == 0 or i == len(parti) - 1:
                n -= 1
            else:
                return False
    return n == k["num_paragraphs"]


def end_checker(r, k):
    return r.strip().strip('"').lower().endswith(k["end_phrase"].strip().lower())


def postscript(r, k):
    m = k["postscript_marker"].lower()
    if m == "p.p.s":
        pat = r"\s*p\.\s?p\.\s?s.*$"
    elif m == "p.s.":
        pat = r"\s*p\.\s?s\..*$"
    else:
        pat = r"\s*" + re.escape(m) + r".*$"
    return bool(re.findall(pat, r.lower(), re.M))


def capital(r, k):
    return r == r.upper()


def capital_words(r, k):
    n = sum(1 for w in _parole(r) if w.isupper())
    return _confronta(n, k["capital_relation"], k["capital_frequency"])


def two_responses(r, k):
    parti = [p.strip() for p in r.split("******")]
    piene = [p for i, p in enumerate(parti) if p or (0 < i < len(parti) - 1)]
    return len(piene) == 2 and all(piene) and piene[0] != piene[1]


def json_format(r, k):
    t = r.strip()
    t = re.sub(r"^```(?:json|Json|JSON)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t).strip()
    try:
        json.loads(t)
        return True
    except ValueError:
        return False


def sections(r, k):
    parti = re.split(r"\s?" + re.escape(k["section_spliter"]) + r"\s?\d+\s?", r)
    return len(parti) - 1 >= k["num_sections"]


def nth_first_word(r, k):
    parti = [p for p in re.split(r"\n\n", r)]
    n = sum(1 for p in parti if p.strip())
    if n != k["num_paragraphs"]:
        return False
    piene = [p for p in parti if p.strip()]
    i = k["nth_paragraph"] - 1
    if i >= len(piene):
        return False
    w = re.sub(r"^[^\w]+", "", piene[i].strip()).split()
    first = re.sub(r"[^\w]", "", w[0]).lower() if w else ""
    return first == k["first_word"].lower()


def constrained(r, k):
    return any(o in r for o in ("My answer is yes.", "My answer is no.", "My answer is maybe."))


VERIFICHE = {
    "punctuation:no_comma": no_comma,
    "length_constraints:number_words": number_words,
    "keywords:forbidden_words": forbidden_words,
    "detectable_format:number_highlighted_sections": highlighted,
    "keywords:frequency": frequency,
    "combination:repeat_prompt": repeat_prompt,
    "startend:quotation": quotation,
    "change_case:english_lowercase": lowercase,
    "keywords:existence": existence,
    "detectable_format:title": title,
    "keywords:letter_frequency": letter_frequency,
    "detectable_format:number_bullet_lists": bullets,
    "detectable_content:number_placeholders": placeholders,
    "length_constraints:number_paragraphs": paragraphs,
    "startend:end_checker": end_checker,
    "detectable_content:postscript": postscript,
    "change_case:english_capital": capital,
    "change_case:capital_word_frequency": capital_words,
    "combination:two_responses": two_responses,
    "detectable_format:json_format": json_format,
    "detectable_format:multiple_sections": sections,
    "length_constraints:nth_paragraph_first_word": nth_first_word,
    "detectable_format:constrained_response": constrained,
}
