# Verify Like a User

Build and check UI the way a person meets it. Measure the rendered page instead of
trusting the source, break it on purpose at several widths and along the paths people
actually take, fix the root cause, re-measure, and report what was driven versus what
was only compiled.

Comes with a **failure catalogue** ([patterns.md](patterns.md)) — the UI bugs that pass
code review and only show up on a screen: a size class silently dropped by the class
merger, a border clipped because it was a shadow, a dead end on a short window, a
redirect that never moves the URL, "installed" that reads from two sources of truth.
Symptom → cause → fix, so the second time costs nothing.

Output: `./skill-outputs/verify-like-a-user/` (defect reports in break-it and overhaul modes)

## Modes

| Mode | Use when |
|------|----------|
| **fix-a-screenshot** | User sends a screenshot and says what is wrong |
| **verify-a-change** | You just touched UI — prove it at four widths and on the click-through path |
| **break-it** | "Test like a dumb user", "break the product" — ranked defects with proof, then fixes |
| **overhaul** | "This whole section is bad" — audit → structure → rebuild → re-verify every page |

## Usage

```
@verify-like-a-user this looks bad — [screenshot]
@verify-like-a-user verify the settings pages at other widths
@verify-like-a-user break the create flow from every angle
@verify-like-a-user overhaul agent settings; tabs not a sidebar
why is the border cut off / the text huge / the button unreachable?
```

## What it insists on

1. A user's screenshot outranks your reading of the source.
2. No "done" without a number from the rendered page.
3. Four widths (1440 / 1000 / 640 / 400), the click-through path, a reload, and one
   mid-animation frame, every time.
4. Search the patterns file before diagnosing from scratch; add to it when you find one.
5. One component per recurring affordance; one piece of state per control.
6. Never commit a test file you did not run after editing it.

## Files

```
verify-like-a-user/
├── SKILL.md       # the loop: ground truth → measure → break → fix cause → re-measure → report
├── laws.md        # UX laws, each with the concrete rule it produced
├── patterns.md    # failure catalogue: symptom → cause → fix
└── measure.md     # DOM measurement recipes + browser-automation gotchas
```

## Install

```bash
npx skills add hiteshbandhu/skills-i-use --skill verify-like-a-user
# or
ln -sfn /path/to/skills-i-use/skills/verify-like-a-user ~/.claude/skills/verify-like-a-user
```

## Pairs with

- [`ui-ux`](../ui-ux/) — the audit and polish workflow; this skill is the verification
  loop and the catalogue underneath it.
- [`ship-check`](../ship-check/) — run after the re-measure, before commit.
