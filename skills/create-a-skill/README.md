# Create-a-Skill

Interview, stress-test, and author skills for the skills-i-use repo — or improve
existing ones.

Asks hard questions → runs three reviewer subagents → writes a design brief →
generates files → validates conventions → registers in README and OUTPUT.md.

Output: `./skill-outputs/create-a-skill/`

## Scripts

This skill includes `scripts/validate-skill.sh`. **Read the script before running it.**
It checks skill folder conventions and is read-only, but always verify paths and flags —
do not run blindly.

## Usage

```
@create-a-skill I want a skill for X
@create-a-skill improve ui-ux — add mobile-only audit mode
create a skill from this conversation
```

## Workflow

```
Intake → repo scan → reviewer subagents → design brief → you confirm
    → write skill files → validate → register → optional commit
```

| Reviewer | Lens |
|----------|------|
| **Skeptic** | Kill duplicates, vagueness, vendor lock-in |
| **Maintainer** | CONTRIBUTING conventions, file plan, registry |
| **Practitioner** | Real triggers, daily usefulness, skill pairing |

## Modes

- **new** — create `skills/my-skill/` from scratch
- **improve** — extend or fix an existing skill folder

Never commits without your explicit confirmation.

## Files

```
create-a-skill/
├── SKILL.md
├── questions.md
├── reviewers.md
├── design-brief-template.md
├── templates/
├── scripts/validate-skill.sh
└── README.md
```

## Pair with

- **`ship-check`** — before committing new skills with scripts
- **`architecture-review`** — when the new skill implies a structural workflow choice

## License

Part of [skills-i-use](https://github.com/hiteshbandhu/skills-i-use).
