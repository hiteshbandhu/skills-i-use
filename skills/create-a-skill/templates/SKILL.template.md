---
name: {{skill-name}}
description: >
  {{Third-person description — what it does and when to trigger it. Include 5+ natural
  trigger phrases. Max 1024 chars.}}
---

# {{Skill Title}}

{{One-line summary. Agent-agnostic. No vendor APIs unless fallback documented.}}

**Supporting files** (read when needed):
- [{{file}}]({{file}}) — {{purpose}}

Output: `{SKILL_OUTPUT_DIR}/{{skill-name}}/` — see [../OUTPUT.md](../OUTPUT.md)

---

## Step 0 — {{Scope / intake}}

{{When to ask vs infer. Stop conditions.}}

---

## Step 1 — {{First action}}

{{Clear steps. Subagents if needed. Scripts if needed.}}

---

## Step N — Output to user

1. {{What to tell the user}}
2. {{File paths}}
3. {{Never auto-commit unless user confirms}}

---

## Edge cases

- {{edge case}}

---

## Invocation examples

```
{{example 1}}
{{example 2}}
```
