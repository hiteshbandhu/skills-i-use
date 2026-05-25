---
name: observe-ai-production
description: >
  Observes and improves production LLM apps with Arize Phoenix—tracing, layered
  agent evals, prompt learning loops, and PM/engineering eval pipelines. Use when
  the user mentions Arize, Phoenix, OpenInference, agent router evals, prompt
  optimization from traces, or shipping AI with production observability.
---

# Observe AI production (Arize)

Action playbook from six Arize @ AI Engineer talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files:** [workflows.md](workflows.md) · [source-index.md](source-index.md)

Optional: `./skill-outputs/observe-ai-production/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Layered agent evals (router, skills, convergence)     → agent-evals
├─ Hands-on Phoenix agent eval workshop                  → phoenix-workshop
├─ Prompt learning from production traces                → prompt-learning
├─ PM-facing eval frameworks and release gates           → pm-evals
└─ Org-scale eval pipelines (CI, versioning)             → eval-pipelines
```

See [workflows.md](workflows.md). Related: `run-llm-evals` for cross-vendor eval theory.

---

## Install

```bash
cp -r skills/observe-ai-production ~/.claude/skills/
cp -r skills/observe-ai-production ~/.cursor/skills/
cp -r skills/observe-ai-production ~/.codex/skills/
```

Source: `playlists/arize-ai-engineer/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Eval router decisions, not only final answers | [src-001 @ 0:08:21] |
| Trace every tool/LLM call for agent eval substrate | [src-002 @ 0:06:18] |
| Calibrate LLM judges on human labels before automation | [src-002 @ 0:89:37] |
| Close loop: observability → dataset → prompt patch | [src-003 @ 0:20:00] |
| Version datasets/scorers like production code | [src-005 @ 0:10:00] |

---

## Output

Name workflow; save artifacts to `./skill-outputs/observe-ai-production/` when requested; do not auto-commit.
