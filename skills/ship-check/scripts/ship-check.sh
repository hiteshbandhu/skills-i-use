#!/usr/bin/env bash
# Pre-ship checks for ship-check skill.
# Usage: ./scripts/ship-check.sh [--skip-build] [--skip-tests]
# Env: SHIP_CHECK_STRICT=1 to exit non-zero on any failure

set -uo pipefail

SKIP_BUILD=0
SKIP_TESTS=0
STRICT="${SHIP_CHECK_STRICT:-0}"

for arg in "$@"; do
  case "$arg" in
    --skip-build) SKIP_BUILD=1 ;;
    --skip-tests) SKIP_TESTS=1 ;;
  esac
done

PASS=0
WARN=0
FAIL=0

pass() { echo "PASS|$1"; PASS=$((PASS + 1)); }
warn() { echo "WARN|$1"; WARN=$((WARN + 1)); }
fail() { echo "FAIL|$1"; FAIL=$((FAIL + 1)); }

run_step() {
  local name="$1"
  shift
  if "$@" >/dev/null 2>&1; then
    pass "$name"
    return 0
  else
    fail "$name"
    return 1
  fi
}

echo "META|cwd|$(pwd)"
echo "META|time|$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u)"

# --- Git state ---
if git rev-parse --git-dir >/dev/null 2>&1; then
  pass "git repository detected"
  if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
    pass "uncommitted changes present"
    git diff --stat 2>/dev/null | while read -r line; do echo "DIFF_STAT|$line"; done
  else
    warn "working tree clean — nothing to ship"
  fi
  if git grep -lE '(api[_-]?key|secret|password|token)\s*[:=]\s*["\x27][^"\x27]{8,}' \
    -- ':!*.lock' ':!package-lock.json' ':!pnpm-lock.yaml' ':!yarn.lock' \
    ':!.env.example' ':!**/test/**' ':!**/*.test.*' 2>/dev/null | head -5 | grep -q .; then
    fail "possible hardcoded secrets in tracked files — review before ship"
  else
    pass "no obvious hardcoded secrets in grep scan"
  fi
  if git status --porcelain 2>/dev/null | grep -qE '\.env$|\.env\.local|credentials'; then
    fail "env/credential files staged or modified — do not commit secrets"
  else
    pass "no .env files in git status"
  fi
else
  fail "not a git repository"
fi

# --- Detect package manager ---
PM="npm"
if [ -f pnpm-lock.yaml ]; then PM="pnpm"
elif [ -f yarn.lock ]; then PM="yarn"
elif [ -f bun.lockb ] || [ -f bun.lock ]; then PM="bun"
fi
echo "META|package_manager|$PM"

run_pm() {
  case "$PM" in
    pnpm) pnpm "$@" ;;
    yarn) yarn "$@" ;;
    bun)  bun run "$@" ;;
    *)    npm run "$@" --if-present ;;
  esac
}

has_script() {
  node -e "
    const p=require('./package.json');
    const s=p.scripts||{};
    process.exit(s['$1']?0:1);
  " 2>/dev/null
}

# --- Node / TS projects ---
if [ -f package.json ]; then
  pass "package.json found"

  if has_script lint; then
    run_step "lint" run_pm lint || true
  else
    warn "no lint script — skip or add to package.json"
  fi

  if has_script typecheck; then
    run_step "typecheck" run_pm typecheck || true
  elif has_script "check-types"; then
    run_step "typecheck" run_pm check-types || true
  elif [ -f tsconfig.json ]; then
    if command -v npx >/dev/null 2>&1; then
      run_step "tsc --noEmit" npx tsc --noEmit || true
    else
      warn "tsconfig present but no typecheck script or npx"
    fi
  fi

  if [ "$SKIP_TESTS" -eq 0 ]; then
    if has_script test; then
      run_step "test" run_pm test || true
    else
      warn "no test script"
    fi
  fi

  if [ "$SKIP_BUILD" -eq 0 ]; then
    if has_script build; then
      run_step "build" run_pm build || true
    else
      warn "no build script — skip build check"
    fi
  fi
fi

# --- Python projects ---
if [ -f pyproject.toml ] || [ -f requirements.txt ]; then
  pass "python project detected"
  if command -v ruff >/dev/null 2>&1; then
    run_step "ruff check" ruff check . || true
  fi
  if [ -d .venv ] || [ -d venv ]; then
    pass "python venv present"
  fi
fi

# --- Summary ---
echo "SUMMARY|pass|$PASS"
echo "SUMMARY|warn|$WARN"
echo "SUMMARY|fail|$FAIL"

if [ "$FAIL" -gt 0 ] && [ "$STRICT" = "1" ]; then
  exit 1
fi
exit 0
