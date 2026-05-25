# Ship Check — Gate Checklist

Read during Step 1. Every item must pass or be explicitly waived by the user.

## Git hygiene

- [ ] Changes are intentional — user reviewed `git diff`
- [ ] No `.env`, credentials, or API keys in the diff
- [ ] No debug `console.log` / `print` left in hot paths (unless intentional)
- [ ] No commented-out blocks of old code without reason
- [ ] Branch is correct (not accidentally on `main` for WIP — warn if so)

## Automated checks (via `scripts/ship-check.sh`)

- [ ] Lint passes (or waived with reason)
- [ ] Typecheck passes (or waived with reason)
- [ ] Tests pass (or waived with reason)
- [ ] Build passes (or waived with reason)

## Diff quality

- [ ] Diff scope matches stated intent — no drive-by refactors
- [ ] New dependencies are justified
- [ ] Migrations / schema changes are noted in commit body if present

## Commit message

Draft using conventional commits when the repo already uses them:

```
type(scope): imperative summary

Why this change. What was verified. Any follow-ups.
```

Types: `feat`, `fix`, `refactor`, `docs`, `test`, `chore`, `perf`

## Ship decision

| Verdict | Meaning |
|---------|---------|
| **READY** | All checks pass — safe to commit (and push if user asks) |
| **READY WITH WARNINGS** | Non-blocking issues noted — user decides |
| **BLOCKED** | Must fix failures before commit |

Never commit or push without explicit user confirmation after presenting the report.
