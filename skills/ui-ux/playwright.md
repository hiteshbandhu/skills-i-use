# UI/UX — Playwright Verification

Use Playwright to **see and interact with the UI**, not just read code. Run this during
Step 1b (after loading context) and again after Step 3 (implement) to verify fixes.

**Preferred:** Playwright MCP tools (`browser_navigate`, `browser_snapshot`,
`browser_take_screenshot`, `browser_click`, `browser_type`, `browser_resize`,
`browser_console_messages`).

**Fallback:** project Playwright test suite (`npx playwright test`) or CLI if MCP
unavailable — note reduced coverage in the report.

---

## When to run

| Mode | Playwright |
|------|------------|
| **audit** | Yes — full snapshot + interaction checks |
| **polish-pass** | Yes — before and after screenshots at stated viewport |
| **pre-ship** | Yes — smoke + console error check |
| **review-only / don't code** | Yes for audit; skip re-verify after implement |

Skip only if: no runnable URL, user says "code review only", or app requires auth
you don't have — then note "Playwright skipped" in report.

---

## Step A — Resolve target URL

1. Ask user for URL if not obvious, OR infer:
   - Next.js / Vite default: `http://localhost:3000` + route path
   - Check `package.json` `dev` script for port
2. If server not running — start it (`npm run dev`, etc.) and wait until ready
3. Record base URL and route in the report

---

## Step B — Viewports

Test at least the viewport user cares about. Default both if unspecified:

| Name | Size |
|------|------|
| desktop | 1280 × 800 |
| mobile | 390 × 844 |

Use `browser_resize` before each pass.

Save screenshots to:
`{output_dir}/screenshots/[slug]-[viewport]-[before|after]-YYYY-MM-DD.png`

---

## Step C — Capture

For each viewport:

1. **Navigate** to the target route
2. **Snapshot** — accessibility tree for structure, labels, focus order
3. **Screenshot** — full page or element for visual review
4. **Console** — `browser_console_messages` level `error`; flag any errors/warnings

Compare snapshot + screenshot against [principles.md](principles.md).

---

## Step D — Interaction smoke (scope-dependent)

Run checks relevant to the screen. Examples:

| Flow | Playwright action | Pass criteria |
|------|-------------------|---------------|
| Scroll | scroll main content area | No nested scroll trap; reaches bottom |
| Chat input | type multiline text, paste | Newlines preserved; input grows |
| Slash / @ menu | open command menu | Visible, scrollable, not wider than input |
| Primary CTA | click main button | Navigates or submits with feedback |
| Form error | submit empty required field | Inline error, focus moves to field |
| Destructive | click delete (staging only) | Confirmation dialog appears |
| Loading | hard refresh | Skeleton or content, not blank flash |

Use snapshot to find element refs before click/type. Prefer role-based targets
(`button`, `textbox`, `link`) over brittle CSS.

Do not run destructive actions on production URLs.

---

## Step E — Document findings

Add a **Playwright verification** section to the report:

```markdown
## Playwright verification

| Viewport | URL | Console errors | Screenshot |
|----------|-----|----------------|------------|
| desktop | /dashboard | 0 | [link](screenshots/...) |

### Interaction results
- Scroll: PASS / FAIL — [note]
- Input paste: PASS / FAIL — [note]
```

Failures here can be **Critical** severity even if code review looked fine.

---

## Step F — Re-verify after fixes

After Step 3 (implement):

1. Re-navigate to same URL + viewports
2. New **after** screenshots
3. Re-run failed interaction checks only
4. Confirm console clean (or explain remaining warnings)

Report before/after screenshot paths in the final summary.

---

## Auth & staging

- If route requires login — ask user for test credentials, staging URL, or auth cookie approach
- Never paste real credentials into the report file
- Prefer local dev or explicit staging over production

---

## Quick MCP sequence (reference)

```
browser_resize → browser_navigate → browser_snapshot
browser_take_screenshot → browser_console_messages (error)
[interactions] → browser_snapshot → browser_take_screenshot
```

If the dev server is on the user's machine, MCP browser must reach `localhost` —
confirm connectivity; use `--host 0.0.0.0` on dev server if needed.
