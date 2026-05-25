# Optimize LLM inference

Eight AIEWF 2024 GPU/inference talks as optimization workflows.

Output: `./skill-outputs/optimize-llm-inference/` (checklists, rubrics, diagrams when you run a workflow).

## Usage

```
@optimize-llm-inference compare inference $/token
MoE cluster network design
```

## What it does

- Routes you to workflows **A–G**
- Step-by-step actions with citations to source talks
- Agent deliverables and stop conditions per workflow

## Files

```
optimize-llm-inference/
├── SKILL.md
├── README.md
├── workflows.md
└── source-index.md
```

## Install

```bash
cp -r optimize-llm-inference ~/.claude/skills/
cp -r optimize-llm-inference ~/.cursor/skills/
cp -r optimize-llm-inference ~/.codex/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `gpus-inference-aie-world-s-fair-2024`.
