# Design Contract — {target API/protocol}

**Date:** {YYYY-MM-DD} · **Target:** {name} · **Version:** {spec version} · **Spec URL:** {url}
**Probe access:** {sandbox / test tenant / prod read-only}

> Live behavior is the source of truth. Where the spec disagreed, this contract follows
> reality. No secrets recorded — credentials referenced by name.

## Operations used

### {operation 1 — e.g. list things}
- **Request:** {method, path, params that matter}
- **Response (verified):** {real shape — field names, casing, nullability, from the probe}
- **Auth:** {token type, header, scope}
- **Errors (verified):** {real bodies/status for 401/404/429/5xx}
- **Stateful:** {session/cursor behavior, what a drop returns}

### {operation 2}
- …

## Spec-vs-reality deltas

| # | Spec says | Reality is | Design against |
|---|-----------|------------|----------------|
| 1 | {documented} | {observed} | {reality} |

(If none: "Spec verified against live behavior — no deltas.")

## Edge cases the code must handle
- {empty result shape}
- {dropped session / expired token recovery}
- {last page / pagination end signal}
- {rate-limit / retry behavior}

## Invariants (→ become test cases)
1. {invariant traceable to an observed behavior}
2. {…}

## Verdict
- **Go / Caution:** {is it as expected, or did the probe change the plan?}
- **Open questions:** {anything the probe couldn't resolve — what's needed to close it}

## Handoffs
- Real build-vs-buy or two-mechanism fork surfaced by the probe → `architecture-review`
- New persisted state in the integration → `state-lifetime-decision`
