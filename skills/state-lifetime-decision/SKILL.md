---
name: state-lifetime-decision
description: >
  Decide the right home for a new piece of state — its scope (turn, step, chat/thread,
  user-session, user, org, global) and its durability (ephemeral, TTL'd, durable, log) —
  as an explicit product-and-systems decision rather than a default. Forces the
  cross-cutting checks that get missed: per-user/tenant isolation, staleness and
  invalidation, growth/bloat bounds, and the cache implication. Triggers on "where should
  this live", "how long should we keep this", "should this persist", "what's the scope of
  this state", "cache or db or redis", "per chat or per user", "ttl for this", "session vs
  chat scope", "should we remember this". Use when adding or changing stored/remembered
  state in an app or agent — before picking a store.
---

# State-Lifetime Decision

New state has a home whether you choose it or not — and the wrong home is a class of bug
(forgets too soon, leaks across users, grows unbounded, serves stale). **Decide scope ×
durability on purpose, run the four cross-cutting checks, and name the tradeoff.**

Works with any agent. No vendor APIs. Reasons about your app's state and stores.

**Supporting files** (read when needed):
- [decision-grid.md](decision-grid.md) — the scope × durability grid, store mapping, the four checks
- [decision-record-template.md](decision-record-template.md) — the short SDR output format

Output: `{SKILL_OUTPUT_DIR}/state-lifetime-decision/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — Name the state

Establish (infer from the request; ask only if missing):

1. **What is the state** — the thing being remembered (a flag, a result, a set, a token,
   a counter).
2. **Who produces it and who reads it** — and across what boundaries (same step? next turn?
   a different chat? a different device? another user — never).
3. **What breaks if it's missing** — re-work, a re-ask, a wrong answer? This sizes how
   durable it must be.

Resolve output dir per [../OUTPUT.md](../OUTPUT.md). Default `./skill-outputs/state-lifetime-decision/`.

---

## Step 1 — Pick the scope

Read [decision-grid.md](decision-grid.md). Choose the **narrowest scope at which the state
is still useful** — wider than needed leaks and bloats; narrower forgets.

`request/turn` → `step` → `chat/thread` → `user-session` → `user` → `org/tenant` → `global`

The test: "who, exactly, should see this, and for how long does it stay true?" If the
answer is "this user, across their chats, for about an hour" → `user-session` with a TTL.

---

## Step 2 — Pick the durability

Choose how long and how hard it persists, matched to the cost of losing it:

`ephemeral` (in-memory, dies with the process) → `TTL'd` (Redis/cache, expires) →
`durable` (DB, until deleted) → `log/immutable` (append-only, audit).

Cheap to re-derive → ephemeral. Useful for a bounded window → TTL'd (and pick the TTL:
sliding vs fixed). Must survive restarts / is user data → durable.

---

## Step 3 — Run the four cross-cutting checks

These are the ones that get skipped and become incidents:

1. **Isolation** — what key guarantees one user/tenant never sees another's state? Write
   the actual key (e.g. `feature:state:<userId>`). Per-user isolation is not optional.
2. **Staleness & invalidation** — when does this become wrong, and what makes it right
   again (TTL expiry, explicit bust, version stamp)? State with no invalidation story is a
   future stale-data bug.
3. **Growth bound** — can this set/map grow without limit? What caps it (TTL, max size,
   LRU)? "Remember everything" re-creates the bloat you were avoiding.
4. **Cache / cost implication** — does reading or writing it add per-unit work, bust a
   prompt/CDN cache, or add a round-trip? Name it.

---

## Step 4 — Name the tradeoff and write the record

Every scope/durability choice trades something (freshness vs cost, recall vs bloat,
simplicity vs durability). State it in one line. Fill in
[decision-record-template.md](decision-record-template.md) — a short State Decision Record:
what, scope, durability, store, key, invalidation, growth bound, tradeoff. Save it; update
`index.md`.

---

## Step 5 — Output to user

1. The one-line decision: "{state} → {scope} / {durability} in {store}, key `{key}`, {TTL}."
2. The four checks, answered (isolation key, invalidation, growth bound, cache cost).
3. The tradeoff, named.
4. The path to the saved record. Do not implement here — this is the decision input to a
   confirmed build step.

---

## Edge cases

- **"Just cache it"** without a scope — that's the bug this skill prevents; force scope ×
  durability before a store is picked.
- **Cross-device requirement** — rules out `ephemeral` and process-local memory; needs a
  shared store (Redis/DB) keyed by user.
- **Sounds global but is per-user** — most "global" state is actually per-user; double-check
  the isolation key before choosing `global`.
- **Unbounded by nature** (e.g. per-user event history) → `durable` + pagination/retention,
  not a TTL'd set.
- **Security-sensitive state** (tokens, grants) → durable + encrypted at rest + explicit
  invalidation on revoke; never a long-lived ephemeral copy.
- **The decision is actually an architecture fork** (new store, big migration) → hand to
  `architecture-review`.

---

## Invocation examples

```
@state-lifetime-decision the model searched up some tools — where should that live, and for how long?
should this be per-chat or per-user? and what TTL?
where does this go — redis, db, or memory?
how long should we remember the user's last filter?
scope and durability for this draft autosave
```
