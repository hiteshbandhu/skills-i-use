---
name: cross-model-review
description: >
  Review a PR or working diff twice — once with the primary model, then again with a
  different vendor's model that is told nothing about the first pass — then verify the
  second model's claims against real code and reconcile both into one ranked review.
  Catches the class of bug a single model is systematically blind to. Triggers on
  "cross-model review", "second opinion on this PR", "review this with another model",
  "double-check this review", "have another model look at it", "blind review".
  Use when being wrong is expensive: unfamiliar code, an outside contributor's PR, or
  anything touching auth, money, migrations, or data loss.
---

# Cross-Model Review — Two Models, One Reconciled Verdict

A single model reviews a diff with a single set of blind spots. Running a second model
from a **different vendor**, with **no knowledge of the first review**, surfaces findings
the first pass structurally could not reach — and independently re-rates severity the
first pass got wrong.

The value is not "two reviews." It's that the overlap is *earned*: when both models
independently land on the same finding, that is corroboration. When only one does, that
is a lead to verify — never a finding to publish.

**Output:** `{SKILL_OUTPUT_DIR}/cross-model-review/` — see [../OUTPUT.md](../OUTPUT.md)

---

## When NOT to use this

Skip it and just review normally when:

- The diff is small and self-evident (config bumps, copy changes, dependency pins)
- You wrote the code yourself and already know where the bodies are
- The PR is already blocked on something else — don't spend a second pass on a moving target
- You need an answer in under two minutes

Running this on every trivial PR turns a real technique into ceremony, and the
reconciliation step stops getting the attention that makes it work.

---

## Step 0 — Establish the target and the scope

| Target | How to get the diff |
|--------|---------------------|
| GitHub PR | `gh pr view <n> --json title,body,author,baseRefName,headRefName,additions,deletions,changedFiles` + `gh pr diff <n>` |
| Local branch | `git diff <base>...HEAD` |
| Working tree | `git diff` and `git diff --staged` |

**The diff is the review scope.** For a PR, local working-tree changes are out of scope —
say so if the checkout is dirty.

Save the diff to the output dir so both passes review byte-identical input.

**Checkout mismatch matters.** If reviewing a PR while the local checkout is on another
branch, do not read local files as if they were the PR's. Fetch the PR's version:

```bash
gh api "repos/<owner>/<repo>/contents/<path>?ref=<head-branch>" --jq '.content' | base64 -d
```

Getting this wrong silently reviews the wrong code — it is the most common failure here.

---

## Step 1 — Primary review (you)

Review the diff yourself, first, before involving any other model. Produce findings with
file:line, a concrete failure scenario, and a severity.

Do this first for a reason: if you run the second model first, you anchor on its findings
and lose the independence the whole method depends on.

Read surrounding code for anything the diff doesn't make self-contained. A diff hunk shows
what changed, not what it breaks.

---

## Step 2 — Pick the second model

It must be a **different vendor** from the primary. Probe what is actually available —
never assume a CLI is installed or a model ID still exists:

```bash
for c in agent codex claude; do printf "%s: " "$c"; command -v "$c" || echo "not found"; done
```

Then list models for whichever exists (e.g. `agent models`, or the CLI's `--list-models`).

**Preference order** (use the first that is available):

1. `gpt-5.6-sol-low` or `gpt-5.6-sol-medium` — the calibrated default
2. Any other model from a vendor different to the primary
3. No cross-check available → see Step 5

Model IDs age out fast. Treat the names above as preference, not requirement — resolve
against the live list every run rather than hardcoding.

---

## Step 3 — Blind second review

Run the second model with **no knowledge of the first review**. Do not paste your
findings, do not hint at areas of concern, do not ask it to "confirm" anything. A leading
prompt produces agreement, and agreement you induced is worth nothing.

Run read-only where the CLI supports it (e.g. `--mode plan`), and print to stdout:

```bash
agent -p --model <resolved-model> --mode plan "Review <target> in this repo.

Get the diff yourself with <the commands from Step 0>. Read surrounding files for
context where the diff isn't self-contained. Note: the checkout is on <branch>, so for
files this change touches, fetch the change's version rather than reading local ones.

Give a rigorous code review. Prioritise:
- Actual bugs and broken behaviour a user would hit
- Logic that looks right but isn't
- Missing or misleading test coverage
- Security issues
- Places where the UI and the underlying state disagree

Cite file and line. Rank by severity. Don't pad with praise or generic advice. If
something looks wrong but you verified it's fine, say so briefly."
```

Give it a generous timeout — a real review takes minutes, and a truncated one is worse
than none.

---

## Step 4 — Verify, then reconcile

**Verify before you believe anything.** This is the step that makes the skill work, and
the step most likely to get skipped. A second model states wrong findings with exactly the
same confidence as right ones.

For every finding the second model raised that you did not:

1. Open the actual code it cites — not the diff, the file
2. Confirm the claim mechanically (does that alias really exist? does that filter really
   drop the whole entry?)
3. Only then accept it

Discard anything that doesn't survive. Do not publish a finding you have not personally
confirmed, no matter how plausible it reads.

Then sort everything into four buckets:

| Bucket | Meaning | What to do |
|--------|---------|------------|
| **Both found** | Independent corroboration | Highest confidence — lead with these |
| **Only primary** | Second model missed it, or it's wrong | Re-check your own reasoning, then keep or drop |
| **Only second (verified)** | Your blind spot | Keep — these are the reason you ran this |
| **Severity disagreement** | Same finding, different weight | Reconsider honestly; a second opinion re-rating your "minor" note is signal |

Take severity disagreements seriously in both directions. Under-rating is as common as
over-rating, and "it's opt-in" or "it's a dev script" are conventions, not guardrails.

---

## Step 5 — When the cross-check can't run

If no second-vendor model is reachable, fall back to any available model from a vendor
other than the primary. If none exists at all, **say so plainly**: deliver the
single-model review clearly labelled as un-cross-checked.

Never present a single-model review as though it were cross-checked. The label is the
product here — a reader who believes two models looked at something will trust it more
than they should.

---

## Step 6 — Deliver the reconciled review

Produce one ranked review, most severe first, in the voice of the person who will post it.
Do not present it as "model A said X, model B said Y" — reconcile it into a single
coherent verdict.

For each finding: what breaks, the file:line, and a concrete failure path. Note where
two models independently agreed, since that is real evidence.

Call out any finding that is **pre-existing** rather than introduced by this change — it
belongs in the tracker, not as a change request against the author.

**Stop here.** Present the draft and wait. Do not post to GitHub, do not request changes,
do not merge. Posting is outward-facing and lands in someone else's notifications —
that's the human's call.

If the user then asks to post: `gh pr comment <n> --body-file <path>` for a plain comment,
or `gh pr review <n> --request-changes` for a blocking state. Note that "request changes"
only actually blocks when branch protection requires approving reviews — otherwise it is
a visual marker.

---

## Why this beats one review

- **Different vendors have different blind spots** — the second pass reaches findings the
  first structurally could not
- **Blind means the overlap is evidence** — agreement you didn't induce is worth something
- **Verification gates the noise** — a second model's confidence is not correctness
- **Severity gets a second vote** — the "minor note" you'd have shipped past gets re-weighed

---

## Edge cases

- **No `gh`** — PR mode is unavailable; fall back to local diff against the base branch
- **Huge diff** — review by subsystem and run the second pass per subsystem; a truncated
  review is a false negative that reads like a clean bill of health
- **Second model reviews the wrong branch** — its findings will cite lines that don't
  match; if file:line references look off, re-check Step 0 before trusting anything
- **Both models miss something you spot later** — record it; two models agreeing is
  evidence, not proof
- **Generated or vendored files in the diff** — exclude them from both passes explicitly
