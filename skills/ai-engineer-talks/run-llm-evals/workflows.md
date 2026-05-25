# Workflows — Run LLM evals

Read the matching section when the user’s goal matches the decision tree in [SKILL.md](SKILL.md).

---

## Workflow A — Eval program kickoff (business case + flywheel)

**Use when:** team needs mandate, metrics, and operating habits for evals.

### Steps

1. Frame evals as application labs, not accuracy trivia [src-001 @ 2:32]
2. Tie offline metrics to prod logs for prioritization [src-001 @ 3:20]
3. Adopt success signals: 24h model upgrades, complaint→dataset path, offensive pre-ship forecasts [src-003 @ 0:40]
4. Brief executives on ROI/governance, not dashboards alone [src-004 @ 10:04]
5. Plan for agent-assisted eval ops as models improve judges [src-002 @ 2:02]

### Agent deliverables

- [ ] One-page eval charter (purpose, owners, cadence)
- [ ] Three measurable adoption milestones (swap speed, feedback intake, pre-launch forecasts)

### Stop if

- Stakeholders want only leaderboard benchmarks unrelated to product tasks [src-014 @ 1:07]

---

## Workflow B — Domain-specific eval system (zero → production)

**Use when:** vertical agent/app needs a disciplined harness (Hamel ladder).

### Steps

1. Write code assertions on tools, formats, invariants [src-006 @ 4:41]
2. Log all traces; pick observability tool [src-006 @ 6:39]
3. Build frictionless “look at data” UI/filters [src-006 @ 7:51]
4. Start spreadsheet/Metabase eval; curate failure rows [src-006 @ 5:55]
5. Human-review queue; only then LLM-as-judge with binary alignment [src-006 @ 12:33]

### Agent deliverables

- [ ] Assertion list + logging plan
- [ ] First labeled set (≥30 failures) and review SOP

### Stop if

- Team jumps to generic vendor eval templates before assertions exist [src-006 @ 14:16]

---

## Workflow C — Product LLM eval (not unit tests)

**Use when:** generative product (v0-style) needs coverage + CI.

### Steps

1. Map query difficulty on a “court” from easy → corner cases [src-005 @ 5:47]
2. Build dataset from thumbs-down + traced prod samples [src-005 @ 8:03]
3. Manual review batch (~100) to learn failure mix [src-005 @ 8:19]
4. Section evals per pipeline stage (RAG, tools, post-process) [src-005 @ 9:47]
5. Structured output tags for reliable scorers [src-005 @ 12:23]
6. Gate prompt PRs with full-suite regression [src-005 @ 12:55]

### Agent deliverables

- [ ] Court diagram + dataset buckets
- [ ] CI eval config stub per section

### Stop if

- Demo-twice-then-ship without distribution testing [src-005 @ 2:09]

---

## Workflow D — Metrics and rubrics workshop

**Use when:** scores don’t correlate with human judgment.

### Steps

1. Define user-visible “good” per use case [src-010 @ 11:50]
2. Decompose outputs into atomic scorable factors [src-010 @ 20:46]
3. Label rows; measure thumb agreement [src-010 @ 29:02]
4. Draft rubric with copilot from examples; refine pass 2 [src-010 @ 25:48]
5. Automate only where labelers agree [src-010 @ 9:52]

### Agent deliverables

- [ ] Rubric doc + labeled spreadsheet schema
- [ ] Agreement stats before automation

### Stop if

- Chasing automation before operational quality definition exists [src-010 @ 8:01]

---

## Workflow E — Playground → production eval platform

**Use when:** adopting Braintrust-style eval + online loop.

### Steps

1. Model task as input → run → scorer 0–1 [src-012 @ 8:37]
2. Version prompts/datasets; run experiments [src-012 @ 13:43]
3. Add LLM judge + human review on disagreements [src-012 @ 42:17]
4. Wire SDK logging to project [src-012 @ 56:45]
5. Promote prod traces to datasets; online sample scoring [src-012 @ 65:38]

### Agent deliverables

- [ ] Project layout (datasets, scorers, eval runner)
- [ ] Online/offline scorer parity checklist

### Stop if

- Playground wins without persisted dataset [src-012 @ 34:05]

---

## Workflow F — Agentic application eval

**Use when:** multi-step agents (tools, sub-agents) need shipping gates.

### Steps

1. Trace every tool/sub-call [src-016 @ 6:18], [src-007 @ 6:12]
2. Eval at router, tool-args, and outcome layers [src-007 @ 4:46]
3. Build evallets from prod failures (domain invariants) [src-016 @ 50:04]
4. Decompose agent when monolithic judge fails [src-016 @ 61:16]
5. Calibrate judges vs human labels; track precision/recall [src-016 @ 89:37]
6. Optimize accuracy per dollar [src-016 @ 107:58]

### Agent deliverables

- [ ] Trace schema + evallet catalog
- [ ] Judge calibration report template

### Stop if

- Only final-answer LLM judge with no tool traces [src-016 @ 15:10]

---

## Workflow G — Voice agent simulation eval

**Use when:** phone/voice AI needs trust before scale.

### Steps

1. Scenario library with environmental variation [src-017 @ 3:37]
2. Reference-free metrics: resolution, interruptions [src-017 @ 6:03]
3. Pre-ship automated sims; post-ship spot checks [src-017 @ 7:42]
4. Promote prod failures to sim cases [src-017 @ 11:36]
5. Component benchmarks (STT/LLM/TTS) before E2E [src-017 @ 16:10]

### Agent deliverables

- [ ] Sim scenario spec (accents, noise, barge-in)
- [ ] Metric definitions + promotion workflow

### Stop if

- Static phrase tests only [src-017 @ 4:42]

---

## Workflow H — Agent observability ↔ eval gap

**Use when:** Azure/Microsoft-style agents lack prod feedback loops.

### Steps

1. Enforce traceability on all tool calls [src-018 @ 27:56]
2. Build → observe → evaluate → improve phases [src-018 @ 7:06]
3. Sample sets from telemetry [src-018 @ 55:21]
4. Run safety + agentic evaluators [src-018 @ 34:21]
5. Alert on gap metric shifts [src-018 @ 77:24]

### Agent deliverables

- [ ] Observability checklist + eval sample set plan
- [ ] Intent/policy eval matrix

### Stop if

- Multi-agent deploy with no per-agent traces [src-018 @ 45:40]

---

## Workflow I — LLM judges, fuzzing, calibration

**Use when:** adopting or auditing LLM-as-judge and red-team search.

### Steps

1. Log conversations before judging [src-008 @ 2:16]
2. Programmatic checks first; rubric second [src-008 @ 8:33]
3. Meta-eval judges when rubrics/models change [src-013 @ 8:15]
4. Weak→strong critique pattern for cost [src-013 @ 9:55]
5. Search input space beyond golden sets [src-013 @ 14:22]

### Agent deliverables

- [ ] Rubric + bias audit plan
- [ ] Fuzz/stress harness outline

### Stop if

- Judge deployed with zero human-labeled baseline [src-016 @ 75:12]

---

## Workflow J — Model & infra benchmarking

**Use when:** comparing base models, hosting stacks, or honesty.

### Steps

1. Split perf (GuideLLM: TTFT, throughput, P99) from quality [src-011 @ 4:33]
2. Run knowledge harness tasks (e.g., MMLU-Pro) on served weights [src-011 @ 21:11]
3. Add safety/bias gates [src-011 @ 14:43]
4. Slice live arena-style dissatisfaction by category [src-014 @ 13:28]
5. Targeted honesty/sycophancy benches [src-014 @ 2:10]

### Agent deliverables

- [ ] Benchmark matrix (perf + quality + safety)
- [ ] Category weakness report template

### Stop if

- Leaderboard Elo alone drives procurement [src-014 @ 1:07]

---

## Workflow K — Enterprise conversation intelligence

**Use when:** CX/voice-of-customer products need deployable accuracy.

### Steps

1. Ingest near-100% conversations, not samples [src-023 @ 2:36]
2. Define insight schema (topics, sentiment, risk) [src-023 @ 3:18]
3. LLM label at scale; humans audit edges [src-023 @ 10:36]
4. Ground-truth sets before fine-tune [src-023 @ 12:00]
5. Prove ROI with vertical case study [src-023 @ 4:59]

### Agent deliverables

- [ ] Ingestion + labeling architecture
- [ ] Eval set derived from adjudicated conversations

### Stop if

- Sales summaries substitute for raw conversation eval [src-023 @ 1:43]

---

## Workflow L — Zapier-style eval ops (ship + learn)

**Use when:** automation/copilot products with PM+eng shared ownership.

### Steps

1. PM-defined criteria per integration/top apps [src-019 @ 5:11]
2. Seed datasets from logs; continuous regression diffs [src-019 @ 6:09]
3. Rich logging + implicit/explicit feedback mining [src-020 @ 2:38]
4. Cluster failures; unit-test vs trajectory rubrics [src-020 @ 9:15]
5. Core vs aspirational dataset split [src-020 @ 15:03]

### Agent deliverables

- [ ] Integration-tier eval matrix
- [ ] Feedback→dataset playbook

### Stop if

- Mocked tools diverge from prod in trajectory evals [src-020 @ 12:59]

---

## Workflow M — Dynamic web / AI search eval

**Use when:** choosing or improving search/RAG APIs on live web.

### Steps

1. Accept moving ground truth; contextual truth [src-015 @ 3:29]
2. Build/refresh dynamic Q&A with cited evidence [src-015 @ 6:34]
3. Score completeness, doc relevance, hallucination (reference-free) [src-015 @ 14:11]
4. Triangulate failure modes (retrieve vs generate vs abstain) [src-015 @ 18:57]
5. Require full retrieved docs, not citation-only [src-015 @ 16:01]

### Agent deliverables

- [ ] Dynamic eval refresh cadence
- [ ] Provider comparison rubric (three metrics)

### Stop if

- Static SimpleQA-only vendor selection [src-015 @ 11:16]

---

## Workflow N — Subjective quality & durable architecture

**Use when:** aesthetic media eval or long-lived LLM system design.

### Steps

1. **Subjective:** human/perceptual ground truth over FID/CLIP [src-024 @ 7:35]
2. **Subjective:** user studies for taste, not proxy scores alone [src-024 @ 9:02]
3. **Durable:** evals as stable contract; swappable models [src-025 @ 15:25]
4. **Durable:** signatures/composition over prompt castles [src-025 @ 12:44]
5. **Durable:** subtract agency; optimize with search when metrics clear [src-025 @ 6:23]

### Agent deliverables

- [ ] Human eval protocol OR DSPy-style module graph + eval contract

### Stop if

- Optimizing leaderboard proxies users reject instantly [src-024 @ 0:55]

---

## Workflow cross-reference (themes)

| Theme | Primary workflows |
|-------|-------------------|
| Domain evals | B, C, L |
| Agent evals | F, G, H |
| Metrics workshops | D, E |
| Product evals | C, E, L, M |
| LLM judges | I, F |
| Benchmarks | J, M |
| Enterprise | K |
| Observability | H, E |
