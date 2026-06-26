# State Decision Grid

The reference for Step 1–3. State is a **product decision wearing a systems costume**:
where it lives and how long it lasts directly shapes what the user experiences (does it
remember me? across chats? on my other device? did it leak?). Decide it on purpose.

---

## Axis 1 — Scope (who sees it, for how long it's true)

Pick the **narrowest scope at which the state is still useful.** Too wide leaks and
bloats; too narrow forgets and forces re-work.

| Scope | Lives across | Typical use | Watch out |
|-------|--------------|-------------|-----------|
| **request / turn** | one request or agent turn | intermediate compute, this-turn flags | gone next turn — fine if that's intended |
| **step** | steps within one turn | mid-turn activation, loop state | invisible to the next message |
| **chat / thread** | turns of one conversation | conversation context, per-chat enablement | doesn't follow the user to a new chat |
| **user-session** | a user's chats for a window | "remember this for the next hour, anywhere" | needs a TTL and a per-user key |
| **user** | everything a user does, indefinitely | preferences, connections, their data | must be durable + isolated |
| **org / tenant** | everyone in an org | shared config, team resources | isolation is now a security boundary |
| **global** | all users | catalogs, feature flags, models | rarely what you want — verify it's truly shared |

The test question: *"Who, exactly, should see this — and how long does it stay true?"*
The answer maps almost directly onto a row.

---

## Axis 2 — Durability (how hard it persists, matched to cost-of-loss)

| Durability | Where | Survives | Use when |
|------------|-------|----------|----------|
| **ephemeral** | in-process memory | nothing (dies with the process) | cheap to re-derive, single-process, this-run only |
| **TTL'd** | Redis / cache | restarts, until expiry | useful for a bounded window; auto-expiry is the point |
| **durable** | database | until deleted | user data, must survive restarts, queryable |
| **log / immutable** | append-only store | forever, audit | events, history, things you never overwrite |

Rule of thumb: **cheap to re-derive → ephemeral; useful for a window → TTL'd; user data or
must-survive-restart → durable.**

### TTL choice (for TTL'd state)
- **Sliding** (refresh on each use) → "active session stays warm, idle expires." Good for
  session-scoped recall.
- **Fixed** (expire N after write) → "valid for exactly N regardless of use." Good for
  caches with a known freshness window.

---

## Scope × durability → store

| | ephemeral | TTL'd | durable |
|---|---|---|---|
| **turn/step** | local variable ✓ | (rarely) | (no) |
| **chat/thread** | in-memory map | Redis keyed by chatId | DB row per chat |
| **user-session** | (no — needs to cross requests) | **Redis keyed by userId + TTL** ✓ | DB + last-seen |
| **user / org** | (no) | cache in front of DB | **DB, isolated by user/org** ✓ |
| **global** | process cache | CDN/Redis | DB / config |

The bolded cells are the common, correct homes.

---

## The four cross-cutting checks (where incidents come from)

Run all four — these are the ones that get skipped:

### 1. Isolation
Write the **actual key**. `feature:state:<userId>` — not `feature:state`. The key is the
proof that user A never reads user B's state. For org scope, the tenant id is a security
boundary, not a convenience. **Per-user isolation is never optional.**

### 2. Staleness & invalidation
When does this state become *wrong*, and what makes it right again?
- TTL expiry (time-based), explicit bust (on the event that invalidates it), or a version
  stamp (compare-and-refresh).
- State with **no** invalidation story is a future stale-data bug. Name the story.

### 3. Growth bound
Can it grow without limit? A per-user set that only ever adds members will bloat.
- Bound it: a TTL, a max size, an LRU, or retention/pagination for durable history.
- "Remember everything forever" re-creates the very cost (context bloat, slow reads) you
  were trying to avoid.

### 4. Cache / cost implication
Does touching this state add work?
- A per-turn read/write, a round-trip, a busted prompt cache or CDN cache.
- Often acceptable — but **name it** so the tradeoff is a choice, not a surprise.

---

## Naming the tradeoff

Every choice trades something. Say it in one line:

- **Narrow scope** → less leak/bloat, but more re-derivation (more round-trips/re-asks).
- **Wide scope / long TTL** → better recall, but more staleness risk and more bloat.
- **Ephemeral** → fast and simple, but forgets on restart and can't cross processes.
- **Durable** → survives and is queryable, but costs a write and a migration and must be
  isolated and invalidated.

A good decision makes the tradeoff small and bounded. If it's large, the choice may be an
architecture fork — hand to `architecture-review`.
