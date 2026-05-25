# Workflows — Build generative media

---

## Workflow: image-models

**Use when:** selecting FLUX or similar image backbones.

### Steps

1. Match FLUX variant (base, Context) to gen vs edit use case [src-001 @ 0:02:13]
2. Clarify enterprise licensing vs open weights [src-001 @ 0:01:05]
3. Benchmark on domain imagery before commit [src-001 @ 0:05:49]

### Agent deliverables

- [ ] Model selection memo with eval samples

---

## Workflow: comfy-workflows

**Use when:** productionizing node-graph media pipelines.

### Steps

1. Build modular graphs (ControlNet, img2img) [src-002 @ 0:01:51]
2. Embed workflow metadata in outputs [src-002 @ 0:01:58]
3. Pin workflow versions for CI reproduction [src-002 @ 0:02:27]

### Agent deliverables

- [ ] Versioned Comfy workflow JSON + runbook

---

## Workflow: scale-launch

**Use when:** consumer launch may go viral.

### Steps

1. Run staged 10x capacity drills with monitoring [src-003 @ 0:01:37]
2. Plan queueing and repeated spike handling [src-003 @ 0:01:57]
3. Harden GPU path pre-marketing [src-003 @ 0:03:08]

### Agent deliverables

- [ ] Launch scale runbook (capacity steps, alerts, rollback)

### Stop if

- No load test before social/PR push [src-003 pitfalls]

---

## Workflow: api-ux

**Use when:** creator-facing API or product surface.

### Steps

1. Optimize for fast visual preview feedback [src-004 @ 0:01:15]
2. Label model capabilities clearly in catalog [src-004 @ 0:02:00]
3. Demo flows as if expert reviewers will judge [src-004 @ 0:14:18]

### Agent deliverables

- [ ] API UX spec with preview latency targets

---

## Workflow: media-platform

**Use when:** routing multiple models via a platform (fal-class).

### Steps

1. Route workloads across model catalog [src-005 @ 0:00:32]
2. Tune stacks per vertical (ads, fashion, gaming) [src-005 @ 0:05:27]
3. Track new open weights (FLUX, etc.) on platform [src-005 @ 0:04:37]

### Agent deliverables

- [ ] Multi-model routing matrix + SLA tiers

---

## Workflow: google-video

**Use when:** Veo 3 or GenMedia enterprise chains.

### Steps

1. Integrate Veo via generative media APIs [src-008 @ 0:00:49]
2. Check watermark/rights policies [src-008 @ 0:08:36]
3. Chain image→video→upscale for campaigns [src-006 @ 0:10:57]
4. Enable enterprise safety defaults on prompts [src-006 @ 0:15:04]

### Agent deliverables

- [ ] GenMedia pipeline diagram + compliance checklist

---

## Workflow: training-scale

**Use when:** training/serving large diffusion video.

### Steps

1. Model video token cost vs images [src-007 @ 0:04:52]
2. Use coarse-to-fine schedules for video [src-007 @ 0:08:55]
3. Align codecs/resolution with infra budget [src-007 @ 0:05:11]

### Agent deliverables

- [ ] Training cost estimator (resolution × duration × FPS)

---

## Workflow: curiosity-lab

**Use when:** exploring new gen-AI product ideas.

### Steps

1. Ship small demos per model capability [src-009 @ 0:07:03]
2. Follow non-obvious use cases via experimentation [src-009 @ 0:02:29]
3. Avoid only building obvious wrappers [src-009 @ 0:09:26]

### Agent deliverables

- [ ] Demo backlog with learnings per experiment
