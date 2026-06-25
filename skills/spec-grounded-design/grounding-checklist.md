# Grounding Checklist

The reference for Step 2–3. The premise: **docs lag reality.** Reverse-engineered specs,
SDK READMEs, and even official references drift from what the live endpoint actually does.
The probe is what closes the gap — and the rule when they disagree is always the same.

---

## The reality-wins rule

> When the spec and the live endpoint disagree, **the live endpoint is the truth.** Design
> and test against observed behavior, not documented behavior. Record the spec as "stale"
> with the delta — don't silently follow either one.

This is the whole point of the skill. A design built on an assumed spec produces code that
works in theory and breaks on the first real call.

---

## What to verify live (not from the spec)

Probe these for every operation the feature uses — they are where docs are most often wrong
or silent:

| Area | What to capture live |
|------|----------------------|
| **Response shape** | exact field names, casing, nesting, which fields are nullable/omitted |
| **Errors** | force a 401, 404, 429, 5xx — capture the real status, body, and headers |
| **Auth** | token type, header name, scope behavior, what an expired/invalid token returns |
| **State** | session/cursor lifetime; what a *dropped* session returns; how to recover |
| **Pagination** | cursor vs offset, page size limits, what the last page looks like |
| **Rate limits** | the real limit, the headers that report it, the retry-after behavior |
| **Defaults / empties** | what an empty result returns; silent server-side defaults |
| **Idempotency** | does a retry duplicate? is there an idempotency key? |

---

## Probe patterns (smallest safe request)

Use the minimal request that reveals behavior. Read the output before writing code.

```bash
# Happy path — capture the real response shape (note casing, nulls, nesting)
curl -sS -H "Authorization: Bearer $TOKEN" "$BASE/v1/things?limit=1" | jq .

# Force an auth error — capture the REAL error body + status, not the documented one
curl -sS -o /dev/null -w '%{http_code}\n' -H "Authorization: Bearer bad" "$BASE/v1/things"
curl -sS -H "Authorization: Bearer bad" "$BASE/v1/things" | jq .

# Force a not-found / dropped-session — this is where stateful APIs surprise you
curl -sS -i "$BASE/v1/session/does-not-exist" | head -20

# Empty result and last page — the shapes the happy path won't show you
curl -sS -H "Authorization: Bearer $TOKEN" "$BASE/v1/things?q=zzz-no-match" | jq .
```

Adapt to the protocol (a WebSocket/MCP probe is a tiny client script, not curl). The
principle holds: **trigger the real behavior, capture the real output.**

### Safety
- **Never mutate production to "test."** Probe read-only against prod; use a sandbox/test
  tenant for write paths.
- **Never hardcode or save secrets.** Reference `$TOKEN` from the env; keep keys out of the
  contract and the saved output.

---

## Turning the probe into invariants

The output of grounding is not a vibe — it's a set of **invariants** the implementation
must hold, each traceable to an observed behavior:

- "A dropped session returns HTTP 404 with `session not found` → the client re-initializes a
  fresh session; it does **not** trigger reauth." (observed in probe)
- "List returns `{ data: [], next: null }` on empty → treat `next: null` as the only
  end-of-pages signal; `data.length` is not reliable." (observed)
- "429 carries `Retry-After` in seconds → honor it; exponential backoff is the fallback."
  (observed)

Each invariant becomes a test case in the build step. That's how grounding pays off twice:
once preventing the design bug, once seeding the test suite.
