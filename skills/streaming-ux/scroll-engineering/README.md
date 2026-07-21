# Scroll Engineering

A portable agent skill for auditing a streaming chat UI against the 15-point scroll
engineering checklist — every principle about reader intent, viewport control, layout
stability, and accessibility. Works by reading the scroll/auto-scroll code or observing
live behavior, then scores each principle **pass**, **fail**, or **n/a**, and ranks the
top fixes by user impact.

The north star principle: **never move the reader against their intent.**

Works with **any coding agent**. No vendor-specific API calls. Reads the code you point
it at, or observes a live URL if given browser access.

Output goes in **`./skill-outputs/scroll-engineering/`** — shared root, see
[../../OUTPUT.md](../../OUTPUT.md).

## What it does

```
Scope the interface → read the scroll logic (auto-scroll, jump-to-latest, layout shift)
   → score 15 principles (reader intent, new-turn flow, out-of-view streaming,
     navigation & persistence, layout stability, performance & accessibility)
   → rank fails by pain × (4 − complexity) → top 3 "ship first" fixes → report.md
```

## Install

Copy this folder into your agent's skills directory:

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.cursor/skills/scroll-engineering/` or `.cursor/skills/scroll-engineering/` |
| Claude Code | `~/.claude/skills/scroll-engineering/` |
| Codex | `~/.codex/skills/scroll-engineering/` |

Or: `npx skills add hiteshbandhu/skills-i-use --skill scroll-engineering`

### Output directory

```bash
export SKILL_OUTPUT_DIR=./skill-outputs   # shared root for all skills
# this skill writes to: ./skill-outputs/scroll-engineering/
```

## Usage

```
@scroll-engineering audit the chat scroll behavior in components/research/
review my streaming UI for scroll engineering issues — live at localhost:3000
check if our auto-scroll respects reader intent
scroll engineering audit on this chat interface
does our jump-to-latest work correctly?
audit streaming UX for reader intent violations
```

## Output

| File | Purpose |
|------|---------|
| `report.md` | Scored 15-point table + top 3 ranked fixes (pain × complexity), n/a call-outs |

## Files

```
scroll-engineering/
├── SKILL.md    # Agent workflow — 15-point checklist, scoring, fix ranking
└── README.md
```

## Credit

Checklist derived from [@shadcn's](https://x.com/shadcn/status/2070394918720221522) "What
Makes a Great Streaming Chat Experience" thread (Jun 2026).

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use). Use and adapt freely.
