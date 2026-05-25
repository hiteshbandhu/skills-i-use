---
name: ship-check
description: >
  Pre-ship gate before commit or push — runs lint, typecheck, tests, build, secret scan,
  and git diff review, then outputs a READY/BLOCKED verdict with a proposed commit
  message. Never commits without explicit user confirmation. Triggers on "ship check",
  "ready to commit", "pre-push check", "commit and push", "ship this", "can I push".
---

# Ship Check — Pre-Ship Gate

Run automated checks + human-readable diff review before any commit or push.
**Never commit or push unless the user explicitly confirms after seeing the report.**

Works with any coding agent with shell access.

**Supporting files:**
- [checklist.md](checklist.md) — manual gate items
- [report-template.md](report-template.md) — output format
- [scripts/ship-check.sh](scripts/ship-check.sh) — automated checks

**Scripts:** read `scripts/ship-check.sh` before running. It executes project lint/test/build
commands — review what it will run in this repo. Double-check every time.

Output: `{SKILL_OUTPUT_DIR}/ship-check/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — Scope

Infer or ask:

| Setting | Default |
|---------|---------|
| Skip build | no — unless user says "skip build" |
| Skip tests | no — unless user says "skip tests" or "quick check" |
| Commit after | only if user confirms after report |
| Push after | only if user explicitly asks **after** commit succeeds |

---

## Step 1 — Collect State

Run in parallel where possible:

```bash
git status
git diff
git diff --cached
git branch --show-current
git log -3 --oneline
```

Then run automated checks:

```bash
bash scripts/ship-check.sh
# Optional: SHIP_CHECK_STRICT=1 bash scripts/ship-check.sh
# Flags: --skip-build --skip-tests
```

If `scripts/ship-check.sh` is not in cwd, locate it from the skill folder or run
equivalent checks manually per [checklist.md](checklist.md).

Review script output: lines prefixed `PASS|`, `WARN|`, `FAIL|`, `DIFF_STAT|`, `SUMMARY|`.

---

## Step 2 — Diff Review

Read [checklist.md](checklist.md). Manually inspect the diff for:

- Scope creep unrelated to the task
- Secrets, tokens, `.env` files
- Debug logging left behind
- Breaking changes without migration notes

Assign verdict:

| Verdict | When |
|---------|------|
| **BLOCKED** | Any `FAIL|` from script, secrets in diff, or broken build/tests |
| **READY WITH WARNINGS** | Warnings only, or user waived a check |
| **READY** | All checks pass, diff looks intentional |

---

## Step 3 — Draft Commit Message

Analyze the full diff. Match the repo's existing commit style (`git log -5`).

Use conventional commits unless the repo uses something else. Focus on **why**, not just what.

---

## Step 4 — Write Report

Fill [report-template.md](report-template.md).

**Path:** `{output_dir}/ship-check-YYYY-MM-DD-HHMM.md`

Update `{output_dir}/index.md`:

```markdown
# Ship Checks

| When | Branch | Verdict | Report |
|------|--------|---------|--------|
```

Append newest first.

---

## Step 5 — Present to User

1. Verdict in one line (READY / READY WITH WARNINGS / BLOCKED)
2. Blockers and warnings (if any)
3. Proposed commit message in a copy-paste block
4. Path to saved report
5. Ask: **"Commit?"** — only proceed on yes
6. Ask: **"Push?"** — only if user wants push, and only after successful commit

If **BLOCKED**, list fixes needed. Do not commit.

---

## Edge Cases

- **Clean working tree** — report READY with note "nothing to commit"
- **Staged + unstaged mix** — show both diffs; ask what to include
- **Monorepo** — run checks from correct package directory or root per project convention
- **No package.json** — rely on checklist + git review; skip Node checks
- **User says "commit anyway"** on BLOCKED — warn once, then follow explicit override
- **Pre-commit hook fails** — fix issue, re-run ship-check, new report (never amend unless user rules allow)

---

## Invocation Examples

```
ship check
ready to commit?
pre-push check
commit and push   ← runs gate first; commit/push only after confirmation
quick ship check — skip tests
ship this branch
```
