---
name: build-robotics-ai
description: >
  Runs workflows for robotics/autonomy talks — lab co-scientist loops, Optimus systems latency, kitchen supervised autonomy, Waymo EMMA, GR00T N1 humanoid FM, open $9k humanoids. Use when the user builds robots, humanoids, AV planning, or lab automation agents.
---

# Build robotics AI systems

Action playbook from six AI Engineer / World's Fair talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–F (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/build-robotics-ai/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Closed-loop lab / co-scientist agent                  → A
├─ Humanoid systems performance (latency/data)         → B
├─ Commercial kitchen/service robotics                 → C
├─ AV + VLM planning (Waymo EMMA)                      → D
├─ Adopt humanoid foundation model (GR00T)             → E
└─ Ship affordable open humanoid platform              → F
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/build-robotics-ai ~/.claude/skills/
cp -r skills/build-robotics-ai ~/.cursor/skills/
cp -r skills/build-robotics-ai ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/robotics-autonomy-ai-engineer/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Profile end-to-end control latency | [src-002 @ 7:11] |
| Sim/real eval before planner changes | [src-004 @ 14:16] |
| Teleop safety before full autonomy | [src-006 @ 10:29] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–F; save artifacts to `./skill-outputs/build-robotics-ai/` when requested; do not auto-commit.

---

## Invocation examples

```
@build-robotics-ai humanoid data pipeline architecture
lab agent with live sensors
```
