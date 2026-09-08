# Measurement recipes

Each is one `eval` in whatever browser-automation you have (Playwright MCP,
`agent-browser`, a Playwright script). Copy, adapt the selector, read the number.

---

## Reach and overlap

```js
// Is the primary action reachable? (run at 1000x560 too)
(() => {
  const b = [...document.querySelectorAll('main button')].find(x => /Continue|Save|Install|Meet/.test(x.textContent));
  const r = b.getBoundingClientRect();
  const sc = [...document.querySelectorAll('main *')].find(e => {
    const o = getComputedStyle(e).overflowY; return (o === 'auto' || o === 'scroll') && e.scrollHeight > e.clientHeight + 40;
  });
  return { bottom: Math.round(r.bottom), vh: innerHeight, scrollable: !!sc, scrollHeight: sc?.scrollHeight, clientHeight: sc?.clientHeight };
})()
```

```js
// Do two controls overlap? (close X vs primary button)
(() => {
  const a = el1.getBoundingClientRect(), b = el2.getBoundingClientRect();
  const overlap = !(a.left >= b.right || a.right <= b.left || a.top >= b.bottom || a.bottom <= b.top);
  return { overlap, gap: Math.round(a.left - b.right), sameRow: Math.abs(a.top - b.top) < 8 };
})()
```

```js
// Does the row align with the box above it?
({ boxRight: Math.round(box.getBoundingClientRect().right), btnRight: Math.round(btn.getBoundingClientRect().right) })
```

## What actually rendered

```js
// Font that rendered, not the class you wrote
(() => { const cs = getComputedStyle(el); return { font: cs.fontFamily.slice(0, 20), size: cs.fontSize, weight: cs.fontWeight }; })()
```

```js
// Border inside the box? radius on a tab?
(() => { const cs = getComputedStyle(el); return { border: cs.borderLeftWidth + ' ' + cs.borderLeftStyle, shadow: cs.boxShadow, radius: cs.borderRadius }; })()
```

```js
// Any title clipping? Any clamp not clamping?
[...document.querySelectorAll('main a span, main h2')].filter(s => s.scrollWidth > s.clientWidth + 1).length
(() => ({ clamped: el.scrollHeight <= el.clientHeight + 1 }))()
```

```js
// Grid: how many tracks did it resolve to?
getComputedStyle(grid).gridTemplateColumns.split(' ').length
```

## Transitions and timing

```js
// Poll a control through a transition (Install → Uninstall)
(async () => {
  const snap = () => [...document.querySelectorAll('[role=dialog] button')].map(b => b.textContent.trim()).join(',');
  const log = ['t0 ' + snap()]; btn.click();
  for (let i = 1; i <= 16; i++) { await new Promise(r => setTimeout(r, 500)); log.push('t' + i * 0.5 + 's ' + snap()); }
  window.__log = log; return 'ok';
})()
// then read window.__log, collapsed to changes only
```

```js
// Streaming/animation timeline from page show (sample every 60–120ms)
// record: element opacity, words revealed, box opacity; report first/last times
```

```js
// Did a full-screen loading state appear during tab navigation?
(() => {
  window.__seen = []; const strip = document.querySelector('nav[aria-label="Settings"]'); window.__strip = strip;
  new MutationObserver(() => { if (/LoadingBrandText/.test(document.body.innerText)) window.__seen.push(1); })
    .observe(document.body, { childList: true, subtree: true, characterData: true });
  tab.click(); return 'ok';
})()
// later: { stripSameNode: window.__strip === document.querySelector(...), loadingSeen: window.__seen.length > 0 }
```

Mid-close frame: trigger close, screenshot immediately (~80ms), then sweep:
```js
[...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
  return r.width > 40 && r.height > 0 && r.height < 3 && cs.opacity !== '0' && cs.backgroundColor !== 'rgba(0, 0, 0, 0)'; }).length
```

## Input gates

```js
// Grapheme count vs UTF-16 length
(() => { const s = '🙂🙂🙂🙂'; let n = 0; for (const _ of new Intl.Segmenter(undefined, { granularity: 'grapheme' }).segment(s)) n++; return { length: s.length, graphemes: n }; })()
```

## Setting a React-controlled input from a script

```js
(() => { const t = document.querySelector('textarea');
  const set = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
  set.call(t, 'text'); t.dispatchEvent(new Event('input', { bubbles: true })); return t.value.slice(0, 20); })()
```

---

## Browser-automation gotchas (each cost real time)

- **Use the host the dev server expects** (`localhost`, not `127.0.0.1`). Next dev blocks
  cross-origin chunk loads from the other; the page serves 200 and sits on its loading
  shell forever, which looks exactly like a hung server component.
- **Refs shift after every interaction.** Snapshot, click by ref, snapshot again. Filling
  two fields from one snapshot puts both values in the first.
- **Some "find … click" grammars silently do nothing.** If a click produced no network
  request, it did not click. Click by ref or by a locator you have verified.
- **Log in through the auth callback**, not the form, when the app's post-login redirect
  points at a different port (`NEXTAUTH_URL`). `POST /api/auth/callback/credentials`
  with the CSRF token, then read `/api/auth/session`.
- **A screenshot that "hangs"** usually means the browser daemon is busy; the
  measurement `eval` still works. Take the number, then the picture.
- **Restart the dev server after `prisma generate`** — the running process holds the old
  client, so a new column reads as `undefined` and every row falls into the default
  bucket.
- **Restart after `next.config` changes** (redirects are read at boot).
- **A subagent's session dies with the server.** Ask it to report before you restart.
- **Memory.** Three dev servers plus three `tsc --noEmit` on an 8GB laptop is a
  crashloop. One server; `NODE_OPTIONS=--max-old-space-size=8192` for tsc.
