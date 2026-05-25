# Design agent skills

Three AI Engineer skills talks as authoring workflows.

Output: `./skill-outputs/design-agent-skills/` (checklists, rubrics, diagrams when you run a workflow).

## Usage

```
@design-agent-skills write a skill for our API
combine MCP with skills for Supabase
```

## What it does

- Routes you to workflows **A–C**
- Step-by-step actions with citations to source talks
- Agent deliverables and stop conditions per workflow

## Files

```
design-agent-skills/
├── SKILL.md
├── README.md
├── workflows.md
└── source-index.md
```

## Install

```bash
cp -r design-agent-skills ~/.claude/skills/
cp -r design-agent-skills ~/.cursor/skills/
cp -r design-agent-skills ~/.codex/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `skills-ai-engineer`.
