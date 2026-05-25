# Workflows — Architect enterprise AI

---

## Workflow A — AI architect role & definition

**Sources:** [src-015], [src-009]

### Steps

1. Define AI architect: tools, embeddings, vector DB, integrations [src-015 @ 9:41].
2. Contrast with classic software architect expectations [src-015 @ 9:01].
3. Align exec definition of “AI engineer” with scope [src-009].
4. Staff agent builders vs platform owners [src-015 @ 10:19].

### Deliverables: RACI for AI architecture.

---

## Workflow B — AI products that actually work

**Sources:** [src-003], [src-010]

### Steps

1. List production failure modes (eval, UX, data) [src-003].
2. Apply agent design patterns from production [src-010].
3. Ship narrow vertical slice before platform [src-003].
4. Instrument feedback loops early [src-011] cross-ref.

### Deliverables: production readiness checklist.

---

## Workflow C — Agentic platform

**Sources:** [src-004], [src-005]

### Steps

1. Platform primitives: tools, memory, policies [src-004 @ 10:19].
2. Microsoft-style app integration patterns [src-005].
3. Multi-tenant isolation and quotas [src-004].
4. Developer self-service vs central governance [src-004].

### Deliverables: platform capability matrix.

---

## Workflow D — Voice agents

**Source:** [src-006]

### Steps

1. Latency budget for speech loop [src-006].
2. Barge-in, turn-taking, error recovery [src-006].
3. Eval with real audio scenarios [src-006].
4. Telephony vs app SDK paths [src-006].

### Deliverables: voice agent architecture.

---

## Workflow E — CIAM for agents

**Source:** [src-007]

### Steps

1. Map human vs agent identities [src-007].
2. OAuth/API keys/scoped tokens per tool [src-007].
3. AuthZ policies on agent actions [src-007].
4. Audit trail for delegated access [src-007].

### Deliverables: agent IAM design doc.

---

## Workflow F — Trusted inference for enterprise

**Source:** [src-008]

### Steps

1. Telemetry: latency, cost, quality per model [src-008].
2. CIO narrative: compliance, residency, SLAs [src-008].
3. Gateway pattern for model routing [src-008].
4. Incident response for model outages [src-008].

### Deliverables: inference trust pack.

---

## Workflow G — Browser as agent runtime

**Source:** [src-019]

### Steps

1. Headless browser tools for agents [src-019].
2. Sandboxing and credential isolation [src-019].
3. Compare browser vs API integrations [src-019].

### Deliverables: browser agent threat model.

---

## Workflow H — AX (agent experience)

**Source:** [src-002]

### Steps

1. Treat AX as primary UX surface [src-002].
2. Dev environments for agent iteration [src-002].
3. Measure time-to-first-success [src-002].

### Deliverables: AX requirements list.

---

## Workflow I — AI that pays (ROI)

**Source:** [src-001]

### Steps

1. Tie models to revenue cycle outcomes [src-001].
2. Unit economics per automated task [src-001].
3. Pilot → measure $ impact → expand [src-001].

### Deliverables: ROI model spreadsheet spec.

---

## Workflow J — Feedback loops & mentoring models

**Sources:** [src-011], [src-013]

### Steps

1. Close loop: user correction → training/eval [src-011].
2. “Mentor the machine” patterns for coding agents [src-013].
3. Avoid static prompts without learning [src-011].

### Deliverables: feedback pipeline design.

---

## Workflow K — Monetization & markets

**Sources:** [src-014], [src-012]

### Steps

1. Pricing AI features (Orb-style) [src-014].
2. Market dynamics / buying & selling machines [src-012].
3. Packaging for enterprise procurement [src-014].

### Deliverables: pricing/packaging memo.

---

## Workflow L — Modern AI team structure

**Source:** [src-016]

### Steps

1. Roles: research, platform, product, eval [src-016].
2. Embed in product squads vs central [src-016].
3. Hiring profile for AI engineers [src-016].

### Deliverables: org design options.

---

## Workflow M — Product survival & build-operate

**Sources:** [src-017], [src-018]

### Steps

1. Knife-fight positioning vs incumbents [src-017].
2. Bridge product vision ↔ operational reality [src-018].
3. Operate agents in prod (SRE, eval, cost) [src-018].

### Deliverables: product strategy one-pager.
