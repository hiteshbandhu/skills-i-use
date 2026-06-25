# skills-i-use

A curated collection of skills, plugins, and tools that I use in my day-to-day workflow as a developer.

Built by [@hiteshbandhu](https://github.com/hiteshbandhu) — open for anyone to use, fork, or build on.

---

## Install with `npx skills`

Install skills into Cursor (and 50+ other agents) using the [Agent Skills CLI](https://github.com/vercel-labs/skills) ([skills.sh](https://skills.sh)):

```bash
# List installable skills from this repo
npx skills add hiteshbandhu/skills-i-use --list

# Install one skill into the current project
npx skills add hiteshbandhu/skills-i-use --skill ship-check

# Install globally (available across all projects)
npx skills add hiteshbandhu/skills-i-use --skill ship-check -g

# Target Cursor explicitly
npx skills add hiteshbandhu/skills-i-use --skill ship-check -a cursor

# Search the public skills directory
npx skills find ship check
```

The CLI discovers **43 skills** — nine core skills under `skills/` plus **34** in the [`ai-engineer-talks`](skills/ai-engineer-talks/) bundle (via [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json)):

```bash
# List all skills (core + ai-engineer-talks, grouped in output)
npx skills add hiteshbandhu/skills-i-use --list

# Install an AI engineer talks skill
npx skills add hiteshbandhu/skills-i-use --skill build-rag-search-stacks -a cursor
```

| Skill | Install |
|-------|---------|
| `architecture-review` | `npx skills add hiteshbandhu/skills-i-use --skill architecture-review` |
| `chat-failure-audit` | `npx skills add hiteshbandhu/skills-i-use --skill chat-failure-audit` |
| `create-a-skill` | `npx skills add hiteshbandhu/skills-i-use --skill create-a-skill` |
| `cto-weekly-review` | `npx skills add hiteshbandhu/skills-i-use --skill cto-weekly-review` |
| `friction-audit` | `npx skills add hiteshbandhu/skills-i-use --skill friction-audit` |
| `raise-pr` | `npx skills add hiteshbandhu/skills-i-use --skill raise-pr` |
| `ship-check` | `npx skills add hiteshbandhu/skills-i-use --skill ship-check` |
| `spec-grounded-design` | `npx skills add hiteshbandhu/skills-i-use --skill spec-grounded-design` |
| `state-lifetime-decision` | `npx skills add hiteshbandhu/skills-i-use --skill state-lifetime-decision` |
| `ui-ux` | `npx skills add hiteshbandhu/skills-i-use --skill ui-ux` |

Full index of the **ai-engineer-talks** bundle: [`skills/ai-engineer-talks/README.md`](skills/ai-engineer-talks/README.md).

After install, invoke a skill with `@skill-name` in chat or `/skill-name` in Agent mode.

---

## What's in here

| Folder | What it contains |
|--------|-----------------|
| `skills/` | Reusable skill definitions and workflow prompts for AI agents |
| `plugins/` | Integrations, MCP servers, and tool extensions *(coming soon)* |
| `examples/` | Working configs and usage walkthroughs *(coming soon)* |

---

## Skills

Skill definitions that extend AI agents with specialised workflows. Each skill writes
output to `./skill-outputs/{skill-name}/` in your project (configurable via
`SKILL_OUTPUT_DIR`). See [skills/OUTPUT.md](skills/OUTPUT.md).

| Skill | What it does |
|-------|-------------|
| [`architecture-review`](skills/architecture-review/) | Structured ADR process — subagent persona debate, markdown ADR, optional HTML, decision registry. |
| [`cto-weekly-review`](skills/cto-weekly-review/) | Deep weekly engineering report — parallel data collectors, markdown + HTML, links ADRs from architecture-review. **Includes scripts.** |
| [`ship-check`](skills/ship-check/) | Pre-ship gate — lint, typecheck, tests, build, diff review, commit message draft. Never commits without confirmation. **Includes scripts.** |
| [`raise-pr`](skills/raise-pr/) | Change → merged PR — follows the repo's own commit/branch convention, drafts the PR body from the diff, watches CI, squash-merges when green. Direct-to-main / artifact / red-merge are hard gates. General/portable; optionally pairs with ship-check. |
| [`ui-ux`](skills/ui-ux/) | Product-aware UI/UX review and polish — Playwright verification, principles, checklist audits. |
| [`create-a-skill`](skills/create-a-skill/) | Author or improve repo skills — hard questions, reviewer subagents, validate, register. **Includes scripts.** |
| [`chat-failure-audit`](skills/chat-failure-audit/) | Turn a real transcript into a ranked, root-caused failure list — symptom → cause → layer, six failure classes, frequency × severity. |
| [`friction-audit`](skills/friction-audit/) | Find every place a flow makes the user do work the system could — classify the friction, design the automatic path, keep destructive actions safe. |
| [`spec-grounded-design`](skills/spec-grounded-design/) | Ground an integration in reality before coding — pull the spec, probe the live endpoint, reconcile (reality wins), output a design contract. |
| [`state-lifetime-decision`](skills/state-lifetime-decision/) | Decide where new state lives — scope × durability — with isolation, staleness, growth-bound, and cache checks, then name the tradeoff. |

#### Product-method pipeline

Four of the core skills chain into one workflow for shipping the *right* thing without
friction: **`chat-failure-audit`** (find what's broken) → **`friction-audit`** (remove the
friction) → **`spec-grounded-design`** (ground the fix in real API behavior) →
**`state-lifetime-decision`** (decide any new state) → **`architecture-review`** (for real
forks). Each hands off to the next; use them standalone or end-to-end.

### Skills with scripts

Three skills ship shell scripts under `scripts/`. **Always read a script before running it** — review paths, env vars, and side effects. Do not run blindly.

| Skill | Scripts | What they touch |
|-------|---------|-----------------|
| [`cto-weekly-review`](skills/cto-weekly-review/) | `collect-git.sh`, `collect-ai-sessions.sh`, `collect-context.sh` | Git repos, AI session logs, shell history, file timestamps, optional `gh` |
| [`ship-check`](skills/ship-check/) | `ship-check.sh` | Project lint/typecheck/test/build commands, git status/diff |
| [`create-a-skill`](skills/create-a-skill/) | `validate-skill.sh` | Skill folder structure and conventions (read-only checks) |

Each scripted skill documents its scripts in its README. When an agent proposes running one, double-check the command first.

### AI engineer talks

**34 skills** from [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) — full index in [`skills/ai-engineer-talks/README.md`](skills/ai-engineer-talks/README.md).

Topics include RAG, evals, agents, harnesses, OpenAI/DeepMind/Microsoft, AIEWF 2024 tracks, Summit 2023, Europe 2026 keynotes, security, legal AI, OpenClaw, PM/leadership, inference, robotics, generative media, skills/MCP, and more.

From [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills); [create-a-skill](skills/create-a-skill/) hygiene before sync.

---

## Plugins

Integrations and extensions for various tools. Each plugin lives in its own subfolder with setup instructions. *(Placeholder — contributions welcome.)*

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for skill conventions, PR expectations, and quality bar.
PRs welcome — keep it practical.

---

## License

[MIT](LICENSE)
