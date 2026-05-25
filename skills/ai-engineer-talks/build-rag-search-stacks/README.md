# Build RAG and AI search stacks

Workflow playbooks for production RAG and AI search, distilled from thirteen AI Engineer conference talks (hybrid retrieval, agentic search, enterprise eval, web search, document agents).

Output: `./skill-outputs/build-rag-search-stacks/` (checklists, diagrams, rubrics when you run a workflow).

## Usage

```
@build-rag-search-stacks design hybrid search for our support KB
help me benchmark vector DB vendors
agentic RAG tool design for our codebase agent
```

## What it does

- Routes you to one of **12 workflows** (grounding strategy → product KB)
- Step-by-step actions with citations to source talks
- Agent deliverables and stop conditions per workflow

## Files

```
build-rag-search-stacks/
├── SKILL.md          # Decision tree + orchestration
├── README.md
├── workflows.md      # Full workflow A–L
└── source-index.md   # Talk ↔ learning file map
```

## Install

```bash
cp -r build-rag-search-stacks ~/.claude/skills/
cp -r build-rag-search-stacks ~/.cursor/skills/
cp -r build-rag-search-stacks ~/.codex/skills/
```

Works with any agent that loads a `SKILL.md` folder. Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `rag-search-2025`.

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
