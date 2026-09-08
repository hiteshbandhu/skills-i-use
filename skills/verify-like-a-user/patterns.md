# Failure patterns that survive code review

Symptom → cause → fix. Search this file before diagnosing from scratch. Every entry was
paid for on a real screen; add yours the same way.

---

## The class is in the source but not on the page

**Text renders larger than its class says (16px with `text-12` on it).**
Cause: `cn()` / tailwind-merge only knows stock font sizes; a custom size token
(`text-12`, `text-13`, `text-chip`) is classified as a *colour* and dropped when a real
colour follows it in the same `cn()`.
Fix: extend tailwind-merge's `font-size` class group with every custom token, once, in
the `cn` helper. Check: `getComputedStyle(el).fontSize`.

**`line-clamp-2` does nothing; text runs to four lines.**
Cause: `block` (or any `display:` utility) placed after `line-clamp-*` overrides the
`-webkit-box` display the clamp needs.
Fix: remove `block`; the clamp sets its own display. Check: `scrollHeight` vs
`clientHeight` on the element.

**Swapping the typography token changed nothing.**
Cause: both display tokens were the serif face *by design* (`display-lg`, `display-md`
→ `font-family: var(--font-serif)`). An object's label should not use editorial display
type.
Fix: use the sans size/weight directly (`text-xl font-semibold tracking-tight`) or the
page-title class the design system defines.

**A value imported from a `"use client"` file is "not a function" / not an array in a
server component.**
Cause: non-component exports from a client module arrive in RSC as client references.
Fix: move the constant to a plain module (or the schema), or make the consumer a client
component. Also applies to `AGENT_COLORS`-style lookups.

---

## Layout

**Primary button below the fold and nothing scrolls to it (short window).**
Cause: `flex-1` + `justify-center` on a column inside a fixed-height flex parent centres
by clipping equally at both ends.
Fix: `min-h-full` on the column (it grows past the viewport; the parent scrolls).
Check at 1000×560: button `bottom` ≤ `innerHeight`, or the scroller's
`scrollHeight > clientHeight`.

**Three columns on a narrow screen, two on a wide one.**
Cause: a viewport breakpoint (`lg:grid-cols-3`) measures the window, and a sidebar
takes 256px of it.
Fix: container queries — `@container` on the column, `@3xl:grid-cols-3` on the grid.

**Cards cluster left and the right half of the line is empty.**
Cause: `grid-cols-[repeat(auto-fill,minmax(270px,1fr))]` fits as many as it can, then
stops; with two items you get two narrow cards.
Fix: an exact count at each container width; cards stretch to fill.

**Everything on the page starts at a different x.**
Cause: search flush-left, featured centred on the pane, shelves left.
Fix: one `mx-auto max-w-* @container` column; every section a child of it.

**A card's border is cut off at the container edge.**
Cause: the "border" was `shadow-[0_0_0_1px_…]` — drawn *outside* the box — and the
scrolling parent clipped it.
Fix: a real `border border-hairline`. Check: `borderLeftWidth === "1px"`, card `left` ≥
scroller `left`.

**Featured titles overflow their fixed-width cards.**
Fix: cards stretch in a grid track; title `line-clamp-2 text-balance`. Check:
`scrollWidth > clientWidth` = 0 elements.

**Sticky controls eat the top of every screen.**
Cause: search/recents rendered above the scroll container.
Fix: put them *inside* it; they scroll away with the content. Check: control `top`
before vs after `scrollTop = 400`.

---

## Tabs and navigation

**Tab underline has rounded ends.**
Cause: `rounded-xs` on the tab (for the focus ring) rounds the bottom border too.
Fix: drop the radius from the tab; the ring still draws. Check: `borderRadius === "0px"`.

**Every tab click shows the full loading screen.**
Cause: the tab strip lives in each page, and each page wraps itself in
`<Suspense fallback={<BrandLoading/>}>`.
Fix: strip in a `layout.tsx` (it stays; only the column beneath swaps); a `loading.tsx`
skeleton shaped like the column. Check: the strip is the same DOM node after
navigation; the brand screen text never appears.

**`redirect()` in a nested segment renders an empty page and the URL never moves.**
Fix: declare it in `next.config` `redirects()` (resolved before any segment renders).
Verify with a real navigation: `location.pathname` changed and the target's tab is
active.

**Two back arrows that both lead to the page you are on.**
Cause: a chat's "back to agent" after "agent" started redirecting straight into the
chat. Loops. Remove; the frame above already carries the way out.

**A 404 renders black, outside the shell, with no way back.**
Cause: no `not-found.tsx` under the section; Next's default page has no layout.
Fix: add one; it inherits the section layout.

---

## Modals

**Close X sits on top of the primary button.**
Cause: the dialog draws its X absolutely; padding on the header cannot reliably clear a
button that wraps at some widths.
Fix: turn the dialog's X off, render the close control as a sibling of the button in the
header row. Check overlap of the two rects at 1440/1000/640/400.

**A hairline flashes as the dialog closes.**
Cause: zoom-out reveals the inner scroll container's edge.
Fix: `overflow-hidden` on the content, close on a fade. Check: screenshot ~80ms after
triggering close; sweep for visible boxes with height < 3px.

**The primary button wears a focus ring the moment the dialog opens.**
Fix: `onOpenAutoFocus={(e) => e.preventDefault()}` (focus the search box explicitly if
there is one).

**Browsing a list that opens each item as a new page loses scroll and filter.**
Fix: a plain click opens a dialog over the list; the card stays a real `<a>` so
middle-click and copied URLs still navigate. Test `event.button === 0 && !meta/ctrl/shift`.

---

## State and data

**The header says Install after installing; the footer says Uninstall.**
Cause: header read a prop snapshot; footer read live state. (And an edit meant to fix it
silently did not apply — always assert on the replacement.)
Fix: one control, one `useState` initialised from the prop, flipped on success.

**Newly added item shows its raw id until reload.**
Fix: the picker returns `{id → label, icon, connected}` alongside ids; the parent merges
into a `learned` map used for display.

**"Saved" disappears after saving.**
Cause: `router.refresh()` changed the key → remount → state reset.
Fix: park the flag in `sessionStorage` for one mount, read it in the `useState`
initialiser.

**"Dirty" never clears after a successful save.**
Cause: `dirty = JSON(prop) !== JSON(state)`; the prop is the *first* render's value.
Fix: compare against a `baseline` state you set to `config` on success.

**A button that creates something is a no-op for a fresh item but works for a
re-added one.**
Cause: the action required an existing row (`reinstall` upserted only if a row existed).
Fix: create the row on first use, pinned to the current revision.

**Everything is "installed" and the shelf is empty.**
Cause: a roster loader upserted an installation for every catalogue item on every visit.
Fix: library items are opt-in; skip them in the loader. Existing rows untouched.

**Roster 500s after deleting rows with SQL.**
Cause: an hours-long `use cache` list still holds the deleted ids; rebuilding a child
row hits the foreign key.
Fix: skip a stale entry (catch the FK error per item), and clear the cache. Never
assume a cached id still exists.

**Strict structured output rejects the schema.**
Cause: Zod `.default()` makes a key optional; the provider requires every key in
`required`.
Fix: a planner-only schema with no defaults; fill defaults after.

**Creating a row fails with "unknown argument".**
Cause: a config JSON field (`openers`) spread into a Prisma `create` for a table that has
no such column.
Fix: drop revision-only keys from the projection before `create`, next to the ones
already dropped.

**An empty array is truthy.**
`if (next.needs.length && !context.carry)` where `carry` is `[]`: the branch never runs.
Use an explicit boolean flag, never array presence, for "is this a later round".

**Four emoji pass an 8-character minimum.**
Count graphemes (`Intl.Segmenter`), not `string.length`.

---

## Copy and naming

- "the lawyer's Drive" and "you" in the same paragraph → tell the model who "you" is
  and to never use the third person.
- Approach line reads as instructions to the user → it must be in the agent's own voice
  ("I compare…"), never "You'll connect…".
- A description that is one deliverable → describe a remit.

---

## Process

- **A python edit that silently did not apply.** Always `assert old in s` before
  `replace`; print what was replaced. A no-op edit shipped a header reading stale state.
- **A cut that matched an inner `});`.** When slicing a test out by its closing brace,
  match the exact indented line, and typecheck the file before committing.
- **One width, one screenshot, "done."** No. Four widths, click-through, reload, a
  mid-animation frame.
- **Stopping a subagent before it looked at its own work.** The figure component
  shipped with two defects its author would have caught on the preview page. If you stop
  it, do its verification yourself.
- **Test data left behind** (agents named XXXX…, orphaned drafts). Clean up in the same
  session, or the user finds it first.
