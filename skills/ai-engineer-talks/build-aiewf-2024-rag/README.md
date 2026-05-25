# Build AIEWF 2024 RAG stacks

Eight World's Fair 2024 RAG/framework talks as actionable workflows.

Output: `./skill-outputs/build-aiewf-2024-rag/` (checklists, rubrics, diagrams when you run a workflow).

## Usage

```
@build-aiewf-2024-rag our RAG fails on tables in PDFs
when should we add GraphRAG?
```

## What it does

- Routes you to workflows **A–H**
- Step-by-step actions with citations to source talks
- Agent deliverables and stop conditions per workflow

## Files

```
build-aiewf-2024-rag/
├── SKILL.md
├── README.md
├── workflows.md
└── source-index.md
```

## Install

```bash
cp -r build-aiewf-2024-rag ~/.claude/skills/
cp -r build-aiewf-2024-rag ~/.cursor/skills/
cp -r build-aiewf-2024-rag ~/.codex/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `rag-llm-frameworks-aie-world-s-fair-2024`.
