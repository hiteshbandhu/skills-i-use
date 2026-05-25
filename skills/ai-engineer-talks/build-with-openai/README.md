# Build with OpenAI

Workflow playbooks distilled from twelve OpenAI talks at AI Engineer: function calling, fine-tuning, voice/Realtime, sandboxes, Codex, multimodal, and enterprise agents.

Output: `./skill-outputs/build-with-openai/`

## Usage

```
@build-with-openai set up tool loop with parallel function calls
pick SFT vs RFT for our 80-example routing task
```

## What it does

- Routes to **7 workflow themes** (see [workflows.md](workflows.md))
- Checklists with citations to per-talk learnings
- Agent deliverables and stop conditions per theme

## Files

```
build-with-openai/
├── SKILL.md          # ≤90 lines — decision tree
├── README.md
├── workflows.md      # Themed workflows
└── source-index.md
```

## Install (agent-agnostic)

```bash
cp -r skills/build-with-openai ~/.claude/skills/
cp -r skills/build-with-openai ~/.cursor/skills/
cp -r skills/build-with-openai ~/.codex/skills/
cp -r skills/build-with-openai ~/.agents/skills/
```

Works with any agent that loads a directory containing `SKILL.md`. Source: `playlists/openai-ai-engineer/` in [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills).

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
