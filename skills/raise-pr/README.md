# raise-pr

Take a ready change from working tree to a merged PR — cleanly and consistently.

It branches, writes a **conventional scoped commit**, pushes, opens a PR with a body
drafted from the **actual diff + verification**, watches CI, and **squash-merges when
green**. Direct-to-main, artifact commits, and red merges are hard gates, not vibes.

Pairs with **`ship-check`** (run that first for the quality gate) — this skill owns the
git/GitHub mechanics that come after.

## Install

```
npx skills add hiteshbandhu/skills-i-use --skill raise-pr
```

## Use

```
raise a PR for this
@raise-pr — squash-merge when CI is green
pr this but hold the merge for me
```

Invoke with `@raise-pr` in chat or `/raise-pr` in Agent mode.

## Safety

Performs outward-facing actions (push, open PR, merge) — **confirms before each**, and
**never merges on red or unverified CI**. `--admin` bypass of branch protection is used
only when you own the repo and explicitly approve.

## Files

```
raise-pr/
├── SKILL.md
├── pr-body-template.md
└── README.md
```

## Pair with

- **`ship-check`** — lint/typecheck/test/secret-scan gate before you raise.
- **`ui-ux`** — verify UI changes before the PR.
