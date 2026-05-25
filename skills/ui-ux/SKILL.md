---
name: ui-ux
description: >
  UI/UX and product review for web interfaces — opinionated principles, checklist-driven
  audits, polish passes on screenshots, and pre-ship UI gates. Uses Playwright to
  navigate, screenshot, and smoke-test interactions when a URL is available. Triggers on "review my UI",
  "polish this", "UX audit", "fix the hero", "make it look professional", "ui pass",
  "design review", attaches screenshot with UI feedback. Use when building or reviewing
  interfaces and product flows, not generic code review.
---

# UI/UX — Product-Aware Interface Review

Opinionated UI/UX + product review for web apps. Thinks about **jobs-to-be-done** before
pixels. Works with any coding agent.

**Supporting files:**
- [principles.md](principles.md) — product + UI/UX rules (read every time)
- [review-checklist.md](review-checklist.md) — structured audit
- [playwright.md](playwright.md) — browser verification with Playwright
- [report-template.md](report-template.md) — saved review output

Output: `{SKILL_OUTPUT_DIR}/ui-ux/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — Determine Mode

| Mode | When | Output |
|------|------|--------|
| **audit** | "review my UI", file path given, pre-merge | Findings list + report file |
| **polish-pass** | screenshot attached, "fix the hero", iterative tweaks | Minimal code diff + short rationale |
| **pre-ship** | before commit on UI-heavy change | Audit + pair with `@ship-check` if shipping |

Ask if unclear:
1. **Scope** — file, route, or component?
2. **Viewport** — mobile / desktop / both?
3. **URL** — local dev URL + route (e.g. `http://localhost:3000/dashboard`)
4. **Build or review only?** — "don't code, plan only" → review only

---

## Step 1 — Load Context

1. Read [principles.md](principles.md)
2. Read the target file(s) or explore the route
3. Note existing design system — reuse project components, tokens, patterns
4. If screenshot provided — treat it as source of truth for what's wrong visually

---

## Step 1b — Playwright Verification

Read [playwright.md](playwright.md). **Always run when a URL is reachable** (unless
review-only on code with no running app).

Use Playwright MCP when available; fallback to project Playwright tests or CLI.

Capture before screenshots + snapshot + console errors. Run interaction smoke checks
for the scoped screen (scroll, input, menus, forms, CTAs).

Save artifacts under `{output_dir}/screenshots/`.

If Playwright cannot run, note why in the report and rely on code review + user
screenshots — do not skip silently.

---

## Step 2 — Review

Run [review-checklist.md](review-checklist.md) against scope **and Playwright results**.

For each finding:
- **Severity:** Critical / Important / Suggestion
- **Location:** `file:line` when reviewing code
- **Issue:** one sentence
- **Fix:** concrete — class change, component swap, copy rewrite, layout adjustment

Prioritize:
1. Trust breakers (broken scroll, lost input, silent failures)
2. Clarity (hierarchy, next action, copy)
3. Polish (spacing, motion, micro-interactions)

Do not suggest gradients, glow, purple accents, or animation unless user asked.

---

## Step 3 — Implement (unless review-only)

When building or polishing:
- **Minimal diff** — fix what's broken, don't redesign the whole page
- Match existing code style and component library
- One primary change per iteration when user is in screenshot-driven loop
- After edits, state what changed in plain language

Stack defaults from principles: Tailwind, `cn()`, accessible primitives, `h-dvh`, `motion/react` only when needed.

**Re-run Playwright (Step 1b)** after implementing — capture after screenshots and
confirm failed interaction checks now pass.

---

## Step 4 — Write Report (audit / pre-ship modes)

Fill [report-template.md](report-template.md).

**Path:** `{output_dir}/review-YYYY-MM-DD-[slug].md`

Update `{output_dir}/index.md`:

```markdown
# UI/UX Reviews

| Date | Scope | Verdict | Report |
|------|-------|---------|--------|
```

---

## Step 5 — Output to User

1. Verdict: Ship / Ship with fixes / Needs rework
2. Top 3 issues (most impact first)
3. Report path (if saved)
4. Offer to implement fixes — or done if already implemented

For **polish-pass**: before/after summary in 2–3 bullets, no long essay.

---

## Pair with other skills

- **`@ship-check`** — run after UI changes before commit
- **`@architecture-review`** — when UX change implies a product/architecture fork (e.g. new nav paradigm)

---

## Edge Cases

- **User says "don't code"** — audit + plan only
- **Conflicting project patterns** — follow project, flag deviation from principles as Suggestion
- **Backend-only request** — decline politely; this skill is UI/UX scoped
- **No running dev server** — offer to start it, or audit code-only with note
- **Playwright MCP unavailable** — use `npx playwright test` or document skip reason
- **Whole app redesign** — ask for priority screen; do not boil the ocean in one pass

---

## Invocation Examples

```
@ui-ux review the onboarding flow
@ui-ux audit http://localhost:3000/dashboard — desktop and mobile
polish the hero — dev server on :3000
ui pass before we ship
don't code — give me a plan for the dashboard layout
```
