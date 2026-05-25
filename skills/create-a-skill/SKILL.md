---
name: create-a-skill
description: >
  Interview, stress-test, and author new skills for the skills-i-use repo — or improve
  existing ones. Asks hard questions, runs reviewer subagents, writes design briefs,
  generates SKILL.md and supporting files, validates conventions, and registers in
  README and OUTPUT.md. Triggers on "create a skill", "new skill", "add a skill",
  "improve this skill", "author a skill", "skill for X workflow", "build a skill".
---

# Create-a-Skill — Author & Improve Repo Skills

End-to-end skill authoring for [skills-i-use](https://github.com/hiteshbandhu/skills-i-use):
collect → challenge → review → write → validate → register in repo.

Works with any coding agent that can run subagents. Follows [CONTRIBUTING.md](../../CONTRIBUTING.md).

**Supporting files:**
- [questions.md](questions.md) — intake and hard questions
- [reviewers.md](reviewers.md) — Skeptic / Maintainer / Practitioner subagents + synthesis
- [design-brief-template.md](design-brief-template.md) — pre-build design doc
- [templates/](templates/) — SKILL.md and README starters
- [scripts/validate-skill.sh](scripts/validate-skill.sh) — convention checker

**Scripts:** read `scripts/validate-skill.sh` before running. Double-check paths and flags every time.

Output: `{SKILL_OUTPUT_DIR}/create-a-skill/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — Mode

| Mode | When |
|------|------|
| **new** | User wants a skill that doesn't exist |
| **improve** | User names an existing skill in `skills/` to extend or fix |
| **from conversation** | Infer workflow from current chat — confirm before building |

Locate repo root: `skills-i-use/` (this repo) or ask user for path.

---

## Step 1 — Intake (hard questions)

Read [questions.md](questions.md). Ask **required + hard questions in one message**.

Do not proceed until required items are answered. Push back on weak answers — use
follow-ups from the red-flag table.

**Scan existing skills** before intake completes:

```bash
ls skills/
```

For each existing skill, read `description` in frontmatter (first 20 lines of SKILL.md).
Note overlap in the brief.

If user provided **verbatim wording** for the skill, preserve it exactly in output files.

---

## Step 2 — Build Skill Brief

Compile answers into:

```
WORKFLOW: [repeatable steps]
FREQUENCY: [how often used]
TRIGGERS: [phrases]
OUTPUTS: [artifacts + skill-outputs path]
STOP_CONDITION: [done when]
MODE: [new | improve]
TARGET: [skill name or existing folder]
OVERLAP: [existing skills]
OUT_OF_SCOPE_V1: [explicit]
TRUST_BOUNDARY: [commit/push/delete/spend — yes/no]
VERBATIM: [any exact copy from user]
```

---

## Step 3 — Reviewer Subagents (parallel)

Read [reviewers.md](reviewers.md). Run **Skeptic**, **Maintainer**, and **Practitioner**
in parallel with the skill brief.

Then run **Synthesis** (fourth subagent or orchestrator) → `DECISION: BUILD NEW | EXTEND | REJECT`.

If **REJECT** — explain why and suggest alternative (script, rule, extend X). Stop.

If **EXTEND** — read existing skill folder fully before writing. Prefer minimal diff.

---

## Step 4 — Design Brief

Fill [design-brief-template.md](design-brief-template.md).

**Path:** `{output_dir}/design-YYYY-MM-DD-[skill-name].md`

Present brief to user. Ask: **"Proceed to write files?"** — stop on no.

---

## Step 5 — Write Skill Files

### New skill

Create `skills/[skill-name]/` using [templates/](templates/) as starters. Replace `{{placeholders}}`.

Typical layout per [CONTRIBUTING.md](../../CONTRIBUTING.md):

```
skills/[skill-name]/
├── SKILL.md
├── README.md
├── [principles.md | scripts/ | templates/ as needed]
```

### Improve existing

1. Read entire existing folder
2. Apply changes from brief — do not duplicate a new folder unless synthesis says split
3. Preserve working triggers unless intentionally breaking (note in brief)
4. Extract bloat from SKILL.md into new supporting files if over ~250 lines

**Rules while writing:**
- Agent-agnostic — subagents/shell, not vendor APIs
- Output → `{SKILL_OUTPUT_DIR}/[skill-name]/`
- Safe defaults — no auto-commit/push
- Third-person `description` with what + when

---

## Step 6 — Validate

```bash
bash skills/create-a-skill/scripts/validate-skill.sh skills/[skill-name]
```

Fix all `FAIL|` items. Address `WARN|` items or document why waived in design brief.

---

## Step 7 — Register in Repo

Update registry files (skip if improving and row already exists):

1. **[README.md](../../README.md)** — add row to skills table (alphabetical or logical order)
2. **[skills/OUTPUT.md](../OUTPUT.md)** — add subfolder to layout tree if skill produces output
3. **Cross-skill section** in OUTPUT.md — if skill reads/writes another skill's index

Update `{output_dir}/index.md`:

```markdown
# Create-a-Skill Designs

| Date | Skill | Decision | Brief |
|------|-------|----------|-------|
```

---

## Step 8 — Ship (user confirms)

1. List all created/changed files
2. Show validation result
3. Suggest `@ship-check` if scripts were added
4. Ask: **"Commit to repo?"** — only on explicit yes

```bash
git add skills/[skill-name]/ README.md skills/OUTPUT.md
git commit -m "feat: add [skill-name] skill"
```

Ask separately before push. Never push without explicit request.

---

## Edge Cases

- **Skill outside skills-i-use** — write files where user points; skip Step 7 registry
- **Meta: improving create-a-skill itself** — same workflow; extra care on regressions
- **User says "just write it"** — still run validate; abbreviated intake OK if context is rich
- **Duplicate skill name** — fail validation; pick new name with user
- **Subagents unavailable** — orchestrator plays all three reviewers sequentially

---

## Invocation Examples

```
@create-a-skill I want a skill for retrieval benchmarks
improve ship-check — add Python project support
create a skill from this conversation
new skill: legal contract review with persona debate
author a skill, ask me hard questions first
```
