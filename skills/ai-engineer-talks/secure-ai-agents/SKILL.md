---
name: secure-ai-agents
description: >
  Security workflows for AI agents: OAuth/MCP identity, enterprise CIAM, tool/API
  red teaming, code sandboxes, GenAI fuzzing, Azure PyRIT scans, prompt injection
  drills, web AI bot policy, confidential inference patterns. Use when hardening
  agents, MCP servers, coding agents, or public apps against agent abuse.
---

# Secure AI agents

Action playbook from eleven Security @ AI Engineer talks. **Do not summarize talks** — pick a workflow and execute it.

**Supporting files:**
- [workflows.md](workflows.md) — workflows A–G (steps, deliverables, stop conditions)
- [source-index.md](source-index.md) — src-001…src-011 → learnings

Optional deliverables: `{SKILL_OUTPUT_DIR}/secure-ai-agents/` — see [skills-i-use OUTPUT.md](https://github.com/hiteshbandhu/skills-i-use/blob/main/skills/OUTPUT.md).

---

## Step 0 — Pick workflow

```
What is the user trying to secure?
├─ MCP / OAuth / user-delegated agent access     → A
├─ Multi-tool agent before launch (IDOR, SSRF)   → B
├─ Enterprise B2B agent identity & delegation    → C
├─ Agent that runs shell/code (Codex-style)      → D
├─ Pre-prod brittleness / harm / injection       → E
├─ Public site cost & crawler abuse              → F
└─ Remote inference with privacy guarantees      → G
```

Open [workflows.md](workflows.md) for the chosen letter.

---

## Install

```bash
cp -r skills/secure-ai-agents ~/.cursor/skills/
cp -r skills/secure-ai-agents ~/.codex/skills/
cp -r skills/secure-ai-agents ~/.claude/skills/
```

From [skills-i-use](https://github.com/hiteshbandhu/skills-i-use) or ingest-into-skills after sync.

Source corpus: `playlists/security-ai-engineer/` in [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills).

---

## Output to user

1. Name the workflow (A–G) and deliverables you are producing
2. Save checklists/threat models under `./skill-outputs/secure-ai-agents/` when the user wants files
3. Do not auto-commit

---

## Invocation examples

```
@secure-ai-agents OAuth for our MCP server and token exchange
@secure-ai-agents red-team our agent tools before launch
@secure-ai-agents sandbox and network policy for coding agent
```
