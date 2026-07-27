# Skill Output Convention

All skills in this repo write artifacts to a **shared root folder**. Each skill owns
a named subfolder — no scattered `./reports/`, `./adrs/`, or skill-specific paths at
project root.

## Layout

```
{SKILL_OUTPUT_DIR}/
├── architecture-review/
│   ├── index.md
│   ├── ADR-0001-my-decision.md
│   └── ADR-0001-my-decision.html
├── cto-weekly-review/
│   ├── index.md
│   └── weekly-2026-05-24.html
├── ship-check/
│   ├── index.md
│   └── ship-check-2026-05-24-1430.md
├── ui-ux/
│   ├── index.md
│   ├── review-2026-05-24-hero.md
│   └── screenshots/
├── create-a-skill/
│   ├── index.md
│   └── design-2026-05-24-my-skill.md
├── cross-model-review/
│   ├── index.md
│   ├── pr-161-diff.patch
│   └── review-2026-05-24-pr-161.md
├── operate-openclaw-agents/
├── build-rag-search-stacks/
├── run-llm-evals/
├── secure-ai-agents/
├── build-agent-harnesses/
├── operate-legal-ai-agents/
├── build-with-openai/
│   └── index.md, runbooks, checklists per skill
└── scroll-engineering/
    └── report.md
```

## Resolution order

Every skill resolves its output directory the same way:

| Priority | Source | Result |
|----------|--------|--------|
| 1 | User says "save to `path/to/dir`" | That path (skill subfolder optional if user gives full path) |
| 2 | `$SKILL_OUTPUT_DIR` environment variable | `{SKILL_OUTPUT_DIR}/{skill-name}/` |
| 3 | Default | `./skill-outputs/{skill-name}/` |

Create the directory if it does not exist.

## Environment variable

```bash
export SKILL_OUTPUT_DIR=./skill-outputs   # default; override to relocate all skills at once
```

## Per-skill index

Each skill maintains `{output_dir}/index.md` — a registry of everything it has
generated in that project. Newest entries first.

## .gitignore (consumer projects)

Add to your project if you do not want to commit generated artifacts:

```
skill-outputs/
```

Or commit ADRs and ignore HTML — your call.

## Cross-skill integration

Skills in this repo can read each other's output registries:

- **cto-weekly-review** reads **architecture-review** `index.md` and links ADRs from the report week into its Decisions section.
- **ship-check** pairs with **ui-ux** pre-ship mode — UI audit first, then ship gate before commit.
- **create-a-skill** registers new skills in README and OUTPUT.md; run **ship-check** before committing skill PRs.
- **ingest-into-skills** → **ai-engineer-talks**: must pass create-a-skill `validate-skill.sh` before `sync-skills.sh` (ingest `docs/PUBLISH.md`).

Both skills share the same `{SKILL_OUTPUT_DIR}` root — no scattered output folders.
