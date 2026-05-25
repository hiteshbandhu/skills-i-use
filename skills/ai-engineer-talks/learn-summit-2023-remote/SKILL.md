---
name: learn-summit-2023-remote
description: >
  Applies AI Engineer Summit 2023 remote-talk playbooks for evals, hybrid RAG
  grounding, model selection, fine-tuning, prompt ops, multimodal apps, coding-agent
  maturity, and career transition from fullstack. Use when reproducing summit remote
  lessons, comparing LLM eval tools, or scoping hybrid retrieval; or when the user
  says "summit 2023 remote", "llmeval", "hybrid context query", "AI maturity model".
---

# Learn Summit 2023 remote talks

Action playbook from eleven remote sessions at AI Engineer Summit 2023. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — workflows A–K
- [source-index.md](source-index.md) — src-NNN → learnings

Optional deliverables: `{SKILL_OUTPUT_DIR}/learn-summit-2023-remote/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Ship LLM evals in production (LLMeval)                    → A  [src-001]
├─ Hybrid context query / RAG grounding                    → B  [src-002]
├─ Viral AI app / codegen product (10k apps)               → C  [src-003]
├─ Career path: fullstack → AI engineer                    → D  [src-004]
├─ Pick the right model for a use case                     → E  [src-005]
├─ No-code / low-friction fine-tuning                        → F  [src-006]
├─ Prompt engineering tactics + prompt management            → G  [src-007]
├─ Multimodal TS apps (ModelFusion)                          → H  [src-008]
├─ Code AI maturity model (SAE levels)                       → I  [src-009]
├─ AI software engineer stack (embeddings, retrieval)        → J  [src-010]
└─ Generative infinite game / creative AI loops              → K  [src-011]
```

Open the matching section in [workflows.md](workflows.md).

---

## Install

```bash
cp -r skills/learn-summit-2023-remote ~/.claude/skills/
cp -r skills/learn-summit-2023-remote ~/.cursor/skills/
```

Source: `playlists/ai-engineer-summit-2023-remote-talks/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Store prompts/configs; eval before fine-tune | [src-001 @ 0:00:53] |
| RAG needs deliberate pipeline, not naive retrieval | [src-002 @ 0:01:26] |
| Model choice is use-case specific, not one-size | [src-005 @ 0:00:45] |
| Prompt engineering ≠ prompt hoarding — use tooling | [src-007 @ 0:00:18] |
| Maturity model: partial → supervised agent autonomy | [src-009 @ 0:04:04] |

---

## Output to user

1. Name workflow (A–K) and deliverable
2. Artifacts under `./skill-outputs/learn-summit-2023-remote/` when requested

---

## Invocation examples

```
@learn-summit-2023-remote set up evals like the LLMeval talk
hybrid grounding query design for our copilot
which workshop path for fullstack → AI engineer?
```
