# Workflows — Train LLMs locally

## Workflow A — Environment setup

### Steps

1. Confirm goal: **from scratch**, not fine-tune only [src-001 @ 1:23].
2. Prefer laptop for tiny fast models [src-001 @ 2:31].
3. Fallback: Colab free GPU if local insufficient [src-001 @ 2:39].
4. Clone workshop materials / nanochat-style repo [src-001 @ 1:21].

### Deliverables

- [ ] Hardware sheet (RAM, disk, expected runtime)

---

## Workflow B — Four building blocks

### Steps

1. **Tokenizer** — vocab size drives data needs [src-001 @ 4:42].
2. **Data** — curated corpus for domain [src-001 @ 4:38].
3. **Architecture** — small GPT-style stack for learning [src-001 @ 4:38].
4. **Training loop** — schedules, batching, checkpoints [src-001 @ 6:04].

### Deliverables

- [ ] Block-by-block checklist with sizes/hyperparams

---

## Workflow C — Execute training

### Steps

1. Tune batch size to device [src-001 @ 7:18].
2. Monitor loss; save checkpoints [src-001 @ 6:07].
3. Validate generations at intervals [src-001 @ 6:08].

### Deliverables

- [ ] Run log + sample outputs per checkpoint

---

## Workflow D — Post-training awareness

### Steps

1. Note: pretrain loops similar; fine-tune/post-train diverges [src-001 @ 6:22].
2. Plan optional SFT/alignment only after base model exists [src-001 @ 6:24].

### Deliverables

- [ ] Roadmap slide: scratch → eval → optional SFT
