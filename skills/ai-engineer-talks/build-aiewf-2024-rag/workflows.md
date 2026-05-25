# Workflows — Build AIEWF 2024 RAG

## Workflow A — Layout-aware ingest (EyeLevel)
1. Audit % table/figure pages [src-002 @ 1:21]
2. Layout-preserving chunks + metadata [src-002 @ 3:47]
3. Rerank; golden queries on table facts [src-002 @ 5:24]

## Workflow B — GraphRAG (Neo4j)
1. Baseline vector RAG eval [src-003 @ 10:14]
2. Add entities/relations at ingest [src-003 @ 6:51]
3. Enable community summaries for global queries [src-003 @ 8:32]

## Workflow C — Eval-driven RAG compass
1. Tag failure: retrieval vs generation [src-004 @ 5:01]
2. Iterate split size, rerank, terminology [src-004 @ 14:44]
3. One change per eval run [src-004 @ 9:48]

## Workflow D — Pydantic structured pipeline (Jason Liu)
1. Define answer schema with validators [src-005 @ 12:19]
2. Instructor repair loops [src-005 @ 1:32]
3. Nested types for tables/captions [src-005 @ 11:00]

## Workflow E — MongoDB document + vector
1. RAG vs long-context decision [src-006 @ 1:22]
2. Co-locate vectors + ACL metadata [src-006 @ 6:08]
3. Log prompts with source docs [src-006 @ 10:36]

## Workflow F — Extended Mind Transformers
1. Compare RAG vs memory tokens on horizon tasks [src-007 @ 1:30]
2. Tune memory token capacity [src-007 @ 12:56]

## Workflow G — Construction vertical agents
1. Index massive spec libraries [src-001 @ 1:34]
2. Human-in-loop on safety-critical actions [src-001 @ 4:45]

## Workflow H — Personal assistant data graph
1. Model calendar/contacts as data not prompts [src-008 @ 3:40]
2. LLM only when deterministic rules fail [src-008 @ 13:32]
