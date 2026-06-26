---
name: chat-failure-audit
description: >
  Audit a real user transcript or agent session for failure modes — extract what went
  wrong, map each symptom to its root cause and the system layer that owns it, and rank
  by frequency × severity. Distinguishes symptom from cause (e.g. "it worked on the next
  turn" → root cause is activation not happening in-turn, not "the model is bad") and
  classifies each failure (capability gap, friction, state/lifetime bug, grounding/
  confabulation, recovery gap, UX dead-end). Triggers on "analyse this chat", "what went
  wrong here", "audit this session", "why did the agent fail", "find the failure modes",
  "look at this transcript", "where did this break", "review this conversation". Use when
  you have a real session/log and want grounded failure analysis, not guesses.
---

# Chat Failure Audit

Turn a real transcript into a ranked, root-caused failure list. The discipline:
**ground every finding in the actual session, and always push past the symptom to the
cause and the layer that owns it.**

Works with any agent. No vendor APIs. Reads the transcript/log you provide.

**Supporting files** (read when needed):
- [failure-classes.md](failure-classes.md) — the six failure classes, symptom→cause prompts, severity rubric
- [audit-template.md](audit-template.md) — the failure-mode report format

Output: `{SKILL_OUTPUT_DIR}/chat-failure-audit/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — Get the real session

Establish the source (ask only if missing):

1. **The transcript** — a pasted log, a session file, an exported conversation, or a URL
   the agent can fetch. If it's behind auth and unfetchable, ask the user to paste it.
2. **What "success" was** — what the user was trying to get done. Failures only mean
   something against an intended outcome.

Do not analyse from a summary or from memory — read the actual turns. If you can't see the
real session, say so rather than inventing failures.

Resolve output dir per [../OUTPUT.md](../OUTPUT.md). Default `./skill-outputs/chat-failure-audit/`.

---

## Step 1 — Walk the turns, mark every breakdown

Read the session turn by turn. Mark each point where the outcome diverged from what the
user wanted: a wrong answer, a stall, a re-ask, a tool that failed, a thing the user had
to do twice, an abandonment. Capture the **observable symptom** verbatim — the actual
message or behavior, not your paraphrase.

---

## Step 2 — Symptom → root cause → layer

Read [failure-classes.md](failure-classes.md). For each breakdown, push past the symptom:

> Ask "why" until you hit a cause the system owns. "It worked on the next turn" is a
> symptom; the cause is "activation happens between turns, not within the turn." "The
> model gave a wrong number" may be a grounding failure (bad retrieval), not a model
> failure.

Record: **symptom** (observed) → **root cause** (the system behavior that produced it) →
**layer** (which part owns the fix: prompt, retrieval, tool/transport, state/lifetime,
UX, model choice).

---

## Step 3 — Classify and rate

Tag each with one **failure class**:

- **Capability gap** — the system genuinely can't do the thing yet.
- **Friction** — it can, but made the user do avoidable work (→ hand to `friction-audit`).
- **State / lifetime bug** — state was kept at the wrong scope or dropped across a boundary.
- **Grounding / confabulation** — answered from nothing / stale / wrong source.
- **Recovery gap** — a transient/recoverable error surfaced as a dead-end.
- **UX dead-end** — failed or emptied without offering a next step.

Rate **frequency** (one-off / recurring / every-time) and **severity** (annoyance /
blocks-task / wrong-and-trusted). Wrong-and-trusted outranks everything.

---

## Step 4 — Output to user

Write the report from [audit-template.md](audit-template.md) to the output dir and update
`index.md`. Then in chat:

1. The failure table: symptom → root cause → layer → class → freq × severity.
2. The top failures to fix first, by frequency × severity (not by order of appearance).
3. Explicit handoffs: friction → `friction-audit`; new/changed state →
   `state-lifetime-decision`; protocol/API mismatch → `spec-grounded-design`; big fork →
   `architecture-review`.
4. Do not propose code fixes here — this skill diagnoses; design/implementation is a
   separate, confirmed step.

---

## Edge cases

- **Only a summary, no raw turns** — ask for the real transcript; flag that confidence is
  low without it.
- **One symptom, many causes** — list each cause separately; they may need different fixes.
- **The "failure" is the user's intent being unclear** — that's a real finding (a clarify
  gap), not a model failure; classify as UX dead-end or capability gap.
- **Everything blamed on "the model"** — push harder; most "model failures" are grounding,
  state, or prompt failures the system owns and can fix.
- **Sensitive data in the transcript** — never copy secrets/PII into the saved report;
  redact to the behavior.

---

## Invocation examples

```
@chat-failure-audit analyse this chat: <url or pasted log>
what went wrong in this session — the user gave up at the end
find the failure modes in this agent run
why did this break? push past "the model was wrong"
audit this transcript and rank what to fix first
```
