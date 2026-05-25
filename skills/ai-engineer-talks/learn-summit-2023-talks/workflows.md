# Workflows — Learn Summit 2023 talks

---

## Workflow A — AI engineering discipline & community

**Sources:** [src-018], [src-002], [src-022]

### Steps

1. Frame AI engineering as installation/deployment phase of a tech cycle [src-018 @ 2:48].
2. Contrast engineering vs prompt-only roles [src-018 @ 5:53].
3. Join practitioner network for hiring/learning [src-002].
4. Use **weekend project** cadence for skill growth [src-022].

### Deliverables: role charter, learning cadence. **Stop if:** team has no production feedback loop.

---

## Workflow B — Production RAG & vectors

**Sources:** [src-006], [src-015], [src-017]

### Steps

1. List naive-RAG failure modes (retrieval, chunking, staleness) [src-006 @ 2:58].
2. Harden retrieval stage before generation [src-006 @ 3:12].
3. Compare Postgres/pgvector ops patterns [src-017].
4. Study real-world RAG deployments & lessons [src-015 @ 0:01:41].
5. Add agent tool-use alongside retrieval where needed [src-006 @ 16:01].

### Deliverables: RAG production checklist, index config.

---

## Workflow C — Agents & context-aware apps

**Sources:** [src-019], [src-005]

### Steps

1. Define agent boundaries vs workflows [src-019].
2. Wire LangChain + LangSmith for tracing/eval [src-005].
3. Build context-aware reasoning paths [src-005].
4. Plan human oversight and failure recovery [src-019].

### Deliverables: agent architecture + observability plan.

---

## Workflow D — Domain adaptation & fine-tuning

**Source:** [src-009]

### Steps

1. Decide fine-tune vs RAG vs prompts for domain [src-009].
2. Prepare domain corpus and eval set [src-009].
3. Measure adaptation lift on held-out tasks [src-009].
4. Document refresh/retrain policy [src-009].

### Deliverables: adaptation decision memo.

---

## Workflow E — Local LLMs

**Source:** [src-010]

### Steps

1. Select local runtime/hardware budget [src-010].
2. Quantize and benchmark latency on target devices [src-010].
3. Privacy/offline requirements → local-first architecture [src-010].
4. Fallback to API for quality gaps [src-010].

### Deliverables: local deployment runbook.

---

## Workflow F — Product velocity & inclusive AI

**Sources:** [src-001], [src-011], [src-003]

### Steps

1. Viral growth: infra, moderation, cost at 120k users/week [src-001].
2. **Move fast break nothing:** guardrails while shipping [src-011].
3. Build AI for all: access, safety, education [src-003].

### Deliverables: launch checklist + risk register.

---

## Workflow G — LLM system building blocks

**Source:** [src-004]

### Steps

1. Map product to building blocks: data, model, eval, UX, ops [src-004].
2. Prioritize blocks by risk and user value [src-004].
3. Avoid duplicating blocks across teams [src-004].

### Deliverables: system block diagram.

---

## Workflow H — Interfaces & abstraction

**Sources:** [src-008], [src-021]

### Steps

1. Climb abstraction ladder: tokens → UI affordances [src-008].
2. Design **intelligent interfaces** not chat-only [src-021].
3. Prototype new interaction primitives [src-021].
4. Test with real tasks, not demos [src-008].

### Deliverables: interface spec + prototype brief.

---

## Workflow I — Type-safe LLM integration

**Sources:** [src-014], [src-013]

### Steps

1. Model I/O with Pydantic schemas [src-014].
2. Evaluate TypeChat for natural language → types [src-013].
3. Validate outputs before side effects [src-014], [src-013].
4. Generate SDK/docs from schemas [src-014].

### Deliverables: schema catalog + validation middleware.

---

## Workflow J — Data platform AI pivot

**Source:** [src-020]

### Steps

1. Map data team workflows AI can accelerate [src-020].
2. Integrate with Prefect/Hex-style orchestration [src-020].
3. Measure analyst time saved vs trust [src-020].

### Deliverables: pivot roadmap for data org.

---

## Workflow K — Multimodal APIs

**Source:** [src-016]

### Steps

1. Chain see/hear/speak/draw capabilities [src-016].
2. Pick API surfaces per modality [src-016].
3. Unified eval across modalities [src-016].

### Deliverables: multimodal feature map.

---

## Workflow L — Reactive AI apps

**Source:** [src-007]

### Steps

1. Stream tokens/events to UI [src-007].
2. Handle backpressure and cancellation [src-007].
3. Separate sync vs async agent steps [src-007].

### Deliverables: reactive architecture notes.

---

## Workflow M — Open questions framework

**Source:** [src-012]

### Steps

1. For each hype cycle ask: impossible new builds? faster builds? [src-012 @ 1:01].
2. Retrospect 12 months of launches with those lenses [src-012 @ 0:33].
3. Publish open questions for the team [src-012 @ 0:45].
4. Revisit quarterly [src-012].

### Deliverables: open-questions doc.

---

## Workflow N — Move fast, break nothing

**Source:** [src-011]

### Steps

1. Define what must not break (SLAs, compliance) [src-011].
2. Fast iteration lanes with feature flags [src-011].
3. Automated smoke eval on every release [src-011].

### Deliverables: release policy.
