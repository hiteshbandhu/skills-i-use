---
name: build-agent-harnesses
description: >
  Runs checklists and workflows for designing, hardening, and operating agent
  harnesses — guardrails, verify steps, tool loops, durable sessions, eval,
  quotas, coding/deep-research/voice harnesses. Use when the user builds agent
  runtimes, asks what a harness is, scopes agent vs workflow, or says "agent
  harness", "guardrails", "verify step", "FOMAT", "durable session".
---

# Build agent harnesses

Action playbook from twenty-two AI Engineer talks on agent & harness engineering. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–L (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional deliverables: `{SKILL_OUTPUT_DIR}/build-agent-harnesses/` — see [skills-i-use OUTPUT.md](https://github.com/hiteshbandhu/skills-i-use/blob/main/skills/OUTPUT.md).

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Define harness vs agent loop + guardrails/verify     → A
├─ Decide agent vs workflow for a use case              → B
├─ Maturity path: framework → state machine → scale     → C
├─ Enterprise: quotas, skills, multi-agent platform     → D
├─ Agent evaluation + anti-hype discipline            → E
├─ Long-horizon research / deep research harness        → F
├─ Coding agent / computer-use / IDE harness            → G
├─ Production chat UX: resume, steer, multi-device      → H
├─ Operate many parallel coding agents (FOMAT)          → I
├─ Regulated / domain-vertical knowledge agents         → J
├─ Delete scaffold; maximize LLM compute in backend     → K
└─ Post-training / finetune / RL for tool agents        → L
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/build-agent-harnesses ~/.claude/skills/
cp -r skills/build-agent-harnesses ~/.cursor/skills/
cp -r skills/build-agent-harnesses ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills after sync.

Source corpus: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) `playlists/agent-harness-engineering-ai-engineer/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Harness = tools + context + guardrails + verify around the model | [src-001 @ 4:36] |
| Do not prompt harder when verify shows failure — fix harness | [src-001 @ 9:37] |
| Agents only when ambiguity/value/error profile justify cost | [src-002 @ 2:57] |
| Every agent is a state machine; prune prompts as models improve | [src-003 @ 4:37] |
| Agent eval needs environments + actions, not I/O strings only | [src-006 @ 7:52] |
| Decouple clients via durable sessions for resume/steer | [src-015 @ 5:25] |

Disputed steps: read talk in [source-index.md](source-index.md).

---

## Output to user

1. Name the workflow (A–L) and what you are producing
2. Save artifacts under `./skill-outputs/build-agent-harnesses/` when the user wants files
3. Do not auto-commit

---

## Invocation examples

```
@build-agent-harnesses design a harness for our browser agent
agent vs workflow for this support bot?
we need quotas and verify steps for production agents
```
