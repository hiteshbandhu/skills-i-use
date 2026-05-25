# Navigate AIEWF 2024 keynotes

Workflow playbooks from fifteen AI Engineer World's Fair 2024 keynotes: LLM product discipline, copilots, multimodal vendors, local inference, realtime data, and enterprise agents.

Output: `./skill-outputs/navigate-aiewf-2024-keynotes/`

## Usage

```
@navigate-aiewf-2024-keynotes team eval charter from lessons-from-a-year talk
second-order effects checklist for our AI feature launch
```

## What it does

- Routes to **7 workflow themes** (see [workflows.md](workflows.md))
- Checklists with citations to per-talk learnings
- Agent deliverables and stop conditions per theme

## Files

```
navigate-aiewf-2024-keynotes/
├── SKILL.md
├── README.md
├── workflows.md
└── source-index.md
```

## Install (agent-agnostic)

```bash
cp -r skills/navigate-aiewf-2024-keynotes ~/.claude/skills/
cp -r skills/navigate-aiewf-2024-keynotes ~/.cursor/skills/
cp -r skills/navigate-aiewf-2024-keynotes ~/.codex/skills/
cp -r skills/navigate-aiewf-2024-keynotes ~/.agents/skills/
```

Source: `playlists/keynote-aie-world-s-fair-2024/` in [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills).
