#!/usr/bin/env bash
# Collect git activity across repos for CTO weekly review.
# Usage: SINCE="7 days ago" ME="you@email.com" REPOS="/path/a /path/b" ./collect-git.sh

set -uo pipefail

SINCE="${SINCE:-7 days ago}"
ME="${ME:-$(git config user.email 2>/dev/null || echo "")}"
SEARCH_ROOT="${SEARCH_ROOT:-$HOME}"
MAXDEPTH="${MAXDEPTH:-6}"

if [ -z "$ME" ]; then
  echo "ERROR|git config user.email is not set" >&2
  exit 1
fi

echo "META|SINCE|$SINCE"
echo "META|AUTHOR|$ME"
echo "META|TZ|$(date +%Z 2>/dev/null || echo UTC)"

discover_repos() {
  find "$SEARCH_ROOT" -name ".git" -maxdepth "$MAXDEPTH" \
    -not -path "*/node_modules/*" \
    -not -path "*/.git/*" \
    2>/dev/null | sed 's|/.git||'
}

if [ -n "${REPOS:-}" ]; then
  REPO_LIST=$REPOS
else
  REPO_LIST=$(discover_repos)
fi

for repo in $REPO_LIST; do
  cd "$repo" 2>/dev/null || continue
  RNAME=$(basename "$repo")

  git log --since="$SINCE" --author="$ME" --no-merges \
    --pretty=format:"COMMIT|$RNAME|%H|%ai|%at|%s|%b" \
    2>/dev/null

  git log --since="$SINCE" --author="$ME" --no-merges \
    --pretty=format:"STAT|$RNAME|%H|%at" \
    --stat 2>/dev/null | grep -E "STAT|changed" || true

  git log --since="$SINCE" --author="$ME" --no-merges \
    --pretty=format:"FILE|$RNAME|%H|%at" \
    --name-only 2>/dev/null | grep -v "^$" || true

  git log --since="$SINCE" --author="$ME" \
    --pretty=format:"REVERT|$RNAME|%at|%s" \
    --grep="revert" -i 2>/dev/null || true

  git diff HEAD~20 HEAD 2>/dev/null | grep -E "^[+-].*TODO|FIXME|HACK|XXX" | \
    awk '{if(/^\+/) print "TODO_ADD"; else print "TODO_REMOVE"}' || true

  git log --since="$SINCE" --author="$ME" --no-merges \
    --pretty=format:"%ad" --date=format:"%H %A %u" 2>/dev/null | \
    while read -r line; do echo "HEATMAP|$RNAME|$line"; done

  git log --since="$SINCE" --author="$ME" --no-merges \
    --pretty=format:"SESSION|$RNAME|%at|%ad" \
    --date=format:"%Y-%m-%d %H:%M" 2>/dev/null || true

  git log --since="$SINCE" -p -- package.json yarn.lock pnpm-lock.yaml \
    requirements.txt requirements-dev.txt pyproject.toml 2>/dev/null | \
    grep "^+" | grep -v "^+++" | grep -E '"[a-z@]' | head -20 | \
    while read -r line; do echo "DEP_ADD|$RNAME|$line"; done

  git log --since="$SINCE" --name-only --pretty=format:'' \
    2>/dev/null | grep -iE "migrat|schema|\.sql$" | sort -u | \
    while read -r line; do echo "SCHEMA|$RNAME|$line"; done

  git log --since="$SINCE" --name-only --pretty=format:'' \
    2>/dev/null | grep -iE "\.env|docker|railway|vercel|\.yml$|\.yaml$" | sort -u | \
    while read -r line; do echo "INFRA|$RNAME|$line"; done
done
