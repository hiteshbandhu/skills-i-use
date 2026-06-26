# Friction Audit

A portable agent skill for finding and removing friction from a product flow. It walks
the flow, marks every point where the **system makes the user do work it could do
itself**, classifies each, decides what should become automatic — with a safety
carve-out for destructive, irreversible, or cross-boundary actions — and designs the
automatic path with its tradeoff named.

The operating bias: **anything the system can do for the user, it should — unless it's
destructive, irreversible, or crosses a trust boundary.**

Works with **any coding agent**. No vendor-specific API calls. Reads the code or
transcript you point it at.

Output goes in **`./skill-outputs/friction-audit/`** — shared root, see [../OUTPUT.md](../OUTPUT.md).

## What it does

```
Scope the flow → walk it, mark every user action → classify friction (6 classes)
   → decide automate / keep (safety carve-out) → design the automatic path + tradeoff
   → inventory + ship-first report → index.md
```

| Friction class | The user is forced to… |
|----------------|------------------------|
| **Ask-for-permission** | approve something they already authorized |
| **Re-do / re-send** | repeat an action because state didn't cross a boundary |
| **Manual recovery** | reconnect/retry what the system could self-heal |
| **Re-discovery** | re-find something already found |
| **Dead-end** | stop, with no next step offered |
| **Redundant confirmation** | confirm a non-destructive, reversible action |

## Install

Copy this folder into your agent's skills directory:

| Agent | Typical path |
|-------|--------------|
| Cursor | `~/.cursor/skills/friction-audit/` or `.cursor/skills/friction-audit/` |
| Claude Code | `~/.claude/skills/friction-audit/` |
| Codex | `~/.codex/skills/friction-audit/` |

Or: `npx skills add hiteshbandhu/skills-i-use --skill friction-audit`

### Output directory

```bash
export SKILL_OUTPUT_DIR=./skill-outputs   # shared root for all skills
# this skill writes to: ./skill-outputs/friction-audit/
```

## Usage

```
@friction-audit our connector-enable flow — why does the user have to re-send?
audit this onboarding path for friction
this should just happen automatically — find every place it doesn't
remove the friction in document sharing, but keep deletes safe
```

## Output

| File | Purpose |
|------|---------|
| `audit-<date>-<flow>.md` | Friction inventory + ranked auto-path designs |
| `index.md` | Registry of audits, newest first |

## Cross-skill integration

Part of a product-method pipeline:

- **`chat-failure-audit`** → run first when you only have a transcript of symptoms, not a
  flow; its failure modes point at the flow to audit here.
- **`state-lifetime-decision`** → any auto-path that introduces or changes persisted state
  hands off here for the scope × durability × isolation call.
- **`architecture-review`** → when a fix forks (build vs buy, two mechanisms), escalate.

## Files

```
friction-audit/
├── SKILL.md               # Agent workflow
├── friction-taxonomy.md   # 6 classes, auto-vs-manual rule, tradeoff prompts
├── audit-template.md      # Inventory + auto-path report format
└── README.md
```

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use). Use and adapt freely.
