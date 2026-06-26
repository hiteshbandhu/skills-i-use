# Chat Failure Audit — {session label}

**Date:** {YYYY-MM-DD} · **Source:** {url / pasted / session file} · **Goal:** {what the user wanted}

> Findings are grounded in the actual transcript. Symptoms are quoted; causes are the
> system behavior behind them. Sensitive data redacted to the behavior.

## Failure modes

| # | Symptom (observed) | Root cause (system owns) | Layer | Class | Freq | Severity |
|---|--------------------|--------------------------|-------|-------|------|----------|
| 1 | "{quoted symptom}" | {cause} | state/lifetime | state bug | every-time | blocks-task |
| 2 | "{quoted symptom}" | {cause} | retrieval | grounding | recurring | wrong-and-trusted |

Layers: prompt · retrieval · tool/transport · state/lifetime · UX · model-choice
Classes: capability-gap · friction · state-bug · grounding · recovery-gap · ux-dead-end
Freq: one-off · recurring · every-time   Severity: annoyance · blocks-task · wrong-and-trusted

## Fix first (ranked by frequency × severity)

1. **{failure}** — {one line} → handoff: {friction-audit / state-lifetime-decision / …}
2. **{failure}** — {one line} → handoff: {…}

## Notes
- {pattern across multiple failures, if any}
- {anything that needed the real session to see — confidence caveats}

## Handoffs
- Friction → `friction-audit`
- State/lifetime → `state-lifetime-decision`
- Spec/API mismatch → `spec-grounded-design`
- Build-vs-buy / two-mechanism fork → `architecture-review`
