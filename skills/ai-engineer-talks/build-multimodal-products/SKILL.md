---
name: build-multimodal-products
description: >
  Runs workflows for multimodal AI products — realtime voice latency, tiny VLMs, SSM streams, unbounded UX design, dataset hierarchy, AI education. Use when the user builds voice bots, edge vision, multimodal UX, or says "multimodal product", "voice latency", "Moondream".
---

# Build multimodal products

Action playbook from six AI Engineer / World's Fair talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–F (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/build-multimodal-products/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Ship realtime voice agent                           → A
├─ Deploy edge/tiny vision (Moondream-class)           → B
├─ Long multimodal streams (SSM)                       → C
├─ Design unbounded multimodal UX                      → D
├─ Build training/eval datasets                          → E
└─ EdTech multimodal literacy                            → F
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/build-multimodal-products ~/.claude/skills/
cp -r skills/build-multimodal-products ~/.cursor/skills/
cp -r skills/build-multimodal-products ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/multimodality-aie-world-s-fair-2024/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Measure time-to-first-audio | [src-001 @ 9:28] |
| Show model limits in UX | [src-004 @ 14:11] |
| Dataset legal/diversity before scale | [src-005 @ 1:38] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–F; save artifacts to `./skill-outputs/build-multimodal-products/` when requested; do not auto-commit.

---

## Invocation examples

```
@build-multimodal-products design voice agent under 500ms
multimodal UX without form fields
```
