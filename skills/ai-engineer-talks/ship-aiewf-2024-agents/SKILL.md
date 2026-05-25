---
name: ship-aiewf-2024-agents
description: >
  Runs workflows for AIEWF 2024 agent talks — Vertex governance, Minecraft JSON actions, voice pipelines, agentic commerce, personas, CrewAI dogfooding, job automation realism. Use when shipping agents, voice agents, or agent marketplaces.
---

# Ship AIEWF 2024 agents

Action playbook from seven AI Engineer / World's Fair talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–G (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/ship-aiewf-2024-agents/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Enterprise agent on Vertex (governed tools)          → A
├─ Embodied/sandbox agent (structured actions)          → B
├─ Voice agent (streaming STT/TTS)                      → C
├─ Agentic commerce / machine APIs                      → D
├─ Persona-driven agent product                         → E
├─ Multi-agent internal ops (CrewAI-style)              → F
└─ Automation ROI / job atomization                       → G
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/ship-aiewf-2024-agents ~/.claude/skills/
cp -r skills/ship-aiewf-2024-agents ~/.cursor/skills/
cp -r skills/ship-aiewf-2024-agents ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/agents-aie-world-s-fair-2024/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Validated JSON/tool actions in env loop | [src-002 @ 16:24] |
| Stream audio pipeline for voice | [src-003 @ 5:02] |
| Account setup cost in automation ROI | [src-007 @ 19:42] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–G; save artifacts to `./skill-outputs/ship-aiewf-2024-agents/` when requested; do not auto-commit.

---

## Invocation examples

```
@ship-aiewf-2024-agents ship governed agent on Vertex
voice agent architecture checklist
```
