---
name: navigate-aiewf-2024-keynotes
description: >
  Navigates AI Engineer World's Fair 2024 keynote themes—LLM product discipline,
  copilots, multimodal APIs, enterprise agents, local inference, realtime data,
  and platform second-order effects. Use when planning AIEWF takeaways, auditing
  LLM team practices, or choosing vendor/platform direction from 2024 keynotes.
---

# Navigate AIEWF 2024 keynotes

Action playbook from fifteen World's Fair 2024 keynotes. **Do not summarize talks** — pick a workflow theme and execute it.

**Supporting files:**
- [workflows.md](workflows.md)
- [source-index.md](source-index.md)

Optional deliverables: `./skill-outputs/navigate-aiewf-2024-keynotes/`

---

## Step 0 — Pick workflow theme

```
What is the user trying to do?
├─ Team operating model, evals, data literacy           → product-discipline
├─ Copilots in dev platforms, assistant eval loops      → copilots-platforms
├─ Multimodal / Anthropic / knowledge assistants        → models-vendors
├─ Local CPU inference, edge-friendly distribution    → local-inference
├─ Live data for agents, accidental platformization     → data-platforms
├─ Enterprise agents, Hypermode-style backends          → agents-enterprise
└─ Strategy, education, hardware (MAX, decoder)         → strategy-craft
```

Open the matching section in [workflows.md](workflows.md).

---

## Install

```bash
cp -r skills/navigate-aiewf-2024-keynotes ~/.claude/skills/
cp -r skills/navigate-aiewf-2024-keynotes ~/.cursor/skills/
cp -r skills/navigate-aiewf-2024-keynotes ~/.codex/skills/
cp -r skills/navigate-aiewf-2024-keynotes ~/.agents/skills/
```

Source: [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills) `playlists/keynote-aie-world-s-fair-2024/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Evals + data literacy are core AI engineer skills, not optional | [src-001 @ 0:20:18] |
| Look at production data before scaling agent autonomy | [src-001 @ 0:24:04] |
| Copilots must live in existing dev workflows with telemetry | [src-003 @ 0:10:00] |
| Model churn requires per-vendor eval regression | [src-005 @ 0:22:00] |
| Second-order UX/trust effects matter as much as time saved | [src-009 @ 0:12:00] |

---

## Output to user

1. Name theme + deliverables
2. Save artifacts under `./skill-outputs/navigate-aiewf-2024-keynotes/` when requested
3. Do not auto-commit

---

## Invocation examples

```
@navigate-aiewf-2024-keynotes apply lessons-from-a-year eval operating model
Which keynote themes matter for our enterprise agent rollout?
Map Anthropic vs OpenAI multimodal choices from AIEWF keynotes
```
