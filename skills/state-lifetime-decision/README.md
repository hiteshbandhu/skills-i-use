# State-Lifetime Decision

A portable agent skill for deciding the **right home for a new piece of state** — its
scope (turn → step → chat → user-session → user → org → global) and its durability
(ephemeral → TTL'd → durable → log) — as an explicit decision instead of a reflex. It
then forces the four checks that turn into incidents when skipped: **isolation,
staleness/invalidation, growth bound, and cache cost** — and names the tradeoff.

The premise: **state is a product decision wearing a systems costume.** Where it lives and
how long it lasts is what the user feels — does it remember me, across chats, on my other
device, without leaking to anyone else.

Works with **any coding agent**. No vendor-specific API calls. Reasons about your app's
state and stores.

Output goes in **`./skill-outputs/state-lifetime-decision/`** — shared root, see [../OUTPUT.md](../OUTPUT.md).

## What it does

```
Name the state → pick scope (narrowest useful) → pick durability (cost-of-loss)
   → run the four checks (isolation, staleness, growth, cache) → name the tradeoff
   → State Decision Record → index.md
```

## Why it exists

The wrong home for state is a whole class of bug: it **forgets too soon** (scope too
narrow), **leaks across users** (no isolation), **grows unbounded** (no bound), or **serves
stale** (no invalidation). Picking a store before deciding scope × durability is how those
ship. This skill puts the decision first.

## Install

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.cursor/skills/state-lifetime-decision/` or `.cursor/skills/state-lifetime-decision/` |
| Claude Code | `~/.claude/skills/state-lifetime-decision/` |
| Codex | `~/.codex/skills/state-lifetime-decision/` |

Or: `npx skills add hiteshbandhu/skills-i-use --skill state-lifetime-decision`

### Output directory

```bash
export SKILL_OUTPUT_DIR=./skill-outputs   # shared root for all skills
# this skill writes to: ./skill-outputs/state-lifetime-decision/
```

## Usage

```
@state-lifetime-decision the model searched up some tools — where should that live, and for how long?
should this be per-chat or per-user? and what TTL?
where does this go — redis, db, or memory?
how long should we remember the user's last filter?
```

## Output

| File | Purpose |
|------|---------|
| `sdr-<date>-<state>.md` | State Decision Record: scope, durability, store, key, the four checks, tradeoff |
| `index.md` | Registry of decisions, newest first |

## Cross-skill integration

- **`friction-audit`** → auto-paths that introduce or change persisted state hand off here.
- **`chat-failure-audit`** → failures classed as state/lifetime bugs hand off here.
- **`spec-grounded-design`** → integrations that introduce state (sessions, cursors) hand off here.
- **`architecture-review`** → when the decision is really an architecture fork (new store, migration).

## Files

```
state-lifetime-decision/
├── SKILL.md                       # Agent workflow
├── decision-grid.md               # scope × durability grid, store mapping, the four checks
├── decision-record-template.md    # State Decision Record format
└── README.md
```

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use). Use and adapt freely.
