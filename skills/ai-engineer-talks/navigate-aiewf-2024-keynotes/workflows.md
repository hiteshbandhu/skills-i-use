# Workflows — Navigate AIEWF 2024 keynotes

Read the matching section when the user’s goal matches the decision tree in [SKILL.md](SKILL.md).

---

## Workflow: product-discipline

**Use when:** establishing LLM team practices, eval culture, or data literacy.

### Steps

1. Adopt evals + monitoring as prerequisite for production claims [src-001 @ 0:20:18]
2. Define AI engineer skills: agents, tooling, evals, data pipelines [src-001 @ 0:19:44]
3. Run human review channels (e.g. Slack of outputs) before automation [src-001 @ 0:29:11]
4. Build reference-based evals reusable as guards [src-001 @ 0:32:14]
5. Audit against Simon Willison open challenges: app-specific evals [src-002 @ 0:04:19]

### Agent deliverables

- [ ] Eval + data literacy charter for the team
- [ ] Review SOP and first labeled failure set (≥30 rows)

### Stop if

- Stakeholders want model upgrades without eval regression infrastructure [src-001 @ 0:20:29]

---

## Workflow: copilots-platforms

**Use when:** embedding copilots or assistant eval loops in dev tools.

### Steps

1. Place copilots in IDE/PR/issue surfaces, not orphan chat [src-003 @ 0:10:00]
2. Pair productivity metrics with qualitative feedback [src-003 @ 0:15:00]
3. Bootstrap synthetic eval data for assistants [src-013 @ 0:08:00]
4. Gate prompt changes with eval suites [src-013 @ 0:12:00]

### Agent deliverables

- [ ] Copilot surface map + telemetry plan
- [ ] Synthetic eval dataset outline for top assistant flows

### Stop if

- No acceptance/revert telemetry on AI suggestions [src-003 pitfalls]

---

## Workflow: models-vendors

**Use when:** multimodal product design or Anthropic/OpenAI/knowledge stack choices.

### Steps

1. Map journeys to text vs vision vs voice modalities [src-004 @ 0:05:00]
2. Plan per-modality evals, not one generic judge [src-004 @ 0:18:00]
3. Align Claude prompts/tools with Anthropic release notes [src-005 @ 0:15:00]
4. Instrument RAG + agent stages for knowledge assistants [src-006 @ 0:10:00]

### Agent deliverables

- [ ] Modality decision matrix with eval hooks
- [ ] Vendor migration checklist (eval regression + policy review)

### Stop if

- Port prompts across vendors without re-eval [src-005 pitfalls]

---

## Workflow: local-inference

**Use when:** offline, private, or CPU-first deployment.

### Steps

1. Package models as llamafile for portable CPU inference [src-007 @ 0:08:00]
2. Benchmark latency/quality on target consumer hardware [src-007 @ 0:18:00]
3. Document privacy/air-gap requirements driving local choice [src-007 @ 0:12:00]

### Agent deliverables

- [ ] Local inference deployment guide (hardware targets, binaries)
- [ ] Cloud vs local decision memo

### Stop if

- GPU cloud is mandatory for the use case—local adds no value

---

## Workflow: data-platforms

**Use when:** agents need live data or org is consolidating AI primitives.

### Steps

1. Expose governed realtime APIs for agent context [src-008 @ 0:10:00]
2. Enforce authz at data layer, not prompts alone [src-008 @ 0:15:00]
3. Consolidate duplicated AI stacks into platform APIs [src-014 @ 0:10:00]
4. Staff shared eval/observability standards [src-014 @ 0:18:00]

### Agent deliverables

- [ ] Data connectivity architecture (live queries + authz)
- [ ] Platform consolidation roadmap if ≥2 teams ship assistants

### Stop if

- Stale embeddings suffice and data is static

---

## Workflow: agents-enterprise

**Use when:** enterprise agent platforms or managed AI backends.

### Steps

1. Design workflows with approvals and audit trails [src-011 @ 0:12:00]
2. Integrate enterprise identity and data policies [src-011 @ 0:15:00]
3. Use composable model+function platforms (Hypermode-style) [src-012 @ 0:06:00]

### Agent deliverables

- [ ] Enterprise agent governance checklist
- [ ] Agent platform build-vs-buy criteria

### Stop if

- Single broad-autonomy agent with prod-wide credentials [src-011 pitfalls]

---

## Workflow: strategy-craft

**Use when:** executive strategy, education, or hardware performance planning.

### Steps

1. Model second-order market/UX effects before launch [src-009 @ 0:12:00]
2. Teach decoder mechanics to debug hallucination/repetition [src-010 @ 0:35:00]
3. Profile CPU/GPU workloads with portable perf stacks (MAX) [src-015 @ 0:12:00]

### Agent deliverables

- [ ] Second-order effects brief for proposed AI feature
- [ ] Hardware profiling plan for inference hot paths

### Stop if

- Task is purely tactical implementation—route to other workflows
