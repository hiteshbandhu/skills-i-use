# Spec-Grounded Design

A portable agent skill for grounding an integration in **reality before writing code**.
It pulls the actual spec, probes the live endpoint to capture how the API *really*
behaves, reconciles spec-vs-reality (reality wins), and produces a **design contract** —
verified facts, deltas, edge cases, and invariants — that you build and test against.

The discipline: **read the protocol, then test live before assuming the spec is correct.**
Reverse-engineered and stale docs lag the real API; the live probe is non-negotiable.

Works with **any coding agent** that can fetch docs and run a shell. No vendor-specific
API calls of its own.

Output goes in **`./skill-outputs/spec-grounded-design/`** — shared root, see [../OUTPUT.md](../OUTPUT.md).

## What it does

```
Scope the integration → pull the primary source (real spec) → probe the live endpoint
   → reconcile (reality wins) → design contract: facts, deltas, edge cases, invariants → index.md
```

## Why it exists

The expensive bug is the one you design in before the first real call: code written
against an assumed or stale spec that breaks the moment it meets the live API. This skill
forces a **live probe** — force the real 404, capture the real response shape, observe the
real session behavior — and turns what it finds into invariants that seed the test suite.

## Install

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.cursor/skills/spec-grounded-design/` or `.cursor/skills/spec-grounded-design/` |
| Claude Code | `~/.claude/skills/spec-grounded-design/` |
| Codex | `~/.codex/skills/spec-grounded-design/` |

Or: `npx skills add hiteshbandhu/skills-i-use --skill spec-grounded-design`

### Output directory

```bash
export SKILL_OUTPUT_DIR=./skill-outputs   # shared root for all skills
# this skill writes to: ./skill-outputs/spec-grounded-design/
```

## Usage

```
@spec-grounded-design we're integrating the MCP streamable-HTTP transport — read the protocol and verify before we build
design against the Stripe subscriptions API — is the spec right?
how does this API actually behave on an expired session? probe it first
ground this OAuth flow in the real endpoint before I write the client
```

## Output

| File | Purpose |
|------|---------|
| `contract-<date>-<target>.md` | Verified facts, spec-vs-reality deltas, edge cases, invariants |
| `index.md` | Registry of contracts, newest first |

## Safety

- Probes **read-only** against production; never mutates prod to "test."
- Never writes secrets into the contract or saved output — credentials referenced by name.

## Cross-skill integration

- **`chat-failure-audit`** → failures traced to "the API didn't behave as expected" point here.
- **`architecture-review`** → when the probe surfaces a real build-vs-buy or two-mechanism fork.
- **`state-lifetime-decision`** → when the integration introduces persisted state (sessions, cursors).

## Files

```
spec-grounded-design/
├── SKILL.md                     # Agent workflow
├── grounding-checklist.md       # What to verify live, probe patterns, reality-wins rule
├── design-contract-template.md  # Contract output format
└── README.md
```

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use). Use and adapt freely.
