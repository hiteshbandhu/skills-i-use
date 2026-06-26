---
name: scroll-engineering
description: >
  Audit a streaming chat UI against the 15-point scroll engineering checklist — every
  principle about reader intent, viewport control, layout stability, and accessibility.
  Classifies each point as passing, failing, or not applicable, then ranks the top fixes
  by user impact. Triggers on "audit my scroll behavior", "check auto-scroll", "streaming
  chat UX review", "scroll engineering", "jump to latest", "reader intent", "chat viewport
  issues", "streaming layout shifts". Use when reviewing or building a streaming chat
  interface — not for general UI review (use ui-ux for that).
  Credit: principles by @shadcn (https://x.com/shadcn/status/2070394918720221522).
---

# Scroll Engineering Audit

> **Credit:** This checklist is derived from @shadcn's "What Makes a Great Streaming Chat
> Experience" thread (Jun 2026). The north star principle:
> **Never move the reader against their intent.**

Audit a streaming chat UI against 15 scroll engineering principles. Works by reading code
or observing live behavior. Output: a pass/fail table + a ranked fix list.

---

## Step 0 — Scope

Establish what you're auditing:

1. **The interface** — a codebase path, a live URL, or a described behavior.
2. **Access** — can you read the scroll/auto-scroll logic in code? Can you open the UI in
   a browser? Use what's available; flag what you can't verify.
3. **Streaming type** — token-by-token LLM stream, chunked SSE, or simulated? Matters for
   points 7, 8, and 14.

Resolve output dir. Default `./skill-outputs/scroll-engineering/`.

---

## Step 1 — Read the scroll logic

Before scoring, find where scroll behavior is controlled:

- Search for `scrollTo`, `scrollIntoView`, `scroll`, `auto-scroll`, `useEffect` on message
  length, or mutation observers on the message list.
- Find the "jump to latest" affordance (or note its absence).
- Find where layout-shifting content (images, code blocks, markdown) is rendered.
- Note any `overflow`, `position: sticky`, or virtualization libraries in play.

Do not score from memory or assumption — read the actual control path.

---

## Step 2 — Score each principle

For each of the 15 principles, mark: **pass**, **fail**, or **n/a** (with reason).

### Reader intent — the non-negotiables (1–3)

**1. Move only when the reader asked to move.**
Auto-scroll should never be the default. If someone is reading, don't pull them somewhere
else.
- Pass: scroll is triggered only by explicit user action or by the user already being at
  the live edge.
- Fail: the interface auto-scrolls unconditionally as tokens arrive.

**2. Follow only while they're following.**
If the user is at the live edge, keep the stream in view. If they scroll away, leave them.
- Pass: a "following" flag is tracked; scrolling away disables auto-follow.
- Fail: no distinction between "user is at bottom" and "user scrolled away".

**3. Every interaction is intent.**
Scrolling is not the only signal. Selecting text, pressing a key, opening a link, or
searching should all stop the interface from moving.
- Pass: pointer events, keyboard events, and selection events are all treated as "stop
  following" signals.
- Fail: only scroll events are checked; text selection or keyboard use mid-stream still
  causes jumps.

### New turn flow (4–6)

**4. Start a new turn near the top of the viewport.**
The new turn should have room to be read from its beginning — not arrive at the very bottom
edge.
- Pass: on a new user message, the view snaps/scrolls so the assistant turn starts near the
  top third of the viewport.
- Fail: new turns arrive at the absolute bottom with no breathing room.

**5. Stream the answer into the available space.**
After positioning, let the streaming answer grow downward into the space below.
- Pass: the assistant bubble grows naturally without repositioning the viewport.
- Fail: each new token causes a scroll event that moves the viewport.

**6. Keep part of the previous turn in context.**
Enough of the prior turn should remain visible so the reader knows where they are.
- Pass: the scroll position on a new turn leaves 1–3 lines of the prior message visible
  above the fold.
- Fail: the view jumps so the prior message is completely off screen.

### Out-of-view streaming (7–9)

**7. Let new content arrive offscreen.**
The conversation can keep streaming without changing what the reader is looking at.
- Pass: if the user has scrolled up, new tokens append to the DOM without moving the
  viewport.
- Fail: appending new content shifts the scroll position even when the user is not at the
  bottom.

**8. Show what's happening out of view.**
Make it clear when a response is still streaming or when new messages have arrived.
- Pass: a streaming indicator or "new message" badge is visible while the user is scrolled
  away.
- Fail: no signal that streaming is in progress when the user isn't watching the bottom.

**9. Make it easy to return.**
A "Jump to latest" action brings the reader back and resumes following.
- Pass: a visible, reachable button appears when the user is not at the live edge.
- Fail: the only way to return is to manually scroll to the bottom.

### Navigation & persistence (10–11)

**10. Let people jump anywhere in the conversation.**
Long threads need message links, search, unread markers, or direct navigation.
- Pass: at least one of — anchored message URLs, a search affordance, or visible unread
  markers — is present.
- Fail: the only navigation is manual scrolling through the entire history.

**11. Reopen where the reader left off.**
A saved conversation should open at the last meaningful turn — usually the last user
message, not the absolute bottom.
- Pass: returning to a conversation restores the position near the last user message, not
  `scrollTop = scrollHeight`.
- Fail: every reopen dumps the user at the very bottom (or very top).

### Layout stability (12–13)

**12. Keep place when layout changes.**
Images loading, markdown expanding, code blocks rendering, or older messages appearing
above — none of that should lose the reader's place.
- Pass: layout-shifting content uses reserved height, lazy load with anchoring, or a scroll
  anchor technique (`overflow-anchor: auto` + explicit anchoring).
- Fail: images popping in or markdown rendering jumps the viewport.

**13. Handle interruptions without stealing position.**
Stopping, retrying, regenerating, branching, or errors should not unexpectedly move the
conversation.
- Pass: stop/retry/regenerate operations do not trigger a scroll event.
- Fail: clicking "stop" or "retry" causes a viewport jump.

### Performance & accessibility (14–15)

**14. Stay responsive in long threads.**
Streaming text, markdown, code, images, and long history should still feel responsive.
- Pass: virtualization or windowing is in place for long histories; streaming does not degrade
  with 50+ messages.
- Fail: the page slows noticeably in long threads; streaming causes visible jank.

**15. Be accessible without the noise.**
Keep the transcript navigable, preserve keyboard focus, announce important events at a
comfortable pace — not on every token.
- Pass: screen reader announcements are debounced; keyboard focus is not stolen by scroll
  updates; the transcript is navigable via landmarks or headings.
- Fail: each token fires an ARIA live update, flooding screen readers; or keyboard focus
  jumps on scroll.

---

## Step 3 — Rank the fixes

Take every **fail** and score it:

| # | Principle | User pain (1–3) | Fix complexity (1–3) | Priority = pain × (4 − complexity) |
|---|-----------|-----------------|----------------------|--------------------------------------|

Sort descending by priority. Surface the top 3 as "ship first."

For each top fix, write:
- **What fails today** (one sentence, concrete).
- **The fix** (where in the code, what to change — do not implement, just specify).
- **The tradeoff** (what you're giving up or adding; nothing is free).

---

## Step 4 — Output

Write results to `{output_dir}/report.md`:

1. Metadata: interface audited, date, access method.
2. The scored table (all 15, pass/fail/n/a).
3. Top 3 fixes ranked by priority.
4. Anything marked n/a and why (so the requester can challenge it).

Then in chat:
- The scored table.
- Top 3 fixes.
- One-line summary: "X/15 passing. Biggest gap: [principle N]."

Do not implement fixes here — this skill audits and specifies. Implementation is a
separate confirmed step.

---

## Edge cases

- **No code access, only a URL** — use a browser tool to observe behavior: scroll mid-stream,
  select text mid-stream, switch tabs and return, reload on a long thread. Score from
  observation and note "observed, not verified in code."
- **Simulated streaming (no real SSE)** — points 7 and 8 still apply; fake-stream delays
  are implementation details, not exemptions.
- **Mobile-only interface** — point 3 (intent signals) should include touch-scroll
  interruption; point 9 (jump to latest) must be reachable with one thumb.
- **Fully virtualized list** — point 12 (layout stability) is handled by the virtualizer;
  verify the virtualizer's scroll anchor behavior specifically.
- **Big architectural gap found** (e.g., no scroll state model at all) — defer to
  `architecture-review` before specifying fixes.

---

## Invocation examples

```
@scroll-engineering audit the chat scroll behavior in components/research/
review my streaming UI for scroll engineering issues — live at localhost:3000
check if our auto-scroll respects reader intent
scroll engineering audit on this chat interface
does our jump-to-latest work correctly?
audit streaming UX for reader intent violations
```
