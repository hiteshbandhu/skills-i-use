---
name: build-with-openai
description: >
  Runs OpenAI API workflows for agents, function calling, voice/Realtime, fine-tuning
  (SFT/DPO/RFT), sandboxes, Codex coding agents, and multimodal products. Use when
  building with OpenAI Agents SDK, Realtime API, tool loops, enterprise agent rollout,
  microVM sandboxes, or GPT-4o vision/voice.
---

# Build with OpenAI

Action playbook from twelve OpenAI @ AI Engineer talks. **Do not summarize talks** — pick a workflow theme and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — voice, fine-tuning, function-calling, sandboxes, coding-agents, multimodal, agents-enterprise
- [source-index.md](source-index.md)

Optional deliverables: `./skill-outputs/build-with-openai/`

---

## Step 0 — Pick workflow theme

```
What is the user trying to do?
├─ Tool loops, schemas, parallel calls, RAG-as-tools     → function-calling
├─ SFT / DPO / RFT, graders, shrink prompts             → fine-tuning
├─ Realtime, speech-to-speech, WebRTC vs WebSocket      → voice
├─ Isolate agent code exec, microVMs, RL rewards        → sandboxes
├─ Codex harness, Agents SDK, PR/terminal agents        → coding-agents
├─ Vision, image gen, video frames, GPT-4o modalities   → multimodal
└─ Enterprise pilot, guardrails, co-create UX           → agents-enterprise
```

Open the matching section in [workflows.md](workflows.md).

---

## Install

```bash
cp -r skills/build-with-openai ~/.claude/skills/
cp -r skills/build-with-openai ~/.cursor/skills/
cp -r skills/build-with-openai ~/.codex/skills/
cp -r skills/build-with-openai ~/.agents/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) `playlists/openai-ai-engineer/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Agents = model + instructions + tools + runtime loop | [src-007 @ 0:01] |
| Default 10–20 tools per turn; route if more | [src-004 @ 1:16] |
| Eval tool execution, not just completions | [src-004 @ 1:21] |
| Single agent in prod first; guardrails on edges | [src-002 @ 12:13] |
| Speech-to-speech beats STT→LLM→TTS for latency | [src-008 @ 0:04] |

---

## Output to user

1. Name theme + deliverables
2. Save artifacts under `./skill-outputs/build-with-openai/` when requested
3. Do not auto-commit

---

## Invocation examples

```
@build-with-openai design Realtime voice agent with tool delegation
RFT graders for our support bot tool routing
should we use WebRTC or WebSocket for this voice app?
```
