# UI/UX

Product-aware UI review and polish for web apps. Thinks about **what the screen is for**
before nitpicking pixels.

Opinionated defaults: no gradient/glow/purple, animation only when it helps, inline
errors, obvious next actions, accessible primitives.

**Uses Playwright** to open the app, capture screenshots, check console errors, and
smoke-test interactions (scroll, input, menus) — not just static code review.

Output: `./skill-outputs/ui-ux/` (reports + `screenshots/`)

## Modes

| Mode | Use when |
|------|----------|
| **audit** | Review a file, route, or flow — findings + report |
| **polish-pass** | Screenshot + "fix the hero" — minimal targeted diff |
| **pre-ship** | UI-heavy change going out — audit before `@ship-check` |

## Usage

```
@ui-ux review the dashboard sidebar
@ui-ux audit http://localhost:3000/dashboard
polish this — [screenshot]
UX audit src/app/page.tsx — dev server on :3000
don't code — plan only
```

## Playwright

When a dev URL is available, the skill will:

1. Navigate + snapshot (a11y tree)
2. Screenshot at desktop/mobile viewports
3. Check console errors
4. Smoke-test interactions for the scoped screen
5. Re-verify with after-screenshots post-fix

Details: [playwright.md](playwright.md). Requires Playwright MCP or project Playwright setup.

## Principles (high level)

- One primary job per screen
- Obvious next action in every state
- Inline errors, structural skeletons, confirm destructive actions
- `h-dvh`, safe areas, accessible primitives, no layout animations
- Slash/@ menus: compact, scrollable, search when list grows

Full rules: [principles.md](principles.md)

## Files

```
ui-ux/
├── SKILL.md
├── principles.md
├── playwright.md        # browser verification workflow
├── review-checklist.md
├── report-template.md      # markdown record
├── report-template.html    # shareable HTML report w/ embedded screenshots
└── README.md
```

## Pair with

- **`ship-check`** — gate before commit
- **`architecture-review`** — when UX implies a bigger product bet

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
