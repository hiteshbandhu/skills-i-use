---
name: build-rag-search-stacks
description: >
  Runs checklists and workflows for designing, layering, evaluating, and operating
  production RAG and AI search — hybrid retrieval, agentic context tools, enterprise
  eval, web neural search, managed platforms, document agents. Use when the user
  builds retrieval for agents, picks vector vs lexical vs hybrid, designs eval for
  augmented AI, scales regulated RAG, compares search APIs, or says "RAG stack",
  "hybrid search", "agentic RAG", "vector benchmark".
---

# Build RAG and AI search stacks

Action playbook from thirteen AI Engineer talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–L (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional deliverables: `{SKILL_OUTPUT_DIR}/build-rag-search-stacks/` — see [skills-i-use OUTPUT.md](https://github.com/hiteshbandhu/skills-i-use/blob/main/skills/OUTPUT.md).

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Choose RAG vs long-context vs fine-tune           → A
├─ Design hybrid retrieval (lexical + vector + rerank) → B
├─ Vet vector DB / ANN vendor claims                 → C
├─ Ship regulated / legal / enterprise corpus RAG      → D
├─ Layer techniques without over-building              → E
├─ Build agent tools for multi-source context          → F
├─ Persist memory + tool scale for agents              → G
├─ Evaluate web / augmented AI search in production    → H
├─ Open-web research agent (long semantic queries)     → I
├─ Fast enterprise doc Q&A (tables, grounding)         → J
├─ Document-heavy knowledge work (Excel, SharePoint)   → K
└─ Vertical product KB (sales, onboarding assets)      → L
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

Copy this folder into your agent’s skills directory, for example:

```bash
cp -r skills/ai-engineer-talks/build-rag-search-stacks ~/.claude/skills/
cp -r skills/ai-engineer-talks/build-rag-search-stacks ~/.cursor/skills/
cp -r skills/ai-engineer-talks/build-rag-search-stacks ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills after sync.

Source corpus: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) `playlists/rag-search-2025/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Embeddings are the dominant lever in most stacks | [src-009 @ 4:11] |
| AI search = concept retrieval + intent + filters + agent loops | [src-009 @ 2:27] |
| Instruction-tuned / steerable embeddings for query shape | [src-009 @ 10:37] |
| Agentic loop: decompose → search → LLM expand → search again | [src-009 @ 7:25] |
| Contextual retrieval: enrich chunks with titles/global metadata | [src-010 @ 8:29] |
| Multimodal: screenshot → multimodal embedding for slides/tables | [src-010 @ 15:07] |

Disputed steps: read talk in [source-index.md](source-index.md).

---

## Output to user

1. Name the workflow (A–L) and what you are producing
2. Save artifacts under `./skill-outputs/build-rag-search-stacks/` when the user wants files (diagrams, rubrics, checklists)
3. Do not auto-commit

---

## Invocation examples

```
@build-rag-search-stacks design hybrid retrieval for our legal corpus
help me evaluate web search APIs for agents
we need enterprise RAG — where do we start?
```
