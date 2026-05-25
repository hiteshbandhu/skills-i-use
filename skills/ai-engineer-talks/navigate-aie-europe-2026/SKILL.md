---
name: navigate-aie-europe-2026
description: >
  Navigates AI Engineer Europe 2026 keynote themes — MCP and skills, agent
  orchestration, code mode, application layer shifts, judgment vs automation,
  replacing large codebases with skills, and platform talks (Vercel, Cloudflare,
  Anthropic, Cursor, OpenClaw). Use when planning 2026 agent architecture, MCP
  adoption, or skill-first development; or when the user says "AIE Europe 2026",
  "future of MCP", "code mode", "end of apps", "12k LOC skill".
---

# Navigate AIE Europe 2026

Action playbook from fourteen AIE Europe 2026 keynotes. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — workflows A–N
- [source-index.md](source-index.md) — src-NNN → learnings

Optional deliverables: `{SKILL_OUTPUT_DIR}/navigate-aie-europe-2026/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Agent orchestration / AgentCraft                     → A  [src-001]
├─ Agents beyond chat (legal/work UX)                   → B  [src-002]
├─ Quality bar in slop era (pi / craft)                 → C  [src-003, src-010]
├─ Code mode / code-as-interface                        → D  [src-004]
├─ How AI changes engineering (Pragmatic Engineer)      → E  [src-005]
├─ Gemini / DeepMind research direction                 → F  [src-006]
├─ Replace large code with small skills                 → G  [src-007]
├─ Software fundamentals still matter                   → H  [src-008]
├─ OpenClaw / local agent state                         → I  [src-009]
├─ End of apps / new UX containers                      → J  [src-011]
├─ Judgment vs friction (human in loop)                 → K  [src-012]
├─ MCP roadmap & agent stack                            → L  [src-013]
├─ New application layer (Vercel)                       → M  [src-014]
└─ Skills + subagents in products                       → G  [src-007] + [L]
```

Open [workflows.md](workflows.md).

---

## Install

```bash
cp -r skills/navigate-aie-europe-2026 ~/.claude/skills/
cp -r skills/navigate-aie-europe-2026 ~/.cursor/skills/
```

Source: `playlists/aie-europe-2026-keynotes/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| 2026 agents = skills + MCP + production hardening | [src-013 @ 5:31] |
| Load prompts/skills only when user invokes | [src-007 @ 8:39] |
| Code mode: let executable code carry intent | [src-004] |
| Judgment remains human; friction is signal | [src-012] |
| Fundamentals (types, tests) still gate quality | [src-008] |

---

## Output to user

1. Name workflow (A–N) and deliverable
2. Artifacts under `./skill-outputs/navigate-aie-europe-2026/` when requested

---

## Invocation examples

```
@navigate-aie-europe-2026 MCP adoption plan for our agent
should we replace our rules engine with a 200-line skill?
code mode vs tool-calling for our workflow engine
```
