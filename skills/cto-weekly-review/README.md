# CTO Weekly Review

A portable agent skill that generates a deep, founder-grade weekly engineering report —
not just commit counts.

It treats git history, AI agent session logs, shell history, and file timestamps as a
behavioral dataset and produces **markdown + HTML** reports you can share or print to PDF.

Output goes in **`./skill-outputs/cto-weekly-review/`** — same shared root as all skills.
See [../OUTPUT.md](../OUTPUT.md).

## Scripts

This skill includes shell scripts under `scripts/`. **Read every script before running
it.** They read local data — git history across repos, AI session logs, shell history,
file timestamps, and optional GitHub CLI output. Review paths, env vars (`SINCE`, `ME`,
`REPOS`, `SEARCH_ROOT`), and scope before execution. Do not run blindly.

## What it produces

- **Working hour heatmap** — commits + file edits + AI sessions
- **Focus session analysis** — deep work vs quick fixes vs context switching
- **Sustainability health score** — tunable weights in `scoring.md`
- **Commit quality breakdown** — feat/fix/refactor/experiment by size
- **AI leverage ratio** — AI-adjacent commits and token efficiency
- **Repo intelligence** — per-repo velocity, top files, active days
- **Cross-skill ADR linking** — pulls decisions from `architecture-review` index
- **Written narrative** — shipped, in-progress, blockers, next week
- **Content seeds** — LinkedIn angles from real data

## Install

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.cursor/skills/cto-weekly-review/` |
| Claude Code | `~/.claude/skills/cto-weekly-review/` |
| Codex | `~/.codex/skills/cto-weekly-review/` |

```bash
export SKILL_OUTPUT_DIR=./skill-outputs
```

## Usage

```
give me a weekly review
what did I build this week
weekly digest, last 14 days
markdown only — skip HTML
```

## Workflow

```
Scope → 3 parallel collector subagents → Signal processing → Narrative
    → weekly-YYYY-MM-DD.md + .html → index.md
```

| Subagent | Script | Collects |
|----------|--------|----------|
| Git Collector | `scripts/collect-git.sh` | Commits, stats, heatmap, sessions, deps |
| AI Collector | `scripts/collect-ai-sessions.sh` | Claude/Cursor/Codex session logs |
| Context Collector | `scripts/collect-context.sh` | Shell history, file edits, GitHub CLI |

## Output

| File | Purpose |
|------|---------|
| `weekly-2026-05-24.md` | Git-friendly summary (always written) |
| `weekly-2026-05-24.html` | Visual report with charts |
| `index.md` | Registry of all weekly reports |

## Requirements

- Any coding agent with shell + subagent support
- `git` (required)
- `python3` — for AI log parsing and gh JSON (optional but recommended)
- `gh` CLI — optional, for PR/issue data

Works on macOS and Linux.

## Files

```
cto-weekly-review/
├── SKILL.md                 # Orchestration workflow
├── scripts/
│   ├── collect-git.sh       # Git activity collector
│   ├── collect-ai-sessions.sh
│   └── collect-context.sh   # Shell, fs, GitHub
├── scoring.md               # Health score weights (tune here)
├── report-template.md       # HTML structure and design
├── weekly-template.md       # Markdown output format
├── data-sources.md          # AI log reference
└── README.md
```

## Cross-skill integration

When `skill-outputs/architecture-review/index.md` exists, this skill automatically
includes ADRs from the report week in the **Key decisions** section and Decisions table.

Run `@architecture-review` during the week → ADRs appear in your next weekly review.

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use). Use and adapt freely.
