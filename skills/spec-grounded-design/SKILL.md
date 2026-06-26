---
name: spec-grounded-design
description: >
  Before implementing against any protocol, SDK, or external API, ground the design in
  reality — pull the actual spec, probe the live endpoint to capture how it really
  behaves, reconcile spec-vs-reality (reality wins), and extract a design contract of
  verified facts, edge cases, and invariants to build against. Encodes "read the protocol"
  + "test live before assuming the spec is correct," because reverse-engineered or stale
  docs lag the real API. Triggers on "integrate with X", "design against this API",
  "read the protocol first", "before we build this integration", "is the spec right",
  "how does this API actually behave", "ground this in the docs", "verify before coding".
  Use before writing integration code against an external system, not for internal logic.
---

# Spec-Grounded Design

Don't code an integration from memory or from docs you assume are right. **Get the real
spec, probe the real behavior, treat reality as truth, then design against a contract.**
Reverse-engineered and stale specs lag the live API — the live probe is non-negotiable.

Works with any agent that can fetch docs and run a shell. No vendor APIs of its own.

**Supporting files** (read when needed):
- [grounding-checklist.md](grounding-checklist.md) — what to verify live, probe patterns, reality-wins rule
- [design-contract-template.md](design-contract-template.md) — the contract output format

Output: `{SKILL_OUTPUT_DIR}/spec-grounded-design/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — Scope the integration

Establish (ask only if missing):

1. **The target** — which protocol / SDK / API, and which version or endpoint.
2. **What you need from it** — the specific operations the feature requires (not the whole
   surface — ground what you'll actually use).
3. **Probe access** — is there a sandbox/test key/local instance to hit safely? If the only
   instance is production, see the edge cases (read-only, never mutate prod to "test").

Resolve output dir per [../OUTPUT.md](../OUTPUT.md). Default `./skill-outputs/spec-grounded-design/`.

---

## Step 1 — Pull the primary source

Fetch the **actual** spec — the protocol document, the official API reference, the SDK's
typed source — not a blog, not memory, not a summary. Record the version and the URL.

For each operation you need, capture from the spec: the request shape, the response shape,
auth, error codes, pagination, rate limits, and anything stateful (sessions, cursors,
idempotency keys).

Note where the spec is vague or silent — those are exactly the spots the live probe will
resolve.

---

## Step 2 — Probe the live behavior (non-negotiable)

Read [grounding-checklist.md](grounding-checklist.md). Hit the real endpoint with the
smallest possible request — `curl` or a tiny script — and capture **what actually
happens**, not what the spec says should:

- Real response shape and field names (casing, nesting, nulls).
- Real error behavior — force a 401/404/429 and see the actual body and headers.
- Real stateful behavior — session lifetime, what a dropped session returns, cursor format.
- Real edge cases — empty results, large payloads, the silent defaults.

**Read the probe output before writing any code.** This is the step that catches the
spec-vs-reality gap. Show the user the raw probe result.

---

## Step 3 — Reconcile: reality wins

Diff the spec against the probe. For every difference, **the live behavior is the truth**
and the spec is wrong/stale. Record each delta explicitly:

> SPEC says X · REALITY is Y · DESIGN against Y.

If the probe contradicts a core assumption the feature depended on, surface that now — it
may change the design or the feasibility before a line of code is written.

---

## Step 4 — Write the design contract

Fill in [design-contract-template.md](design-contract-template.md): the verified facts per
operation, the spec-vs-reality deltas, the edge cases the code must handle, and the
**invariants** the implementation must preserve (e.g. "a dropped session returns 404 →
re-initialize, do not reauth"). This contract is what you implement against and test
against.

Save it to the output dir; update `index.md`.

---

## Step 5 — Output to user

1. The path to the saved contract.
2. The 1–3 most important spec-vs-reality deltas — the things that would have caused bugs.
3. The invariants the implementation must hold.
4. A go / caution call: is the integration as expected, or did the probe surface something
   that changes the plan?
5. Do not implement here — the contract is the input to a separate, confirmed build step
   (pair with `architecture-review` if the probe revealed a real fork).

---

## Edge cases

- **No sandbox, only production** — probe **read-only** (GET/list), never mutate prod to
  "test." If you must verify a write path, ask the user for a safe test tenant.
- **Auth blocks the probe** — get a scoped test credential from the user; don't skip the
  probe and design blind. A blind design is the failure mode this skill exists to prevent.
- **Spec and reality agree everywhere** — great; record that the contract is spec-verified
  and move on. The probe still paid for itself.
- **The API is undocumented** — the probe *is* the spec; be extra thorough on errors and
  edge cases, and mark the contract "reverse-engineered, verify on upgrades."
- **Secrets** — never write keys/tokens into the contract or the saved output; reference
  them by name.

---

## Invocation examples

```
@spec-grounded-design we're integrating the MCP streamable-HTTP transport — read the protocol and verify before we build
design against the Stripe subscriptions API — is the spec right?
how does this API actually behave on an expired session? probe it first
ground this OAuth flow in the real endpoint before I write the client
verify the pagination behavior live before we design the sync
```
