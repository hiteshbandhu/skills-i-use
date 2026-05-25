# CTO Weekly Review — HTML Report Template

Read this file during Step 4. Generate a single self-contained HTML file.

## Tech stack

- Inter font (Google Fonts)
- Chart.js from jsdelivr CDN
- Inline CSS only — no external stylesheets beyond fonts/CDN
- Print CSS: white bg, black text, hide buttons

## Design system

```
Page bg:       #f8f7f5
Card bg:       #ffffff
Border:        1px solid #e8e5de
Primary text:  #111111
Muted text:    #6b6b6b
Hint text:     #a8a39a
Dividers:      #e8e5de
Section bg:    #f8f7f5
Font:          Inter, system-ui
Corner radius: 12px on cards
Charts:        #111 primary, #d4d0c8 secondary, #a8a39a tertiary
               NO gradients, NO purple, NO blue
```

## Page sections (in order)

### HEADER (sticky)
- Left: name/product → divider → "CTO Weekly Review"
- Center: date range
- Right: role label + Export PDF button (window.print)
- Link to sibling markdown: `weekly-YYYY-MM-DD.md`

### HERO — The Week in One Line
Full-width, 24px. One-sentence summary.

### SECTION 1: Metrics Row (8 cards, 4×2 grid)
1. Total Commits
2. Lines Added
3. Lines Deleted
4. Net LOC
5. Files Touched
6. Est. AI Tokens
7. AI Sessions
8. Active Repos

### SECTION 2: Working Hours & Patterns
- **Panel A** — 7×24 hourly heatmap (greyscale: `#e8e5de` → `#6b6b6b` → `#111`)
- **Panel B** — Day-by-day commit bar chart
- **Panel C** — Peak hour, avg start time, night commits %

### SECTION 3: Focus & Flow
- **Panel A** — Gantt-style session timeline per day (deep work `#111`, quick fix `#d4d0c8`, context switch `#a8a39a`)
- **Panel B** — Session stats (total, deep work, avg length, longest, most fragmented/focused day)
- **Panel C** — Fragmentation score with label

### SECTION 4: Productivity Health
- Large sustainability score (from [scoring.md](scoring.md)) with label and color
- 6 sub-dimension breakdown bars
- Work pattern donut (core / evening / night / morning)
- Weekly rhythm card (Mon–Sun: active / light / rest)

### SECTION 5: Work Breakdown
- Donut: feat / fix / refactor / experiment / docs / infra
- Commit size stacked bar: micro / small / medium / large
- Churn rate + avg files per commit

### SECTION 6: AI Collaboration
Skip entire section if no AI session logs found.

- Token usage bar by day
- AI leverage ratio %
- Top session topics (5–8 tags)
- Tokens per net line of code

### SECTION 7: Repo Intelligence
Card per active repo: name, commits, sparkline, lines +/-, top file, avg commit size, active days.

### SECTION 8: Narrative
Timeline layout — vertical rule left, dated entries right. All 8 narrative sections from Step 3.

### SECTION 9: Experiments & Decisions Log
**Experiments table:** Experiment | Status | Finding | Commit ref

**Decisions table:** Decision | Context | Outcome | Source

Include ADRs from architecture-review cross-skill link (see SKILL.md Step 2D). Mark
source as `architecture-review` for linked ADRs.

### SECTION 10: Content Seeds
2–3 cards: hook line, insight, data point, hashtags.

### SECTION 11: Next Week
3 numbered priorities + one debt item from blockers.

### FOOTER
`CTO Weekly Review · generated [timestamp] · [timezone]`
