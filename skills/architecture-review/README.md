# Architecture Review

A portable agent skill for structured architecture decisions. Instead of a single
opinionated answer, it runs debating persona subagents — then synthesizes a signed
ADR, updates a decision registry, and optionally produces a visual HTML report.

Works with **any coding agent** that can run subagents. No vendor-specific API calls.

Output goes in **`./skill-outputs/architecture-review/`** — same shared root as all
skills in this repo. See [../OUTPUT.md](../OUTPUT.md).

## What it does

```
User question → Elicit constraints → persona subagents debate → Synthesis
    → Markdown ADR → (optional HTML) → index.md registry
```

| Persona | Lens | Always? |
|---------|------|---------|
| **Pragmatist** | Ships fast, low ops risk, boring proven tech | Yes |
| **Architect** | Long-term maintainability, evolvability, clean abstractions | Yes |
| **Contrarian** | Hidden assumptions, underestimated options, second-order effects | Yes |
| **SRE** | On-call burden, observability, incident response, ops cost | Optional — auto-included for infra-heavy decisions |

## Install

Copy this folder into your agent's skills directory:

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.cursor/skills/architecture-review/` or `.cursor/skills/architecture-review/` |
| Claude Code | `~/.claude/skills/architecture-review/` |
| Codex | `~/.codex/skills/architecture-review/` |

### Output directory

```bash
export SKILL_OUTPUT_DIR=./skill-outputs   # shared root for all skills
# this skill writes to: ./skill-outputs/architecture-review/
```

Override for one run: `"save to docs/decisions"` (full path) or relocate the shared root.

## Usage

```
@architecture-review should I use FTS5 or pgvector for legal search?
include SRE — managed Postgres vs self-hosted
ADR only
```

## Output

| File | Purpose |
|------|---------|
| `ADR-0001-my-decision.md` | Git-friendly signed ADR with debate summary |
| `ADR-0001-my-decision.html` | Visual report (skipped in ADR-only mode) |
| `index.md` | Registry table linking all ADRs, newest first |

## Cross-skill integration

ADRs recorded here are automatically picked up by **cto-weekly-review** when you run
a weekly report — they appear in the Key decisions section for that week.

## Files

```
architecture-review/
├── SKILL.md          # Agent workflow
├── personas.md       # Persona + synthesis prompts
├── adr-template.md   # Markdown ADR format
└── README.md
```

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use). Use and adapt freely.
