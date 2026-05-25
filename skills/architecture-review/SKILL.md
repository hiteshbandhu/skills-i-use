---
name: architecture-review
description: >
  Run a structured architecture decision process using subagent personas that debate
  the decision, then produce a signed ADR (markdown + optional HTML) and update a
  decision registry. Triggers on "should I use X or Y", "architecture decision", "ADR",
  "help me decide between", "which approach", "debate this", "tech decision". Use
  whenever the user is making a technical or architectural choice and needs structured
  thinking, not just a list of tradeoffs.
---

# Architecture Decision Record — Subagent Debate Skill

Structured persona debate → synthesis → markdown ADR (+ optional HTML report) → registry index.

Works with any coding agent that can run subagents. No external API calls required.

**Supporting files** (read when needed):
- [personas.md](personas.md) — persona and synthesis prompts
- [adr-template.md](adr-template.md) — markdown ADR output format

---

## Step 0 — Elicit the Decision

Ask the user (in one message, all at once):

1. **What is the decision?** (e.g. "FTS5 vs pgvector for legal document search")
2. **What are the hard constraints?** (latency, cost, team size, existing infra, timeline)
3. **What is the context?** (stage of product, scale, who will maintain this)
4. **Do you have a leaning already?** (optional — being honest about priors helps)
5. **What does "good" look like?** (what would make this decision clearly correct in 6 months)

Do not proceed until you have at least 1, 2, and 3.

Also resolve **output settings** (infer from request if stated, else use defaults).
See [../OUTPUT.md](../OUTPUT.md) for the shared convention across all skills.

| Setting | Resolution |
|---------|------------|
| Output directory | `{SKILL_OUTPUT_DIR}/architecture-review/` — default root `./skill-outputs/` |
| Include SRE persona | Yes if user asks, or decision touches deployment/monitoring/on-call/scaling/data durability/managed-vs-self-hosted |
| HTML report | Yes by default; skip if user says "ADR only", "markdown only", or "no report" |

Create the output directory if it does not exist.

---

## Step 1 — Brief All Subagents

Construct a decision brief from the user's answers:

```
DECISION: [what is being decided]
CONSTRAINTS: [hard constraints]
CONTEXT: [product stage, scale, team, infra]
OPTIONS: [Option A] vs [Option B] (vs [Option C] if applicable)
SUCCESS CRITERIA: [what good looks like]
USER LEANING: [if stated, else "none stated"]
INCLUDE_SRE: [yes/no]
```

---

## Step 2 — Run the Debate

Read [personas.md](personas.md). Run subagents in parallel when supported.

**Always run (3 subagents):** Pragmatist, Architect, Contrarian

**Optionally run (4th subagent):** SRE — when `INCLUDE_SRE: yes`

Pass each subagent:
1. The decision brief from Step 1
2. The matching persona prompt from `personas.md`
3. Instruction: respond using the format in the persona prompt

Keep subagent contexts isolated — no persona sees another's response until synthesis.

| Persona | Icon | HTML color |
|---------|------|------------|
| Pragmatist | ⚙️ | `#111111` |
| Architect | 🏛 | `#4a5568` |
| Contrarian | ⚡ | `#744210` |
| SRE | 🔧 | `#2c5282` |

---

## Step 3 — Synthesis Pass

After all persona subagents return, synthesize using the **Synthesis** prompt in
[personas.md](personas.md).

**Preferred:** Run a synthesis subagent with all persona responses as context.

**Fallback:** Synthesize yourself as the orchestrating agent using the same format.

---

## Step 4 — Write Markdown ADR

Always save a markdown ADR. Fill in [adr-template.md](adr-template.md) from synthesis
output and persona responses.

**Path:** `{output_dir}/ADR-NNNN-[decision-slug].md`

**ADR numbering:** Scan `{output_dir}/` for existing `ADR-*.md` files. Use the next
sequential number (`ADR-0001`, `ADR-0002`, …). Start at `ADR-0001` if none exist.
The date lives inside the document, not the filename.

---

## Step 5 — Generate HTML Report (optional)

Skip if user chose ADR-only mode.

**Path:** `{output_dir}/ADR-NNNN-[decision-slug].html` (same NNNN and slug as the `.md`)

Link to the markdown ADR from the HTML header.

### Design spec
```
Page bg:        #f8f7f5
Card bg:        #ffffff
Border:         1px solid #e8e5de
Primary text:   #111111
Muted:          #6b6b6b
Hint:           #a8a39a
Pragmatist:     #111111
Architect:      #4a5568
Contrarian:     #744210
SRE:            #2c5282
Synthesis:      #1a3a2a
Font:           Georgia/serif for debate sections + system-ui for chrome
NO gradients. NO purple. Light and premium.
```

### Report sections

**HEADER** — "Architecture Decision Record" · date · link to `.md` · "Export PDF" (print)

**DECISION TITLE** — large, prominent

**CONTEXT STRIP** — 3 pills: constraints, product stage, success criteria

**THE DEBATE** — columns per persona (3 or 4). Each column: icon, POSITION, ARGUMENT,
risks/ops burden, CONFIDENCE badge, CAVEAT in italics.

**TRADEOFF MATRIX** — rows = evaluation dimensions; columns = options; cells = ✓ / ~ / ✗ + note

**DECISION DIAGRAM** — SVG/CSS comparison cards with CHOSEN highlight

**SYNTHESIS** — background `#f0ede8`: VERDICT, REASONING, agreed/decisive/dissent blocks, CONDITIONS

**SIGNED ADR** — monospace card with all ADR fields

**FOOTER** — Architecture Decision Record · generated [timestamp]

---

## Step 6 — Update Decision Registry

Maintain `{output_dir}/index.md` as a chronological registry of all ADRs.

**If index does not exist**, create:

```markdown
# Architecture Decision Records

| ADR | Date | Status | Decision | Verdict |
|-----|------|--------|----------|---------|
```

**After each new ADR**, append a row (do not duplicate if re-running the same file):

```
| [ADR-NNNN: Title](ADR-NNNN-decision-slug.md) | YYYY-MM-DD | Accepted | [options compared] | [one-line verdict] |
```

Sort rows by date descending (newest first). If updating an existing ADR in place,
update its row rather than appending a duplicate.

---

## Step 7 — Output to User

1. List saved file paths (`.md`, `.html` if generated, `index.md` updated)
2. State the verdict in one sentence
3. Name the decisive factor
4. Note the review trigger
5. Mention whether SRE persona participated

---

## Edge Cases

- **More than 2 options**: give all options to every persona
- **Strong user leaning**: tell the Contrarian explicitly; ask them to challenge it
- **Ambiguous decision**: output a decision rule ("use A if X, use B if Y"), not a fake pick
- **Re-run request**: "argue the other side" — re-run debate with swapped priors; write a new ADR or update status to Superseded on the old one
- **Subagents unavailable**: run personas sequentially in isolated turns, or simulate each persona before synthesizing (note lower quality to user)
- **Custom output dir missing**: create it; warn if path is outside the project
- **Re-run same decision**: write a new ADR number; mark the old ADR Status as Superseded with a link to the new one

---

## Invocation Examples

```
"should I use FTS5 or pgvector for legal search"
"ADR: Electron vs web app for our desktop client"
"help me decide between Redis and BullMQ for job queuing"
"debate this: do we build our own auth or use Clerk"
"architecture decision — monorepo vs separate repos"
"include SRE — managed Postgres vs self-hosted"
"ADR only"
"save to skill-outputs/architecture-review"
```
