---
name: evaluate-with-braintrust
description: >
  Evaluates LLM and agent products with Braintrust—offline/online evals, SDK/CI
  workflows, eval platform design, Zapier/Notion product ops, and Loop-style
  optimization. Use when the user mentions Braintrust, eval playground, autoevals,
  production log evals, or agent quality platforms.
---

# Evaluate with Braintrust

Action playbook from seven Braintrust @ AI Engineer talks. **Do not summarize** — pick a workflow.

**Supporting files:** [workflows.md](workflows.md) · [source-index.md](source-index.md)

Related skill: `run-llm-evals` (cross-vendor eval theory).

Optional: `./skill-outputs/evaluate-with-braintrust/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Eval fundamentals (datasets, scorers, modes)        → evals-101
├─ Build/buy eval platform architecture                → platform-design
├─ Five lessons / future of evals (velocity, Loop)     → eval-ops
├─ Zapier-style product + eval integration             → product-ops
├─ Notion-class world-class AI quality bar             → world-class-products
└─ Complex app workshop (Trainline patterns)           → complex-apps
```

---

## Install

```bash
cp -r skills/evaluate-with-braintrust ~/.cursor/skills/
cp -r skills/evaluate-with-braintrust ~/.codex/skills/
```

Source: `playlists/braintrust-ai-engineer/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Eval = data + task + scorers; offline and online | [src-001 @ 0:07:12] |
| Prod logs must feed datasets and online evals | [src-001 @ 0:13:13] |
| Unify offline experiments with trace replay | [src-002 @ 0:14:15] |
| 24h model swaps when evals healthy (Notion bar) | [src-003 @ 0:40] |
| Human-in-loop on Loop optimizations | [src-004 @ 0:03:33] |

---

## Output

Name workflow; artifacts under `./skill-outputs/evaluate-with-braintrust/` when requested.
