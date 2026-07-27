# Cross-Model Review

Review a PR or working diff twice — once with your primary model, then again with a
**different vendor's** model that is told nothing about the first pass — then verify and
reconcile both into one ranked review.

**Stops at a draft. Never posts to GitHub without your say-so.**

Output: `./skill-outputs/cross-model-review/`

## Why

A single model reviews with a single set of blind spots. A second model from a different
vendor, running blind, reaches findings the first structurally could not — and re-rates
severity the first pass got wrong.

The point isn't "two reviews." It's that the overlap is *earned*. Both models landing on
the same finding independently is corroboration. Only one finding it is a lead to verify,
never a finding to publish.

## The method

| Step | What happens |
|------|--------------|
| **1. Primary review** | You review first — running the second model first anchors you |
| **2. Probe** | Find an available CLI + a different-vendor model; never assume one exists |
| **3. Blind pass** | Second model reviews with **zero** knowledge of your findings |
| **4. Verify** | Open the real code behind every new claim before believing it |
| **5. Reconcile** | Sort into: both found / only primary / only second / severity disagreement |
| **6. Deliver** | One ranked review in your voice — then stop and wait |

Step 4 is the one that makes it work and the one most likely to get skipped. A second
model states wrong findings with the same confidence as right ones.

## Model selection

Preference order, resolved against the live model list each run:

1. `gpt-5.6-sol-low` / `gpt-5.6-sol-medium` — the calibrated default
2. Any other model from a vendor different to the primary
3. None available → single-model review, **explicitly labelled as un-cross-checked**

Model IDs age out. The names above are preference, not requirement.

## Install

```bash
npx skills add hiteshbandhu/skills-i-use --skill cross-model-review
```

Or copy/symlink the folder into `~/.claude/skills/`, `~/.cursor/skills/`, or your project.

Needs `gh` for PR mode, and at least one agent CLI (`agent`, `codex`, or `claude`) on
`PATH` for the second pass.

## Usage

```
@cross-model-review 161
cross-model review this PR
second opinion on this diff before I push
have another model look at this
double-check my review of #161
```

## When not to use it

- Small self-evident diffs — config bumps, copy changes, dependency pins
- Code you wrote and already know
- When you need an answer in under two minutes

Run it where being wrong is expensive: unfamiliar code, an outside contributor's PR, or
anything touching auth, money, migrations, or data loss. Running it on every trivial PR
turns a real technique into ceremony.

## Real result

On a 14-file PR, the blind second pass caught two bugs the first review missed — an alias
override that silently deleted two canonical slash commands, and a data model that let
several prompts override the same built-in — and correctly re-rated two findings the first
pass had filed as minor. Both were confirmed against the actual source before publishing.
