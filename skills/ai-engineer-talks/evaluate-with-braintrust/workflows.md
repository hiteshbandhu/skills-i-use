# Workflows — Evaluate with Braintrust

---

## Workflow: evals-101

**Use when:** onboarding team to Braintrust eval concepts.

### Steps

1. Define dataset, task function, scorers [src-001 @ 0:07:12]
2. Run offline evals in playground/CI via SDK [src-001 @ 0:08:42]
3. Enable production logging for online evals [src-001 @ 0:08:59]
4. Start with autoevals/LLM judges after human spot checks [src-001 @ 0:15:38]
5. Wire SDK agents to re-run evals after changes [src-001 @ 0:22:01]

### Agent deliverables

- [ ] First Braintrust eval project (data + task + 2 scorers)
- [ ] Online logging integration checklist

### Stop if

- No production logs feeding eval datasets [src-001 pitfalls]

---

## Workflow: platform-design

**Use when:** designing or evaluating eval/observability platforms.

### Steps

1. Treat evals + observability as one agent-quality system [src-002 @ 0:03:46]
2. Support agent execution inside eval runs [src-002 @ 0:09:07]
3. Version prompts/tools/params per experiment [src-002 @ 0:13:05]
4. Ingest production traces for replay evals [src-002 @ 0:14:15]
5. Enable PM/eng/domain collaboration on scorers [src-002 @ 0:10:17]

### Agent deliverables

- [ ] Platform requirements doc (execution, persistence, traces, RBAC)

### Stop if

- Spreadsheet-only evals past POC stage [src-002 pitfalls]

---

## Workflow: eval-ops

**Use when:** maturing eval velocity and automation.

### Steps

1. Target 24h model upgrade cycles when evals green [src-003 @ 0:40]
2. Turn complaints into one-step dataset adds [src-003 @ 1:13]
3. Use offensive evals to forecast launch readiness [src-003 @ 1:40]
4. Apply Loop with human side-by-side diffs [src-004 @ 0:03:33]
5. Enable autonomous Loop only after trust [src-004 @ 0:04:01]

### Agent deliverables

- [ ] Eval ops metrics dashboard spec (swap speed, complaint→test, pre-ship forecasts)

---

## Workflow: product-ops

**Use when:** product teams shipping AI features with Braintrust (Zapier patterns).

### Steps

1. Integrate evals into feature development workflow [src-005 @ 0:10:00]
2. Connect PM/eng on datasets from prod failures [src-005 @ 0:15:00]
3. Gate releases on regression suites [src-005 @ 0:20:00]

### Agent deliverables

- [ ] Feature eval RACI (PM owns rubrics, eng owns harness)

---

## Workflow: world-class-products

**Use when:** raising quality bar (Notion-style).

### Steps

1. Define quality dimensions beyond fluency [src-006 @ 0:08:00]
2. Pair product taste with automated scorers [src-006 @ 0:12:00]
3. Iterate prompts/models against shared datasets [src-006 @ 0:18:00]

### Agent deliverables

- [ ] Quality rubric aligned with Notion-class expectations

---

## Workflow: complex-apps

**Use when:** shipping multi-step AI apps (Trainline workshop).

### Steps

1. Map pipelines stages for separate scorers [src-007 @ 0:10:00]
2. Trace all steps; eval intermediate outputs [src-007 @ 0:15:00]
3. Run workshop-style eval exercises before prod [src-007 @ 0:20:00]

### Agent deliverables

- [ ] Stage-level eval matrix for complex app architecture
