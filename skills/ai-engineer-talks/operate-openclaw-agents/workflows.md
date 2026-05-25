# Workflows — Operate OpenClaw agents

Read the matching section when the user’s goal matches the decision tree in [SKILL.md](SKILL.md).

---

## Workflow A — Personal OpenClaw (incremental trust)

**Use when:** one person, life/work context, Obsidian or similar KB, no big-bang access.

### Steps (in order — do not skip)

1. **Single channel** — WhatsApp/Telegram/Discord; one chat capability only [src-005 @ 1:51].
2. **One workflow** — e.g. morning briefing OR inbox links OR one integration; prove it works [src-005 @ 2:08].
3. **Add knowledge base** — markdown vault (Obsidian); agent gets search + memory hooks [src-005 @ 5:03].
4. **Split channels by job** — general, inbox, briefing, playground (experiments only) [src-005 @ 13:10].
5. **Ambient ops** — scheduled: backup state, reindex, upgrade OpenClaw with pre-flight checks [src-005 @ 9:02].
6. **Memory files** — maintain `soul.md`, `critical-rules.md` (rules repeated at top of agent instructions) [src-005 @ 15:22].

### Agent deliverables

- [ ] Channel list + what each is allowed to do
- [ ] Cron/launchd (or equivalent) for overnight backup + index
- [ ] Upgrade runbook: verify → upgrade → restart gateway → smoke test
- [ ] `critical-rules.md` draft (5–10 non-negotiables)

### Stop if

- User wants email/OS/calendar on day one → refuse; explain incremental path [src-005 @ 1:34].
- No markdown KB and no plan for context → agent will hallucinate confidently [src-006 @ 3:35].

### Prefer local when

- Personal life context (messages, banks, health) → Mac mini or dedicated machine [src-006 @ 6:30].

---

## Workflow B — Enterprise OpenClaw in containers

**Use when:** team rollout, security review, reproducible onboarding.

### Steps

1. **Containerize** — Podman or Docker; state on volumes; no native host install [src-001 @ 4:02].
2. **Secrets** — host secrets (Podman secrets / K8s secrets) → OpenClaw **secret refs**, not raw env in config [src-001 @ 6:22].
3. **Baseline image** — company-approved MCPs, skills, auth template; clone per hire [src-001 @ 11:45].
4. **Personalize** — per-user overlay (extra skills/MCPs) after baseline works [src-001 @ 12:30].
5. **Lift to K8s** — same image + PVC; develop locally first [src-001 @ 9:03].

### Agent deliverables

- [ ] `Containerfile` or image reference + volume mounts documented
- [ ] Secret mapping table (secret name → OpenClaw ref → provider)
- [ ] Baseline vs personalized directory layout
- [ ] Security one-pager for reviewers (sandbox, secret indirection, no keys in logs)

### Stop if

- API keys in plain `config.yaml` or committed env files → fix before deploy [src-001 @ 7:24].

---

## Workflow C — Scale agents on Kubernetes

**Use when:** many parallel tasks, per-task isolation, not one shared Slack bot for everything.

### Steps

1. **Clarify protocol** — MCP = tools; ACP = client↔agent session; pick deliberately [src-002 @ 5:22].
2. **One agent per task** — disposable pod/VM per job; sync state (rsync/Dropbox-style) if needed [src-002 @ 13:18].
3. **Orchestrator** — operator/Helm (e.g. Spritz pattern) spawns agents; UI when Slack can't multi-agent [src-002 @ 15:14].
4. **Do not** assume one Slack app = many isolated agents without platform support [src-002 @ 13:33].

### Agent deliverables

- [ ] Architecture diagram: concierge → spawns task agent → artifact sync
- [ ] Pod spec template (resources, secrets, volume, harness CLI)
- [ ] Lifecycle: create → run → archive logs → destroy

---

## Workflow D — Maintainer / PR triage

**Use when:** OpenClaw contrib, drowning in PRs, "please fix" spam.

### Steps for each PR

1. **Ask intent** — what broke? repro? don't trust AI-generated description alone [src-002 @ 8:17].
2. **Classify** — bug / feature / user slop / needs human design → bin, don't auto-merge [src-002 @ 9:00].
3. **Mechanical fixes first** — CI green, conflicts resolved by agent loop where safe [src-002 @ 10:01].
4. **Review loop** — superficial pass → fundamental issues → escalate human [src-002 @ 10:47].
5. **Extract signal** — even bad PRs indicate broken UX/docs [src-002 @ 9:00].

### Agent deliverables

- [ ] PR triage comment template (intent, repro, verdict)
- [ ] Labels or bins: `slop` `needs-design` `mechanical-only` `ready`
- [ ] Optional ACPX-style JSON checklist for automated pre-review

### Stop if

- Merge without repro or without intent → reject [src-002 @ 8:35].

---

## Workflow E — Malleable evals (changing harness)

**Use when:** OpenClaw or any self-modifying harness; static benchmarks feel stale.

### Steps

1. **Abandon frozen-only suites** as sole gate [src-003 @ 4:22].
2. **Define intent outcomes** — rubrics for ambiguity, personality, org policy [src-003 @ 10:01].
3. **Mine production traces** — when user behavior shifts, auto-suggest new cases [src-003 @ 10:43].
4. **Always-on eval** — sample live traffic; agents judging agents where bounded [src-003 @ 11:19].
5. **Wire telemetry** — cost, errors, tool failures → harness self-correction hooks [src-003 @ 11:36].
6. **Watch the 20%** — weird edge usage; evals must adapt, not freeze [src-003 @ 13:33].

### Agent deliverables

- [ ] Intent rubric (5–10 dimensions, scored)
- [ ] Trace → test-case promotion rule
- [ ] Dashboard metrics: drift alerts, regression on intent not exact strings

---

## Workflow F — Local vs cloud personal agent

**Use when:** user asks "should I run my agent in the cloud?"

### Decide

| Question | If yes → |
|----------|----------|
| Needs iMessage, multi-app personal context? | Strong bias **local** [src-006 @ 3:48] |
| Must work while laptop closed? | **Dedicated machine** (Mac mini), not phone [src-006 @ 6:30] |
| Buying/subscriptions/deletes possible? | Require **catastrophic-action** human confirm [src-006 @ 16:07] |
| Only summarizing public web/news? | Cloud may suffice |

### Agent deliverables

- [ ] Recommendation: local / hybrid / cloud with explicit tradeoffs
- [ ] List of integrations and which machine they run on
- [ ] Action allowlist + "always ask" list for irreversible ops

---

## Workflow G — Company agent in Slack (Viktor-style)

**Use when:** building **team** agent, not personal OpenClaw.

### Steps

1. **Treat as hire** — permissions onboarding, not "install a tool" [src-004 @ 15:53].
2. **Shared integrations** — one admin connects Meta/PostHog/etc.; scope per team [src-004 @ 6:08].
3. **Channel isolation** — exec context must not leak to eng channel [src-004 @ 7:59].
4. **Rollout proactivity slowly** — pilot users first; day-one DM-everyone fails security review [src-004 @ 14:05].
5. **Slack UX** — threads, edits, reactions, DMs = input; map to sandboxes explicitly [src-004 @ 10:26].

### Agent deliverables

- [ ] Integration matrix: who connects, who inherits, visibility per channel
- [ ] Rollout phases: pilot → team → proactivity
- [ ] DM/thread continuity rule (don't spawn blank context on new DM) [src-004 @ 11:11]

### Stop if

- Personal Gmail/workspace connected as team integration → block [src-004 @ 16:06].

---

## Quick reference (sources)

| Workflow | Primary source |
|----------|----------------|
| A Personal | [src-005](https://www.youtube.com/watch?v=sJ2jc7leKBk) |
| B Enterprise containers | [src-001](https://www.youtube.com/watch?v=F1DYkY1BlfM) |
| C K8s scale | [src-002](https://www.youtube.com/watch?v=VaS2h-dY1-4) |
| D Maintainer | [src-002](https://www.youtube.com/watch?v=VaS2h-dY1-4) |
| E Evals | [src-003](https://www.youtube.com/watch?v=4VhbYlfC7Gs) |
| F Local/private | [src-006](https://www.youtube.com/watch?v=jMoAaZP_Kkw) |
| G Company Slack | [src-004](https://www.youtube.com/watch?v=ohKt066uFhg) |

Playlist: https://www.youtube.com/playlist?list=PLcfpQ4tk2k0XkJKw4Idupyhb66vjx4Eu9

Raw transcripts: `playlists/openclaw/raw/` in [ingest-into-skills](https://github.com/hiteshbandhu/ingest-into-skills).
