# UI/UX + Product Principles

Read this file for every review or build pass. These are opinionated defaults — match
the project's existing patterns when they conflict, but flag regressions.

---

## Product (think before pixels)

1. **One primary job per screen** — if you cannot name the screen's job in one sentence, split it.
2. **Progressive disclosure** — show the minimum needed to act; reveal depth on intent (expand, drill-down, command palette).
3. **Obvious next action** — every state (empty, loading, error, success) tells the user what to do next.
4. **Feedback closes the loop** — every user action gets visible acknowledgment within 200ms (optimistic UI or skeleton, not silence).
5. **Respect user input** — never strip paste, never lose focus state, never surprise-navigate away from in-progress work.
6. **Density matches context** — dashboards can be dense; onboarding and hero must breathe.
7. **Copy is UI** — labels beat icons alone; verbs beat nouns on buttons ("Save draft" not "Submit").

---

## Layout & hierarchy

- **F-pattern for dashboards** — primary metric / action top-left; secondary across top.
- **Single focal point on marketing/hero** — one headline, one input or CTA, no competing CTAs.
- **Sidebar = wayfinding** — not a junk drawer; group by user mental model (Work, Settings, not internal team names).
- **Fixed chrome, scroll content** — nav/header stays; only the canvas scrolls.
- Use `h-dvh` not `h-screen`; respect `safe-area-inset` on fixed elements.
- Fixed `z-index` scale — no arbitrary `z-[9999]`.

---

## Interaction

- **Destructive actions** → confirmation dialog (AlertDialog), never instant delete.
- **Errors inline** — next to the field or button that caused them, not a toast-only graveyard.
- **Loading** → structural skeletons matching final layout, not spinners floating in space.
- **Keyboard first** for power users — `/` commands, `@` mentions, shortcuts documented in UI.
- Icon-only buttons need `aria-label`.
- Use accessible primitives (Radix, Base UI, React Aria) — never hand-roll focus traps.

---

## Typography & data

- Headings: `text-balance` · Body: `text-pretty` · Numbers: `tabular-nums`
- `truncate` / `line-clamp` in dense lists — full text on hover or detail view.
- Do not touch `letter-spacing` unless explicitly designing display type.
- Max 2 font weights per view for calm UI.

---

## Motion

- **No animation by default** — add only when it communicates state (enter/exit, reorder, progress).
- Animate only `transform` and `opacity` — never width/height/margin for layout.
- Interaction feedback ≤ 200ms, `ease-out` on entrance.
- Respect `prefers-reduced-motion`.
- No looping animation unless functional (typing indicator); pause when off-screen.
- No gradient/glow/purple/multicolor as primary affordance.

---

## Stack defaults (when building)

- Tailwind defaults unless project already customizes
- `cn()` (`clsx` + `tailwind-merge`) for class logic
- `motion/react` when JS animation is required
- Project's existing component primitives first — never mix primitive systems on one surface

---

## Anti-patterns (flag immediately)

| Smell | Fix direction |
|-------|---------------|
| Hero with 3+ equal CTAs | One primary, rest secondary/tertiary |
| Empty state with no action | One button or link |
| Modal for non-blocking info | Inline banner or side panel |
| Toast for form validation | Inline field error |
| Full-page loader for partial update | Skeleton on affected region |
| Scroll broken / nested scroll traps | One scroll owner per pane |
| Slash menu wider than input | Compact, max ~3 visible rows + scroll |
| Duplicate timestamps / labels | Deduplicate; one source of truth |
| Input doesn't expand on paste | Auto-grow textarea; preserve newlines |

---

## Review severity

| Level | Meaning |
|-------|---------|
| **Critical** | Blocks usability, accessibility, or trust — fix before ship |
| **Important** | Meaningful friction or polish debt — fix soon |
| **Suggestion** | Nice-to-have refinement |

Output findings with file:line when reviewing code.
