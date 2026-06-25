# Friction Taxonomy

Friction is **any point where the system makes the user do work it could do itself.**
The goal of the audit is to find each one, decide whether it should be automatic, and —
if so — design the path. This file is the reference the skill reads in Step 2–3.

---

## The six classes

### 1. Ask-for-permission
The system stops to ask the user to approve an action the user **already authorized**.

- *Tell*: a confirmation/consent prompt for something the user connected, enabled, or
  configured earlier. "Shall I use your connected Gmail?" — they connected it; just use it.
- *Root*: the system treats standing authority as per-action authority.
- *Fix shape*: act on the standing grant; only re-ask if the grant is gone or the scope
  genuinely widened.

### 2. Re-do / re-send
The user repeats an action because **state didn't cross a boundary** the system drew.

- *Tell*: "send your message again", "re-run it now that X is on", do-it-twice.
- *Root*: a turn / request / session boundary dropped state that was valid across it.
- *Fix shape*: carry the state across the boundary, or do the dependent work in the same
  unit (same turn, same request) so the user never sees the seam.

### 3. Manual recovery
The user must reconnect / refresh / retry something the system **could self-heal**.

- *Tell*: "reconnect your account", "refresh and try again", a dead session the user must
  revive by hand.
- *Root*: the system surfaces a transient/recoverable error as a user task.
- *Fix shape*: distinguish recoverable (expired session, transient 5xx, stale client) from
  truly-hard (revoked grant, deleted resource); auto-heal the first class, only prompt on
  the second.

### 4. Re-discovery
The user **or the model** re-finds something already found.

- *Tell*: re-searching the same tools, re-asking what was answered, re-loading the same
  context every turn.
- *Root*: a discovery result wasn't remembered at the right scope.
- *Fix shape*: persist the result at the scope it stays useful (hand to
  `state-lifetime-decision`) so it's there next time without the round-trip.

### 5. Dead-end
The system fails or stops **without offering the next step**.

- *Tell*: a bare error, an empty state with no action, "no results" with no path forward.
- *Root*: error/empty paths weren't designed, only the happy path.
- *Fix shape*: every failure and empty state names the next action (retry, alternative,
  who to contact, what to connect).

### 6. Redundant confirmation
A confirm gates a **non-destructive, reversible** action.

- *Tell*: "Are you sure?" for something trivially undoable.
- *Root*: confirmation used as a generic safety blanket instead of for real risk.
- *Fix shape*: drop the confirm; if you want safety, prefer an undo window over a
  pre-action prompt.

---

## The auto-vs-manual rule

> **Make it automatic — unless** the action is **destructive** (deletes/overwrites data),
> **irreversible** (can't be undone), **crosses a boundary** (another user, tenant, or
> external party's data), **spends real money or quota without a cap**, or the user
> **genuinely wants the choice** (a real decision, not a rubber stamp).
>
> Those stay manual — but with a **confirm or an undo window**, never a silent surprise.

Three verdicts:

| Verdict | When | Example |
|---------|------|---------|
| `automate` | none of the carve-outs apply | use the already-connected tool; self-heal the expired session |
| `automate-with-guardrail` | mostly safe but spends/changes something | auto-send but cap volume; auto-apply but keep an undo |
| `keep` | a carve-out applies, or it's a real choice | deleting a document; choosing which account to post from |

A `keep` is not a failure of the audit — calling out the *legitimate* friction is part of
the value. But always state *why* it's kept so it can be challenged.

---

## Naming the tradeoff

No automation is free. For every `automate`, state the cost in one line so the user
decides with eyes open:

- **Latency** — does the auto-path add a round-trip or a probe?
- **Cache / cost** — does it bust a cache or add per-turn work?
- **Context bloat** — (agent flows) does carrying state grow the active set every turn?
- **Surprise** — does acting without asking risk doing the wrong thing? How is that bounded?
- **Staleness** — if you remember a result, when is it wrong, and how does it expire?

A good auto-path makes the tradeoff small and bounded. If the tradeoff is large, that's a
signal it may belong in `architecture-review`, not a quick automation.

---

## Anti-patterns (don't do these in the name of "less friction")

- **Silent destructive action** — removing a confirm from a real delete. That's not less
  friction, that's a data-loss bug.
- **Guessing on the user's behalf for a real decision** — automating a genuine choice
  produces confident wrong answers.
- **Hiding errors to look smooth** — self-heal the recoverable, but a truly-hard failure
  must still surface, with the next step.
- **Unbounded memory** — "remember everything" re-bloats the very thing you were trimming.
  Persist at a scope with a bound and a TTL.
