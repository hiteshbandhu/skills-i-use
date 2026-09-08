# UX laws, as applied

Each law below is paired with the concrete rule it produced when building real screens.
The law is the why; the rule is what you type.

---

## Recognition over recall

**Law.** People recognise what they have seen; they do not recall what a label meant.

- **The tab's name is the page's title.** "Profile" must open a page whose H1 is
  "Profile", not "How it appears to you". Cute titles break the link between what was
  clicked and where you are.
- **One back, everywhere, named for where it goes.** Not the word "back". "Your agents",
  "Library". One component, so it looks the same on every page.
- **A control says where it takes you.** "Settings" on the conversation, "Chat" on
  settings. A Settings button shown on the settings page is a control that does nothing.
- **A name carries its category.** "Meeting Summary Agent", not "Meeting Summary" — the
  name travels into search results and mentions where no label follows it.

## One thing at a time

**Law.** A screen with one job is understood faster than one with three.

- **Three nested chromes is two too many.** App sidebar → section header → a settings
  rail with its own back is a third chrome. Use tabs under the header; one column.
- **One primary action per view.** Install *or* Uninstall in the same spot, flipping.
  Not Install plus an "Added" badge plus a footer with the way out.
- **Not everything is a card.** Border, fill, radius and shadow each mean "separate
  object". A card inside a pane inside a panel says nothing. Sections with a heading and
  one rule under it, rows with padding only.
- **Filters are the size of filters.** Chips at 11.5px on 4px padding; not buttons.

## Consistency

**Law.** Every departure from the pattern is something to learn.

- Follow the design system's tokens for titles and section headers — and know which
  tokens are serif *by design* before reaching for them for an object's label.
- A grid is three across, or it is not. `auto-fill` that fits as many as it can leaves
  the right half of the line empty on a wide screen and reads as broken.
- The same edge for everything in a column: search, featured band, chips, shelves.
  Centre the column, then align to it.

## Feedback and state

**Law.** Every action needs a visible result, from one source of truth.

- **One state per control.** The header and the footer must not read different copies
  of "installed".
- **Name what was just added immediately**, not after a reload. Carry the label with
  the id.
- **A save says saved** — and survives the remount a refresh causes.
- **Errors name the field.** "Check the highlighted fields" with nothing highlighted is
  worse than no message. Read the server's per-field errors and mark the field.
- **Distinguish empty states.** "You have every agent" is not "Nothing matches".

## Never trap, never lose

**Law.** People forgive slowness; they do not forgive losing their work.

- Warn before a reload throws away typed input or a plan that cost a model call.
- Every long request has a timeout that ends as a sentence someone can act on.
- A primary action is reachable at every window height — the container scrolls, or
  the layout does not centre by clipping.
- Two arrows that both lead back to the page you are on are loops. Remove them.

## Opt-in over silent

**Law.** Nothing is installed, granted or promised without the person choosing it.

- A library is for what you do not have. Auto-installing everything on every visit
  leaves the shelf with nothing to offer and the Install button with nothing to do.
- Adding something you have not connected is allowed — and shown as **Not connected**
  with the way to connect it, never hidden behind "no longer available".
- An agent, run, or job never claims reach it does not have. Unavailable things are
  listed for it; it says so when the task needs them.

## Motion

**Law.** Movement should feel like something happening, not something performing.

- A line that streams should land like tokens: longer words take longer, punctuation
  pauses. An even beat reads as a typewriter trick.
- The whole opening — figure, line, input — inside two seconds.
- Nothing waits on decoration. Time the next thing against the animation's computed
  duration; never on an event that might not fire.
- Close with a fade, clip the edges; zoom-out shows the scroll container's seam.

## Copy

- Address the person as **you**. Never "the lawyer's documents" and "you" in one sentence.
- The lede is one line. No eyebrow that explains the title. No second sentence that
  restates the first.
- Descriptions describe a remit, not one deliverable — broad enough that the
  neighbouring request still fits.
