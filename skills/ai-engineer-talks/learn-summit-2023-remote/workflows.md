# Workflows — Learn Summit 2023 remote talks

---

## Workflow A — LLM application evals (LLMeval)

**Source:** [src-001]

### Steps

1. Version prompts, configs, and datasets alongside model versions [src-001 @ 0:00:53].
2. Add eval before defaulting to fine-tune [src-001 @ 0:01:03].
3. Automate regression runs on prompt/model changes [src-001 @ 0:01:32].
4. Report pass rates by scenario class (not single score) [src-001].

### Deliverables: eval matrix, CI hook spec. **Stop if:** no labeled failure cases.

---

## Workflow B — Hybrid context query for grounding

**Source:** [src-002]

### Steps

1. Map user query → hybrid retrieval (lexical + semantic) [src-002 @ 0:00:28].
2. Build RAG pipeline stages explicitly [src-002 @ 0:01:26].
3. Tune context assembly for LLM grounding [src-002 @ 0:01:20].
4. Measure retrieval precision before answer quality [src-002].

### Deliverables: pipeline diagram, query routing rules.

---

## Workflow C — High-velocity AI web apps (GPT Web App Generator)

**Source:** [src-003]

### Steps

1. Study codegen agent loop: spec → generate → deploy [src-003 @ 0:03:10].
2. Cap scope per app; ship many small apps vs one platform [src-003 @ 0:04:05].
3. Instrument usage (10k apps/month lesson) [src-003].
4. Plan abuse/safety at viral scale [src-003].

### Deliverables: agent loop checklist, launch guardrails.

---

## Workflow D — Fullstack → AI engineer

**Source:** [src-004]

### Steps

1. Inventory transferable skills (APIs, product, debugging) [src-004 @ 0:00:31].
2. Follow curated learning path + community [src-004 @ 0:01:05].
3. Build portfolio projects on foundation models [src-004 @ 0:01:22].
4. Pair with [src-010] for tooling depth [src-004].

### Deliverables: 90-day learning plan.

---

## Workflow E — Model evaluation for your use case

**Source:** [src-005]

### Steps

1. Reject one-size-fits-all benchmarks [src-005 @ 0:00:45].
2. Define task-specific success criteria [src-005 @ 0:00:35].
3. Run head-to-head on *your* prompts and data [src-005 @ 0:00:31].
4. Document cost/latency/quality tradeoffs [src-005].

### Deliverables: model selection rubric.

---

## Workflow F — No-code fine-tuning

**Source:** [src-006]

### Steps

1. Clarify fine-tune vs prompt when to use each [src-006 @ 0:01:19].
2. Use no-code path for fast domain adaptation experiments [src-006 @ 0:00:26].
3. Validate on held-out real user queries [src-006 @ 0:00:34].
4. Plan rollback to base model [src-006].

### Deliverables: fine-tune experiment log template.

---

## Workflow G — Prompt engineering tactics

**Source:** [src-007]

### Steps

1. Centralize prompts in management tooling [src-007 @ 0:00:18].
2. Apply tactical patterns from talk (structure, roles, constraints) [src-007 @ 0:00:26].
3. A/B prompt versions with eval hooks [src-007].
4. Share prompt library across teams [src-007].

### Deliverables: prompt repo layout + review checklist.

---

## Workflow H — Multimodal apps (ModelFusion / TS)

**Source:** [src-008]

### Steps

1. Orchestrate modalities via TypeScript library [src-008 @ 0:00:25].
2. Chain: prompt → model calls → composition [src-008 @ 0:03:02].
3. Keep story/narrative state in structured prompts [src-008 @ 0:03:10].
4. Test each modality path independently [src-008].

### Deliverables: multimodal sequence diagram.

---

## Workflow I — Code AI maturity model

**Source:** [src-009]

### Steps

1. Map current workflows to SAE-like levels [src-009 @ 0:02:26].
2. Identify partial automation vs full agent handoff [src-009 @ 0:04:04].
3. Set next maturity milestone with metrics [src-009 @ 0:02:59].
4. Align tooling spend to maturity stage [src-009].

### Deliverables: maturity assessment + roadmap.

---

## Workflow J — Rise of the AI software engineer

**Source:** [src-010]

### Steps

1. Stack: embeddings + vector + graph retrieval [src-010 @ 0:02:08].
2. Integrate code index / morph-style retrieval [src-010 @ 0:02:38].
3. Treat AI engineer as systems role, not prompt-only [src-010 @ 0:02:41].
4. Cross-read [src-004] for career framing [src-010].

### Deliverables: tooling architecture for code AI.

---

## Workflow K — Infinite generative game

**Source:** [src-011]

### Steps

1. Design loop: player action → LLM scene → state update [src-011 @ 0:01:56].
2. Grid/world constraints (16 scenes, etc.) [src-011 @ 0:00:51].
3. Guard narrative coherence across turns [src-011 @ 0:00:42].
4. Monitor cost per session [src-011].

### Deliverables: game-state schema + prompt template.
