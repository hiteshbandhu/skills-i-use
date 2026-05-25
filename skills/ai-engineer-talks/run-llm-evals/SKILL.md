---
name: run-llm-evals
description: >
  Runs checklists and workflows for designing, operating, and improving LLM evals —
  domain harnesses, agent/voice evals, LLM judges, metrics workshops, product flywheels,
  dynamic search eval, enterprise conversation intelligence. Use when the user says
  "evals", "LLM judge", "eval harness", "regression on prompts", "agent eval",
  "eval dataset", or needs to ship with measurement before prod.
---

# Run LLM evals

Action playbook from twenty-five AI Engineer eval/benchmark talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–N (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/run-llm-evals/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Start or justify an eval program                    → A
├─ Build domain-specific eval from scratch             → B
├─ Design product/LLM app eval (not unit tests)        → C
├─ Define metrics/rubrics that match humans            → D
├─ Braintrust-style playground → CI → online eval      → E
├─ Ship agentic apps with trace-native eval            → F
├─ Voice / phone agent simulation eval                 → G
├─ Close observability ↔ eval gap (Azure agents)       → H
├─ Calibrate LLM judges / adversarial fuzzing          → I
├─ Benchmark models (perf + knowledge + honesty)       → J
├─ Enterprise CX: 100% conversations + labeling        → K
├─ Zapier-style PM+eng eval ops & post-ship feedback   → L
├─ Evaluate web/RAG search APIs (dynamic sets)         → M
└─ Subjective media eval or long-lived architecture    → N
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

Copy this folder into your agent’s skills directory:

```bash
cp -r skills/run-llm-evals ~/.claude/skills/
cp -r skills/run-llm-evals ~/.cursor/skills/
cp -r skills/run-llm-evals ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/evals-benchmarks-ai-engineer/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Evals ≠ unit tests; cover distributions and offense, not one-shot demos | [src-005 @ 2:57] |
| Look at data before fancy judges | [src-006 @ 7:15], [src-009 @ 8:25] |
| Align offline scorers with online logging | [src-001 @ 3:23] |
| Layer evals on routers, tools, and final answers | [src-007 @ 4:46] |
| Calibrate LLM judges; meta-eval the judge | [src-013 @ 8:15] |
| Separate core-traffic vs aspirational datasets | [src-020 @ 15:03] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–N; save artifacts to `./skill-outputs/run-llm-evals/` when requested; do not auto-commit.
