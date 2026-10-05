#!/usr/bin/env python3
"""Build the local STE word lists from the official ASD-STE100 PDF.

The specification is free to download from asd-ste100.org, but it is
copyrighted by ASD. This script builds the word lists on your own machine
instead of shipping them with the skill. Do not redistribute the output.

Usage:
    python3 build_dictionary.py                 # download Issue 9 and build
    python3 build_dictionary.py path/to/spec.pdf

Output (next to this script, in ../dictionary/):
    approved.txt    APPROVED WORD (part of speech) — approved verb forms
    unapproved.txt  word (part of speech) → APPROVED ALTERNATIVE (pos), ...

Requires pdftotext (poppler): brew install poppler
"""
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

SPEC_URL = "https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf"
OUT = Path(__file__).resolve().parent.parent / "dictionary"

HEADWORD = re.compile(r"^([A-Za-z](?:[A-Za-z'\-]| (?! ))*?) \(([a-z, ]+|TN|-)\)")
ALT = re.compile(r"^([A-Z][A-Z' \-]*? \((?:[a-z, ]+|TN|TV)\))")
ALT_BARE = re.compile(r"^([A-Z][A-Z'\-]*(?: [A-Z'\-]+)*)$")  # only on the headword line
BARE = re.compile(r"^([A-Za-z](?:[A-Za-z'\-]| (?! ))*[A-Za-z])(\s{2,}.*)?$")
POS_LINE = re.compile(r"^\(([a-z, ]+)\)(\s.*)?$")
SKIP = ("Issue 9", "Page 2-")


def pdf_to_text(pdf: Path) -> list[str]:
    txt = subprocess.run(
        ["pdftotext", "-layout", str(pdf), "-"], check=True, capture_output=True, text=True
    ).stdout
    return txt.split("\n")


def dictionary_lines(lines: list[str]) -> list[str]:
    # The dictionary proper starts at the first "A (art)" entry after the
    # explanatory pages of Part 2 (those also contain sample entries).
    starts = [i for i, l in enumerate(lines) if l.startswith("A (art)")]
    return lines[starts[-1]:] if starts else lines


def normalize(lines: list[str]) -> list[str]:
    """Join headwords whose part of speech wraps to the next line, and mark
    headwords that have no part of speech (for example "such as")."""
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        b = BARE.match(line) if line and not HEADWORD.match(line) else None
        if b and not line.startswith(SKIP) and not line.startswith(("Word ", "(part")):
            nxt = POS_LINE.match(lines[i + 1]) if i + 1 < len(lines) else None
            if nxt:
                out.append(f"{b.group(1)} ({nxt.group(1)}){b.group(2) or ''}")
                out.append(" " * 4 + (nxt.group(2) or "").strip())
                i += 2
                continue
            if b.group(1)[0].islower() and b.group(2):
                line = f"{b.group(1)} (-){b.group(2)}"
        out.append(line)
        i += 1
    return out


def parse(lines: list[str]):
    approved, unapproved = {}, {}
    cur, kind = None, None
    for line in lines:
        if line.startswith(SKIP) or "Simplified Technical English" in line:
            continue
        if line.strip().startswith(("Word ", "(part of")):
            continue
        m = HEADWORD.match(line)
        rest, on_head = line, bool(m)
        if m:
            word, pos = m.group(1), m.group(2)
            rest = line[m.end():]
            if word == word.upper():
                kind, cur = "A", word
                approved.setdefault(word, {"pos": set(), "forms": []})["pos"].add(pos)
            else:
                kind, cur = "U", f"{word} ({pos})"
                unapproved.setdefault(cur, [])
        elif kind == "A" and line and line[0] != " ":
            f = re.match(r"^([A-Z]{2,}),?(\s{2,}|\s*$)", line)
            if f:
                approved[cur]["forms"].append(f.group(1))
        if kind == "U":
            parts = re.split(r"\s{2,}", rest.strip())
            if parts:
                a = ALT.match(parts[0].strip()) or (on_head and ALT_BARE.match(parts[0].strip()))
                if a:
                    unapproved[cur].append(a.group(1))
    return approved, unapproved


def main() -> None:
    if len(sys.argv) > 1:
        pdf = Path(sys.argv[1])
    else:
        pdf = Path(tempfile.gettempdir()) / "ASD-STE100_ISSUE9.pdf"
        if not pdf.exists():
            print(f"Downloading {SPEC_URL}")
            urllib.request.urlretrieve(SPEC_URL, pdf)
    approved, unapproved = parse(normalize(dictionary_lines(pdf_to_text(pdf))))
    OUT.mkdir(exist_ok=True)
    with open(OUT / "approved.txt", "w") as f:
        for w in sorted(approved, key=str.lower):
            d = approved[w]
            forms = [x for x in dict.fromkeys(d["forms"]) if x != w]
            tail = f" — {', '.join(forms)}" if forms else ""
            f.write(f"{w} ({', '.join(sorted(d['pos']))}){tail}\n")
    n_alt = 0
    with open(OUT / "unapproved.txt", "w") as f:
        for w in sorted(unapproved, key=str.lower):
            alts = list(dict.fromkeys(unapproved[w]))
            if alts:
                n_alt += 1
                f.write(f"{w} → {', '.join(alts)}\n")
    print(f"{len(approved)} approved headwords, {n_alt} unapproved words with alternatives → {OUT}")


if __name__ == "__main__":
    main()
