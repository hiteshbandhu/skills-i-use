# Workflows — Secure AI agents

Read the matching section when the user’s goal matches the decision tree in [SKILL.md](SKILL.md).

---

## Workflow A — OAuth & MCP authorization

**Use when:** replacing API keys, wiring MCP clients, or multi-hop agent toolchains.

### Steps

1. **Split roles** — MCP server = resource server only; separate authorization server (IdP/Keycard/Auth0) [src-001 @ 6:21], [src-009 @ 7:30].
2. **Flows** — Authorization code + consent for user-delegated agents; client credentials only for true service agents [src-001 @ 10:54].
3. **Kill shared secrets** — Backend token exchange; vault upstream creds; agent never holds long-lived env keys [src-009 @ 3:14].
4. **Headless consent** — CIBA / push approve for background jobs [src-009 @ 6:33], [src-001 @ 17:13].
5. **Registration** — Prefer push client registration or known public clients over anonymous dynamic registration [src-001 @ 12:46].
6. **Downstream APIs** — Token exchange + identity assertion for MCP→API chains; RAR for per-action scopes (payments) [src-001 @ 15:49].
7. **RAG** — Enforce ACL at retrieval middleware, not inside the model [src-009 @ 5:51].
8. **UX** — End users authorize like any app; no hand-edited MCP JSON for identity [src-011 @ 1:30].

### Agent deliverables

- [ ] OAuth architecture diagram (AS, RS, agent, user)
- [ ] Token lifetime + scope matrix per tool
- [ ] Incident traceability: user + agent + delegation chain

### Stop if

- MCP server also issues tokens and authenticates users → split AS/RS first [src-001 @ 7:47].

---

## Workflow B — Pre-launch agent vulnerability audit

**Use when:** agent has tools, sandboxes, or multi-tenant data APIs.

### Steps

1. **Recon** — Extract system prompt; map tools and data paths [src-002 @ 3:25].
2. **AuthZ** — Every tool call checks object ownership (IDOR on `user_id` / `document_id`) [src-002 @ 4:20].
3. **Principal** — Agent acts as end user, not service account with broad grants [src-002 @ 6:14].
4. **I/O hygiene** — Sanitize agent inputs/outputs like web apps [src-002 @ 7:18].
5. **Sandbox** — Firecracker-class isolation; read-only FS; block IMDS/credential paths [src-002 @ 8:47].
6. **SSRF** — No user-controlled URLs in privileged fetchers (Git, internal APIs) [src-002 @ 12:37].
7. **Prompt** — Policy puppeteering / inversion after classic appsec passes [src-002 @ 3:25], [src-010].

### Agent deliverables

- [ ] Tool matrix: AuthN, AuthZ, data scope per tool
- [ ] Red-team findings ranked P0/P1 with repro steps

### Stop if

- Shipping with service-level tokens and LLM-chosen access → block launch [src-002 @ 6:58].

---

## Workflow C — Enterprise agent identity (CIAM for AI)

**Use when:** B2B agents across CRM, email, tickets with compliance needs.

### Steps

1. **Headless login** — Long-lived refreshable sessions for agents; not human-only SSO UX [src-003 @ 2:00].
2. **Persona shadowing** — Scoped secondary principal per agent (`agent-1-user`) [src-003 @ 6:43].
3. **Delegation chains** — JWTs carrying original user across hops [src-003 @ 7:52].
4. **Capability tokens** — Time-bound single-action vouchers [src-003 @ 8:52].
5. **Human escalation** — Approve risky ops; monitor consent fatigue [src-003 @ 9:41].
6. **Middleware** — Untrusted agent code never hits systems directly (FGA, bot detection) [src-003 @ 15:52].
7. **Standards watch** — OAuth/OIDC-MCP, UMA, GNAP, OIDC-A, VCs [src-003 @ 11:20].

### Agent deliverables

- [ ] Identity pattern choice (shadow vs chain vs capability) per integration
- [ ] Audit log fields: human, agent, action, downstream system

### Stop if

- Pure impersonation with full human privileges → rescope [src-003 @ 7:20].

---

## Workflow D — Code-executing agent hardening

**Use when:** local CLI, Codex, shell tools, or containerized coding agents.

### Steps

1. **Isolate** — One VM/container per task; not host-wide yolo [src-005 @ 4:26].
2. **Network** — Default deny; domain allowlist when network required [src-005 @ 5:04].
3. **OS sandbox** — seatbelt / landlock / seccomp patterns (see openai/codex) [src-005 @ 6:47].
4. **Human review** — PR/diff review; operator watch + allowlists for browser agents [src-005 @ 9:51].
5. **Model + system** — Suspicion flags plus hard blocks; don’t trust LM-only monitors for high stakes [src-005 @ 9:40].
6. **Supply chain** — Scan deps on install paths (e.g. Socket MCP) [src-005 @ 11:46].

### Agent deliverables

- [ ] Sandbox + network policy doc
- [ ] Review gates for write/deploy/payment tools

### Stop if

- Unrestricted fetch of user-supplied issue/doc URLs → fix before enable [src-005 @ 8:58].

---

## Workflow E — Pre-production adversarial testing

**Use when:** subjective quality, safety categories, or injection risk before prod.

### Steps

1. **Brittleness fuzz** — Search over input perturbations with strong judges (Verdict/ensemble), not static golden-only [src-006 @ 6:16].
2. **Judges** — Debate/self-verify ensembles; domain GRPO rubrics where needed [src-006 @ 9:21].
3. **Hosted scan** — PyRIT / Azure Red Teaming Agent against app URL (query in, string out) [src-007 @ 5:24].
4. **Iterate** — Attack → score harm category → fix → rescan [src-007 @ 8:53].
5. **Injection drills** — Encoding, multilingual, long preamble, policy puppeteering exercises [src-010 @ 2:57].
6. **Layer** — Red team complements AuthZ/sandbox; does not replace [src-007 @ 4:06].

### Agent deliverables

- [ ] Eval harness spec (fuzz loop + harm categories)
- [ ] Top failures with mitigations and owners

### Stop if

- 100% on fixed golden set with no perturbation testing → add fuzz [src-006 @ 4:46].

---

## Workflow F — Public web AI bot policy

**Use when:** docs/app bandwidth spikes or unwanted training/operator crawlers.

### Steps

1. **Inventory** — GPTBot vs SearchBot vs ChatGPT-User vs Operator behaviors [src-008 @ 5:41].
2. **Policy** — robots.txt for intent; enforce with rate limits + bot SDK [src-008 @ 7:42].
3. **Segment** — Allow SEO/index bots; block training scrapers; separate rules for operator/checkout abuse [src-008 @ 4:27].
4. **Protect expensive paths** — Dynamic routes and APIs first [src-008 @ 1:13].
5. **Measure** — Bandwidth and cost before/after policy changes [src-008 @ 3:07].

### Agent deliverables

- [ ] Per-bot allow/block table tied to business goals
- [ ] Rate limit + detection config for prod

### Stop if

- Blocking all bots and losing discovery traffic without explicit decision [src-008 @ 5:19].

---

## Workflow G — Confidential remote inference

**Use when:** regulated or privacy-sensitive offload to cloud GPUs (PCC-style).

### Steps

1. **Requirements** — Stateless compute, enforceable guarantees, non-targetability, no privileged runtime, verifiable transparency [src-004 @ 2:30].
2. **Transport privacy** — OHTTP / relay so operator cannot tie user to payload [src-004 @ 5:46].
3. **Auth separation** — Blind signatures so auth metadata ≠ inference payload [src-004 @ 6:20].
4. **Attestation** — Client verifies build claims before encrypting [src-004 @ 10:03].
5. **Transparency log** — Public deployment hashes; detect drift [src-004 @ 11:52].
6. **Portable building blocks** — TPM, Sigstore/Rekor, confidential VMs on your cloud [src-004 @ 17:37].

### Agent deliverables

- [ ] Threat model vs “trust the API vendor ZDR checkbox”
- [ ] Control checklist mapped to your infra (not Apple-only)

### Stop if

- User expects custom fine-tune on PCC-class system → scope down [src-004 @ 16:32].
