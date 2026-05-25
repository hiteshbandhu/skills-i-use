# Contributing

Thanks for improving this repo. Keep it practical — if it doesn't help someone ship
better work with an AI agent, it probably doesn't belong here.

---

## What fits here

| Area | Good fit | Poor fit |
|------|----------|----------|
| **Skills** | Repeatable agent workflows you actually use | One-off prompts, chat transcripts |
| **Plugins** | MCP servers, tool integrations with setup docs | Wrappers with no instructions |
| **Examples** | Real configs that work out of the box | Placeholder folders |

**Skills first.** That's where most value lives today. Plugins and examples are welcome
when they're as concrete as the skills.

Fork freely for your own taste. PRs back here should benefit others, not just your setup.

---

## Design principles (non-negotiable)

1. **Agent-agnostic** — subagents, shell, markdown. No vendor-specific APIs unless there's a documented fallback.
2. **Shared output root** — every skill writes to `{SKILL_OUTPUT_DIR}/{skill-name}/`. See [skills/OUTPUT.md](skills/OUTPUT.md).
3. **Progressive disclosure** — slim `SKILL.md` (orchestration); details in sibling files (`principles.md`, `scripts/`, templates).
4. **Explicit triggers** — YAML `description` must say what the skill does and when to use it (third person).
5. **Safe defaults** — never auto-commit, auto-push, or exfiltrate secrets. Ask before destructive actions.

---

## Skill folder layout

```
skills/my-skill/
├── SKILL.md              # required — workflow + frontmatter
├── README.md             # required — human overview, install, usage
├── principles.md         # optional — rules the agent reads when needed
├── report-template.md    # optional — output format
└── scripts/              # optional — runnable collectors/checks
```

### `SKILL.md` frontmatter

```yaml
---
name: my-skill
description: >
  What it does and when to trigger it. Include natural phrases users say.
  Third person. Specific, not vague.
---
```

### Register new skills

1. Add the folder under `skills/`
2. Add a row to the skills table in [README.md](README.md)
3. Add the output subfolder to the layout in [skills/OUTPUT.md](skills/OUTPUT.md) if applicable
4. Note any cross-skill links (e.g. reads another skill's `index.md`)

Or run **`@create-a-skill`** to author a skill interactively — it handles registry updates.

---

## Quality bar

Before opening a PR:

- [ ] `SKILL.md` is under ~250 lines — extract detail to supporting files
- [ ] Description includes **what** + **when** (trigger phrases)
- [ ] Output path follows `skill-outputs/{skill-name}/`
- [ ] Scripts run locally without hardcoded personal paths (`~/Developer/...`)
- [ ] No API keys, tokens, or `.env` contents
- [ ] README explains install path (`~/.claude/skills/`, `~/.cursor/skills/`, or project copy)

**Optional but valued:** smoke-test the skill in at least one agent (Cursor, Claude Code, Codex).

---

## Pull requests

- **One skill per PR** — easier review, cleaner history
- **Commit style:** `feat: add my-skill`, `fix: ship-check secret scan`, `docs: …`
- **Scope:** one concern per commit within the PR when possible
- Small fixes to existing skills (typos, clearer steps) — single PR is fine

Describe in the PR:

1. What workflow this automates
2. Example invocation (`@my-skill …`)
3. What you tested

---

## Install (for contributors testing locally)

Copy or symlink into your agent's skills directory:

```bash
SKILLS_REPO="/path/to/skills-i-use/skills"

# one skill
ln -sfn "$SKILLS_REPO/ship-check" ~/.claude/skills/ship-check

# or all skills
for skill in "$SKILLS_REPO"/*/; do
  ln -sfn "$skill" "$HOME/.claude/skills/$(basename "$skill")"
done
```

Same pattern for `~/.cursor/skills/`.

---

## What we won't merge

- Vendor-locked skills with no generic fallback
- Skills that write artifacts all over the project root
- Megabyte SKILL.md files — split them
- Generated reports, `skill-outputs/` from your machine, or session logs
- AI-slop READMEs — match the tone of existing skills

---

## Questions?

Open an issue with the workflow you're trying to capture. Sometimes a skill isn't the
right shape — a short example or plugin might fit better.

MIT license — contributions follow the same license as the repo.
