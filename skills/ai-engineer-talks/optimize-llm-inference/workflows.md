# Workflows — Optimize LLM inference

## Workflow A — Groq / LPU latency
1. Tokens/sec + variance SLOs [src-002 @ 2:08]
2. Agent loops that benefit from speed [src-002 @ 14:25]

## Workflow B — OSS production inference
1. Quantization + kernels [src-004 @ 8:43]
2. Router small/large models [src-004 @ 2:07]
3. Pain-per-token at concurrency [src-004 @ 10:24]

## Workflow C — MoE networking
1. Rail-optimized IB for expert traffic [src-001 @ 7:56]
2. Eliminate choke points [src-001 @ 12:38]

## Workflow D — Serverless fine-tune bursts
1. Package training fn; autoscale GPUs [src-005 @ 2:53]
2. Compare many LoRAs quickly [src-005 @ 0:43]

## Workflow E — Frontier system design
1. Prefill vs decode bottlenecks [src-006 @ 5:11]
2. Interconnect/transceiver plan [src-006 @ 15:05]

## Workflow F — Coding agent infra
1. Sandboxed execution [src-007 @ 8:37]
2. Ticket-level eval [src-007 @ 12:10]

## Workflow G — Gemma tier selection
1. Size tier vs latency [src-008 @ 4:35]
2. Instruction-following for agents [src-008 @ 13:18]
