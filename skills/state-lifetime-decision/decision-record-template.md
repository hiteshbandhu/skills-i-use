# State Decision Record — {state name}

**Date:** {YYYY-MM-DD} · **State:** {what is being remembered} · **Feature:** {where it's used}

## Decision (one line)
{state} → **{scope}** / **{durability}** in **{store}**, key `{key}`, TTL `{sliding/fixed N | n/a}`.

## Producers & readers
- **Produced by:** {who writes it, on what event}
- **Read by:** {who reads it, across what boundary — turn / chat / session / device}
- **Cost if missing:** {re-work / re-ask / wrong answer — sizes the durability}

## Scope & durability
- **Scope:** {turn / step / chat / user-session / user / org / global} — *why this is the
  narrowest useful scope:* {reason}
- **Durability:** {ephemeral / TTL'd / durable / log} — *why:* {reason}

## The four checks
| Check | Answer |
|-------|--------|
| **Isolation** | key = `{actual key}` — guarantees per-{user/tenant} separation |
| **Staleness & invalidation** | {TTL expiry / explicit bust on <event> / version stamp} |
| **Growth bound** | {TTL / max size / LRU / pagination — what caps it} |
| **Cache / cost** | {per-turn read? round-trip? busts which cache? — or "none"} |

## Tradeoff
{the one-line cost of this choice and why it's worth it}

## Handoff
- New store / migration / big fork → `architecture-review`
