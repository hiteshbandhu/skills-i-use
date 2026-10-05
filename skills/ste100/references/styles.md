# Visual styles: Hairline and Blueprint minimalism

[diagrams.md](diagrams.md) says *what* to draw. This file says *how it looks*.
Use a visual only when it carries information the text cannot carry as well.
When a picture is not necessary, do not draw one.

| Style | Use it for | Color |
|---|---|---|
| **Hairline** | One idea, one object: a concept figure, a hero image, an explainer figure for a single mechanism | Monochrome greys + one bright stroke. Optional: one accent hue for the bright stroke. |
| **Blueprint minimalism** | Systems with parts, sizes, and relations: architecture, layouts, specs, exploded views | Two colors only: line color and ground color (blue on white or white on blue) |

Both styles use thin lines, no fills, no gradients, no shadows, and no
decoration. The difference: Hairline has **no words in the drawing**.
Blueprint **labels and dimensions everything**.

---

## Hairline

Source: Hairline by Lucas Marques — https://hairline.lucasmarkes.com
(MIT, npm `@lucasmarkes/hairline`, rules in the repo at
`skills/hairline-create/rules.md`). The original figures are interactive: they
react to the pointer. The rules below keep the look and apply it to static SVG
too (for PDFs and reports). For interactive Hairline figures, use the author's
own skill: `npx skills add lucasmarkes/hairline`, then `/hairline-create <idea>`.

### The look

- **Isometric 2:1 view.** Objects are small 3D solids seen from above at 45°. ViewBox 400 × 320, object centered near (200, 166).
- **One stroke width: 0.9 px.** No other weights.
- **A grey ramp of four steps.** These are the Hairline defaults (light theme):

  | Token | Light | Role |
  |---|---|---|
  | `--hl-plate` | `#ffffff` | Ground. Also the fill of solids, so near solids hide far lines |
  | `--hl-hi` | `#232327` | The **one** bright stroke: the thing that matters |
  | `--hl-edge` | `#a4a4ac` | Silhouettes |
  | `--hl-mid` | `#c3c3c9` | Secondary strokes, inner creases |
  | `--hl-lo` | `#e0e0e4` | Receding or inactive parts, guides |

  For dark mode, reverse the ramp: dark plate, light `hi`.
- **With color (variant):** keep the greys and change only `--hl-hi` to one accent hue. Everything else stays grey. Never add a second hue. (This variant is not part of Hairline itself.)

### The rules (adapted from Hairline's ten rules)

1. **The stroke is the only highlight.** No fills, glows, shadows, opacity effects, or extra weights. Exactly **one** place is bright, and it means one thing.
2. **Bright outside, dim inside.** A solid is its silhouette (`edge`) plus one dim crease (`mid`) a little inside the top edge. Do not draw vertical corner lines. A box never shows 12 edges.
3. **Round every corner.** No sharp corners. Draw less.
4. **No words in the figure.** No text, digits, arrows, icons, or logos inside the drawing. Show identity with geometry: a notch, a row of dots, a bright edge. Names go **outside**, in a caption or a key. Number parts with dots (●, ●●, ●●●) and name them in the caption. This matches S1000D callouts and STE rule 8.3: "the queue (3)".
5. **Honest construction.** Solids are opaque, filled with the plate color. Paint back to front. A far edge never shows through a near solid. Dashed guides go behind the plate they belong to.
6. **Rest is composed, never flat.** The still image is the thumbnail. Give it a shape (a slope, a lean, a slight explode), not a flat regular grid. Put the bright stroke where the eye must start.
7. **It must read at 240 px wide.** If you cannot name the object at thumbnail size, simplify it. Max about 100 solids, no part smaller than 10 viewBox units.
8. **One figure, one idea.** If the figure needs a label to make sense, the concept is not ready.
9. **Motion (interactive only):** a choice gets a 700 ms ease-out `cubic-bezier(.32,.72,0,1)`; pointer following gets a spring (k 100, c 18, m 1); motion spreads out from the pointer with a 30–60 ms stagger per step of distance; nothing moves offscreen; respect `prefers-reduced-motion`.

### Use Hairline when

- A section explains **one** mechanism or object (a rate limiter, a queue, a vault, a branch).
- The text around it does the explaining, and the figure gives the mental model.
- Not for: data with values, multi-part architecture with many named parts, anything that needs labels to be correct.

---

## Blueprint minimalism

There is no single formal standard for this style. It takes the visual grammar
of engineering drawings, defined in **ISO 128** (lines), **ISO 3098**
(lettering), **ISO 129** (dimensioning), and **ISO 7200** (title block), and
removes everything that is not necessary.

### The look

- **Two colors.** Choose one:
  - *Blueprint:* ground `#0f3b73` (deep blue), lines and text `#e8f0ff`.
  - *Whiteprint:* ground `#fbfcfe`, lines and text `#1d4f91`.
  - A third color is permitted for **one** thing only (a red revision mark or the changed part). Same rule as Hairline: one highlight, one meaning.
- **Grid.** A faint square grid behind everything: minor lines every 8 px at about 8% opacity, major lines every 40 px at about 15%. The grid shows scale and alignment. It is never darker than the drawing.
- **Lettering.** Monospace or a technical sans (ISO 3098 style): uppercase for labels and titles, one size for labels and one for titles. All text horizontal.
- **Flat orthographic views** (top, front, side) or isometric. Do not mix the two in one figure.

### Line types (ISO 128, simplified)

Each line type has one meaning. Use two weights only: thick ≈ 2 × thin.

| Line | Weight | Meaning | Software use |
|---|---|---|---|
| Continuous | thick (1.5 px) | Visible outline | Component boundaries |
| Continuous | thin (0.75 px) | Dimension lines, leaders, hatching | Connections, callout leaders |
| Dashed | thin | Hidden or internal edges | Internal or private parts, async paths |
| Dash-dot (chain) | thin | Centre lines, symmetry, paths of motion | Main data path, axis of a flow |
| Dash-dot, thick at the ends | thin | Cutting plane (section) | "Section A-A": a zoomed detail of one part |

### Elements

- **Callouts:** small circles with a number, on a thin leader line with a dot or a short tick at the part. The key or the text names them: "the scheduler (4)".
- **Dimensions:** use them to show quantities: latency, size, limits, counts. A dimension line has end ticks (or small arrowheads) and the value above the line: `├── 120 ms ──┤`. This is where blueprint style shines for software: put the numbers *on* the drawing.
- **Detail views:** a circle on the main view labeled "A", and an enlarged "DETAIL A" next to it.
- **Section views:** cut through a part to show inside. Hatch the cut faces with thin 45° lines.
- **Title block** (ISO 7200, minimal), bottom-right: title, drawing number or figure number, date (ISO 8601), revision, author, scale (or "not to scale"). In a report, the figure caption can do this job.
- **Revision marks:** a small triangle with the revision letter beside the changed part.

### Rules

1. Every line type has one meaning, and the legend says what it is.
2. Max two line weights. Max two colors (+ one highlight color).
3. Every number has a unit (`20 ms`, `4 GB`), SI style with a space.
4. Labels are outside the shapes, on leaders, or in a key. Do not put long text inside boxes.
5. Align everything to the grid. Orthogonal lines only, except leaders.
6. White space is part of the drawing. Leave about 10% of the frame empty at each edge.

### Use Blueprint when

- The reader needs the parts, how they connect, and the numbers (sizes, limits, timings).
- Architecture diagrams, network layouts, data pipelines, hardware, exploded views, spec sheets.
- Not for: a single idea that one object shows better (use Hairline), or charts of data (use standard chart rules).

---

## Choosing, with STE

- **Text first.** Write the STE text. Then ask: which sentence is still hard? Draw for that sentence only.
- **Same names.** The caption, the callouts, and the text use the same terms (STE rule 1.11).
- **Captions in STE:** "Figure 3: The rate limiter (1) stops requests after the bucket (2) is empty." One sentence, 25 words max.
- **Print and PDF:** both styles print well. For print, use Whiteprint (blue lines on white) or Hairline light. Check that the thinnest line is still visible at 100% zoom in the PDF. If not, use 0.75 pt minimum for print.
