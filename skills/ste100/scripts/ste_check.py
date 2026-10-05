#!/usr/bin/env python3
"""Check a text against the ASD-STE100 rules that a script can check.

This is a heuristic linter, not a full STE checker. It cannot know your
technical nouns and verbs (rules 1.5 and 1.12), so treat word flags as
questions, not errors.

Usage:
    python3 ste_check.py FILE [--mode procedure|descriptive] [--level strict|standard|light]
    echo "text" | python3 ste_check.py -

Exit code: 0 when no errors, 1 when there are errors.
"""
import argparse
import re
import sys
from pathlib import Path

DICT = Path(__file__).resolve().parent.parent / "dictionary"

LIMITS = {  # max words per sentence (rules 5.1 and 6.3), relaxed by level
    "strict": {"procedure": 20, "descriptive": 25},
    "standard": {"procedure": 20, "descriptive": 25},
    "light": {"procedure": 25, "descriptive": 30},
}
PARA_MAX = {"strict": 6, "standard": 6, "light": 8}  # rule 6.6

CONTRACTION = re.compile(r"\b\w+(n't|'re|'ll|'ve|'d|'m)\b|\b(it's|that's|there's|what's)\b", re.I)
LATIN = re.compile(r"\b(e\.g\.|i\.e\.|etc\.|viz\.|cf\.|vs\.|via|per se|ad hoc)", re.I)
PERFECT = re.compile(r"\b(has|have|had)\s+(been\s+)?\w+(ed|en)\b", re.I)
PASSIVE = re.compile(
    r"\b(is|are|was|were|be|been|being)\s+(\w+ly\s+)?(\w+ed|built|done|made|set|sent|shown|"
    r"given|taken|written|run|known|found|held|kept|left|put|seen|told|used)\b", re.I)
MODAL_PASSIVE = re.compile(r"\b(must|should|can|will|may|might|could|would)\s+be\s+\w+(ed|en)\b", re.I)
PHRASAL = re.compile(
    r"\b(set|carry|find|figure|turn|look|give|put|bring|come|get|take|make|point|"
    r"fill|break|back|shut|pick|hold|run|go|check|sort|work|end|wind)s?(ed|ing)?\s+"
    r"(up|out|off|on|over|in|down|back|through|away|about)\b", re.I)
GENDERED = re.compile(r"\b(he|she|him|her|his|hers|himself|herself)\b", re.I)
WHEN_ING = re.compile(r"\b(when|while|after|before|by|for)\s+\w+ing\b", re.I)
DROPPED_THAT = re.compile(r"\b(make sure|makes sure|shows|recommends|tells you)\s+(?!that\b)(the|a|an|you|it|all)\b", re.I)


def load_words():
    approved, alternatives = set(), {}
    a, u = DICT / "approved.txt", DICT / "unapproved.txt"
    if a.exists():
        for line in a.read_text().splitlines():
            head, _, forms = line.partition(" — ")
            approved.add(head.split(" (")[0].lower())
            for f in forms.split(","):
                if f.strip():
                    approved.add(f.strip().lower())
    if u.exists():
        for line in u.read_text().splitlines():
            head, _, alts = line.partition(" → ")
            w = head.split(" (")[0].lower()
            if w not in approved:
                alternatives.setdefault(w, []).append(alts)
    return approved, alternatives


def sentences(par: str):
    par = re.sub(r"\([^)]*\)", "(X)", par)  # rule 8.5: text in parentheses = one word
    return [s.strip() for s in re.split(r"(?<=[.!?:])\s+(?=[A-Z0-9\"(])", par) if s.strip()]


def word_count(s: str) -> int:
    # rule 8.6/8.7: numbers with units, identifiers and hyphenated words count as one
    s = re.sub(r"\b\d+(\.\d+)?\s?(mm|cm|m|km|kg|g|ms|s|min|h|V|A|W|Hz|kHz|MHz|GHz|MB|GB|KB|%|°C|°F)\b", "N", s)
    s = re.sub(r"\"[^\"]*\"|“[^”]*”|`[^`]*`", "Q", s)
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9\-_./']*", s))


def check(text: str, mode: str, level: str):
    approved, alternatives = load_words()
    issues = []

    def add(sev, rule, where, msg):
        issues.append((sev, rule, where, msg))

    paragraphs = [p for p in re.split(r"\n\s*\n", text) if p.strip()]
    for pi, par in enumerate(paragraphs, 1):
        if par.lstrip().startswith(("```", "    ")):
            continue  # code blocks
        sents = sentences(" ".join(par.split()))
        if mode == "descriptive" and len(sents) > PARA_MAX[level] and not re.match(r"^\s*([-*]|\d+\.)", par):
            add("warn", "6.6", f"para {pi}", f"{len(sents)} sentences (max {PARA_MAX[level]})")
        for si, s in enumerate(sents, 1):
            where = f"para {pi}, sent {si}"
            n = word_count(s)
            lim = LIMITS[level][mode]
            if n > lim:
                add("error", "5.1" if mode == "procedure" else "6.3", where, f"{n} words (max {lim}): {s[:70]}…")
            if ";" in s:
                add("error", "8.1", where, "semicolon — split into two sentences")
            for m in CONTRACTION.finditer(s):
                add("error", "4.2", where, f"contraction '{m.group(0)}'")
            for m in LATIN.finditer(s):
                add("warn", "GR-6", where, f"Latin abbreviation '{m.group(0)}' — use English words")
            for m in PERFECT.finditer(s):
                add("error", "3.4", where, f"perfect tense '{m.group(0)}' — use simple past or present")
            for m in MODAL_PASSIVE.finditer(s):
                add("error", "3.4/3.6", where, f"'{m.group(0)}' — name the agent or use a command")
            for m in PASSIVE.finditer(s):
                if not MODAL_PASSIVE.search(m.group(0)):
                    sev = "error" if mode == "procedure" else "warn"
                    add(sev, "3.6", where, f"possible passive '{m.group(0)}' — use active voice")
            for m in PHRASAL.finditer(s):
                add("warn", "9.3", where, f"possible phrasal verb '{m.group(0)}'")
            for m in GENDERED.finditer(s):
                add("error", "GR-7", where, f"gendered pronoun '{m.group(0)}'")
            for m in WHEN_ING.finditer(s):
                add("warn", "3.5", where, f"'-ing' clause '{m.group(0)}' — write 'when you …'")
            for m in DROPPED_THAT.finditer(s):
                add("warn", "GR-1", where, f"add 'that' after '{m.group(1)}'")
            if mode == "procedure":
                if re.search(r"\b(and then|then)\b", s, re.I) and s.count(",") >= 1:
                    add("warn", "5.2", where, "possibly two instructions in one sentence")
            if alternatives:
                for w in re.findall(r"\b[a-z][a-z'-]+\b", s):
                    if w in alternatives and w not in approved:
                        add("info", "1.1", where, f"'{w}' is not approved → {" | ".join(alternatives[w])} (OK if it is your technical noun/verb)")
    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--mode", choices=["procedure", "descriptive"], default="descriptive")
    ap.add_argument("--level", choices=["strict", "standard", "light"], default="standard")
    args = ap.parse_args()
    text = sys.stdin.read() if args.file == "-" else Path(args.file).read_text()
    issues = check(text, args.mode, args.level)
    if args.level == "light":
        issues = [i for i in issues if i[0] != "info"]
    if not (DICT / "unapproved.txt").exists():
        print("note: no dictionary found — run scripts/build_dictionary.py for word checks\n")
    for sev, rule, where, msg in issues:
        print(f"[{sev:5}] rule {rule:7} {where:18} {msg}")
    errors = sum(1 for i in issues if i[0] == "error")
    print(f"\n{errors} errors, {sum(1 for i in issues if i[0] == 'warn')} warnings, "
          f"{sum(1 for i in issues if i[0] == 'info')} word flags")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
