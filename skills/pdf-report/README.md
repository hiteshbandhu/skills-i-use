# PDF Report

Produce a client-ready PDF — proposal, audit, brief, one-pager — by authoring HTML/CSS and
rendering with headless Chrome.

**Covers the traps that silently ruin print documents**, not just the happy path.

Output: `./skill-outputs/pdf-report/`

## Why

A PDF is not a web page that happens to be saved. Fixed canvas, no scrollbar to rescue
overflow, no second chance once it is emailed. Content that overflows is **cut off at the
page edge without warning** — the reader sees a table missing its last column and concludes
you are sloppy.

The failures are consistent and mostly invisible in the browser:

- **Grid children clip off the right edge.** `min-width: auto` means they refuse to shrink.
  Always `minmax(0, 1fr)`.
- **Backgrounds vanish** without `print-color-adjust: exact`.
- **Fonts fall back to Times** unless Chrome is given `--virtual-time-budget`.
- **`--print-to-pdf-no-header` is silently ignored** in new headless. The flag is
  `--no-pdf-header-footer`.
- **A tall figure jumps a page** and leaves 60% white behind it.

## What is in here

| File | Contents |
|---|---|
| [SKILL.md](SKILL.md) | The process, page budgets, the five failures, evidence discipline |
| [print-css.md](print-css.md) | CSS that behaves differently on paper, with the clipping bugs |
| [render.md](render.md) | Chrome flags, page-count checking, hitting an exact length, safe edit scripts |
| [diagrams.md](diagrams.md) | Inline SVG that survives print — four shapes worth having |
| [document-craft.md](document-craft.md) | Structure, tone, and the evidence rules |
| [template.html](template.html) | A working starter with every trap already handled |

## Quick start

```bash
cp skills/pdf-report/template.html report.html
# edit, then:
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-sandbox --no-pdf-header-footer \
  --virtual-time-budget=15000 \
  --print-to-pdf="Report.pdf" "file://$PWD/report.html"

# check the page count
python3 -c "
import re; d=open('Report.pdf','rb').read()
print('pages:', len(re.findall(rb'/Type\s*/Page[^s]', d)))"
```

Then **look at the rendered pages**. Rendering successfully is not evidence of rendering
correctly.

## The part people skip

Page count is a constraint you design against, not an outcome you discover. A 20-page
document nobody finishes is worth less than a 5-page one they do. When cutting, remove
prose and let diagrams carry the argument — do not shrink type until it is unreadable.

And a client document gets challenged. Separate what you were told from what you
concluded from what you measured, state your limits, verify anything cheaply checkable
before asserting it, and attribute problems to systems rather than to named people.
