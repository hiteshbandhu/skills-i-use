---
name: build-with-deepmind
description: >
  Builds products on Google DeepMind Gemini, Gemma, Nano, Live agents, proactive
  async agents, and edge deployment. Use when integrating Gemini API, Gemma open
  models, Android on-device AI, conversational/voice agents, agent manager patterns,
  or edge Gemma inference.
---

# Build with DeepMind

Action playbook from nine Google DeepMind @ AI Engineer talks. **Do not summarize talks** — pick a workflow theme and execute it.

**Supporting files:**
- [workflows.md](workflows.md)
- [source-index.md](source-index.md)

Optional: `./skill-outputs/build-with-deepmind/`

---

## Step 0 — Pick workflow theme

```
What is the user trying to do?
├─ Gemini API / Gemini 3 / multimodal generation     → gemini-api
├─ Gemma open models, fine-tune, self-host           → gemma-open
├─ Android on-device Gemini Nano                     → gemini-nano
├─ Voice / Live conversational agents                → live-agents
├─ Proactive async coding agents (Jules patterns)    → proactive-agents
├─ Agent manager / browser / IDE control plane         → agent-manager
├─ Edge Gemma deployment                             → edge-ai
└─ Train/serve diffusion image/video at scale          → generative-scale
```

Open [workflows.md](workflows.md) for the matching section.

---

## Install

```bash
cp -r skills/build-with-deepmind ~/.claude/skills/
cp -r skills/build-with-deepmind ~/.cursor/skills/
cp -r skills/build-with-deepmind ~/.codex/skills/
cp -r skills/build-with-deepmind ~/.agents/skills/
```

Source: `playlists/google-deepmind-ai-engineer/` in [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Track Gemini model + API + app releases together | [src-001 @ 0:04:53] |
| Eval tool-calling when upgrading Gemini generations | [src-002 @ 0:02:12] |
| Match Gemma size to device latency budget | [src-003 @ 0:01:28] |
| Live API for realtime voice; batch API for async | [src-005 @ 0:09:04] |
| Log proactive agent actions for trust | [src-006 @ 0:09:00] |

---

## Output to user

1. Name theme + deliverables
2. Save artifacts under `./skill-outputs/build-with-deepmind/` when requested
3. Do not auto-commit
