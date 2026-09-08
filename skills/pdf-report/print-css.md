# Print CSS — What Behaves Differently On Paper

Everything here is a real failure, not a precaution. Each one renders fine in a browser
and breaks in the PDF.

---

## 1. The grid overflow that clips your right edge

**The single most expensive bug in print layout.**

Grid and flex children default to `min-width: auto`, which means they will not shrink
below their content's intrinsic width. On a scrolling web page this produces a horizontal
scrollbar you notice. On a fixed page it produces **content sliced off at the paper edge**
— usually the right-hand card in a row, missing its border or its last column.

```css
/* BROKEN — the third item slides off the page */
.cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm; }

/* CORRECT */
.cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4mm; }
.cards > * { min-width: 0; }
```

Apply to **every** grid and flex container in a print document, including two-column
layouts and any row with a fixed-width sidebar:

```css
.row { display: grid; grid-template-columns: 6mm minmax(0,1fr) minmax(0,1.2fr); }
.issue { display: grid; grid-template-columns: 5mm minmax(0,1fr) 28mm; }
```

**How to spot it:** the last element in a row has no right border, or a table's final
column is missing. It is not a rendering glitch — it is overflow.

---

## 2. Colour is stripped unless you insist

```css
body {
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
```

Without this, background fills on callouts, table headers, chart bars and status pills all
render as white. The layout survives; the meaning does not.

---

## 3. Page setup

```css
@page { size: A4; margin: 15mm 15mm 12mm; }
```

- Set `size` explicitly — do not inherit Letter/A4 from the renderer's locale.
- 15mm side margins is a good default. Below 12mm looks cramped; above 20mm wastes the
  page budget.
- The printable width for A4 at 15mm margins is **180mm**. Any element wider than that
  overflows.

---

## 4. Page breaks

```css
.page { page-break-after: always; }
.page:last-child { page-break-after: auto; }

h2, h3, h4 { break-after: avoid; }              /* never a heading alone at the foot */
table, figure, .card, .callout { break-inside: avoid; }
```

**The trade-off:** `break-inside: avoid` on a tall figure will push the whole figure to the
next page, leaving most of the previous page blank. When that happens, either shrink the
figure's `viewBox` height so it fits the space remaining, or restructure so it opens a
section.

Wrap each page in an explicit `<section class="page">` when you want deterministic pagination
— one section per page, and you always know what is where.

---

## 5. Units: mm for layout, pt for type

```css
padding: 4mm 4.5mm;   /* layout — thinks in paper */
font-size: 9.6pt;     /* type — thinks in print */
```

Avoid `px` and `rem` in a print stylesheet. They work, but every size decision then needs
mental conversion and the numbers stop being meaningful.

**Type scale that works on A4:**

| Role | Size |
|---|---|
| Document title | 28–32pt |
| Section heading | 17–20pt |
| Subheading | 9.5–10.5pt |
| Body | 9–10pt |
| Table / caption | 8–8.5pt |
| Label / eyebrow | 6.5–7.5pt uppercase, letter-spaced |

Below 7pt is unreadable when printed, however good it looks on a retina screen.

---

## 6. Web fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=…&display=swap">
```

```css
--fd: "Spectral", Georgia, serif;                        /* display */
--fb: "IBM Plex Sans", "Helvetica Neue", Arial, sans-serif; /* body */
--fm: "IBM Plex Mono", "SF Mono", Menlo, monospace;      /* data */
```

Two rules:
1. **Always give a real fallback stack.** If the font fails, you want Georgia, not whatever
   the renderer picks.
2. **Give Chrome time to fetch them** — `--virtual-time-budget=15000`. Without it the PDF
   renders in fallbacks and you may not notice until a client mentions it.

---

## 7. Tables

```css
table { border-collapse: collapse; width: 100%; font-size: 8.5pt; }
th {
  text-align: left; font-weight: 400;
  font-family: var(--fm); font-size: 6.8pt;
  letter-spacing: .1em; text-transform: uppercase;
  border-bottom: .8pt solid var(--rule-hard);
  padding: 0 4mm 2mm 0;
}
td { padding: 2mm 4mm 2mm 0; border-bottom: .4pt solid var(--rule); vertical-align: top; }
td.n { font-family: var(--fm); font-variant-numeric: tabular-nums; white-space: nowrap; }
```

- **Horizontal rules only.** Vertical borders and zebra striping make a print table noisy.
- `vertical-align: top` — mixed-length cells look broken when centred.
- `tabular-nums` on any numeric column, so digits align down the page.
- Constrain the first column with `style="width:30%"` when the content is uneven; auto
  layout gives long text too much and numbers too little.

---

## 8. Hairlines

Sub-point borders render inconsistently. Use these and they hold:

```css
--hairline: .4pt;   /* table row separators */
--rule: .75pt;      /* box borders */
--strong: 1.2pt;    /* section underline */
--heavy: 2pt;       /* accent edge, top of a card */
```

Never go below `.4pt` — some renderers drop it entirely.

---

## 9. Status pills and fixed-width labels

Uppercase letter-spaced mono text is **much wider than it looks**. A pill reading
`PARTLY WORKING` at 6.4pt needs about 30mm. If the grid column is 22mm, the text clips —
and because it is the last column, it clips off the page.

```css
.pill {
  font-family: var(--fm); font-size: 6.4pt;
  letter-spacing: .08em; text-transform: uppercase;
  border: .5pt solid currentColor; padding: .6mm 1.4mm;
  text-align: center; white-space: nowrap;
}
```

Either size the column generously, or shorten the label. `PARTLY` beats a clipped
`PARTLY WORKI`.

---

## 10. Single theme, painted explicitly

A PDF has no dark mode. Do not write `prefers-color-scheme` blocks — but **do** paint
every colour explicitly, including `body { background: #FFFFFF }`. Never rely on an
inherited or default colour.

---

## Starter block

```css
:root{
  --paper:#FFFFFF; --sunk:#F4F4F2;
  --ink:#1A1A18; --ink-mid:#4A4A46; --ink-soft:#6E6E68; --ink-faint:#9A9A92;
  --rule:#DCDCD6; --rule-hard:#ADADA4;
  --accent:#4A5D45; --accent-bg:#EDF0EB;   /* pick per subject, not blue-by-default */
  --warn:#8A5A16;  --warn-bg:#F8F0E1;
}
@page{ size:A4; margin:15mm 15mm 12mm; }
*{ box-sizing:border-box }
body{
  background:var(--paper); color:var(--ink);
  font-family:var(--fb); font-size:9.6pt; line-height:1.5; margin:0;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
}
.page{ page-break-after:always }
.page:last-child{ page-break-after:auto }
h2,h3,h4{ break-after:avoid }
table,figure,.card,.callout{ break-inside:avoid }
.cols2{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:7mm }
.cols3{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:4mm }
.cols2>*,.cols3>*{ min-width:0 }
```
