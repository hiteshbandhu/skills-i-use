# Workflows — Run AIEWF 2024 evals

---

## Workflow A — Domain eval ladder (Hamel/Emil)

**Use when:** vertical agent needs eval from scratch.

### Steps
1. Code assertions on tools/formats [src-001 @ 4:41]
2. Full trace logging + inspect UI [src-001 @ 6:39]
3. Spreadsheet/Metabase eval from logged failures [src-001 @ 5:55]
4. Human review queue; then aligned LLM judge [src-001 @ 12:33]

### Deliverables
- [ ] Assertion list + logging plan
- [ ] First labeled failure set (≥30 rows)

### Stop if
- Jumping to vendor judge templates first [src-001 @ 14:16]

---

## Workflow B — Trace-native task evals (Arize)

**Use when:** multi-step app (router + tools + answer).

### Steps
1. Trace each hop; score router before answer quality [src-004 @ 4:46]
2. Prefer explanatory pass/fail over fake 0.8 precision [src-004 @ 10:43]
3. Calibrate numeric judges on correlated failures [src-004 @ 12:42]

### Deliverables
- [ ] Layered eval diagram + per-hop scorers

### Stop if
- Single aggregate score on agent graph [src-004 @ 4:22]

---

## Workflow C — LLM judges (Volkov)

**Use when:** adding automated judges.

### Steps
1. Log multi-turn traces [src-003 @ 2:16]
2. Programmatic checks for structured fields [src-003 @ 8:33]
3. Document rubric criteria before LLM judge [src-003 @ 12:47]
4. Audit bias when models change [src-003 @ 14:19]

### Deliverables
- [ ] Rubric doc + judge calibration notebook

---

## Workflow D — PM+eng eval ops (Zapier)

**Use when:** shipping model upgrades without regressions.

### Steps
1. PM-owned pass criteria per integration [src-002 @ 5:11]
2. Seed datasets from prod logs [src-002 @ 6:09]
3. Diff regressions on model swap [src-002 @ 7:39]
4. Split router vs editor evals for copilot [src-002 @ 9:48]

### Deliverables
- [ ] Regression gate in CI/release

---

## Workflow E — Enterprise conversation intelligence (Echo)

**Use when:** CX/voice products need deploy-grade eval.

### Steps
1. Ingest 100% conversations [src-005 @ 2:36]
2. Define insight schema (topics, sentiment) [src-005 @ 3:18]
3. LLM label at scale; human audit sample [src-005 @ 10:36]
4. Fine-tune after label quality proven [src-005 @ 12:18]

### Deliverables
- [ ] Insight schema + labeling SOP

---

## Workflow F — GenAI maturity / fine-tune gate (OpenPipe)

**Use when:** debating fine-tuning.

### Steps
1. Plot quality vs $/token for base models [src-006 @ 2:27]
2. Probe ceiling with inference-time teachers (MoA) [src-006 @ 4:21]
3. Require customer eval sets before FT [src-006 @ 5:55]
4. Distill teacher outputs to smaller FT model [src-006 @ 5:35]

### Deliverables
- [ ] Fine-tune decision memo with Pareto chart

### Stop if
- FT before eval plateau [src-006 @ 11:33]
