#!/usr/bin/env bash
# Collect AI agent session logs (Claude Code, Cursor, Codex).
# Usage: SINCE="7 days ago" ./collect-ai-sessions.sh

set -uo pipefail

SINCE="${SINCE:-7 days ago}"
SINCE_EPOCH=$(date -d "$SINCE" +%s 2>/dev/null || date -v-"${SINCE%% *}d" +%s 2>/dev/null || date -v-7d +%s 2>/dev/null)

echo "META|SINCE_EPOCH|$SINCE_EPOCH"

TOTAL_CHARS=0
TOTAL_SESSIONS=0

for dir in "$HOME/.claude" "$HOME/.cursor" "$HOME/.codex"; do
  [ -d "$dir" ] || continue
  find "$dir" -name "*.jsonl" 2>/dev/null | while read -r f; do
    MOD=$(stat -c %Y "$f" 2>/dev/null || stat -f %m "$f" 2>/dev/null)
    [ "${MOD:-0}" -lt "${SINCE_EPOCH:-0}" ] 2>/dev/null && continue

    LINES=$(wc -l < "$f" | tr -d ' ')
    CHARS=$(wc -c < "$f" | tr -d ' ')
    EST_TOKENS=$((CHARS / 4))

    FIRST_TS=$(head -1 "$f" 2>/dev/null | python3 -c "
import sys, json
try:
    d = json.loads(sys.stdin.read())
    print(d.get('timestamp') or d.get('createdAt') or '')
except: print('')
" 2>/dev/null)

    LAST_TS=$(tail -1 "$f" 2>/dev/null | python3 -c "
import sys, json
try:
    d = json.loads(sys.stdin.read())
    print(d.get('timestamp') or d.get('createdAt') or '')
except: print('')
" 2>/dev/null)

    PROJECT=$(echo "$f" | sed -E 's|.*/projects/([^/]+).*|\1|' | head -1)

    echo "AI_SESSION|$PROJECT|$LINES|$CHARS|$EST_TOKENS|$FIRST_TS|$LAST_TS|$f"

    grep -E '"role":"(user|human)"' "$f" 2>/dev/null | python3 -c "
import sys, json
for line in sys.stdin:
    try:
        d = json.loads(line)
        content = d.get('content', '')
        if isinstance(content, list):
            for c in content:
                if c.get('type') == 'text':
                    print('TOPIC|' + c['text'][:120].replace(chr(10), ' '))
                    break
        elif isinstance(content, str):
            print('TOPIC|' + content[:120].replace(chr(10), ' '))
    except: pass
" 2>/dev/null | head -5

    echo "SESSION_CHARS|$CHARS"
  done
done

# Totals (re-scan for count — subshell-safe summary)
TOTAL_CHARS=$(find "$HOME/.claude" "$HOME/.cursor" "$HOME/.codex" -name "*.jsonl" 2>/dev/null | while read -r f; do
  MOD=$(stat -c %Y "$f" 2>/dev/null || stat -f %m "$f" 2>/dev/null)
  [ "${MOD:-0}" -lt "${SINCE_EPOCH:-0}" ] 2>/dev/null && continue
  wc -c < "$f"
done | awk '{s+=$1} END {print s+0}')

TOTAL_SESSIONS=$(find "$HOME/.claude" "$HOME/.cursor" "$HOME/.codex" -name "*.jsonl" 2>/dev/null | while read -r f; do
  MOD=$(stat -c %Y "$f" 2>/dev/null || stat -f %m "$f" 2>/dev/null)
  [ "${MOD:-0}" -lt "${SINCE_EPOCH:-0}" ] 2>/dev/null && continue
  echo 1
done | wc -l | tr -d ' ')

echo "TOTAL_AI_TOKENS|$((TOTAL_CHARS / 4))"
echo "TOTAL_AI_SESSIONS|$TOTAL_SESSIONS"
