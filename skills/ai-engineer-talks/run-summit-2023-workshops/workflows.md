# Workflows — Run Summit 2023 workshops

Read the matching section when the user's goal matches the decision tree in [SKILL.md](SKILL.md).

---

## Workflow A — AI Engineering 101 foundations

**Use when:** onboarding engineers or aligning vocabulary before building LLM features. **Source:** [src-003]

### Steps

1. Map the stack: models, APIs, embeddings, fine-tuning, apps, safety [src-003 @ 6:41].
2. Run a **hello-world** path: API key → prompt → structured output → simple UI [src-003 @ 13:00].
3. Catalog what the team already knows vs gaps (math, MLOps, product) [src-003 @ 0:24].
4. Define a shared glossary and “questions we’re afraid to ask” forum [src-003 @ 0:49].
5. Pick one pilot app (not a platform) to exercise the full loop [src-003 @ 7:17].

### Agent deliverables

- [ ] Onboarding checklist (concepts + hands-on labs)
- [ ] Pilot app spec with success metrics

### Stop if

- Team skips fundamentals and jumps to agents without API literacy → complete steps 1–2 first.

---

## Workflow B — Inference workshop (201)

**Use when:** choosing or operating inference infrastructure. **Source:** [src-004]

### Steps

1. Define **inference-as-a-service** boundaries: model, hardware, batching, SLA [src-004 @ 1:00].
2. Document latency vs throughput tradeoffs for your traffic shape [src-004 @ 0:55].
3. Plan deployment: containers, autoscaling, cold start, GPU sharing [src-004 @ 1:48].
4. Add observability: request logs, token usage, error taxonomy [src-004 @ 0:53].
5. Cost model: $/1M tokens × peak QPS × cache hit rate [src-004 @ 1:00].

### Agent deliverables

- [ ] Inference architecture diagram + SLO table
- [ ] Runbook stub (deploy, rollback, scale)

### Stop if

- Product needs retrieval/agents but team only optimizes raw inference → pair with Workflow C.

---

## Workflow C — Rest of the Owl (product around inference)

**Use when:** shipping user value beyond model calls. **Source:** [src-001]

### Steps

1. Frame product as **language user interfaces (LUI)** atop existing or new features [src-001 @ 1:20].
2. Enumerate emerging patterns: chat UX, tools, RAG, agents, eval loops [src-001 @ 0:42].
3. Add **monitoring + observability + evaluation** as first-class, not post-hoc [src-001 @ 0:50].
4. Identify what breaks when inference alone is “solved” (data, UX, trust) [src-001 @ 0:18].
5. Roadmap: inference MVP → eval harness → production hardening [src-001 @ 0:56].

### Agent deliverables

- [ ] LUI pattern map for the product
- [ ] Eval/observability milestone plan

### Stop if

- Team treats inference latency as the only blocker while UX/eval are undefined.

---

## Workflow D — Prompt engineering principles (Anthropic)

**Use when:** improving task prompts for Claude or similar APIs. **Source:** [src-002]

### Steps

1. Explain why prompting is hard: intent gap, model opacity, coherence [src-002 @ 0:51].
2. Apply writing principles: clear objective, constraints, guidance to quality output [src-002 @ 5:22].
3. Put **context at the beginning**, explicit task after [src-002 @ 6:43].
4. Use task-specific keywords and few-shot examples to steer attention [src-002 @ 1:33].
5. Prefer **inference-time techniques** (CoT, self-correct) before fine-tune [src-002 @ 19:39].
6. Version prompts; measure regressions when models update [src-002 @ 26:37].

### Agent deliverables

- [ ] Prompt template with context/task/examples sections
- [ ] Before/after eval set (≥20 cases)

### Stop if

- User wants domain knowledge in weights → evaluate fine-tune vs RAG vs long context first [src-002 @ 1:53].
