# Ship Check

Pre-ship gate before commit or push. Runs automated checks, reviews your diff, drafts
a commit message, and gives a **READY / BLOCKED** verdict.

**Never commits or pushes without your explicit confirmation.**

Output: `./skill-outputs/ship-check/`

## Scripts

This skill includes `scripts/ship-check.sh`. **Read the script before running it.**
It runs your project's lint, typecheck, test, and build commands plus git checks. Review
what it executes in your repo — do not run blindly.

## What it checks

| Layer | Checks |
|-------|--------|
| **Automated** | lint, typecheck, tests, build, secret grep, `.env` in git status |
| **Manual review** | scope creep, debug code, diff quality |
| **Output** | verdict + proposed commit message + saved report |

## Usage

```
@ship-check
ready to commit?
commit and push        ← gate runs first; you confirm before anything ships
quick ship check — skip tests
```

## Verdicts

| Verdict | Meaning |
|---------|---------|
| **READY** | Safe to commit |
| **READY WITH WARNINGS** | Your call |
| **BLOCKED** | Fix first |

## Files

```
ship-check/
├── SKILL.md
├── checklist.md
├── report-template.md
└── scripts/ship-check.sh
```

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
