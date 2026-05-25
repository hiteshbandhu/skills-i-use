# Workflows — Build agent harnesses

Read the matching section when the user's goal matches the decision tree in [SKILL.md](SKILL.md).

---

## Workflow A — Harness fundamentals (guardrails + verify)

**Use when:** defining or hardening a runtime around a model (browser, API, internal tools).

### Steps

1. Inventory harness parts: tool registry, model slot, context management, guardrails, loop, **verify** [src-001 @ 4:36]
2. Add guardrails before prompt changes: max steps, max messages, compression policy [src-001 @ 10:22]
3. Implement deterministic **verify** on tool/environment trace (not model self-report) [src-001 @ 13:24]
4. Put secrets/recovery (login, retries) in harness code, not system prompt [src-001 @ 15:40]
5. Optional: outer retry loop (`runHarness` × max attempts) around inner agent attempt [src-001 @ 13:59]

### Agent deliverables

- [ ] Harness component diagram
- [ ] Guardrail table (limit, action on breach)
- [ ] Verify function spec + failure codes

### Stop if

- Team only tunes prompts while agent lies about success [src-001 @ 9:37]

---

## Workflow B — Agent vs workflow gate

**Use when:** choosing autonomy level for a new product feature.

### Steps

1. Map decision tree — if mappable, prefer explicit workflow [src-002 @ 3:11]
2. Check token budget vs task value (e.g. 30–50k tokens per support ticket) [src-002 @ 3:35]
3. Derisk critical capabilities (write, debug, recover) on pilot trajectories [src-002 @ 4:02]
4. Assess error cost + discoverability; scope read-only/HITL if high stakes [src-002 @ 4:34]
5. If agent: keep environment + tools + system prompt minimal first [src-002 @ 5:54]

### Agent deliverables

- [ ] Checklist scored for the use case
- [ ] Chosen pattern (workflow / agent / hybrid) with explicit non-goals

---

## Workflow C — Build maturity ladder

**Use when:** going from prototype to org-scale coding agents.

### Steps

1. Level 1 — framework spike for PMF (hours, not months) [src-003 @ 3:02]
2. Level 2 — own state machine; minimal prompts; CLI-testable agent [src-003 @ 4:37], [src-003 @ 7:24]
3. Human-designed architecture before model-generated code rip [src-003 @ 9:09]
4. Level 3 — Kanban UX for parallel inference-bound runs [src-003 @ 11:28]
5. Level 4 — cloud agents for long QA and shared env [src-003 @ 14:24]
6. Validate reasoning-trace API formats per provider [src-003 @ 10:13]

### Agent deliverables

- [ ] Current level + next level plan
- [ ] State machine diagram for level 2+

---

## Workflow D — Enterprise platform (scale, quotas, skills)

**Use when:** many users/agents inside a large org or product surface.

### Steps

1. Decompose monolith into specialists + horizontal guardrails/eval [src-005 @ 15:02], [src-005 @ 17:41]
2. Semi-agentic slices: autonomous where trusted, coded guardrails always on [src-005 @ 9:03]
3. Per-user/team token quotas; model tiering (small/local vs frontier) [src-004 @ 8:20]
4. Skills library with curation/Darwinian pruning [src-004 @ 6:05]
5. Mock/light harness eval without full GPU burn [src-004 @ 9:12]
6. Customer/agent ADLC: transcript QA + forward-deployed iteration [src-007 @ 12:18]

### Agent deliverables

- [ ] Agent topology (specialists + shared services)
- [ ] Quota + model routing policy
- [ ] Skills governance rules

---

## Workflow E — Evaluation & trust

**Use when:** proving agents work before launch or auditing vendor claims.

### Steps

1. Build environment-based eval (actions), not single-shot I/O [src-006 @ 7:52]
2. Domain benchmarks with verifiers (reproduction, legal fidelity, etc.) [src-006 @ 4:48]
3. Finance/knowledge: scope behaviors; simple tools; vertical workflows [src-008 @ 5:48], [src-008 @ 11:13]
4. Monitor published outputs with remediation/circuit breakers [src-005 @ 8:13]
5. Watch reward hacking / LLM-judge-only demos [src-006 @ 6:49]

### Agent deliverables

- [ ] Eval harness outline + pass thresholds
- [ ] Failure taxonomy (lie, drift, tool error, env error)

---

## Workflow F — Long-horizon research harness

**Use when:** multi-minute web/deep research agents.

### Steps

1. Editable plan card before run; async expectations [src-009 @ 3:22]
2. Live transparency (sites browsed / thoughts) [src-009 @ 4:01]
3. Artifact report + follow-up Q&A pinned [src-009 @ 4:35]
4. Checkpoint state; recover from partial failures [src-009 @ 6:17]
5. Planner handles partial info, parallel subtasks, entity resolution [src-009 @ 7:31]
6. Context policy: recency + compressed notes/RAG for older tasks [src-009 @ 11:30]
7. Generalize pipeline via shared filesystem between stages [src-004 @ 5:14]

### Agent deliverables

- [ ] Research state machine + persistence layout
- [ ] UX wire for plan → progress → artifact

---

## Workflow G — Coding / computer-use harness

**Use when:** IDE agents, bash/browser tools, long coding loops.

### Steps

1. Separate agent definition from transport/streaming [src-012 @ 10:47]
2. Sandbox bash/browser; trajectory or step visibility [src-011 @ 8:19], [src-012 @ 56:29]
3. `prepareStep` or equivalent per-step context pruning [src-012 @ 37:56]
4. Accept/reject diffs; terminal integration; web search + repo context [src-011 @ 3:35]
5. Antigravity-style: plan review, DOM/browser verify, scratchpad trace [src-004 @ 4:06]

### Agent deliverables

- [ ] Tool list + sandbox boundaries
- [ ] Context pruning rules per step band
- [ ] Human review points in loop

---

## Workflow H — Durable session UX

**Use when:** chat/copilot products with mobile, multi-tab, or interruptible agents.

### Steps

1. Identify failures of direct SSE (drop = lost stream) [src-015 @ 4:36]
2. Insert durable session bus between agents and clients [src-015 @ 5:25]
3. Resume streams from cursor; buffer events while disconnected [src-015 @ 6:10]
4. Sync session across tabs/devices [src-015 @ 3:46]
5. Allow steer/interrupt while agent works [src-015 @ 4:07]

### Agent deliverables

- [ ] Session/event schema
- [ ] Reconnect + steer sequence diagram

---

## Workflow I — Multi-agent ops (FOMAT)

**Use when:** running many coding agents in parallel.

### Steps

1. Central pane for all sessions (Claude, Codex, Cursor, etc.) [src-013 @ 3:36]
2. Push notify on blocked/finished [src-013 @ 11:59]
3. Remote start/monitor from phone/web [src-013 @ 4:44]
4. Daily digest of agent activity [src-013 @ 10:17]
5. Pair with Kanban isolation per task [src-003 @ 12:16]

### Agent deliverables

- [ ] Ops dashboard requirements
- [ ] Alert rules for blocked > N minutes

---

## Workflow J — Domain-vertical harness

**Use when:** healthcare, finance, voice, games, canvas — expert grounding required.

### Steps

1. Embed domain experts in eval rubric + iteration [src-016 @ 7:26]
2. External verifier (engine, ledger, phone tree) before narrative LLM [src-019 @ 8:42], [src-008 @ 4:12]
3. Voice: prescriptive design → call recording eval; own realtime stack [src-018 @ 11:08]
4. Canvas/spatial tools with shared visual state [src-020 @ 10:24]
5. Constrain scope; vertical workflows over raw chat [src-008 @ 7:33]

### Agent deliverables

- [ ] Domain verifier integration spec
- [ ] Expert review loop in harness

---

## Workflow K — Scaffold deletion / compute-forward backend

**Use when:** migrating rigid pipelines to LLM-led systems.

### Steps

1. List scaffolding added for weak models; delete as capability rises [src-010 @ 1:07]
2. Prefer parallel LLM+verifier over hand-written parsers when engineer time scarce [src-010 @ 7:01]
3. Architect for more blue-arrow (LLM) share of backend [src-010 @ 10:17]
4. Keep classical escapes (code exec, SQL) inside agent tools [src-010 @ 8:58]

### Agent deliverables

- [ ] Before/after architecture (rigid vs compute-forward)
- [ ] Cost model: engineer time vs inference

---

## Workflow L — Post-training & finetune

**Use when:** prompt/RAG plateau on high-volume vertical agent.

### Steps

1. Baseline prompts + retrieval; measure hallucination taxonomy [src-014 @ 7:07]
2. Define accuracy/latency SLO before finetune [src-014 @ 9:41]
3. Use teacher model to label for smaller deploy model [src-014 @ 14:56]
4. Plan RL/verifiers for multi-step tools (longer horizon) [src-017 @ 10:03]
5. Co-creation/creative: post-train for long horizon + collaboration [src-021 @ 8:22]

### Agent deliverables

- [ ] Finetune gate checklist (only if metrics justify)
- [ ] Roadmap: prompt → finetune → RL

### Stop if

- No labeled eval set exists [src-014 @ 13:59]
