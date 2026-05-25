# Workflows — Operate legal AI agents

Read the matching section when the user's goal matches the decision tree in [SKILL.md](SKILL.md).

---

## Workflow A — Verifier's-rule task map

**Use when:** deciding what to automate in legal workflows.

### Steps

1. List tasks (definitions check, draft contract, litigation strategy, etc.) [src-001 @ 4:07]
2. Score each: **easy to verify** vs **easy to generate** vs **objective truth exists** [src-001 @ 3:22]
3. Automate high-verify tasks first (definition linting); keep strategy human-led [src-001 @ 4:33]
4. Add **proxy verifiers** where true verification is delayed (golden-contract similarity) [src-001 @ 6:21]

### Agent deliverables

- [ ] Task matrix with verify score, agent ownership, human gate
- [ ] Proxy metrics for "unverifiable until court" work

### Stop if

- User wants full autonomous contract negotiation with no human review → require guardrails + artifact UX [src-001 @ 7:12]

---

## Workflow B — Human/agent split

**Use when:** economics shifted to planning/review as bottleneck.

### Steps

1. Identify **planning** artifacts humans must own (risk profile, precedent, negotiation stance) [src-001 @ 6:43]
2. Delegate verifiable execution (formatting, definition lint, clause extraction) [src-001 @ 6:55]
3. Size review UX for large outputs (avoid "review entire PR" pain) [src-001 @ 2:59]

### Agent deliverables

- [ ] RACI-style split per workflow step
- [ ] Review surface spec (what lawyer sees before agent continues)

---

## Workflow C — Artifact-first UX

**Use when:** replacing chat-as-primary interface.

### Steps

1. Model work as **DAG/tree**, not linear chat [src-001 @ 8:00]
2. Pick durable artifact: document, table, dashboard—match vertical [src-001 @ 11:43]
3. Enable **localized control**: highlight clause 3 → agent edits clause 3 only [src-001 @ 12:06]
4. Support comments, @-mentions, handoff to specialist sub-agents [src-001 @ 12:10]
5. Keep chat box for **intent input** only [src-001 @ 13:10]

### Agent deliverables

- [ ] Wireframe or component list for artifact + chat roles
- [ ] Event model: human edit → agent scope boundary

---

## Workflow D — Skills, guardrails, elicitation

**Use when:** encoding firm judgment into agent behavior.

### Steps

1. Author **skills** per work-node (e.g. confidentiality review procedure) [src-001 @ 9:49]
2. Add **guardrails**: allowed files, sites, tools [src-001 @ 7:12]
3. Implement **elicitation** at unknown nodes; default: decide + **decision log** [src-001 @ 10:38]
4. Surface decision log in artifact UI—not 50 chat prompts [src-001 @ 11:20]

### Agent deliverables

- [ ] Skill outline per task type
- [ ] Guardrail config + decision log schema

---

## Workflow E — Tabular review

**Use when:** multi-document contract or diligence review.

### Steps

1. Agent proposes **tabular review** primitive users already know [src-001 @ 12:18]
2. Agent fills cells; **flags** uncertain rows for human judgment [src-001 @ 12:34]
3. Human completes flagged cells; agent resumes downstream report/draft [src-001 @ 12:49]

### Agent deliverables

- [ ] Column schema (clause, risk, citation, status)
- [ ] Flagging rules and resume trigger

---

## Workflow F — Recover from chat-only agents

**Use when:** long runs, compaction, or whole-document rewrites.

### Steps

1. Diagnose: compaction, unrelated diffs, 30+ min opaque runs [src-001 @ 0:40]
2. Move state to **persistent artifact** with versioned clause edits [src-001 @ 12:06]
3. Replace replan-from-scratch with **skills + elicitation** at discovery points [src-001 @ 9:00]
4. Cap autonomous scope per step (guardrails) [src-001 @ 7:12]

### Agent deliverables

- [ ] Migration checklist from chat thread to artifact model
- [ ] Anti-compaction strategy (checkpoint per artifact section)
