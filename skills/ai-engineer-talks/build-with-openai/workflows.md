# Workflows — Build with OpenAI

Themes map to talk clusters. Open the section matching [SKILL.md](SKILL.md).

---

## Theme: function-calling

**Talks:** src-004 (primary), src-002, src-003

**Use when:** building tool loops, agents, or RAG via tools.

### Steps

1. Define tools as **JSON Schema** functions on `chat.completions` or Responses API [src-004 @ 0:17]
2. Loop: append `assistant` tool_calls → run tools → append `tool` results → call model again [src-004 @ 0:23]
3. Cap active tools ~**10–20**; use routing agent or flat FT if 100+ [src-004 @ 1:16]
4. Enable **parallel** tool calls for independent IO [src-004 @ 0:50]
5. Model RAG as retrieve + answer tools, not a separate magic layer [src-004 @ 0:23]
6. Add handoffs only after **evals** show single-agent limits [src-004 @ 1:12]
7. **Eval tool execution** and side effects [src-004 @ 1:21]
8. Memory: retrieve-before-write; hybrid semantic + keyword [src-004 @ 1:32]

### Deliverables

- [ ] Tool schema pack + loop diagram
- [ ] Eval set for tool selection and args

### Stop if

- 50+ tools with no router → add hierarchy or fine-tune [src-004 @ 1:16]

---

## Theme: fine-tuning

**Talks:** src-005 (primary), src-004

**Use when:** prompts cannot route tools or enforce format.

### Steps

1. Exhaust prompt/schema fixes first [src-005 @ 1:13]
2. **SFT** for imitation / trajectories (include function-call messages) [src-005 @ 0:27]
3. **DPO** for preference pairs; validate held-out [src-005 @ 1:03]
4. **RFT** when you have graders: string, similarity, sandboxed Python, model judge [src-005 @ 0:48]
5. RFT datasets: **40–80** high-signal examples for narrow tasks [src-005 @ 0:47]
6. Use cookbooks for graders + function-calling datasets [src-005 @ 1:12]
7. Analyze failures with reasoning model to find missing data (even if not FT) [src-005 @ 1:45]

### Deliverables

- [ ] Grader spec + example JSONL
- [ ] SFT vs DPO vs RFT decision note

---

## Theme: voice

**Talks:** src-007, src-008, src-009

**Use when:** shipping speech interfaces or Realtime API.

### Steps

1. Choose architecture: **speech-to-speech** (Realtime) vs STT→LLM→TTS [src-008 @ 0:04]
2. Prototype transport: **WebSocket**; production consumer: **WebRTC** [src-009 @ 0:04]
3. Use **Agents SDK** + Realtime; delegate hard logic to o3/o4-mini via tools [src-008 @ 0:08]
4. Instructions: announce long work; never say "calling a tool" [src-007 @ 1:04]
5. Eval: **traces first**, then WER, task success, latency, quality [src-008 @ 0:13]
6. Telephony: consider μ-law audio modes [src-007 @ 0:41]
7. Wake word: **not built-in**—custom VAD + manual commit [src-007 @ 1:24]
8. Consider Pipecat for faster integration [src-009 @ 0:01]

### Deliverables

- [ ] Transport choice doc (WS vs WebRTC)
- [ ] Voice eval rubric + trace dashboard requirements

---

## Theme: sandboxes

**Talks:** src-006

**Use when:** running untrusted agent code or RL rewards.

### Steps

1. Classify need: inference **code exec**, **RL reward** batch, full **Linux agent** [src-006 @ 0:01]
2. Isolate with **containers** for deps + **microVMs** for tenancy [src-006 @ 0:10]
3. Control plane: API spawns VM, overlay FS, seeded runtimes (Python/Node) [src-006 @ 0:30]
4. Plan persistence: snapshots (btrfs), memory ballooning for density [src-006 @ 0:39]
5. Build vs buy: evaluate Arrakis-class OSS vs managed interpreter [src-006 @ 0:00]

### Deliverables

- [ ] Threat model + isolation boundary diagram
- [ ] Session lifecycle (spawn → exec → teardown/snapshot)

---

## Theme: coding-agents

**Talks:** src-012 (primary), src-004

**Use when:** coding agents or terminal agents in product.

### Steps

1. Split **model vs harness**; expect rebuild pressure each model gen [src-012 @ 0:01]
2. Prefer **Codex** harness (repo edit, terminal, PR, Slack, MCP) over greenfield [src-012 @ 0:08]
3. Tune prompts per model when adding **custom tools** [src-012 @ 0:04]
4. Expose via **Agents SDK** + Codex tool for dynamic connectors [src-012 @ 0:13]
5. Read harness source for non-coding automation patterns [src-012 @ 0:17]

### Deliverables

- [ ] Build-vs-buy on Codex vs custom harness
- [ ] Integration map (GitHub, Slack, MCP)

---

## Theme: multimodal

**Talks:** src-010, src-011

**Use when:** vision, image, video, or GPT-4o native audio/screen.

### Steps

1. **GPT-4o** for native voice + vision sessions [src-010 @ 0:06]
2. Screen-share coaching: vision + voice on live UI [src-010 @ 0:11]
3. Video: **frame sample → vision describe**, not transcript-only [src-011 @ 0:14]
4. Image products: plan iteration UX; API quality will improve [src-011 @ 0:09]
5. Roadmap **agents with image input** for visual web tasks [src-011 @ 0:18]

### Deliverables

- [ ] Modality matrix (input/output per feature)
- [ ] Frame pipeline spec for video features

---

## Theme: agents-enterprise

**Talks:** src-001, src-002, src-003

**Use when:** strategy, enterprise rollout, co-create UX.

### Steps

1. Executive framing: **domain agents** on foundation models [src-001 @ 38:30]
2. Enterprise journey: strategy → **1–2 pilots** → enablement [src-002 @ 4:10]
3. Define evals **before** production scale [src-002 @ 5:24]
4. Ship **one purpose-built agent**; observe bottlenecks [src-002 @ 12:13]
5. **Guardrails** parallel; defer refunds/PII until pass [src-002 @ 15:45]
6. Co-create UX: canvas/artifact, multi-agent on same doc [src-003 @ 18:03]
7. Synthetic **user personas** for collaboration eval [src-003 @ 12:12]

### Deliverables

- [ ] Pilot charter + guardrail matrix
- [ ] Co-create surface spec (beyond chat)

### Stop if

- Multi-agent network on day one → revert to single agent [src-002 @ 16:12]
