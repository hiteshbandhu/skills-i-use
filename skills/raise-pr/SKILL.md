---
name: raise-pr
description: >
  Take a ready change from working tree to merged PR — branch, conventional scoped
  commit, push, open PR with a body drafted from the diff, watch CI, and squash-merge
  when green. Encodes a clean, opinionated PR workflow. Never commits, pushes, or merges
  without explicit confirmation. Triggers on "raise a PR", "open a PR", "pr this",
  "push and pr", "ship this PR", "merge when green", "commit and open a pr".
---

# Raise PR — change → merged PR, cleanly

Drives the whole path from a ready working tree to a squash-merged PR, in a
consistent house style. Pairs with **`ship-check`** (run that first for the
quality gate; this skill handles the git/GitHub mechanics).

**This skill performs outward-facing actions (push, open PR, merge). Confirm
before each: committing, pushing/opening the PR, and merging. Never merge on red
or unverified CI.**

Works with any coding agent that has `git` + `gh` (GitHub CLI, authenticated).

**Supporting files:**
- [pr-body-template.md](pr-body-template.md) — the PR description structure

Output: `{SKILL_OUTPUT_DIR}/raise-pr/` (optional run log) — see [../OUTPUT.md](../OUTPUT.md)

---

## House style (the defaults this skill enforces)

| Thing | Default |
|-------|---------|
| Commit format | Conventional + scoped — `type(scope): summary` (`feat`, `fix`, `chore`, `refactor`, `docs`, `test`) |
| Subject | Specific. Multiple changes → comma-separated list, never "various fixes" |
| Body | What + why, plain prose, 1–3 sentences. Not a bullet wall |
| Co-author trailer | **None** by default |
| Branch | `type/kebab-descriptive`, derived from the change |
| Merge | **Squash**, delete branch, gated on green CI |

These are defaults — read a repo's recent `git log` first and match its actual
convention if it differs (scopes used, trailer presence, merge style).

---

## Step 0 — Preconditions (hard gates)

Refuse to proceed and explain if any fail:

1. **Quality gate** — tests/lint/typecheck should be green. If `ship-check` hasn't
   run this session, run it (or the project's lint + typecheck + test) first. Do
   not open a PR on a known-broken tree.
2. **Not on the default branch** — never commit straight to `main`/`master`.
   If on it, Step 1 creates a branch.
3. **Clean of artifacts** — no screenshots, `skill-outputs/`, build output, `.env`,
   or stray binaries staged. If present, offer to gitignore them; do not commit them.
4. **`gh` authenticated** — `gh auth status` succeeds; remote is GitHub.

---

## Step 1 — Branch

- Read `git log --oneline -8` to learn the repo's actual commit/branch convention.
- If on the default branch, create `type/kebab-descriptive` where `type` matches the
  change and the slug summarizes it (`fix/task-dropdowns-doc-edits`).
- If already on a feature branch, reuse it.

---

## Step 2 — Commit

1. **Derive `type` + `scope`** from the diff:
   - `type`: `feat` (new capability), `fix` (bug), `refactor`, `docs`, `test`, `chore`.
   - `scope`: the dominant top-level area touched (e.g. `tasks`, `matters`, `mcp`).
     Multiple areas → slash-joined (`tasks/mcp/docs`) or the umbrella scope.
3. **Subject**: imperative, specific. If the change does several things, list them
   comma-separated rather than going vague.
4. **Body**: 1–3 sentences — what changed and *why*. Add a co-author trailer only if
   the repo's history uses one.
5. **Show the proposed message and the `git status` and confirm before committing.**

---

## Step 3 — Push + open PR

1. Push the branch (`git push -u origin <branch>`).
2. Draft the PR body from [pr-body-template.md](pr-body-template.md), filled from the
   actual diff and the verification you ran (test counts, Playwright, etc.) — not
   boilerplate. Title = the commit subject (or an umbrella summary for multi-commit).
3. `gh pr create --base <default> --head <branch>`. Show the URL.

---

## Step 4 — Watch CI

- Start `gh pr checks <n> --watch` (background it for long runs).
- On **red**: stop, surface the failing job + log link, do not merge. Offer to fix.
- On **green**: confirm `gh pr view <n> --json mergeStateStatus` is `CLEAN` before Step 5.

---

## Step 5 — Merge (only on explicit go + green CI)

- **Squash-merge + delete branch**: `gh pr merge <n> --squash --delete-branch`.
- If branch protection blocks (required review / pending check): surface exactly why.
  Only use `--admin` when the user owns the repo **and** explicitly approves bypassing.
- After merge: `git checkout <default> && git pull --ff-only`; report the squash commit.

---

## Step 6 — Report

PR URL · CI result · squash commit on default · branch deleted · default synced.
If anything was skipped (e.g. merge held for review), say so plainly.

---

## Why this beats the ad-hoc flow

- **No direct-to-main, no artifact commits, no red merges** — they're hard gates, not vibes.
- **Conventional scope + branch name derived from the diff** — consistent history without thinking about it.
- **PR body written from the real diff + verification** — reviewers get signal, not a template.
- **CI-gated squash-merge** — one clean commit per PR on `main`, every time.

---

## Edge cases

- **No `gh`** — do branch + commit + push; print the PR "create" URL for the user to open manually.
- **Multiple logical changes** — suggest splitting into separate commits/PRs; don't bundle unrelated work.
- **Already-open PR for this branch** — update it (push), don't open a duplicate.
- **Non-GitHub remote** — handle commit/push; PR/merge steps are GitHub-specific, note the limitation.
- **User says "just commit, don't PR"** — stop after Step 2.

---

## Invocation examples

```
raise a PR for this
@raise-pr — squash-merge when CI is green
commit and open a pr, then merge once green
pr this but hold the merge for me
```

## Pair with

- **`ship-check`** — run first for the lint/typecheck/test/secret-scan gate.
- **`ui-ux`** — for UI changes, verify before raising the PR.
