---
name: optimize-llm-inference
description: >
  Runs workflows for GPU/inference talks — Groq LPU latency, OSS inference stacks, MoE networking, serverless fine-tune, frontier cluster design, Devin agent infra, Gemma sizing. Use when optimizing inference $/token, training networks, or picking open models.
---

# Optimize LLM inference

Action playbook from eight AI Engineer / World's Fair talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–G (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/optimize-llm-inference/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Ultra-low-latency inference (LPU/Groq-class)         → A
├─ Production OSS inference (quantization/routing)      → B
├─ MoE training network topology                        → C
├─ Fast fine-tune experiment loops                      → D
├─ Frontier cluster / SemiAnalysis planning               → E
├─ Coding agent infra (Devin-style)                     → F
└─ Pick open model tier (Gemma)                         → G
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/optimize-llm-inference ~/.claude/skills/
cp -r skills/optimize-llm-inference ~/.cursor/skills/
cp -r skills/optimize-llm-inference ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/gpus-inference-aie-world-s-fair-2024/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Measure $/token at your concurrency | [src-002 @ 10:24] |
| Network matters for MoE more than GPU count | [src-003 @ 7:56] |
| Right-size model per route | [src-002 @ 2:07] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–G; save artifacts to `./skill-outputs/optimize-llm-inference/` when requested; do not auto-commit.

---

## Invocation examples

```
@optimize-llm-inference compare inference $/token
MoE cluster network design
```
