# Workflows — Build RAG and AI search stacks

Read the matching section when the user’s goal matches the decision tree in [SKILL.md](SKILL.md).

---

## Workflow A — Grounding strategy (RAG vs alternatives)

**Use when:** deciding how proprietary knowledge enters the model.

### Steps

1. **Long context** — corpus fits in window; acceptable to scan whole library per question; watch cost and lost-in-middle [src-010 @ 3:03].
2. **Fine-tune** — only if knowledge is stable, access control is not per-document, and “forgetting” updates is acceptable [src-010 @ 3:48].
3. **RAG (default for enterprise)** — modular, governable, per-doc access; retrieve then answer [src-010 @ 3:03].
4. Plan for the **tricks layer** (chunking, hybrid, graph) to shrink as embeddings/rerankers absorb capability [src-010 @ 8:29].

### Agent deliverables

- [ ] One-page comparison for the user’s corpus size, update frequency, and compliance needs
- [ ] Chosen path + what you will *not* do this quarter

### Stop if

- User wants fine-tune for a 10M-doc vault with per-tenant ACL → redirect to RAG [src-010 @ 3:48].

---

## Workflow B — Hybrid retrieval stack

**Use when:** building or fixing the retrieval layer (not the agent loop yet).

### Steps (in order)

1. **Analyze ingest** — tokenization/stemming/positions for lexical; `_analyze` before indexing [src-007 @ 6:36].
2. **Lexical (BM25)** — brands, SKUs, statute IDs, single-token queries [src-007 @ 56:50].
3. **Dense vectors** — paraphrase and semantic match [src-007 @ 1:40:03].
4. **Sparse (ELSER/SPLADE-style)** — learned term expansion when needed [src-007 @ 56:50].
5. **Hybrid fusion** — RRF or weighted normalized scores; do not assume score calibration across retrievers [src-007 @ 1:28:06].
6. **Filters** — jurisdiction, dates, doc type in store or post-filter; expect filtered ANN to be slower, not faster [src-007 @ 4:01], [src-009 @ 6:05].
7. **Rerank** — cross-encoder on top-k only; rescoring window + min_score [src-007 @ 1:33:57].
8. **Ingest hygiene** — content-hash IDs; `create` not blind re-embed on unchanged files [src-007 @ 1:31:21].
9. **Embeddings** — domain-specific models; Matryoshka + quantization for storage [src-010 @ 6:50], [src-009 @ 5:10].

### Agent deliverables

- [ ] Retriever diagram (lexical + dense + optional sparse → fusion → rerank)
- [ ] Query routing rules (keyword-like vs phrasal)
- [ ] Ingest + index config checklist

### Stop if

- Vector-only on SKU/legal-citation queries without lexical branch [src-007 @ 1:28:06], [src-004 @ 3:43].

---

## Workflow C — Benchmark discipline (vectors and vendors)

**Use when:** comparing vector DBs or believing a vendor benchmark slide.

### Steps

1. Treat marketing benchmarks as **benchmarketing** until reproduced [src-008 @ 1:31].
2. Define **your** workload: data size, read/write ratio, query shape, latency SLO, hardware [src-008 @ 1:48].
3. Require **precision/recall** on ANN, not QPS alone [src-008 @ 7:28].
4. Test **filtered** ANN separately (filter paradox) [src-008 @ 4:01].
5. Run **nightly** automated track (Rally-style data + query mix) [src-008 @ 10:02].
6. When a competitor chart is flawed, extract what scenario they optimized for [src-008 @ 12:52].

### Agent deliverables

- [ ] Benchmark spec doc + nightly job stub
- [ ] Pass/fail gates before vendor selection

---

## Workflow D — Enterprise / regulated RAG

**Use when:** legal, finance, health — long expert queries, compliance, huge corpora.

### Steps

1. **Decompose queries** — semantic parts, implicit filters (dates, jurisdictions), keyword IDs, multi-hop regulations [src-004 @ 3:24].
2. **Eval-driven development** — expert labels → automated precision/recall on folders/sections before algorithm churn [src-004 @ 4:42].
3. **Separate paths** — offline ingestion at tens-of-millions scale vs low-latency online search [src-004 @ 7:05].
4. **Tenant isolation + retention + telemetry** at storage [src-004 @ 8:01].
5. **Lakehouse layout** — one format for blobs, embeddings, analytics, training features when scale demands [src-004 @ 9:28].

### Agent deliverables

- [ ] Query decomposition examples from real user questions
- [ ] Eval rubric + labeled set plan
- [ ] Compliance checklist (isolation, retention, audit logs)

### Stop if

- Team optimizes embeddings before any legal correctness metric exists [src-004 @ 4:51].

---

## Workflow E — Complexity-adjusted RAG roadmap

**Use when:** prioritizing what to build this sprint (David Karam ladder).

### Steps

1. Define **launch bar** + easy/medium/hard query sets [src-005 @ 2:01].
2. **Loss-analyze** failures before adding machinery [src-005 @ 2:01].
3. Ladder: in-memory/long context (small corpus) → BM25 (keyword queries) → vectors (phrasal) → cross-encoder on candidates → domain embeddings → ranking signals (price, popularity) → query fan-out → extra backends → distillation → UX degradation [src-005 @ 4:11–17:18].
4. **Fan out** complex assistant queries into narrow sub-queries; do not dump paragraphs into keyword engines [src-005 @ 12:19], [src-001 @ 13:29].

### Agent deliverables

- [ ] Failure bucket table → next technique (one change per experiment)
- [ ] Explicit “not yet” list to prevent premature rerank/graph spend

---

## Workflow F — Agentic search (context engineering)

**Use when:** agent must pull from files, DBs, web, memory — not fixed retrieve→prompt.

### Steps

1. Replace one-shot RAG with **search tools** the model calls when needed [src-001 @ 3:45].
2. Inventory tools per source: files, skills, semantic/SQL DB, web, memory, shell [src-001 @ 5:51].
3. Write rich tool docs: purpose, when to use/not use, prerequisites (load skill before ESQL) [src-001 @ 10:43].
4. Reinforce routing in system prompt when models pick wrong tool [src-001 @ 10:01].
5. Prefer **SQL/ESQL** for aggregations — never make the LLM count rows [src-001 @ 33:05].
6. Shell/grep: sandbox; optional semantic grep CLI for fuzzy local search [src-001 @ 36:38], [src-001 @ 41:30].
7. Reduce tool parameters or fan out queries yourself when backends are picky [src-001 @ 13:29].

### Agent deliverables

- [ ] Tool catalog with descriptions and guardrails
- [ ] System prompt addendum for routing
- [ ] Sandbox policy for shell tools

---

## Workflow G — Agent memory architecture

**Use when:** persistent copilots need believable state across sessions.

### Steps

1. Model memory types: persona, toolbox, conversation, workflow/episodic, entity, long-term [src-011 @ 3:57].
2. Loop: generate → store → retrieve → integrate → update → soft forget (no hard deletes) [src-011 @ 7:00].
3. Use large windows to **pull relevant** memory, not store everything [src-011 @ 6:45].
4. Store tool schemas in DB; retrieve ~10–21 relevant tools per call [src-011 @ 10:38].
5. Persist failed workflow steps for the next run [src-011 @ 12:14].
6. Expose vector, text, graph, geospatial retrieval modes to agentic RAG tools [src-011 @ 7:52].

### Agent deliverables

- [ ] Memory type map for the product
- [ ] Retention/decay policy
- [ ] Tool retrieval schema

---

## Workflow H — Evaluate augmented AI search

**Use when:** choosing or operating web search / RAG APIs with live ground truth.

### Steps

1. Accept web truth is **dynamic and contextual** [src-003 @ 3:29].
2. Complement static sets (SimpleQA) with **dynamic Q&A** from live search + evidence-linked generation [src-003 @ 6:34].
3. Score reference-free: completeness, % relevant retrieved docs, hallucination vs grounding [src-003 @ 14:11].
4. Triangulate failures: incomplete + relevant docs → retrieve more; no relevant docs → abstain [src-003 @ 18:57].
5. Require providers to return **retrieved documents**, not citations-only [src-003 @ 16:01].

### Agent deliverables

- [ ] Eval harness outline + metric definitions
- [ ] Provider comparison matrix (docs returned, dynamic eval rank)

---

## Workflow I — Neural web search for research agents

**Use when:** open-web agents need long semantic queries and high recall.

### Steps

1. Treat agent search as: exact intent, multi-paragraph queries, large result sets [src-006 @ 9:06].
2. Expose knobs: `num_results`, domains, dates, neural vs keyword [src-006 @ 14:43].
3. Chain: neural discovery → keyword drill-down on entities [src-006 @ 17:00].
4. Use research endpoints that run many searches + synthesis when appropriate [src-006 @ 18:16].

### Agent deliverables

- [ ] Tool contract for web search (modes, limits, filters)
- [ ] Example multi-step research trace

### Stop if

- Single keyword query expected to return “every startup in X” [src-006 @ 11:20].

---

## Workflow J — Managed enterprise RAG (fast path)

**Use when:** time-to-production beats owning BM25+embed+rerank+LLM glue.

### Steps

1. Datastore → upload docs → verify table/image parsing in UI [src-012 @ 7:08].
2. Default agent stack; test grounded answers on contradictory docs [src-012 @ 23:44].
3. Tune extraction, reranking, retrieval, generation in agent editor [src-012 @ 26:27].
4. Use **grounded LM** for regulated domains [src-012 @ 15:47].
5. Optional MCP to desktop clients [src-012 @ 18:22].

### Agent deliverables

- [ ] Ingest checklist + grounding test cases
- [ ] Swap plan if you later need modular components

---

## Workflow K — Document toolbox for knowledge work

**Use when:** PDFs, Excel, SharePoint — automation beyond naive vector RAG.

### Steps

1. Connectors with permissions + metadata sync [src-013 @ 4:26].
2. **Parsing quality gate** (LLM+VLM+validation) before indexing [src-013 @ 6:20].
3. Tools: semantic search, file lookup, manipulation, structured SQL — not vector-only [src-013 @ 5:12].
4. Match UX to orchestration: chat → ReAct + human steering; batch → constrained workflows [src-013 @ 11:32].
5. Excel: semantic map of sheet + specialized tools (not raw text-to-CSV) [src-013 @ 9:51].

### Agent deliverables

- [ ] Connector list + permission model
- [ ] Parse QA samples
- [ ] Assistant vs automation architecture choice

---

## Workflow L — Product knowledge base (e.g. sales agent)

**Use when:** users upload assets async; agent retrieves per task (Alice pattern).

### Steps

1. Upload → parse/chunk/embed pipeline (webhooks from specialist parsers) [src-002 @ 8:54].
2. Chunk: markdown headers → sentences → tokens [src-002 @ 14:28].
3. Retrieval at generation time; avoid manual “library” blocking campaigns [src-002 @ 4:51].
4. Trust UI: chunk inspector / embedding visualization for stakeholders [src-002 @ 19:05].
5. Ship production; benchmark parsers after real traffic [src-002 @ 21:10].

### Agent deliverables

- [ ] Ingest pipeline diagram
- [ ] Chunking config + parser vendor choices
- [ ] Demo script for trust UI
