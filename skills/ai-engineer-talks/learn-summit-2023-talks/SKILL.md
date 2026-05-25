---
name: learn-summit-2023-talks
description: >
  Applies AI Engineer Summit 2023 main-stage playbooks for RAG, agents, interfaces,
  local LLMs, fine-tuning, product velocity, TypeChat/Pydantic, LangChain observability,
  and the discipline of AI engineering (Swyx, Willison). Use when grounding team practice
  in summit talks, shipping RAG/agents, or onboarding to AI engineering; or when the
  user says "summit 2023 talks", "1000x AI engineer", "production RAG Jerry Liu",
  "open questions Willison".
---

# Learn Summit 2023 talks

Action playbook from twenty-two AI Engineer Summit 2023 talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — workflows A–N
- [source-index.md](source-index.md) — src-NNN → learnings

Optional deliverables: `{SKILL_OUTPUT_DIR}/learn-summit-2023-talks/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Define AI engineering career / 1000x leverage           → A  [src-018, src-002, src-022]
├─ Production RAG + vectors + wild deployments             → B  [src-006, src-015, src-017]
├─ Agents + context-aware reasoning                      → C  [src-019, src-005]
├─ Domain fine-tuning / adaptation                       → D  [src-009]
├─ Local / private LLM deployment                        → E  [src-010]
├─ Viral AI product / growth lessons                     → F  [src-001, src-011, src-003]
├─ LLM system building blocks (product)                  → G  [src-004]
├─ Interfaces & abstraction ladder                     → H  [src-008, src-021]
├─ Type-safe LLM I/O (Pydantic / TypeChat)               → I  [src-014, src-013]
├─ Data platform AI pivot                                → J  [src-020]
├─ Multimodal APIs (see/hear/speak/draw)                 → K  [src-016]
├─ Reactive / streaming AI apps                          → L  [src-007]
├─ Open questions & yearly retrospectives                → M  [src-012]
└─ Move fast without breaking prod                       → N  [src-011]
```

Open [workflows.md](workflows.md) for steps and deliverables.

---

## Install

```bash
cp -r skills/learn-summit-2023-talks ~/.claude/skills/
cp -r skills/learn-summit-2023-talks ~/.cursor/skills/
```

Source: `playlists/ai-engineer-summit-2023-talks/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| AI engineering ≠ prompting; systems wrap non-AGI models | [src-018 @ 5:53] |
| Naive RAG fails in production — plan retrieval + eval | [src-006 @ 2:58] |
| Ask: impossible new builds vs faster builds (Willison) | [src-012 @ 1:01] |
| Structured outputs reduce integration risk | [src-014], [src-013] |
| Agents need product-grade interfaces, not chat-only | [src-019], [src-021] |

---

## Output to user

1. Name workflow (A–N) and artifact
2. Save under `./skill-outputs/learn-summit-2023-talks/` when requested

---

## Invocation examples

```
@learn-summit-2023-talks production RAG checklist from Jerry Liu
framework for open questions in our AI roadmap
pydantic vs typechat for our API layer
```
