#!/usr/bin/env bash
# Collect shell history, file edit timestamps, and GitHub CLI data.
# Usage: SINCE="7 days ago" ./collect-context.sh

set -uo pipefail

SINCE="${SINCE:-7 days ago}"
SEARCH_ROOT="${SEARCH_ROOT:-$HOME}"
SINCE_EPOCH=$(date -d "$SINCE" +%s 2>/dev/null || date -v-"${SINCE%% *}d" +%s 2>/dev/null || date -v-7d +%s 2>/dev/null)
SINCE_DATE=$(date -d "$SINCE" +%Y-%m-%d 2>/dev/null || date -v-"${SINCE%% *}d" +%Y-%m-%d 2>/dev/null || date -v-7d +%Y-%m-%d 2>/dev/null)

echo "META|SINCE_EPOCH|$SINCE_EPOCH"

# Shell history
if [ -f "$HOME/.zsh_history" ]; then
  grep "^:" "$HOME/.zsh_history" 2>/dev/null | \
    awk -F: '{print $2, substr($0, index($0,$3))}' | \
    awk -v since="$SINCE_EPOCH" '$1 > since {print "SHELL|" $0}' 2>/dev/null | \
    grep -E "git |npm |pnpm |yarn |node |python|docker|railway|curl|brew" | head -100 || true
fi

if [ -f "$HOME/.bash_history" ] && grep -q "^#[0-9]" "$HOME/.bash_history" 2>/dev/null; then
  grep -A1 "^#[0-9]" "$HOME/.bash_history" 2>/dev/null | \
    awk -v since="$SINCE_EPOCH" '/^#/{ts=$1+0; next} ts>since {print "SHELL|" ts, $0}' | head -100 || true
fi

echo "=== TOOL USAGE ==="
cat "$HOME/.zsh_history" "$HOME/.bash_history" 2>/dev/null | \
  grep -oE "^(git|npm|pnpm|node|python3?|docker|railway|curl|gh|brew)" | \
  sort | uniq -c | sort -rn | head -20 | while read -r count tool; do
    echo "TOOL|$tool|$count"
  done

# File system edit timestamps
find "$SEARCH_ROOT" -type f \( -name "*.ts" -o -name "*.tsx" -o -name "*.js" \
  -o -name "*.py" -o -name "*.sql" -o -name "*.md" -o -name "*.json" \) \
  -newer "$SINCE_DATE" \
  -not -path "*/node_modules/*" \
  -not -path "*/.git/*" \
  -not -path "*/dist/*" \
  -not -path "*/.next/*" \
  2>/dev/null | while read -r f; do
    TS=$(stat -c %Y "$f" 2>/dev/null || stat -f %m "$f" 2>/dev/null)
    HOUR=$(date -d "@$TS" +%H 2>/dev/null || date -r "$TS" +%H 2>/dev/null)
    echo "FSEDIT|$f|$TS|$HOUR"
  done

# GitHub CLI
if command -v gh &>/dev/null; then
  gh pr list --author="@me" --state=all --limit=30 \
    --json number,title,state,createdAt,mergedAt,closedAt,additions,deletions,changedFiles \
    2>/dev/null | python3 -c "
import sys, json
try:
    for pr in json.load(sys.stdin):
        print('GH_PR|' + str(pr.get('number','')) + '|' + pr.get('title','') + '|' + pr.get('state','') + '|' + str(pr.get('createdAt','')))
except: pass
" 2>/dev/null || true

  gh issue list --assignee="@me" --state=closed --limit=20 \
    --json number,title,closedAt,createdAt,labels \
    2>/dev/null | python3 -c "
import sys, json
try:
    for i in json.load(sys.stdin):
        print('GH_ISSUE|' + str(i.get('number','')) + '|' + i.get('title','') + '|' + str(i.get('closedAt','')))
except: pass
" 2>/dev/null || true

  gh pr list --reviewer="@me" --state=all --limit=20 \
    --json number,title,author,state,createdAt \
    2>/dev/null | python3 -c "
import sys, json
try:
    for pr in json.load(sys.stdin):
        author = pr.get('author') or {}
        name = author.get('login','') if isinstance(author, dict) else str(author)
        print('GH_REVIEW|' + str(pr.get('number','')) + '|' + pr.get('title','') + '|' + name)
except: pass
" 2>/dev/null || true
else
  echo "GH_MISSING|install with: brew install gh"
fi
