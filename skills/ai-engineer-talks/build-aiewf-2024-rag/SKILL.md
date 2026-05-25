---
name: build-aiewf-2024-rag
description: >
  Runs workflows for AIEWF 2024 RAG talks — layout-aware ingest, GraphRAG, eval-driven tuning, Pydantic structured IO, MongoDB vectors, EMT memory, construction vertical agents, personal-assistant data graphs. Use when the user says "RAG", "GraphRAG", "chunking PDF", "Pydantic RAG", or AIEWF retrieval playlist.
---

# Build AIEWF 2024 RAG stacks

Action playbook from eight AI Engineer / World's Fair talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–H (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/build-aiewf-2024-rag/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Fix PDF/table RAG failures (layout ingest)           → A
├─ Add knowledge graphs (GraphRAG)                        → B
├─ Tune RAG with eval compass                             → C
├─ Harden LLM IO with Pydantic/Instructor                 → D
├─ Unified doc+vector on MongoDB                          → E
├─ Explore beyond RAG (EMT memory tokens)                 → F
├─ Vertical spec-heavy RAG (construction)                 → G
└─ Personal assistant structured data (minimize LLM)    → H
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/build-aiewf-2024-rag ~/.claude/skills/
cp -r skills/build-aiewf-2024-rag ~/.cursor/skills/
cp -r skills/build-aiewf-2024-rag ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/rag-llm-frameworks-aie-world-s-fair-2024/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Fix ingest before more retrieval tricks | [src-002 @ 1:21] |
| Eval-driven chunk/rerank changes | [src-004 @ 1:48] |
| Structured outputs via Pydantic | [src-005 @ 12:19] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–H; save artifacts to `./skill-outputs/build-aiewf-2024-rag/` when requested; do not auto-commit.

---

## Invocation examples

```
@build-aiewf-2024-rag our RAG fails on tables in PDFs
when should we add GraphRAG?
```
