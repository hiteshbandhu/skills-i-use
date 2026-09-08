# Diagrams For Print

A diagram earns its place when it shows a **mechanism** — a flow, a comparison, a gap.
It does not earn its place as decoration, and a diagram that merely restates the adjacent
sentence costs a page and buys nothing.

Use **inline SVG**. No charting library: for the handful of shapes a report needs, a
library adds a dependency, a load-timing risk and less control. Write the SVG yourself.

---

## Rules that stop diagrams breaking

**Every shape gets an explicit `fill`.** Inherited or default fills render inconsistently
in print. Including `<rect width="100%" height="100%" fill="#FFFFFF"/>` as the first child
guarantees a white ground.

**Leave room in the `viewBox` for outermost labels.** Text at `x` near the viewBox width
gets cut. If your rightmost label sits at `x=700`, the viewBox needs to be ~760 wide.

**Scale by width, never fix a height.**
```css
svg { display: block; width: 100%; height: auto; }
```
Then control the aspect through the `viewBox`. To make a figure shorter so it fits the
space left on a page, reduce the viewBox height and reposition — do not set a CSS height.

**Take colours from the document palette.** Hard-coded hexes drift from the rest of the
page. Keep a mirror of the tokens at the top of the file and use those exact values.

**Give it an `aria-label`** describing what it shows. It costs one attribute and the
document becomes accessible.

**Font sizes inside SVG are in user units, not points.** With a 760-wide viewBox rendered
at 180mm, `font-size="10"` lands around 8pt. Sanity-check by eye in the render — SVG text
too small to read is a common miss.

---

## The four shapes worth having

### 1. Comparison bar — one number against another

The strongest single visual in an audit. Two bars, wildly different lengths, does more
than a paragraph.

```svg
<svg viewBox="0 0 760 168" role="img" aria-label="System A holds 1.72 crore against system B's 12.82 crore">
  <rect width="760" height="168" fill="#FFFFFF"/>
  <text x="0" y="14" font-family="IBM Plex Mono,monospace" font-size="9"
        fill="#9A9A92" letter-spacing="1.3">WHERE THE MONEY ACTUALLY IS</text>

  <text x="0" y="46" font-family="IBM Plex Sans,sans-serif" font-size="11" fill="#4A4A46">CRM · deals marked won</text>
  <rect x="0" y="54" width="94" height="26" fill="#DCDCD6"/>
  <text x="104" y="72" font-family="IBM Plex Mono,monospace" font-size="14" fill="#8A5A16">₹1.72 cr</text>

  <text x="0" y="110" font-family="IBM Plex Sans,sans-serif" font-size="11" fill="#4A4A46">Books · invoices raised</text>
  <rect x="0" y="118" width="700" height="26" fill="#4A5D45"/>
  <text x="10" y="136" font-family="IBM Plex Mono,monospace" font-size="14" fill="#FFFFFF">₹12.82 cr</text>
</svg>
```

Scale bars to the data honestly. A truncated axis in a client document is a credibility
problem, not a design choice.

### 2. Process flow with a marked break

Boxes left to right, arrows between, and **one box styled differently** where the problem
is. The eye lands on the exception immediately.

```svg
<!-- normal step -->
<rect x="0" y="14" width="136" height="86" fill="#FFFFFF" stroke="#ADADA4"/>
<!-- the broken step -->
<rect x="468" y="14" width="136" height="86" fill="#F8F0E1" stroke="#8A5A16" stroke-width="1.4"/>
<!-- arrow: line plus solid triangle -->
<path d="M136 57 h14 M145 53 l9 4 -9 4 z" fill="#ADADA4"/>
```

Add a consistent one-line annotation under each box (`Written: nowhere`) — the repetition
across steps is what makes the gap obvious.

### 3. Completeness bars — what exists versus what is filled in

For "this was built but never used", nothing beats four bars where one is full and three
are empty.

```svg
<text x="0" y="38" font-size="9.5" fill="#4A4A46">Linked to the right deal</text>
<rect x="196" y="28" width="440" height="13" fill="#EDF0EB"/>
<rect x="196" y="28" width="426" height="13" fill="#4A5D45"/>
<text x="648" y="38" font-family="IBM Plex Mono,monospace" font-size="10" fill="#4A5D45">97%</text>

<text x="0" y="62" font-size="9.5" fill="#4A4A46">Owner named</text>
<rect x="196" y="52" width="440" height="13" fill="#F8F0E1"/>
<text x="648" y="62" font-family="IBM Plex Mono,monospace" font-size="10" fill="#8A5A16">0%</text>
```

Keep the empty track visible so the reader sees the full width the bar *could* have been.

### 4. Target architecture — zones, not boxes-and-arrows soup

Three or four labelled zones in a row, each with a heading strip, three lines of content,
and a one-line answer to "what question does this zone answer?". Arrows between carry the
transition condition (`paid`, `done`).

```svg
<rect x="0" y="24" width="230" height="126" fill="#FFFFFF" stroke="#ADADA4"/>
<rect x="0" y="24" width="230" height="19" fill="#F4F4F2"/>   <!-- header strip -->
<text x="10" y="37" font-family="IBM Plex Mono,monospace" font-size="8.4"
      fill="#4A5D45" letter-spacing="1">WIN THE WORK · CRM</text>
```

Highlight the **one** zone that is the crux with a filled background; leave the rest plain.

---

## Colour

Monotone plus one accent plus one warning tone. That is the whole palette.

| Role | Use |
|---|---|
| Greys | Structure, rules, secondary text, "normal" bars |
| Accent | The proposal, the good state, the thing being introduced |
| Warning | The gap, the break, the number that is wrong |

Two disciplines:
- **Never encode meaning in colour alone.** Pair it with a label, a border weight or a
  position. Clients print in greyscale.
- **Avoid default corporate blue.** Pick a hue with some relationship to the subject.

---

## Checking a diagram

- [ ] Nothing clipped at the viewBox edges — check the rightmost and lowest elements
- [ ] Every shape has an explicit `fill`
- [ ] Text legible at final print size, not just on screen
- [ ] Still readable printed in greyscale
- [ ] It shows something the surrounding text does not already say
