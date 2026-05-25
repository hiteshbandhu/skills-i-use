---
name: ship-ai-as-pm
description: >
  Runs PM workflows from World's Fair talks — AI PM role, knife-fight strategy, ship-to-user focus, uncertain capabilities, expert systems, domain experts, agent coordination platforms, post-engineer orgs, taste-led UX. Use when the user is an AI PM, founder, or shipping AI product strategy.
---

# Ship AI as PM

Action playbook from nine AI Engineer / World's Fair talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files** (read when needed):
- [workflows.md](workflows.md) — workflows A–I (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-NNN → talk learnings in ingest-into-skills

Optional: `{SKILL_OUTPUT_DIR}/ship-ai-as-pm/`

---

## Step 0 — Pick workflow

Use the decision tree below. Open the matching section in [workflows.md](workflows.md).

```
What is the user trying to do?
├─ Define AI PM role / ownership                         → A
├─ Competitive strategy (knife fight, moats)             → B
├─ Ship to real users fast                               → C
├─ Roadmap under capability uncertainty                  → D
├─ Expert-in-the-loop vertical product                   → E
├─ Domain expert + eval ownership                        → F
├─ Agent coordination in work tools                      → G
├─ Post-engineer engineering org                         → H
└─ Taste-led UX (anti-slop)                              → I
```

**Stop summarizing** once a workflow is identified — run its checklist.

---

## Install

```bash
cp -r skills/ship-ai-as-pm ~/.claude/skills/
cp -r skills/ship-ai-as-pm ~/.cursor/skills/
cp -r skills/ship-ai-as-pm ~/.codex/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills (`playlists/product-management-ai-engineer-world-s-fair/`).

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Ship to someone weekly beats platform build | [src-005 @ 0:19] |
| Evals as discovery under uncertainty | [src-004 @ 9:03] |
| Experts own rubrics in verticals | [src-006 @ 7:26] |

Disputed steps: see [source-index.md](source-index.md). Name workflow A–I; save artifacts to `./skill-outputs/ship-ai-as-pm/` when requested; do not auto-commit.

---

## Invocation examples

```
@ship-ai-as-pm AI product strategy for crowded market
roadmap when we dont know model limits
```
