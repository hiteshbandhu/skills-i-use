# Ship AIEWF 2024 agents

Seven World's Fair 2024 agent talks as shipping workflows.

Output: `./skill-outputs/ship-aiewf-2024-agents/` (checklists, rubrics, diagrams when you run a workflow).

## Usage

```
@ship-aiewf-2024-agents ship governed agent on Vertex
voice agent architecture checklist
```

## What it does

- Routes you to workflows **A–G**
- Step-by-step actions with citations to source talks
- Agent deliverables and stop conditions per workflow

## Files

```
ship-aiewf-2024-agents/
├── SKILL.md
├── README.md
├── workflows.md
└── source-index.md
```

## Install

```bash
cp -r ship-aiewf-2024-agents ~/.claude/skills/
cp -r ship-aiewf-2024-agents ~/.cursor/skills/
cp -r ship-aiewf-2024-agents ~/.codex/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `agents-aie-world-s-fair-2024`.
