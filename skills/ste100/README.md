# STE100

Write explanations, documents and diagrams in ASD-STE100 Simplified Technical English, the
controlled language aerospace uses for maintenance manuals. Shapes each document to its
type and the reader's intent, and draws diagrams to engineering conventions.

## Why

LLM output is getting longer and our job is shifting to reading it. STE is a 53-rule spec
built so a tired, non-native reader can follow a procedure with no misunderstanding: one
idea per sentence, 20 words per step, active voice, one word for one meaning. Models know
it well, and text written to it is much easier to read. "80% of the way to STE" is the
sweet spot for everyday explanations.

## How it works

1. **Intent first.** Find the reader, the action they must take, the document type, and
   the trajectory (the section order that gets them to the action). The answer comes first.
2. **Write to the rules** at a chosen level: strict (procedures, safety text), standard
   (default, "80% STE"), or light (chat).
3. **Draw only when a picture carries more than the text.** Structure from engineering
   diagram standards, look from Hairline or Blueprint minimalism.
4. **Check.** `scripts/ste_check.py` lints sentence length, passive voice, tenses,
   phrasal verbs, contractions, semicolons, Latin abbreviations and unapproved words.

## What is in here

| File | Contents |
|---|---|
| [SKILL.md](SKILL.md) | Levels, the 15 core rules, word swaps, workflow, output shapes |
| [references/rules.md](references/rules.md) | All 53 rules + 8 general recommendations of Issue 9, paraphrased with software examples |
| [references/documents.md](references/documents.md) | Intent → type → trajectory for memos, PRDs, design docs, ADRs, postmortems, runbooks, guides, papers, briefs, release notes; PDF rules |
| [references/diagrams.md](references/diagrams.md) | IDEF0, ISO 5807, GRAFCET, IEC 61082/60617, IEC 81346, S1000D callouts, ISA-5.1, C4/BPMN, IEC 60073 colours |
| [references/styles.md](references/styles.md) | Hairline (monochrome or one accent) and Blueprint minimalism (ISO 128 line types, dimensions, title block) |
| [scripts/ste_check.py](scripts/ste_check.py) | Heuristic STE checker |
| [scripts/build_dictionary.py](scripts/build_dictionary.py) | Builds the local word lists from the official spec PDF |

### Scripts

Read them before you run them.

- `build_dictionary.py` downloads the ASD-STE100 Issue 9 PDF from asd-ste100.org to your
  temp folder and writes `dictionary/approved.txt` and `dictionary/unapproved.txt` next to
  the skill. Needs `pdftotext` (`brew install poppler`).
- `ste_check.py` reads a text file (or stdin) and prints findings. Read-only. Word checks
  need the dictionary; without it the other checks still run.

The STE specification and its dictionary are copyrighted by ASD. The spec is free to
download, but this repo does not include it or the generated word lists
(`dictionary/` is gitignored). Build them locally and do not redistribute them.

## Install

```bash
npx skills add hiteshbandhu/skills-i-use --skill ste100
python3 ~/.claude/skills/ste100/scripts/build_dictionary.py   # once, for word checks
```

Or copy the folder into `~/.claude/skills/` or `~/.cursor/skills/`.

## Usage

```
Explain how our job queue retries work, in STE.
Write a runbook for rotating the API keys — strict STE.
Turn these notes into a PRD, 80% STE, with a blueprint-style architecture diagram.
```

```bash
python3 ~/.claude/skills/ste100/scripts/ste_check.py draft.md --mode procedure --level strict
```

Pairs with [`pdf-report`](../pdf-report/) and [`research-report`](../research-report/) when
the output is a PDF.

## Credits

- [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org), Issue 9 (2025), by ASD.
- Hairline style rules adapted from [Hairline](https://hairline.lucasmarkes.com) by Lucas
  Marques (MIT). For interactive Hairline figures use his own skill:
  `npx skills add lucasmarkes/hairline`.
