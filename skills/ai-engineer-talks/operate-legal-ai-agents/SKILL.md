---
name: operate-legal-ai-agents
description: >
  Runs checklists for legal and vertical AI agents — artifact-first UX, tabular
  review, skills at work nodes, verifier's-rule task mapping, guardrails, decision
  logs, and human control vs trust. Use when building law-firm agents, contract
  workflows, Legora-style workspaces, or escaping chat-only legal copilots.
---

# Operate legal AI agents

Action playbook from Jacob Lauritzen (Legora) at AI Engineer. **Do not summarize the talk** — pick a workflow and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — workflows A–F
- [source-index.md](source-index.md)

Optional deliverables: `./skill-outputs/operate-legal-ai-agents/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Map legal tasks to verify/control profile     → A
├─ Split human vs agent responsibilities         → B
├─ Design artifact-first collaboration UX        → C
├─ Encode firm judgment (skills + guardrails)    → D
├─ Run multi-doc review (tabular pattern)        → E
└─ Fix long chat agents (compaction, rewrites)   → F
```

Open [workflows.md](workflows.md) for the chosen letter.

---

## Install

```bash
cp -r skills/operate-legal-ai-agents ~/.claude/skills/
cp -r skills/operate-legal-ai-agents ~/.cursor/skills/
cp -r skills/operate-legal-ai-agents ~/.codex/skills/
cp -r skills/operate-legal-ai-agents ~/.agents/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) `playlists/ai-in-law-legal-ai-engineer/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Planning/review is the bottleneck; generation is cheap | [src-001 @ 2:44] |
| Chat is low-bandwidth for work trees | [src-001 @ 11:31] |
| Skills beat upfront planning for unknown contingencies | [src-001 @ 9:49] |
| Elicit with decision log + unblock-first | [src-001 @ 10:38] |

---

## Output to user

1. Name workflow (A–F) and deliverables
2. Save checklists/UX sketches under `./skill-outputs/operate-legal-ai-agents/` when requested
3. Do not auto-commit

---

## Invocation examples

```
@operate-legal-ai-agents design tabular review for M&A diligence
map our contract tasks on the verifier spectrum
we need artifact-first UX not another legal chatbot
```
