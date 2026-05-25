---
name: build-generative-media
description: >
  Builds and ships generative image/video products—FLUX, ComfyUI workflows, Veo,
  fal platforms, Luma-scale launches, and API-first creator UX. Use when working
  on diffusion pipelines, Comfy graphs, video models, generative media infra, or
  viral consumer media launches.
---

# Build generative media

Action playbook from nine AI Engineer generative media talks. **Do not summarize** — pick a workflow theme.

**Supporting files:** [workflows.md](workflows.md) · [source-index.md](source-index.md)

Optional: `./skill-outputs/build-generative-media/`

---

## Step 0 — Pick workflow

```
What is the user trying to do?
├─ Choose image model (FLUX, open research)           → image-models
├─ ComfyUI reproducible node pipelines                → comfy-workflows
├─ Viral consumer launch / GPU scale (Luma)           → scale-launch
├─ Creator API UX (Replicate-style)                   → api-ux
├─ Multi-model platform routing (fal)                 → media-platform
├─ Google Veo / GenMedia enterprise chains            → google-video
├─ Diffusion training/serving at scale (DeepMind)     → training-scale
└─ Exploration mindset for new modalities             → curiosity-lab
```

---

## Install

```bash
cp -r skills/build-generative-media ~/.cursor/skills/
cp -r skills/build-generative-media ~/.codex/skills/
```

Source: `playlists/generative-media-ai-engineer/`.

---

## Cross-cutting rules

| Rule | Source |
|------|--------|
| Embed workflow JSON in outputs for reproducibility | [src-002 @ 0:01:58] |
| Rehearse 10x scale before viral marketing | [src-003 @ 0:01:37] |
| Video compute ≠ image—budget tokens separately | [src-007 @ 0:04:52] |
| Enterprise gen media needs brand/safety defaults | [src-006 @ 0:15:04] |
| Demoable, legible APIs beat opaque pipelines | [src-004 @ 0:01:15] |

---

## Output

Name theme; artifacts under `./skill-outputs/build-generative-media/` when requested.
