---
name: cto-weekly-review
description: >
  Generate a deep CTO self-review report: working hours, productivity patterns, focus
  sessions, AI collaboration depth, cognitive load signals, sustainability health, and
  codebase velocity — not just commit counts. Triggers on "weekly review", "CTO report",
  "week summary", "what did I build", "productivity report", "show me my week", "engineer
  report", "weekly digest". Scans git across repos, AI agent session logs, shell
  history, file timestamps, and produces markdown + HTML reports. Always trigger this
  skill for any weekly or periodic review of engineering or product work.
---

# CTO Weekly Review — Deep Signal Extraction

Founder-grade weekly report from git history, AI session logs, shell history, and file
timestamps — not just commit counts.

Works with any coding agent that can run subagents and shell commands.

**Supporting files** (read when needed):
- [scripts/collect-git.sh](scripts/collect-git.sh) — git activity across repos
- [scripts/collect-ai-sessions.sh](scripts/collect-ai-sessions.sh) — AI session logs
- [scripts/collect-context.sh](scripts/collect-context.sh) — shell, file edits, GitHub CLI
- [data-sources.md](data-sources.md) — AI log fallback reference
- [scoring.md](scoring.md) — sustainability health score weights and formulas
- [report-template.md](report-template.md) — HTML report structure and design
- [weekly-template.md](weekly-template.md) — markdown summary format

**Scripts:** read every file under `scripts/` before running. They scan git repos, AI session
logs, shell history, and local file timestamps. Confirm `SINCE`, `ME`, `REPOS`, and
`SEARCH_ROOT` before execution. Double-check every time.

---

## Step 0 — Scope Confirmation

Ask once (or infer from the request):

| Setting | Default | Notes |
|---------|---------|-------|
| Date range | last 7 days | Accept "last 14 days", specific dates, "this sprint" |
| Repos | crawl `~/` | Accept explicit paths via `REPOS` env var |
| Author email | `git config user.email` | Ask if multiple identities |
| Timezone | system TZ | Critical for working-hour analysis |
| Output directory | `{SKILL_OUTPUT_DIR}/cto-weekly-review/` | See [../OUTPUT.md](../OUTPUT.md) |

Create the output directory if it does not exist.

Set env vars for collectors: `SINCE`, `ME`, `REPOS` (optional), `SEARCH_ROOT` (optional).

---

## Step 1 — Data Collection (parallel subagents)

Run three collector subagents in parallel when supported. Each returns structured
pipe-delimited output. Keep contexts isolated until Step 2.

**Fallback:** Run scripts sequentially yourself, or inline if scripts unavailable.

### Subagent 1 — Git Collector

```bash
SINCE="7 days ago" ME="user@email.com" bash scripts/collect-git.sh
# Optional: REPOS="/path/a /path/b" SEARCH_ROOT="$HOME"
```

Collects: commits, stats, files, reverts, TODOs, heatmap hours, flow sessions,
dependency/schema/infra changes.

### Subagent 2 — AI Collector

```bash
SINCE="7 days ago" bash scripts/collect-ai-sessions.sh
```

See [data-sources.md](data-sources.md) for output format. Skip gracefully if empty.

### Subagent 3 — Context Collector

```bash
SINCE="7 days ago" bash scripts/collect-context.sh
```

Collects: shell history, tool usage, file edit timestamps, GitHub PRs/issues/reviews.

---

## Step 2 — Signal Processing

Merge all collector output. Compute derived metrics using [scoring.md](scoring.md).

### 2A. Working Hours Profile

From commit timestamps + AI session timestamps + `FSEDIT` records:
- Commits by hour and day, peak hour, night/morning/core/evening percentages
- Days active, weekend percentage, daily start/end spans

### 2B. Focus Session Analysis

Cluster commits with gap > 90 min = new session. Classify per scoring.md:
deep work / quick fix / context switching / normal.

### 2C. Commit Quality Analysis

Classify by size (micro/small/medium/large) and type (feature/fix/refactor/experiment/docs/infra/revert).
Compute churn rate, avg files per commit, revert count.

### 2D. Cross-Skill ADR Linking

Read architecture decisions written this week from the shared output tree:

```
{SKILL_OUTPUT_DIR}/architecture-review/index.md
{SKILL_OUTPUT_DIR}/architecture-review/ADR-*.md
```

If the index exists, parse rows and include ADRs whose date falls within the report's
date range in:
- **Key decisions** narrative (Step 3)
- **Decisions table** in markdown and HTML (Section 9)
- Set Source column to `architecture-review` with link to the ADR file

If no ADRs this week, note "No ADRs recorded this week" — do not invent decisions.

### 2E. AI Leverage

Cross-reference AI session end times with commit timestamps. See scoring.md.

---

## Step 3 — Narrative Synthesis

After processing, write these sections (orchestrating agent or synthesis subagent):

1. **The week in one line** — crisp, honest, specific
2. **What actually shipped** — merged/deployed only
3. **What's in progress** — branches, PRs, WIP
4. **Key decisions made** — include linked ADRs from Step 2D
5. **Experiments & findings** — actual results if detectable
6. **Debt & blockers** — what slowed you down
7. **Sustainability reflection** — honest paragraph on intensity
8. **Next week top 3** — specific and actionable

**Tone:** Founder briefing co-founder. Specific numbers. Honest about bad weeks.
No corporate fluff.

---

## Step 4 — Generate Reports

Always write **both** markdown and HTML.

### Markdown (required)

Fill [weekly-template.md](weekly-template.md).

**Path:** `{output_dir}/weekly-YYYY-MM-DD.md`

### HTML (required unless user says "markdown only")

Follow [report-template.md](report-template.md). Link to the `.md` file in header.

**Path:** `{output_dir}/weekly-YYYY-MM-DD.html`

---

## Step 5 — Update Registry

Maintain `{output_dir}/index.md`:

```markdown
# CTO Weekly Reviews

| Week ending | Markdown | HTML | Health | Commits | Highlights |
|-------------|----------|------|--------|---------|------------|
```

Append row (newest first):

```
| YYYY-MM-DD | [weekly-YYYY-MM-DD.md](weekly-YYYY-MM-DD.md) | [weekly-YYYY-MM-DD.html](weekly-YYYY-MM-DD.html) | [score]/100 | [n] | [one-line summary] |
```

---

## Step 6 — Output to User

1. List saved paths (`.md`, `.html`, `index.md`)
2. PDF export hint (Cmd+P or Export PDF button)
3. Best content angle from this week
4. One honest line about week health — don't sugarcoat
5. Note ADRs linked from architecture-review (if any)

---

## Edge Cases

- **No git history** — use AI sessions + file timestamps; note absence
- **No AI session logs** — skip AI section; note absence
- **No `gh` CLI** — skip PR section; suggest `brew install gh`
- **macOS vs Linux dates** — scripts handle both `date -d` and `date -v`
- **No shell timestamps** — skip shell section silently
- **Repos outside `~/`** — pass explicit `REPOS` paths
- **Monorepos** — one repo, break down by package directory
- **Multiple git identities** — comma-separate emails in `ME` or run twice
- **Subagents unavailable** — run three scripts sequentially
- **architecture-review index missing** — skip ADR linking silently

---

## Invocation Examples

```
"give me a weekly review"
"generate my CTO report for this week"
"what did I build this week"
"weekly digest, last 14 days"
"markdown only — skip HTML"
```
