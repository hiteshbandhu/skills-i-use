# Run LLM evals

Workflow playbooks for designing and operating LLM evaluations, distilled from twenty-five AI Engineer conference talks (Braintrust, Notion, Zapier, Arize, Microsoft, Arena, and workshops).

Output: `./skill-outputs/run-llm-evals/` (rubrics, dataset plans, CI eval stubs when you run a workflow).

## Usage

```
@run-llm-evals design evals for our coding agent
help me set up LLM-as-judge with human calibration
enterprise voice-of-customer eval strategy
```

## What it does

- Routes you to one of **14 workflows** (program kickoff → subjective/durable systems)
- Step-by-step actions with citations to source talks
- Agent deliverables and stop conditions per workflow

## Files

```
run-llm-evals/
├── SKILL.md          # Decision tree + orchestration
├── README.md
├── workflows.md      # Full workflow A–N
└── source-index.md   # Talk ↔ learning file map
```

## Install

```bash
cp -r run-llm-evals ~/.claude/skills/
cp -r run-llm-evals ~/.cursor/skills/
cp -r run-llm-evals ~/.codex/skills/
```

Works with any agent that loads a `SKILL.md` folder. Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `evals-benchmarks-ai-engineer`.

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
