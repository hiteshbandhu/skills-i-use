# CTO Weekly Review — AI Session Log Sources

Used by the **AI Collector** subagent (Step 1). Prefer running the script:

```bash
SINCE="7 days ago" bash scripts/collect-ai-sessions.sh
```

If scripts are unavailable, follow the manual steps below.

## Log locations by agent

| Agent | Session log path | Format |
|-------|------------------|--------|
| Claude Code | `~/.claude/projects/**/*.jsonl` | JSONL with `timestamp`, `role`, `content` |
| Cursor | `~/.cursor/projects/**/agent-transcripts/*.jsonl` | JSONL — adapt field names |
| Codex | `~/.codex/sessions/**/*.jsonl` | JSONL — adapt field names |

## Script output format

```
AI_SESSION|project|lines|chars|est_tokens|first_ts|last_ts|filepath
TOPIC|first 120 chars of user message
TOTAL_AI_TOKENS|12345
TOTAL_AI_SESSIONS|7
```

## AI leverage ratio

**AI-adjacent commits** = commits made within 30 minutes after any AI session ends.
Cross-reference `LAST_TS` from AI sessions with `COMMIT|...|%at` from git collection.

If no session logs exist, return empty and note absence — do not fail the report.
