# Failure Classes

The reference the skill reads in Step 2–3. The whole point is to **stop blaming the
symptom (or "the model") and name the cause the system actually owns** — because that's
the thing you can fix.

---

## Symptom is not cause

The most common mistake in failure analysis is recording the symptom and stopping. Push
past it with "why" until you reach a system behavior:

| Symptom (observed) | Lazy read | Real root cause |
|--------------------|-----------|-----------------|
| "It worked on the next turn" | flaky model | the dependent work happens *between* turns, not *within* the turn |
| "The agent gave a wrong number" | model hallucinated | retrieval returned a stale/wrong source (grounding) |
| "User had to send the message twice" | user error | state didn't carry across the turn boundary (state/lifetime) |
| "It asked me to reconnect" | expected | a recoverable session error surfaced as a user task (recovery gap) |
| "It re-searched the same thing" | normal | the prior result wasn't remembered at the right scope (re-discovery) |
| "It said no results and stopped" | nothing there | the empty path wasn't designed (UX dead-end) |

Rule: a cause you can't act on isn't a root cause yet. "The model is bad" is never a root
cause — pin it to prompt, retrieval, tooling, state, or UX.

---

## The six classes

### Capability gap
The system genuinely cannot do the thing yet — no tool, no data, no integration.
- *Fix owner*: roadmap / build. Don't paper over with a prompt.
- *Careful*: many "capability gaps" are actually friction or grounding in disguise. Confirm
  the capability is truly absent.

### Friction
The system *can* do it, but made the user do avoidable work.
- *Fix owner*: → **`friction-audit`** (classify and design the automatic path).
- *Tell*: re-send, re-enable, reconnect, re-confirm, re-ask.

### State / lifetime bug
State was kept at the wrong scope, or dropped across a boundary (turn, request, session).
- *Fix owner*: → **`state-lifetime-decision`** (pick the right scope × durability).
- *Tell*: "worked next turn", "forgot what I just told it", "lost it when I switched chats".

### Grounding / confabulation
The system answered from nothing, from stale data, or from the wrong source.
- *Fix owner*: retrieval / source plumbing / citations — not the model.
- *Tell*: confident wrong facts, dropped sources, answers with no basis.

### Recovery gap
A transient or recoverable error (expired session, transient 5xx, stale client) was
surfaced to the user instead of being healed.
- *Fix owner*: the transport/error layer — classify recoverable vs hard, auto-heal the
  first.
- *Tell*: "reconnect", "try again", a dead session the user revives by hand.

### UX dead-end
The system failed or emptied without offering a next step.
- *Fix owner*: design the error/empty paths, not just the happy path.
- *Tell*: bare error, empty state, "no results" with nowhere to go.

---

## Severity rubric

Rate each failure so the fix order is by impact, not by where it appeared in the log.

| Severity | Meaning | Examples |
|----------|---------|----------|
| **wrong-and-trusted** | system was confidently wrong and the user would act on it | confabulated fact, wrong legal/financial output presented as sure |
| **blocks-task** | the user could not complete what they came to do | tool dead, hard loop, abandonment |
| **annoyance** | completed, but with avoidable effort/delay | re-send, redundant confirm, slow round-trip |

**wrong-and-trusted outranks everything** — a smooth flow that gives a confident wrong
answer is worse than a clunky flow that's correct.

Frequency multiplies severity: `every-time × blocks-task` is a fire; `one-off × annoyance`
is a note. Rank the fix list by frequency × severity.

---

## Handoffs

This skill **diagnoses**; it does not design or implement. Route findings:

- Friction → `friction-audit`
- State/lifetime → `state-lifetime-decision`
- Protocol/API behavior didn't match expectations → `spec-grounded-design`
- A fix with a real build-vs-buy or two-mechanism fork → `architecture-review`
