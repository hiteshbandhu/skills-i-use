# Workflows — Plan sovereign AI

## Workflow A — Pillar assessment

**Use when:** scoping sovereignty for a new or migrated system.

### Steps

1. **Data:** storage + processing jurisdiction; embedding/API leakage [src-001 @ 1:55].
2. **Model:** swap freedom, provider lock-in, training-data provenance [src-001 @ 4:28].
3. **Infrastructure:** air-gap → VPC → sovereign cloud → SaaS spectrum [src-001 @ 3:22].
4. **Operational:** traceability, HITL in HR/finance, auditable updates [src-001 @ 5:50].
5. Pick minimum pillar set for domain—not always full air-gap [src-001 @ 6:30].

### Deliverables

- [ ] Pillar matrix with pass/partial/fail per component

---

## Workflow B — Retrofit impact (what breaks)

**Use when:** “make our working system sovereign.”

### Steps

1. **Model swap:** prompt rewrites, re-eval from scratch [src-001 @ 7:31].
2. **Data move:** multi-DB, federated search design [src-001 @ 7:52].
3. **On-prem:** K8s/GPU/network ops previously managed by cloud [src-001 @ 8:26].
4. **Observability:** black box becomes visible; versioning needed [src-001 @ 9:07].

### Deliverables

- [ ] Ordered migration plan with test gates after each step

### Stop if

- Greenfield → start with Workflow C.

---

## Workflow C — Reference sovereign agent

**Use when:** designing agents under compliance.

### Steps

1. Input guardrail: injection + regulatory intent checks [src-001 @ 11:45].
2. Agent with scoped tools/MCP—not all tools from server [src-001 @ 15:15].
3. Searchable tool set when tool count is large (BM25) [src-001 @ 16:06].
4. Output guardrail before user sees response [src-001 @ 12:44].
5. Human-in-the-loop on sensitive tool classes [src-001 @ 17:01].
6. OpenTelemetry / own observability backend [src-001 @ 14:00].

### Deliverables

- [ ] Pipeline diagram + data-flow table (typed I/O)

---

## Workflow D — Acceptance checklist

### Steps

1. Can you swap models without changing application logic? [src-001 @ 18:13]
2. Reproducible run logs in compliant storage? [src-001 @ 18:18]
3. Incident response without calling a hyperscaler? [src-001 @ 18:22]

### Deliverables

- [ ] Signed checklist with owners and evidence links
