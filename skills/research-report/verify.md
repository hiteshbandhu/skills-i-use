# Verify a long, chart-heavy report

The [`pdf-report`](../pdf-report/) skill covers the general print traps (grid clipping,
fonts, backgrounds, header flags). These are the extra ones that showed up on a 24-page
research report with a dozen charts.

## Look at every page

```bash
pdftoppm -r 50 -png report.pdf pages/p        # one PNG per page
```

Tile them into contact sheets (six across, two down) and read the sheets, then re-render any
suspect page at ~90 dpi. Reading the HTML is not verification — clipping only exists on paper.

## Traps

| Symptom | Cause | Fix |
|---|---|---|
| Rating chips in the last table column cut off at the page edge | chip has `white-space: nowrap` and the table can't shrink the column | `td .chip { white-space: normal; }` |
| Label after an open-ended gantt bar runs off the chart | label placed right of the bar end, past the SVG width | if `bar_end + label_width > svg_width`, anchor the label `end` to the left of the bar |
| Contents page shows numbers for subsections but not sections | page lookup via `pdftotext` misses headings styled uppercase or letter-spaced (`E X E C U T I V E`) | compare lowercased text; hardcode pages that never move (cover 1, contents 2, summary 3) |
| A section heading alone at the bottom of a page, its chart on the next | `break-after: avoid` on headings is not reliably honoured before a figure | `break-before: page` on that heading |
| The same caveat sentence above and below a chart | intro paragraph and figure footnote written separately | keep the footnote, cut the sentence — see "Never add duplication" |

## Two-pass contents page

Render once with placeholder page numbers, find each heading's page with `pdftotext`,
render again with the real numbers. Check the page count did not change between passes.
