---
name: pdf-report
description: >
  Produce a client-ready PDF — proposal, audit, brief, one-pager — by authoring HTML/CSS
  and rendering with headless Chrome. Covers the print-CSS traps that silently clip content,
  inline SVG diagrams that survive print, hitting an exact page count, and the evidence
  discipline that keeps a client document defensible. Triggers on "make a PDF", "client
  proposal", "audit report", "one-pager", "deck for the client", "print this", "turn this
  into a document", "5 page report", "professional report".
  Use when the deliverable leaves your team — a document a client, board or admin reads.
  Not for READMEs, internal notes, or web pages that stay on screen.
---

# PDF Report — Client Documents That Survive Contact With A Printer

A PDF is not a web page that happens to be saved. It has a fixed canvas, no scrollbar to
rescue overflow, no hover to hide detail behind, and no second chance once it is emailed.
Content that overflows is **silently cut off at the page edge** — the reader sees a table
missing its last column and assumes you are sloppy.

This skill is the pipeline (HTML → headless Chrome → PDF), the traps that cost real
rework, and the content rules that keep a client document defensible when someone
challenges a number in it.

**Supporting files:**
- [print-css.md](print-css.md) — the CSS that behaves differently on paper, and the clipping bugs
- [diagrams.md](diagrams.md) — inline SVG that survives print, and when a diagram earns its place
- [render.md](render.md) — the Chrome pipeline, exact flags, and how to verify the output
- [document-craft.md](document-craft.md) — structure, audience, and evidence discipline
- [template.html](template.html) — a working starter with the traps already handled

Output: `{SKILL_OUTPUT_DIR}/pdf-report/` — see [../OUTPUT.md](../OUTPUT.md)

---

## When NOT to use this

- **It stays on screen.** A web page, dashboard or artifact wants different craft — use `ui-ux`.
- **It is internal.** A note for your own team does not need a cover, sources or page discipline.
- **Someone must edit it.** If the client will rewrite half of it, send the source format they
  use. A PDF is a final form, not a working draft.
- **It is one paragraph.** Say it in the message.

---

## The process

### 1. Decide the page budget first

The page count is a **hard constraint you design against**, not an outcome you discover.
It changes what the document can be:

| Pages | What fits | What it is |
|---|---|---|
| 1 | One argument, one diagram, five numbers | A one-pager that gets read in a meeting |
| 4–6 | One idea per page, diagram-led | A brief an executive actually finishes |
| 12–20 | Sections, contents page, worked examples | A reference document people dip into |

A 20-page document nobody reads is worth less than a 5-page one they finish. If you are
asked to cut length, **cut prose and let diagrams carry the argument** — do not shrink type
until it is unreadable.

### 2. Establish the reader before writing a word

Ask, or decide explicitly and say so:

- **Who reads this?** A technical lead and a non-technical admin need different documents.
  For a non-technical reader, define every term of art the first time it appears, and put a
  short glossary near the front.
- **What must they do after reading?** Approve something, confirm something, decide
  something. That action belongs in the document, near the end, stated plainly.
- **What will they push back on?** Pre-answer it with evidence. "No new software needed"
  invites "are you sure?" — so check the licence tier and print the answer.

### 3. Author HTML, not a PDF library

Write a single `.html` file with inline `<style>`. Reasons: you can see it in a browser
instantly, the CSS is real CSS, and diagrams are inline SVG you fully control. PDF
libraries (reportlab, fpdf) cost more effort for a worse result on anything with layout.

Read [print-css.md](print-css.md) **before** writing the CSS. The grid-overflow trap in
there has cost multiple rebuild cycles and is invisible in the browser.

### 4. Render, then look at it

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
  --virtual-time-budget=15000 \
  --print-to-pdf="Report.pdf" "file://$PWD/report.html"
```

Then **actually look at the rendered pages** — read the PDF back as images. Do not trust
that it rendered correctly because the HTML was well-formed. Clipping, page breaks and
font fallbacks are only visible in the output. See [render.md](render.md).

### 5. Fix in one pass, re-render, stop

Look → list every problem → fix them together → re-render → verify once. Do not iterate
one fix at a time; each render cycle is slow and the reader is waiting.

---

## The five failures that actually happen

**1. Right-edge clipping from grid children.**
CSS grid items default to `min-width: auto` and refuse to shrink below their content. On a
fixed page they overflow the printable width and the right-hand item loses its border —
or its whole column — off the page edge. Always `minmax(0, 1fr)`, never bare `1fr`.

**2. Backgrounds and colours dropping out.**
Print stylesheets strip background colours by default. Without
`print-color-adjust: exact` your coloured callouts, filled table headers and chart bars
render white on white.

**3. A figure alone on an empty page.**
`break-inside: avoid` on a tall figure pushes it whole to the next page, leaving 60% of
the previous page blank. Either shrink the figure to fit the remaining space, or move it
to the top of the next section deliberately.

**4. Web fonts silently falling back.**
Headless Chrome will render before Google Fonts arrive unless you give it
`--virtual-time-budget`. The PDF then ships in Times New Roman and looks amateur. Always
declare a real fallback stack too.

**5. Edit scripts that lose their work.**
When patching HTML with a script, `assert` each replacement matched, and **write the file
after each change or in a way that survives a mid-script failure**. A script that applies
twelve edits and crashes on the thirteenth before `write_text()` loses all twelve, and the
failure looks like the edits were applied.

---

## Evidence discipline

A client document gets challenged. Every number in it should survive the question
"how do you know that?"

- **Separate what you were told, what you concluded, and what you measured.** Keep them
  visually distinct in the document. A reader who cannot tell your inference from your
  measurement will not trust either.
- **State the limits.** Sample sizes, what you could not access, where a match is probable
  rather than confirmed. A limits paragraph makes the rest more credible, not less.
- **Verify before asserting.** If you can check a claim with one API call or one query,
  check it. Asserting something the client knows is wrong costs the whole document.
- **Do not name individuals as the problem.** Attribute to roles, systems and processes.
  "Records are assigned to a closed account" not "X never cleaned up their leads." A named
  person in a client document turns a systems review into a performance review.
- **Check whether a pattern has a boring explanation** before presenting it as a finding.
  One account owning thousands of records usually means an integration authenticating as
  that user — not a heroic employee. Ask the obvious question first.

Read [document-craft.md](document-craft.md) for structure, tone and the sections a
client document needs.

---

## Design defaults that read as professional

- **Monotone plus one or two accents.** A grey scale with a single considered accent
  colour, plus one semantic warning tone, reads more expensive than a palette. Avoid
  corporate blue; pick something specific to the subject.
- **Three type roles.** A serif for headings (authority), a humanist sans for body
  (legibility at small sizes), a mono for numbers and labels (alignment, and it signals
  "measured"). Set `font-variant-numeric: tabular-nums` anywhere digits stack.
- **Let structure encode meaning.** Numbered sections only if order matters. A coloured
  edge only on the thing that needs attention. If every block has a border and a shadow,
  nothing stands out.
- **9–10pt body on A4.** Smaller reads as dense and cheap; larger wastes the page budget.
- **Print in greyscale before sending.** Many clients do. If your amber warning and your
  green success become the same grey, the document stops working.
