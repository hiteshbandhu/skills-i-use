---
name: verify-like-a-user
description: >
  Build and check UI the way a person meets it — measure the rendered page instead of
  trusting the source, break it on purpose at several widths and along the paths people
  actually take, fix the root cause, and re-measure before calling it done. Carries a
  catalogue of UI failures that survive code review (clipped borders, dropped size
  classes, dead ends on short screens, stale caches, redirects that never move the URL)
  with symptom → cause → fix. Triggers on "verify this UI", "does this look right",
  "check it at other widths", "it looks bad, fix it", "break the product", "make these
  pages consistent", "why is this clipped / overflowing / huge / not clickable",
  "audit every page in this section", and any screenshot sent with "fix this".
---

# Verify Like a User

You are not done when the code compiles. You are done when the page, as a person meets
it, does what they asked — and you can show the measurement that says so.

This skill is the discipline that turned a week of "looks fine in the diff" into
shipped UI: ground truth first, measure not eyeball, break it on purpose, fix the cause
not the symptom, re-measure, report honestly. It pairs with [`ui-ux`](../ui-ux/) (which
audits and polishes) — this one is about the loop that makes any UI change true.

**Supporting files — read the one the step names:**
- [laws.md](laws.md) — the UX laws, each with the concrete rule it produced
- [patterns.md](patterns.md) — failure catalogue: symptom → cause → fix (search it first)
- [measure.md](measure.md) — DOM measurement recipes and browser-automation gotchas

Output: `{SKILL_OUTPUT_DIR}/verify-like-a-user/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — Mode

| Mode | When | Ends with |
|------|------|-----------|
| **fix-a-screenshot** | user sends a screenshot and says what is wrong | a measured before/after on that exact element |
| **verify-a-change** | you just changed UI | measurements at four widths + the click-through path |
| **break-it** | "test like a user", "break the product" | a ranked defect list with proof, then fixes |
| **overhaul** | "this section is bad, redo it" | audit → structure decision → rebuild → re-verify every page |

If the user's screenshot and your reading of the code disagree, **the screenshot is
right**. Find why the code you read is not what rendered ([patterns.md](patterns.md) §
"The class is in the source but not on the page").

---

## Step 1 — Ground truth before pixels

1. Read the project's design rules first: `DESIGN.md`, `CLAUDE.md`, the tokens file,
   `globals.css`. Note what a page title *is* (size/weight/face), what a section header
   is, which radius tier means what, which tokens are serif.
2. Find the page in the product that already does this right (the real settings page,
   the real list page). Copy its classes, not its idea.
3. Read [laws.md](laws.md). Decide, before touching anything, which structure the
   screen needs: tabs vs rail, popup vs page, one column vs grid, one button that
   flips vs two.

Do not start from what the previous version did. Start from what the rules say and
what the user said — in that order when they conflict, and say so.

---

## Step 2 — Measure, don't eyeball

A screenshot tells you something is wrong. A measurement tells you what. Use
[measure.md](measure.md) — every check below is one `eval`.

Minimum for any change to a screen:

- **Widths:** 1440, 1000, 640, 400. Primary action reachable at each (in the viewport,
  or the container scrolls to it).
- **Rects:** the two things that must not overlap, do not. The thing that must align
  with the box above it, does (same left/right edge to the pixel).
- **Computed styles:** the font-size and family that *rendered* on the element you
  care about, not the class you wrote. Border width and style. Border radius on a tab.
- **Overflow:** which ancestor scrolls, and whether the content is taller than it.
  `scrollHeight > clientHeight` on the wrong element is the dead end.
- **Text:** `scrollWidth > clientWidth` on any title = clipping. Line-clamp actually
  clamping (2 lines, not 4).
- **State:** `aria-selected`, `aria-pressed`, `aria-invalid` on what you think is active.

Take the screenshot *after* the measurement, to see what the numbers mean.

---

## Step 3 — Break it on purpose

Your own happy path proves nothing. Do these every time, and log each as pass or fail
with the number that proves it:

1. **The click-through path, not the direct URL.** Navigate from where a person would
   (the list, the sidebar, the card). Direct load and client navigation render
   differently; redirects, layouts and loading states differ between them.
2. **Reload and Back mid-flow.** Is typed work lost silently? Is there a
   `beforeunload` guard where there should be?
3. **Short window.** 1000×560. Is the primary button below a fold nothing scrolls to?
4. **Empty and full.** Zero items, one item, forty items. Does an empty shelf say
   "you have everything" or lie with "no matches"?
5. **Invalid input.** Clear a required field, paste 10,000 characters, four emoji
   (JavaScript counts UTF-16 units, not graphemes). Does the error name the field?
6. **Rapid double-click** on any button that creates something. Count what got created.
7. **Mid-animation frames.** Trigger a close or a transition and screenshot at ~80ms.
   Seams, flashes and stray hairlines live there.
8. **Stale state.** Change data another way (a script, another tab) and reload. Caches
   with hour lifetimes, and code that assumes a row still exists, fail here.
9. **A second machine's view.** Different host (`localhost` vs `127.0.0.1`), fresh
   session, no cookies. The dev server treats them differently.

Rank what you find by what a person loses: dead ends and lost work first, lies
second ("Added" on something you cannot act on), looks last.

---

## Step 4 — Fix the cause

Before writing a fix, look the symptom up in [patterns.md](patterns.md). Most of these
have been paid for already:

- a rendered size that ignores the class → the class merger dropped it
- a border cut off at one edge → it was a shadow outside the box, clipped by a scroller
- content clipped equally top and bottom, nothing scrolls → `flex-1` centring, not
  `min-h-full`
- three columns on one screen, two on a bigger one → viewport breakpoint measured the
  window, not the pane; use container queries
- a redirect that renders an empty page and never moves the URL → do it in the router
  config, not inside a nested segment
- a value imported from a `"use client"` module is not an array → it is a client
  reference; move the constant or make the consumer a client component

Fix the cause. If you also have to work around a symptom, say which is which in the
commit.

Then:
- Route every affordance for the same thing through **one component** (one back link,
  one section header, one service mark). Eleven call sites edited by hand is eleven
  chances to drift.
- **One piece of state per control.** A header that reads a prop snapshot and a footer
  that reads live state will disagree the moment something changes.
- Never gate the input on decoration. The greeting can stream; the box appears on a
  timer computed from the text, not on an event that may never fire.

---

## Step 5 — Re-measure, then look once

Run the exact `eval`s from Step 2 again. Numbers first, then one screenshot per
changed screen. If a screenshot contradicts a number, the screenshot wins — find out
why before moving on.

Do not call a flow done from one width, one path, or one screenshot. Two of the three
worst defects this skill was written from were only visible at 577px tall and only on
the click-through path.

---

## Step 6 — Report honestly

Lead with what was **driven** (in a browser, against real data) versus what was only
**compiled**. Give the measurement, not the adjective:

> Continue's right edge sits on the box's right edge (1027 = 1027). Meet your agent is
> at 532 in a 577 viewport. Strip is the same DOM node across navigation; the brand
> loading screen never appeared.

State what you could not reproduce and what you did not test. A user who is told "I
couldn't reproduce this at 1440 or 400 — send me your window size" can help you; one
told "fixed" cannot.

Write the record to `{output_dir}/verify-YYYY-MM-DD-[slug].md` in break-it and overhaul
modes: defects ranked, each with what you did / expected / got / proof, then the fixes
and their re-measurements.

---

## Hard rules

1. A screenshot from the user outranks your reading of the source.
2. No "done" without a number from the rendered page.
3. Four widths, the click-through path, a reload, and one mid-animation frame — every time.
4. Search [patterns.md](patterns.md) before diagnosing from scratch; add to it when you find a new one.
5. One component per recurring affordance; one state per control.
6. Never commit a test file you did not run after editing it.
