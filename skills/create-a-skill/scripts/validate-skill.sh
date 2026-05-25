#!/usr/bin/env bash
# Validate a skill folder against skills-i-use conventions.
# Usage: ./scripts/validate-skill.sh skills/my-skill

set -uo pipefail

SKILL_DIR="${1:-}"
FAIL=0

if [ -z "$SKILL_DIR" ] || [ ! -d "$SKILL_DIR" ]; then
  echo "FAIL|directory missing: $SKILL_DIR"
  exit 1
fi

NAME=$(basename "$SKILL_DIR")

if ! echo "$NAME" | grep -qE '^[a-z0-9-]+$'; then
  echo "FAIL|folder name must be lowercase-hyphens: $NAME"
  FAIL=1
else
  echo "PASS|folder name: $NAME"
fi

for f in SKILL.md README.md; do
  if [ -f "$SKILL_DIR/$f" ]; then
    echo "PASS|required file: $f"
  else
    echo "FAIL|missing required file: $f"
    FAIL=1
  fi
done

if [ -f "$SKILL_DIR/SKILL.md" ]; then
  LINES=$(wc -l < "$SKILL_DIR/SKILL.md" | tr -d ' ')
  if [ "$LINES" -gt 250 ]; then
    echo "WARN|SKILL.md is $LINES lines (target ≤250 — extract to supporting files)"
  else
    echo "PASS|SKILL.md line count: $LINES"
  fi

  if head -1 "$SKILL_DIR/SKILL.md" | grep -q '^---'; then
    echo "PASS|YAML frontmatter present"
  else
    echo "FAIL|missing YAML frontmatter"
    FAIL=1
  fi

  if grep -qiE 'anthropic|claude api|openai api' "$SKILL_DIR/SKILL.md" 2>/dev/null; then
    echo "WARN|possible vendor lock-in — ensure subagent fallback documented"
  fi

  if grep -qE '\./reports/|\./adrs/' "$SKILL_DIR/SKILL.md" 2>/dev/null; then
    echo "FAIL|hardcoded output path — use skill-outputs/{skill-name}/"
    FAIL=1
  else
    echo "PASS|no legacy output paths in SKILL.md"
  fi
fi

if [ "$FAIL" -gt 0 ]; then
  echo "SUMMARY|validation failed"
  exit 1
fi
echo "SUMMARY|validation passed"
exit 0
