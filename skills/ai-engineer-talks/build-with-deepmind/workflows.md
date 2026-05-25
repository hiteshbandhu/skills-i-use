# Workflows — Build with DeepMind

---

## Workflow: gemini-api

**Use when:** shipping on Gemini API / Gemini 3 / Nano Banana visuals.

### Steps

1. Baseline on latest Gemini Pro for reasoning tasks [src-001 @ 0:01:16]
2. Use Gemini 3 tool-calling for agentic flows; eval regressions [src-002 @ 0:02:12]
3. Prototype images with Nano Banana Pro; integrate via API quickstarts [src-002 @ 0:05:12]
4. Subscribe to API release notes; rerun eval suite per upgrade [src-001 @ 0:04:53]

### Agent deliverables

- [ ] Gemini integration checklist (models, tools, quotas)
- [ ] Eval matrix for model upgrade PR

### Stop if

- Pinning deprecated Gemini without migration plan [src-001 pitfalls]

---

## Workflow: gemma-open

**Use when:** self-hosting or fine-tuning open Gemma models.

### Steps

1. Select Gemma 4 variant by parameter count vs hardware [src-003 @ 0:01:28]
2. Test on-device agent demos on target phones [src-003 @ 0:02:46]
3. Fine-tune for domain coding/agent tasks if needed [src-003 @ 0:03:29]

### Agent deliverables

- [ ] Model size vs latency benchmark table
- [ ] Hosting plan (GPU/CPU) with cost estimate

---

## Workflow: gemini-nano

**Use when:** Android on-device features with Gemini Nano.

### Steps

1. Integrate ML Kit Prompt API for Nano [src-004 @ 0:05:22]
2. Gracefully degrade when Nano unavailable [src-004 @ 0:05:54]
3. Keep sensitive prompts on-device [src-004 @ 0:02:09]

### Agent deliverables

- [ ] Android capability detection + fallback UX spec

---

## Workflow: live-agents

**Use when:** voice or realtime conversational agents.

### Steps

1. Prototype with Gemini API calls, then add Live audio [src-005 @ 0:09:04]
2. Use Interactions API for multi-step agent flows [src-005 @ 0:10:03]
3. Design support-style flows with tool hooks [src-005 @ 0:08:25]

### Agent deliverables

- [ ] Live vs batch API architecture diagram
- [ ] Voice latency + tool-call eval plan

---

## Workflow: proactive-agents

**Use when:** async coding agents (Jules-class) with human trust.

### Steps

1. Add observation gates before autonomous actions [src-006 @ 0:04:34]
2. Insert critic/review agent before merging changes [src-006 @ 0:09:52]
3. Dashboard agent activity for users [src-006 @ 0:09:00]

### Agent deliverables

- [ ] Proactive agent permission model + activity log schema

---

## Workflow: agent-manager

**Use when:** IDE-integrated agents with browser/tools.

### Steps

1. Centralize tools/browser/editor in agent manager hub [src-007 @ 0:02:20]
2. Scope browser retrieval with safety policies [src-007 @ 0:03:24]
3. Mirror IDE sidebar patterns for visibility [src-007 @ 0:02:46]

### Agent deliverables

- [ ] Agent control plane component list (tools, browser, editor)

---

## Workflow: edge-ai

**Use when:** laptop/IoT/mobile edge inference.

### Steps

1. Pick Gemma edge sizes (E2B/E4B) for constraints [src-008 @ 0:04:00]
2. Benchmark edge vs cloud for realtime features [src-008 @ 0:03:04]
3. Plan hybrid fallback to cloud API [src-008 @ 0:04:21]

### Agent deliverables

- [ ] Edge deployment matrix (device classes, models, SLAs)

---

## Workflow: generative-scale

**Use when:** training/serving large diffusion image/video.

### Steps

1. Budget video token volume separately from images [src-009 @ 0:04:52]
2. Use coarse-to-fine / multi-scale training for video [src-009 @ 0:08:55]
3. Align codec and resolution targets with infra capacity [src-009 @ 0:05:11]

### Agent deliverables

- [ ] Media training cost model (resolution × duration × FPS)
