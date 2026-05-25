# Run AIEWF 2024 evals & LLM ops

Workflow playbooks from six AI Engineer World's Fair 2024 eval/LLM-ops talks.

Output: `./skill-outputs/run-aiewf-2024-evals/` (checklists, rubrics, diagrams when you run a workflow).

## Usage

```
@run-aiewf-2024-evals build domain eval harness for our agent
should we fine-tune or stay on GPT-4o?
```

## What it does

- Routes you to workflows **A–F**
- Step-by-step actions with citations to source talks
- Agent deliverables and stop conditions per workflow

## Files

```
run-aiewf-2024-evals/
├── SKILL.md
├── README.md
├── workflows.md
└── source-index.md
```

## Install

```bash
cp -r run-aiewf-2024-evals ~/.claude/skills/
cp -r run-aiewf-2024-evals ~/.cursor/skills/
cp -r run-aiewf-2024-evals ~/.codex/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `evals-llm-ops-aie-world-s-fair-2024`.
