---
name: operate-agent-memory
description: >
  Runs checklists and workflows for agent context engineering — separating context
  from memory, smart truncation, sub-agent offload, and long-session evals. Use when
  the user hits context limits on observability or trace-heavy agents, designs
  multi-turn memory, or says "context management", "escape context window",
  "agent forgets follow-ups".
---

# Operate agent memory

Action playbook from Sally-Ann Delucia (Arize Alex). **Do not summarize the talk** — pick a workflow and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — workflows A–E
- [source-index.md](source-index.md) — talk → learnings

Optional deliverables: `{SKILL_OUTPUT_DIR}/operate-agent-memory/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Diagnose context death spiral (retry adds data)     → A
├─ Design in-window vs memory split                    → B
├─ Implement truncation + retrievable store              → C
├─ Add long-session regression evals                     → D
└─ Split main vs sub-agent context budgets               → E
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/operate-agent-memory ~/.claude/skills/
cp -r skills/operate-agent-memory ~/.cursor/skills/
cp -r skills/operate-agent-memory ~/.codex/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) `playlists/memory-ai-engineer/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Context = what the model sees; memory = what survives outside | [src-001 @ 7:48] |
| Agents fail on context, not prompts | [src-001 @ 14:14] |
| Naive head truncation breaks follow-ups | [src-001 @ 5:18] |
| Uncontrolled summarization is unreliable | [src-001 @ 6:15] |
| Long sessions fail late — eval turn N+1 | [src-001 @ 8:44] |

---

## Output to user

1. Name the workflow (A–E) and deliverable
2. Save artifacts under `./skill-outputs/operate-agent-memory/` when useful
3. Do not auto-commit

---

## Invocation examples

```
@operate-agent-memory our agent loses thread on turn 12
design sub-agents for heavy trace search
long-session eval harness for support copilot
```
