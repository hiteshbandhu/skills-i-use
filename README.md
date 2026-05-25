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

The CLI discovers the five top-level skills under `skills/`:

| Skill | Install |
|-------|---------|
| `architecture-review` | `npx skills add hiteshbandhu/skills-i-use --skill architecture-review` |
| `create-a-skill` | `npx skills add hiteshbandhu/skills-i-use --skill create-a-skill` |
| `cto-weekly-review` | `npx skills add hiteshbandhu/skills-i-use --skill cto-weekly-review` |
| `ship-check` | `npx skills add hiteshbandhu/skills-i-use --skill ship-check` |
| `ui-ux` | `npx skills add hiteshbandhu/skills-i-use --skill ui-ux` |

The nested **`skills/ai-engineer-talks/*`** skills are not picked up by the CLI yet — copy or symlink the folder you need into `.cursor/skills/` or `~/.cursor/skills/`. See [`skills/ai-engineer-talks/README.md`](skills/ai-engineer-talks/README.md).

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
| [`ui-ux`](skills/ui-ux/) | Product-aware UI/UX review and polish — Playwright verification, principles, checklist audits. |
| [`create-a-skill`](skills/create-a-skill/) | Author or improve repo skills — hard questions, reviewer subagents, validate, register. **Includes scripts.** |

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
