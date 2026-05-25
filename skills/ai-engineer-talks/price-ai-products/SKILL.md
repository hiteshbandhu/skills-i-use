---
name: price-ai-products
description: >
  Runs Stripe-style workflows for AI product pricing — value definition, charge
  metrics, hybrid models, billing guardrails, and fast iteration. Use when the
  user prices an AI feature, picks usage vs seats, designs credits, or says
  "AI pricing", "hybrid pricing", "margin risk", "price AI SaaS".
---

# Price AI products

Playbook from Mayank Pant (Stripe). Five workflows map to the five-step framework in [workflows.md](workflows.md).

```
├─ Define customer-perceived value          → A
├─ Choose charge metric                     → B
├─ Pick pricing model (hybrid default)      → C
├─ Add billing guardrails                   → D
└─ Iterate pricing (hypothesis, not final)  → E
```

Source: `playlists/aie-for-founders/`. Optional: `{SKILL_OUTPUT_DIR}/price-ai-products/`
