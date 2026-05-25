---
name: architect-enterprise-ai
description: >
  Runs enterprise AI architecture playbooks from AI Architects @ AI Engineer —
  AI architect role, agent platforms, voice agents, agent auth (CIAM), trusted
  inference, team structure, monetization, and product survival. Use when designing
  org-wide AI systems, agent platforms, or CIO-ready inference; or when the user says
  "AI architect", "enterprise agents", "CIAM for agents", "AI that pays", "build-operate divide".
---

# Architect enterprise AI

Action playbook from nineteen AI Architect track talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — workflows A–M
- [source-index.md](source-index.md) — src-NNN → learnings

Optional deliverables: `{SKILL_OUTPUT_DIR}/architect-enterprise-ai/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Define AI architect role & stack choices              → A  [src-015, src-009]
├─ Ship agents that work in production                   → B  [src-003, src-010]
├─ Build agentic platform (Box-style)                  → C  [src-004, src-005]
├─ Voice agents                                          → D  [src-006]
├─ Agent identity / authZ (CIAM)                       → E  [src-007]
├─ CIO-trusted inference & telemetry                     → F  [src-008]
├─ Browser-as-runtime for agents                         → G  [src-019]
├─ Developer experience (AX)                             → H  [src-002]
├─ Revenue / ROI proof (healthcare RCM)                  → I  [src-001]
├─ Feedback loops & learning products                    → J  [src-011, src-013]
├─ Monetization & GTM for AI                             → K  [src-014, src-012]
├─ Modern AI team structure                              → L  [src-016]
├─ Product strategy / knife fight                        → M  [src-017, src-018]
```

Open [workflows.md](workflows.md).

---

## Install

```bash
cp -r skills/architect-enterprise-ai ~/.claude/skills/
cp -r skills/architect-enterprise-ai ~/.cursor/skills/
```

Source: `playlists/ai-architects-ai-engineer/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| AI architect owns integration, tools, embeddings, vector DB | [src-015 @ 9:41] |
| Agents need production design patterns, not demos | [src-010] |
| Feedback loops beat one-shot prompts for quality | [src-011] |
| AuthN/AuthZ for agents is a first-class concern | [src-007] |
| Bridge build vs operate for AI product vision | [src-018] |

---

## Output to user

1. Name workflow (A–M) and deliverable
2. Artifacts under `./skill-outputs/architect-enterprise-ai/` when requested

---

## Invocation examples

```
@architect-enterprise-ai define our AI architect scope
agent auth model for enterprise SaaS
prove ROI for our AI inference platform
```
