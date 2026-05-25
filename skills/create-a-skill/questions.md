# Create-a-Skill — Hard Questions

Ask these in **one message** during Step 1. Do not write files until the user answers
the blockers (marked **required**). Push back on weak answers — ask a follow-up.

---

## Required

1. **What repeatable workflow does this automate?** (Not "help with X" — the exact steps an agent should run.)
2. **How often will you actually use this?** (Daily / weekly / monthly / rarely — if rarely, maybe a one-off prompt instead.)
3. **Trigger phrases** — what will you say to invoke it? List 5+ natural phrases.
4. **Output** — what files or artifacts does it produce? Where do they land?
5. **Stop condition** — how does the agent know it's done?
6. **New skill or improve existing?** If existing, which skill in `skills/` and what's broken or missing?

---

## Hard questions (challenge assumptions)

7. **Why not a slash command, rule, or script?** What does the skill shape buy you that those don't?
8. **Overlap** — which existing skill in this repo already does 80% of this? (`architecture-review`, `ship-check`, `ui-ux`, `cto-weekly-review`, …)
9. **Agent-agnostic?** Can this run on Cursor, Claude Code, and Codex without vendor APIs? If not, what's the fallback?
10. **Failure mode** — what happens when subagents, Playwright, or git aren't available?
11. **Scope creep** — what's explicitly **out of scope** for v1?
12. **Trust boundary** — does this commit, push, delete, or spend money? (Must ask user before any destructive action.)
13. **Verbatim copy** — any exact wording the user wants preserved in the skill? (Use verbatim; do not soften.)
14. **Supporting files** — what belongs in `SKILL.md` vs `principles.md` / `scripts/` / templates?
15. **Cross-skill links** — should it read or write another skill's `skill-outputs/` index?

---

## Improve-existing only

16. **What's wrong with the current skill?** (Too long, wrong triggers, vendor-locked, missing output convention, …)
17. **Breaking changes?** Will existing invocations still work?
18. **Merge or replace?** Extend the folder or split into a new skill?

---

## Before repo commit

19. **Skill folder name** — lowercase-hyphens, max 64 chars. Confirm with user.
20. **Commit now?** Never commit without explicit yes. Offer `@ship-check` first if code/scripts included.

---

## Red flags — push back or reject

| User says | You respond |
|-----------|-------------|
| "General coding helper" | Too vague — narrow to one workflow |
| "Always run automatically" | Skills load on trigger; define triggers precisely |
| "Call Claude API" | Refactor to subagents or document generic fallback |
| "Write to ./reports or ./output" | Must use `skill-outputs/{skill-name}/` |
| "One giant SKILL.md" | Split into supporting files before merging |
| Duplicates existing skill | Recommend extending existing skill instead |
