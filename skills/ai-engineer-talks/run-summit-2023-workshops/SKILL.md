---
name: run-summit-2023-workshops
description: >
  Runs AI Engineer Summit 2023 workshop playbooks — foundations (101), inference
  (201), product patterns beyond inference (Rest of the Owl), and Anthropic prompt
  engineering principles. Use when onboarding to AI engineering, designing inference
  stacks, or improving task prompts; or when the user says "summit 2023 workshop",
  "AI engineering 101", "inference workshop", "prompt principles Karina".
---

# Run Summit 2023 workshops

Action playbook from four AI Engineer Summit 2023 workshops. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–D (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional deliverables: `{SKILL_OUTPUT_DIR}/run-summit-2023-workshops/` — see [skills-i-use OUTPUT.md](https://github.com/hiteshbandhu/skills-i-use/blob/main/skills/OUTPUT.md).

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Baseline AI engineering literacy (models, APIs, apps)     → A  [src-003]
├─ Inference serving, latency, cost, deployment              → B  [src-004]
├─ Product architecture beyond the model (LUI, eval, ops)  → C  [src-001]
└─ Task prompt design (Claude / API best practices)          → D  [src-002]
```

**Stop summarizing** once a workflow is identified — run its checklist in [workflows.md](workflows.md).

---

## Install

```bash
cp -r skills/run-summit-2023-workshops ~/.claude/skills/
cp -r skills/run-summit-2023-workshops ~/.cursor/skills/
cp -r skills/run-summit-2023-workshops ~/.codex/skills/
```

Source corpus: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) `playlists/ai-engineer-summit-2023-workshops/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| AI engineering = systems around models, not prompting alone | [src-003 @ 7:17] |
| Inference is necessary but not sufficient for product value | [src-001 @ 0:25] |
| Prompts steer attention; use task keywords, context, examples | [src-002 @ 0:01:33] |
| Structure: context first, clear task, coherent logical flow | [src-002 @ 6:43] |
| Prefer inference-time compute over retraining when possible | [src-002 @ 1:53] |

---

## Output to user

1. Name the workflow (A–D) and deliverable
2. Save artifacts under `./skill-outputs/run-summit-2023-workshops/` when requested
3. Do not auto-commit

---

## Invocation examples

```
@run-summit-2023-workshops walk me through AI engineering 101 topics
design our inference layer using the 201 workshop
improve task prompts using Anthropic principles
```
