# Sustainability Health Score (0–100)

Read this file during Step 2 signal processing. Tune weights and formulas here without
editing the main skill workflow.

## Dimensions

| Dimension | Weight | Signal | Formula |
|-----------|--------|--------|---------|
| Rest | 0.20 | % commits in night hours (23–05) | `max(0, 100 - (night_pct * 2))` |
| Consistency | 0.20 | Days with at least one commit | `min(100, (active_days / 5) * 100)` |
| Weekend balance | 0.15 | % commits on Sat/Sun | `max(0, 100 - weekend_pct)` |
| Focus | 0.20 | Deep work sessions (>90min, single repo, ≥3 commits) | `min(100, deep_work_sessions * 20)` |
| Session length | 0.15 | Average session duration (minutes) | `min(100, (avg_duration_min / 90) * 100)` |
| Fragmentation | 0.10 | Sessions per active day | `max(0, 100 - (sessions_per_day * 15))` |

## Final score

```
health_score = sum(dimension_score * weight for each dimension)
```

Round to nearest integer. Weights must sum to 1.0.

## Labels

| Score | Label | Color hint |
|-------|-------|------------|
| 80–100 | Healthy | `#1a3a2a` |
| 60–79 | Watchable | `#4a5568` |
| 40–59 | Stretched | `#744210` |
| 0–39 | Unsustainable | `#742a2a` |

## Session classification

Used for Focus and Fragmentation dimensions:

| Type | Criteria |
|------|----------|
| deep work | duration > 90 min AND commits ≥ 3 AND single repo |
| quick fix | duration < 30 min AND commits ≤ 2 |
| context switching | repos touched > 2 in session |
| normal | everything else |

Gap between consecutive commits > 90 min starts a new session.

## AI leverage (separate metric, not part of health score)

```
ai_leverage = ai_adjacent_commits / total_commits * 100
```

AI-adjacent = commit within 30 minutes after an AI session ends.

```
tokens_per_line = total_ai_tokens / max(1, net_lines_added)
```

## Tuning notes

- Increase **Rest** weight if burnout is a concern for the user.
- Increase **Focus** weight for IC engineers; decrease for managers doing reviews.
- **Consistency** assumes a 5-day work week — change divisor for different cadences.
