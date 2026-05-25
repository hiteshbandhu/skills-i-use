# Workflows — Operate agent memory

---

## Workflow A — Diagnose the context death spiral

**Use when:** agent retries after limit errors and context keeps growing.

### Steps

1. Map loop: ingest → spans grow → limit hit → fail → retry with same/heavier payload [src-001 @ 4:08].
2. Confirm whether failures correlate with trace cardinality, not prompt quality [src-001 @ 3:02].
3. Log per-turn token growth and tool-output size [src-001 @ 7:07].

### Agent deliverables

- [ ] Sequence diagram of failure loop
- [ ] Top 3 payload sources (traces, tool JSON, history)

### Stop if

- Root cause is model routing only → still apply Workflow B.

---

## Workflow B — Context vs memory architecture

**Use when:** designing what stays in-window vs external store.

### Steps

1. **Context:** strategic selection for this turn—not max fill [src-001 @ 2:32].
2. **Memory:** persisted segments the agent can re-fetch [src-001 @ 7:48].
3. Treat as product/UX problem: wrong context → bad answers → churn [src-001 @ 3:40].
4. Plan retrieval API: IDs, previews, conversation index [src-001 @ 15:24].

### Agent deliverables

- [ ] Two-column spec: in-window vs store
- [ ] Retrieval tool contract (preview + fetch by id)

### Stop if

- User wants full RAG over corpus → pair with retrieval skill; this skill covers session memory.

---

## Workflow C — Smart truncation + store

**Use when:** implementing Alex-style compression.

### Steps

1. Reject naive head-only truncation [src-001 @ 5:18].
2. Reject blind LLM summarization without retention guarantees [src-001 @ 6:15].
3. Implement head + tail keep (~100 chars each), middle to store [src-001 @ 6:57].
4. Keep latest tool results; do not reset system prompt each compress [src-001 @ 7:13].
5. Allow agent to pull stored segments when follow-up references prior entity [src-001 @ 7:19].

### Agent deliverables

- [ ] Truncation policy doc + pseudocode
- [ ] Test cases: follow-up on “input B” after compress

### Stop if

- Single-turn only app → truncation may suffice without store.

---

## Workflow D — Long-session evals

**Use when:** bugs appear only after many turns.

### Steps

1. Build harness: load 10 turns, assert turn 11 behavior [src-001 @ 9:00].
2. Automate before user reports “agent forgot” [src-001 @ 8:33].
3. Tie eval failures back to truncation policy changes [src-001 @ 13:14].

### Agent deliverables

- [ ] Eval scenario list (10+1 pattern)
- [ ] CI job stub

### Stop if

- Median session < 5 turns and stable → lower priority.

---

## Workflow E — Sub-agent offload

**Use when:** one agent holds chat + heavy search/traces.

### Steps

1. Main agent: light chat + summaries only [src-001 @ 10:24].
2. Sub-agent: heavy queries, span search, intermediate reasoning [src-001 @ 10:32].
3. Return compact result object to main thread [src-001 @ 10:37].
4. Repeat pattern for provider max payload (nested agent-on-agent data) [src-001 @ 11:45].

### Agent deliverables

- [ ] Agent topology diagram
- [ ] Message schema for sub-agent → main handoff

### Stop if

- Data fits in window with filters → defer split.
