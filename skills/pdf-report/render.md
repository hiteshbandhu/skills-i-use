# Rendering And Verifying

## The command

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new \
  --disable-gpu \
  --no-sandbox \
  --no-pdf-header-footer \
  --virtual-time-budget=15000 \
  --print-to-pdf="Report.pdf" \
  "file://$PWD/report.html"
```

Every flag earns its place:

| Flag | Why |
|---|---|
| `--headless=new` | The old headless mode ignores some print flags |
| `--no-pdf-header-footer` | Removes Chrome's date / title / file-path / page-number furniture. **`--print-to-pdf-no-header` is the older name and is silently ignored in new headless** — if you see a file path across the footer, this is why |
| `--virtual-time-budget=15000` | Waits for web fonts and remote assets. Without it the PDF ships in fallback fonts |
| `--disable-gpu --no-sandbox` | Avoids environment-specific failures in CI and containers |

The URL **must** be absolute (`file://$PWD/...`). A relative path renders a blank PDF.

**Expect noise on stderr.** Chrome logs GPU, allocator and web-app-install errors that
have nothing to do with your document. Filter them:

```bash
... 2>&1 | grep -iv "error\|warning\|allocator" | tail -1
```

The line you want is `NNNNN bytes written to file Report.pdf`.

---

## Check the page count without opening it

```bash
python3 -c "
import re
d = open('Report.pdf','rb').read()
print('pages:', len(re.findall(rb'/Type\s*/Page[^s]', d)), '| size:', round(len(d)/1024), 'KB')"
```

The `[^s]` matters — without it you also match `/Type /Pages`, the tree node, and
over-count.

Use this on every render. Page count is the fastest signal that a layout change had a
knock-on effect.

---

## Look at the output. Every time.

**Rendering successfully is not evidence of rendering correctly.** Clipping, bad page
breaks, font fallbacks and empty pages are only visible in the output.

Read the PDF back as images — most agent harnesses render PDF pages visually when you read
the file with a page range. Check:

- [ ] Nothing clipped at the right edge (look at the last item in every row)
- [ ] No page that is mostly white because a figure jumped
- [ ] Headings not stranded at the foot of a page
- [ ] The intended fonts, not Times New Roman
- [ ] Coloured backgrounds present
- [ ] No Chrome header/footer furniture

If you cannot render PDF pages visually, screenshot the HTML at A4 width instead:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --disable-gpu --no-sandbox \
  --window-size=794,1123 --screenshot="page.png" "file://$PWD/report.html"
```

---

## Hitting an exact page count

Page count is a constraint, and you converge on it by adjusting **spacing before type
size**. Shrinking type to fit is the wrong lever — it makes the document worse.

Order of adjustment, from most to least acceptable:

1. **Cut content.** Fewer table rows, shorter footnote, drop a weak paragraph.
2. **Row and cell padding** — `td { padding: 2mm }` → `1.9mm` across 30 rows is ~10mm.
3. **Figure margins** and `figcaption` spacing.
4. **Section header margins.**
5. **Page margins** — 16mm → 15mm gives back ~8mm of height.
6. **Type size** — last resort, and never below 9pt body.

When one page overflows by a little, the spill is often just the footnote. Trimming
its wording is cheaper than restructuring the page.

---

## Patching HTML with a script — do it safely

Reports get revised. When applying edits programmatically:

```python
from pathlib import Path
p = Path("report.html"); s = p.read_text()

def sub(a, b, label):
    global s
    assert a in s, f"MISS: {label}"      # loud when the anchor moved
    s = s.replace(a, b)
    print("ok:", label)

sub("old text", "new text", "what this fixes")
...
p.write_text(s)
```

**The trap:** if `write_text()` is at the end and the script raises on edit 13, the
previous 12 edits are lost — but the log shows twelve `ok:` lines, so it looks like they
applied. You then render, see the old output, and are confused about which change failed.

Two defences:
- Keep the edit batches small, and re-render after each batch.
- Or write the file inside a `try/finally` so partial progress persists.

Always `assert` the anchor exists. A silent no-op `str.replace` is worse than a crash —
it means the fix you think you shipped is not in the file.

---

## Where to put the finished file

Session scratch directories get wiped. Copy the PDF **and its HTML source** somewhere
durable as soon as it is worth keeping:

```bash
cp Report.pdf ~/Downloads/
cp report.html ~/Downloads/Report-source.html
```

Ship the source alongside the PDF. It lets whoever owns the document next fix a typo and
re-render without going back to the author.
