---
name: operate-openclaw-agents
description: >
  Runs checklists and workflows for deploying, securing, scaling, and evaluating
  OpenClaw agents — personal incremental setup, enterprise containers, Kubernetes,
  maintainer PR triage, malleable evals, local vs cloud, team Slack agents. Use when
  the user deploys OpenClaw, hardens a rollout, designs agent evals, sets up a personal
  agent, compares Viktor-style Slack agents vs OpenClaw, or says "OpenClaw K8s",
  "OpenClaw security", "agent eval harness".
---

# Operate OpenClaw agents

Action playbook from six conference talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — workflows A–G (steps, deliverables, stop conditions)

Optional deliverables: `{SKILL_OUTPUT_DIR}/operate-openclaw-agents/` — see [skills-i-use OUTPUT.md](https://github.com/hiteshbandhu/skills-i-use/blob/main/skills/OUTPUT.md).

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Run OpenClaw for themselves, safely        → A (personal, incremental)
├─ Run OpenClaw at work / for a team          → B (enterprise container)
├─ Scale many agents / tasks on Kubernetes    → C (K8s + disposable agents)
├─ Maintain OpenClaw or triage PR flood       → D (maintainer ops)
├─ Measure / eval a changing agent harness    → E (malleable evals)
├─ Decide local vs cloud personal agent       → F (local/private)
└─ Build company agent in Slack (not personal) → G (Viktor-style)
```

Open [workflows.md](workflows.md) for the chosen letter.

---

## Install

```bash
cp -r skills/ai-engineer-talks/operate-openclaw-agents ~/.claude/skills/
cp -r skills/ai-engineer-talks/operate-openclaw-agents ~/.cursor/skills/
cp -r skills/ai-engineer-talks/operate-openclaw-agents ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills after sync.

Source corpus: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) `playlists/openclaw/`.

---

## Output to user

1. Name the workflow (A–G) and deliverables you are producing
2. Save runbooks/checklists under `./skill-outputs/operate-openclaw-agents/` when the user wants files
3. Do not auto-commit

---

## Invocation examples

```
@operate-openclaw-agents set up personal OpenClaw incrementally
harden OpenClaw for enterprise containers
design malleable evals for our OpenClaw harness
```
