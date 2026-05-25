# Build agent harnesses

Workflow playbooks for agent runtimes and harness engineering, distilled from twenty-two AI Engineer conference talks (guardrails, verify, eval, durable UX, coding/research/voice harnesses).

Output: `./skill-outputs/build-agent-harnesses/` (checklists, diagrams, rubrics when you run a workflow).

## Usage

```
@build-agent-harnesses add verify steps to our computer-use agent
should this be an agent or a workflow?
enterprise harness with quotas and skills library
```

## What it does

- Routes you to one of **12 workflows** (harness fundamentals → post-training)
- Step-by-step actions with citations to source talks
- Agent deliverables and stop conditions per workflow

## Files

```
build-agent-harnesses/
├── SKILL.md          # Decision tree + orchestration
├── README.md
├── workflows.md      # Full workflow A–L
└── source-index.md   # Talk ↔ learning file map
```

## Install

```bash
cp -r build-agent-harnesses ~/.claude/skills/
cp -r build-agent-harnesses ~/.cursor/skills/
cp -r build-agent-harnesses ~/.codex/skills/
```

Works with any agent that loads a `SKILL.md` folder. Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `agent-harness-engineering-ai-engineer`.

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
