---
name: design-agent-skills
description: >
  Runs workflows for authoring agent skills — SKILL.md structure, MCP pairing, Langfuse lessons, progressive disclosure, validation. Use when the user writes skills, combines MCP+skills, or says "agent skills", "SKILL.md", "context gap".
---

# Design agent skills

Action playbook from three AI Engineer / World's Fair talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–C (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/design-agent-skills/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Author first skill (structure + triggers)            → A
├─ Pair skills with MCP for live data                   → B
└─ Skill-up coding agents on complex devtools           → C
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/design-agent-skills ~/.claude/skills/
cp -r skills/design-agent-skills ~/.cursor/skills/
cp -r skills/design-agent-skills ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/skills-ai-engineer/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| SKILL.md slim; workflows in sibling files | [src-002 @ 7:06] |
| Third-person description + triggers | [src-002 @ 35:14] |
| Procedures in skills; state via MCP | [src-001 @ 3:17] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–C; save artifacts to `./skill-outputs/design-agent-skills/` when requested; do not auto-commit.

---

## Invocation examples

```
@design-agent-skills write a skill for our API
combine MCP with skills for Supabase
```
