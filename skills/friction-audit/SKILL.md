---
name: friction-audit
description: >
  Audit a product flow for friction — every point where the system makes the user do
  work it could do itself — then design the automatic path for each. Classifies friction
  (ask-for-permission, re-do/re-send, manual recovery, re-discovery, dead-end, redundant
  confirmation), decides what should become automatic with a safety carve-out for
  destructive/irreversible/cross-user actions, and names the tradeoff. Triggers on "audit
  this flow", "where's the friction", "why does the user have to", "make this automatic",
  "remove the friction", "this has too much friction", "it should just happen", "reduce
  steps", "the user shouldn't need to". Use when reviewing a UX flow, agent loop, or
  feature for needless user effort — not for visual/styling review (use ui-ux for that).
---

# Friction Audit

Find every place a flow asks the user to do something the system could do itself, then
design the automatic path. The bias: **anything the system can do for the user, it
should — unless it's destructive, irreversible, or crosses a trust boundary.**

Works with any agent. No vendor APIs. Reads the code/flow you point it at.

**Supporting files** (read when needed):
- [friction-taxonomy.md](friction-taxonomy.md) — the six friction classes, the auto-vs-manual rule, the tradeoff prompts
- [audit-template.md](audit-template.md) — the inventory + auto-path report format

Output: `{SKILL_OUTPUT_DIR}/friction-audit/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — Scope the flow

Establish what you're auditing (infer from the request; ask only if missing):

1. **The flow** — a feature, an agent loop, an onboarding path, a described journey, or a
   real transcript (pair with `chat-failure-audit` if you only have symptoms, not a flow).
2. **The actors** — what is the *user*, what is the *system/agent*, what is *external*
   (a third-party API the system can't control).
3. **Authority already granted** — what has the user already connected / consented to /
   configured? Friction often = re-asking for authority the user already gave.

Resolve output dir per [../OUTPUT.md](../OUTPUT.md). Default `./skill-outputs/friction-audit/`.

---

## Step 1 — Walk the flow, mark every user action

Trace the flow step by step. At each step where the **user must act**, record it as a
candidate. For each, capture: what the user does, why the system requires it today, and
what boundary the action sits behind (none / authority / destructive / external).

Read the actual code or transcript — do not infer the flow from memory or docs. If it's
code, follow the real control path (the handler, the prompt, the state writes).

---

## Step 2 — Classify each friction point

Read [friction-taxonomy.md](friction-taxonomy.md). Tag each candidate with one class:

- **Ask-for-permission** — system asks to do something the user already authorized.
- **Re-do / re-send** — user repeats an action because state didn't cross a boundary.
- **Manual recovery** — user reconnects/refreshes/retries what the system could self-heal.
- **Re-discovery** — user or model re-finds something already found.
- **Dead-end** — system fails or stops without offering the next step.
- **Redundant confirmation** — confirmation gating a non-destructive, reversible action.

Not every user action is friction. A deliberate choice, a destructive confirm, or a real
external dependency is **legitimate** — mark those `keep` with the reason.

---

## Step 3 — Decide auto-vs-manual (the safety carve-out)

For each friction point, apply the rule from the taxonomy:

> Make it automatic **unless** the action is destructive, irreversible, crosses a user/
> tenant boundary, spends real money/quota without a cap, or the user genuinely wants the
> choice. Those stay manual — with a confirm or an undo window, not silent.

State the verdict (`automate` / `keep` / `automate-with-guardrail`) and the reason.

---

## Step 4 — Design the automatic path

For each `automate` verdict, design the fix in one short block:

1. **Trigger** — what now causes the system to act (an event, a step boundary, a turn).
2. **Mechanism** — where the work moves (often: carry state across the boundary the user
   was bridging by hand; self-heal instead of surfacing the error; do it in-loop).
3. **State** — if it introduces or changes persisted state, hand off to
   `state-lifetime-decision` (scope × durability × isolation) rather than guessing.
4. **Tradeoff** — name the cost in one line (latency, cache, context bloat, surprise) and
   why it's worth it. No fix is free; say what you're paying.

---

## Step 5 — Output to user

Write the report from [audit-template.md](audit-template.md) to the output dir and update
`index.md`. Then in chat:

1. The friction inventory as a table (point · class · verdict).
2. The top 1–3 auto-paths to ship first, ranked by user pain × ease.
3. Anything you marked `keep` and why (so the user can challenge it).
4. Never edit code or commit here — this skill audits and designs; implementation is a
   separate, confirmed step.

---

## Edge cases

- **Only a transcript, no flow** — run `chat-failure-audit` first to extract failures, then
  audit the flow those failures live in.
- **Everything looks like friction** — you're probably tagging legitimate choices as
  friction; re-check Step 2's `keep` rule. A flow with zero user input is usually wrong.
- **The fix needs new state** — don't inline a scope/TTL guess; defer to
  `state-lifetime-decision`.
- **Big fork in the fix** (build vs buy, two mechanisms) — defer to `architecture-review`.
- **Destructive action with no confirm today** — that's reverse friction (too little); flag
  it, recommend adding a confirm/undo.

---

## Invocation examples

```
@friction-audit our connector-enable flow — why does the user have to re-send?
audit this onboarding path for friction
where's the friction in the agent's tool-calling loop?
this should just happen automatically — find every place it doesn't
remove the friction in document sharing, but keep deletes safe
```
