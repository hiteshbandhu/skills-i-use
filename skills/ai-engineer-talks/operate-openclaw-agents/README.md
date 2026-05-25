# Operate OpenClaw agents

Workflow playbooks for deploying, securing, scaling, and evaluating OpenClaw agents — from six AI Engineer conference talks.

Output: `./skill-outputs/operate-openclaw-agents/` (runbooks, checklists, architecture notes).

## Usage

```
@operate-openclaw-agents personal setup — one channel first
enterprise OpenClaw in containers with secrets
OpenClaw on Kubernetes — one agent per task
triage OpenClaw PRs as a maintainer
```

## What it does

- Routes to **7 workflows** (personal → team Slack agent)
- Ordered steps with citations; deliverables and stop conditions
- Does not summarize talks — executes the matching checklist

## Files

```
operate-openclaw-agents/
├── SKILL.md
├── README.md
└── workflows.md
```

## Install

```bash
cp -r operate-openclaw-agents ~/.claude/skills/
cp -r operate-openclaw-agents ~/.cursor/skills/
cp -r operate-openclaw-agents ~/.codex/skills/
```

Works with any agent that loads a `SKILL.md` folder. Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) playlist `openclaw`.

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
