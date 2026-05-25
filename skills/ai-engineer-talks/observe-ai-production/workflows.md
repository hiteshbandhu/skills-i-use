# Workflows — Observe AI production

---

## Workflow: agent-evals

**Use when:** multi-step or voice agents need production-grade evaluation architecture.

### Steps

1. Map agent layers: router, skills, trajectory/convergence [src-001 @ 0:08:21]
2. Add router evals (correct next-step/tool choice) [src-001 @ 0:08:31]
3. Eval skills independently (RAG relevance, tool success) [src-001 @ 0:09:45]
4. Track convergence on multi-step plans [src-001 @ 0:11:17]
5. Extend to voice: audio + text chunk evals [src-001 @ 0:12:04]

### Agent deliverables

- [ ] Agent eval layer diagram with scorer per layer
- [ ] Voice agent eval extension if applicable

### Stop if

- Only judging final natural-language answer [src-001 pitfalls]

---

## Workflow: phoenix-workshop

**Use when:** hands-on Phoenix evallets for a financial/research-style agent.

### Steps

1. Record full traces (tools, sub-calls) [src-002 @ 0:06:18]
2. Build cases from production failures [src-002 @ 0:42:45]
3. Write evallets for domain invariants (ticker, actionable advice) [src-002 @ 0:50:04]
4. Decompose agent when monolithic judge fails [src-002 @ 0:61:16]
5. Calibrate judges vs human labels [src-002 @ 0:89:37]
6. Track accuracy-per-dollar on iterations [src-002 @ 0:107:58]

### Agent deliverables

- [ ] ≥5 evallets with human-labeled baseline
- [ ] Judge calibration report (precision/recall)

### Stop if

- LLM judge on “actionable” without human baseline [src-002 pitfalls]

---

## Workflow: prompt-learning

**Use when:** optimizing prompts from Phoenix traces.

### Steps

1. Instrument app with OpenInference/Phoenix [src-004 @ 0:08:00]
2. Export failure spans to learning datasets [src-004 @ 0:12:00]
3. Run offline A/B prompt evals before deploy [src-004 @ 0:18:00]
4. Automate loop: trace → dataset → eval → promote [src-003 @ 0:20:00]

### Agent deliverables

- [ ] Prompt learning loop diagram + first dataset from traces

---

## Workflow: pm-evals

**Use when:** PMs need release gates and rubrics.

### Steps

1. Co-write rubrics with engineering [src-006 @ 0:08:00]
2. Define failure buckets (tone, factuality, tools) [src-006 @ 0:12:00]
3. Use eval dashboards as ship checklist [src-006 @ 0:18:00]

### Agent deliverables

- [ ] PM eval rubric (1 page) + release gate policy

---

## Workflow: eval-pipelines

**Use when:** scaling evals across teams in CI.

### Steps

1. Git-version datasets and scorers [src-005 @ 0:10:00]
2. Gate prompt/model PRs with CI eval runs [src-005 @ 0:15:00]
3. Share dashboards across eng/PM [src-005 @ 0:20:00]

### Agent deliverables

- [ ] CI eval job stub + versioning convention doc
