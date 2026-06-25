# Friction Audit — {flow name}

**Date:** {YYYY-MM-DD} · **Flow:** {what was audited} · **Source:** {code path / transcript / described}

## Actors
- **User:** {what only the user can/should do}
- **System:** {what the system controls}
- **External:** {third-party deps the system can't control}
- **Authority already granted:** {connections / consents / config in place}

## Friction inventory

| # | User does this | Class | Behind a boundary? | Verdict | Why |
|---|----------------|-------|--------------------|---------|-----|
| 1 | {action} | ask-for-permission | none | automate | already authorized |
| 2 | {action} | re-do/re-send | turn | automate | carry state across the turn |
| 3 | {action} | redundant-confirm | none | keep | real delete — keep confirm |

Classes: ask-for-permission · re-do/re-send · manual-recovery · re-discovery · dead-end · redundant-confirm
Verdicts: automate · automate-with-guardrail · keep

## Auto-path designs (ranked: user pain × ease)

### A1 — {friction point}  ·  pain: high · ease: high
- **Trigger:** {event / step boundary / turn that now drives the system to act}
- **Mechanism:** {where the work moves — carry state / self-heal / do in-loop}
- **State:** {none · or → state-lifetime-decision: scope=…, durability=…, isolation=…}
- **Tradeoff:** {the one-line cost and why it's worth it}

### A2 — {friction point}  ·  pain: … · ease: …
- …

## Kept (legitimate friction)
- {point} — {carve-out that applies; why it stays manual}

## Ship first
1. {A1} — {one line}
2. {A2} — {one line}

## Handoffs
- New/changed state → `state-lifetime-decision`
- Build-vs-buy or two-mechanism fork → `architecture-review`
- Symptoms only (no flow) → `chat-failure-audit` first
