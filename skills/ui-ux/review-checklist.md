# UI/UX Review Checklist

Use for file-level or feature-level reviews. Read [principles.md](principles.md) for rationale.

## Product fit

- [ ] Screen has one clear primary job
- [ ] User always knows the next action
- [ ] Empty / loading / error states are designed (not afterthoughts)
- [ ] Copy is specific — no "Submit", "Click here", "Learn more" without context

## Layout

- [ ] Visual hierarchy obvious at a glance (scan in 3 seconds)
- [ ] Spacing rhythm consistent (4/8/12/16/24 scale)
- [ ] No horizontal scroll on mobile
- [ ] Fixed elements respect safe areas
- [ ] Sidebar / nav grouping matches user mental model

## Forms & input

- [ ] Labels visible (not placeholder-only)
- [ ] Paste works; newlines preserved where expected
- [ ] Validation inline; errors persist until fixed
- [ ] Disabled states explain why (tooltip or helper text)
- [ ] Primary button disabled state is intentional, not broken-looking

## Feedback & states

- [ ] Actions acknowledge within 200ms
- [ ] Skeletons match final layout
- [ ] Destructive actions confirmed
- [ ] Success doesn't require reading a paragraph

## Accessibility

- [ ] Focus order logical; visible focus ring
- [ ] Icon buttons labeled
- [ ] Color not sole indicator of state
- [ ] Contrast sufficient on muted text

## Motion

- [ ] Animations purposeful and short
- [ ] `prefers-reduced-motion` respected
- [ ] No layout-thrashing animations

## Code hygiene (UI)

- [ ] No mixed component primitive systems
- [ ] No `h-screen` (use `h-dvh`)
- [ ] No arbitrary z-index sprawl
- [ ] Reuses existing design tokens / components

## Polish pass (when user attaches screenshot)

- [ ] Compare screenshot to principles — list top 3 issues first
- [ ] Propose minimal diff — no redesign unless asked
- [ ] Verify fix in same viewport size user showed

## Playwright (when URL available)

- [ ] Navigated to correct route on desktop and/or mobile viewport
- [ ] Accessibility snapshot reviewed (labels, roles, focus order)
- [ ] Screenshot saved to `skill-outputs/ui-ux/screenshots/`
- [ ] Console has no errors (or explained)
- [ ] Scope-specific interactions smoke-tested (scroll, input, menus, forms)
- [ ] After fixes — re-screenshot and re-test failed items
