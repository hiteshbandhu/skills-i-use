# PR body template

Fill from the **actual diff and verification you ran** — not boilerplate. Drop any
section that doesn't apply. Keep it scannable; reviewers read the first screen.

```markdown
## Why

[1–2 sentences: the problem or goal. Link the issue/report if there is one.]

## What changed

- [the substantive changes, grouped by area — match the commit scope(s)]
- [call out anything removed or migrated, not just additions]

## Verification

- [tests: N passing / new cases added]
- [typecheck/lint clean]
- [manual / Playwright: what you actually checked, incl. before/after if UI]

## Notes / risk

[Optional: follow-ups, deliberate trade-offs, anything a reviewer should watch.]
```

## Rules

- **Title** = the commit subject (conventional, scoped). For a multi-commit PR, an
  umbrella summary in the same style.
- **No invented verification.** If you didn't run it, don't claim it.
- Match the repo's existing PR voice if it has one (check a recent merged PR).
- Trailers (e.g. generated-with) only if the repo's PRs use them.
