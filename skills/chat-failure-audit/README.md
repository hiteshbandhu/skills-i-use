# Chat Failure Audit

A portable agent skill that turns a **real user transcript or agent session** into a
ranked, root-caused list of failure modes. Instead of "the model was wrong," it pushes
every symptom to the system behavior that caused it and the layer that owns the fix —
then ranks by frequency × severity so you fix what actually hurts.

The discipline: **ground every finding in the actual session, and always push past the
symptom to the cause.**

Works with **any coding agent**. No vendor-specific API calls. Reads the transcript or
log you provide.

Output goes in **`./skill-outputs/chat-failure-audit/`** — shared root, see [../OUTPUT.md](../OUTPUT.md).

## What it does

```
Get the real session → walk the turns, mark breakdowns → symptom → root cause → layer
   → classify (6 classes) + rate freq × severity → ranked fix list → index.md
```

| Failure class | What it means |
|---------------|---------------|
| **Capability gap** | the system genuinely can't do it yet |
| **Friction** | it can, but made the user do avoidable work |
| **State / lifetime bug** | state kept at the wrong scope or dropped across a boundary |
| **Grounding / confabulation** | answered from nothing, stale, or the wrong source |
| **Recovery gap** | a recoverable error surfaced as a dead-end |
| **UX dead-end** | failed/emptied with no next step |

## Install

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.cursor/skills/chat-failure-audit/` or `.cursor/skills/chat-failure-audit/` |
| Claude Code | `~/.claude/skills/chat-failure-audit/` |
| Codex | `~/.codex/skills/chat-failure-audit/` |

Or: `npx skills add hiteshbandhu/skills-i-use --skill chat-failure-audit`

### Output directory

```bash
export SKILL_OUTPUT_DIR=./skill-outputs   # shared root for all skills
# this skill writes to: ./skill-outputs/chat-failure-audit/
```

## Usage

```
@chat-failure-audit analyse this chat: <url or pasted log>
what went wrong in this session — the user gave up at the end
why did this break? push past "the model was wrong"
audit this transcript and rank what to fix first
```

## Output

| File | Purpose |
|------|---------|
| `audit-<date>-<session>.md` | Failure-mode table + ranked fix list |
| `index.md` | Registry of audits, newest first |

## Cross-skill integration

The front door of the product-method pipeline — it finds *what* is broken, the others fix
each kind:

- **`friction-audit`** ← failures classed as friction hand off here.
- **`state-lifetime-decision`** ← state/lifetime bugs hand off here.
- **`spec-grounded-design`** ← failures from protocol/API behavior not matching expectations.
- **`architecture-review`** ← fixes with a real build-vs-buy or two-mechanism fork.

## Files

```
chat-failure-audit/
├── SKILL.md              # Agent workflow
├── failure-classes.md    # 6 classes, symptom→cause prompts, severity rubric
├── audit-template.md     # Failure-mode report format
└── README.md
```

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use). Use and adapt freely.
