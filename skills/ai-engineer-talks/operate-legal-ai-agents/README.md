# Operate legal AI agents

Workflow playbooks for vertical legal AI: artifact-first collaboration, tabular review, skills on agent work nodes, and verifier's-rule task design (Legora / AI Engineer).

Output: `./skill-outputs/operate-legal-ai-agents/`

## Usage

```
@operate-legal-ai-agents design contract review UX beyond chat
map which legal tasks agents can own vs lawyer-only
```

## What it does

- Routes to **6 workflows** (task mapping → fixing chat-only agents)
- Step-by-step actions with talk citations
- Agent deliverables and stop conditions per workflow

## Files

```
operate-legal-ai-agents/
├── SKILL.md
├── README.md
├── workflows.md
└── source-index.md
```

## Install (agent-agnostic)

Copy the folder into whichever agent loads `SKILL.md` directories:

```bash
# from ingest-into-skills repo root
cp -r skills/operate-legal-ai-agents ~/.claude/skills/
cp -r skills/operate-legal-ai-agents ~/.cursor/skills/
cp -r skills/operate-legal-ai-agents ~/.codex/skills/
cp -r skills/operate-legal-ai-agents ~/.agents/skills/
```

After sync to [skills-i-use](https://github.com/hiteshbandhu/skills-i-use), same paths under your skills root.

Source corpus: `playlists/ai-in-law-legal-ai-engineer/` in [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills).

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
