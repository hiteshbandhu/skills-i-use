---
name: run-aiewf-2024-evals
description: >
  Runs checklists for AIEWF 2024 eval and LLM ops talks — domain eval ladders, LLM judges, enterprise deploy, Zapier+Braintrust loops, GenAI maturity before fine-tune. Use when the user says "evals", "LLM judge", "fine-tune decision", "enterprise GenAI deploy", or AIEWF eval playlist.
---

# Run AIEWF 2024 evals & LLM ops

Action playbook from six AI Engineer / World's Fair talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–F (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/run-aiewf-2024-evals/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Build domain eval from zero (assertions → judges)     → A
├─ Layer task evals on routers/tools (trace-native)        → B
├─ Calibrate LLM judges / courtroom rubrics              → C
├─ PM+eng eval ops (Zapier/Braintrust regression)          → D
├─ Enterprise CX: full conversation intelligence           → E
└─ Decide fine-tune vs prompt/distill (maturity curve)     → F
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/run-aiewf-2024-evals ~/.claude/skills/
cp -r skills/run-aiewf-2024-evals ~/.cursor/skills/
cp -r skills/run-aiewf-2024-evals ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/evals-llm-ops-aie-world-s-fair-2024/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Evals ≠ demos; log before judges | [src-001 @ 6:39] |
| Assertions before LLM-as-judge | [src-001 @ 4:41] |
| Layer scores on router/tools/answer | [src-004 @ 4:46] |
| Fine-tune only after eval + teacher data | [src-006 @ 5:55] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–F; save artifacts to `./skill-outputs/run-aiewf-2024-evals/` when requested; do not auto-commit.

---

## Invocation examples

```
@run-aiewf-2024-evals build domain eval harness for our agent
should we fine-tune or stay on GPT-4o?
```
