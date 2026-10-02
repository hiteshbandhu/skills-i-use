---
name: research-report
description: >
  Deep research on a new technology paradigm or trend — what it is, how it is built, its
  philosophy — plus the providers that sell it and the places it fits in your own codebase,
  delivered as a clean, visual, team-shareable PDF report. Runs parallel researchers (via a
  deep-research skill when one is installed), a codebase pass, a report writer, then renders
  with the pdf-report skill. Triggers on "do a deep research into X and make me a PDF",
  "research this paradigm, the providers and where we can use it", "what is this new trend
  and should we adopt it", "write the team a report on X".
---

# Research Report — paradigm → providers → your opportunities → visual PDF

Arguments: the topic, plus any products, companies or providers the user named
(e.g. `always-on sandboxes; products: Grok Bot, ChatGPT dots; providers: DigitalOcean, Daytona`).

Output: `{SKILL_OUTPUT_DIR}/research-report/{slug}/` — `notes/`, `{slug}.md`, `{slug}.html`, `{slug}.pdf`.

## The brief

> There is a new paradigm we are seeing: **{topic}**, introduced or popularised by
> **{named products/companies}**. Research it very deeply: how these systems are built, how
> they work, and what their philosophy is.
>
> Cover **which providers actually offer it** to companies and startups like us (start from
> {providers}) and which are best for us.
>
> Then **read our codebase**, understand the product, and name the places and opportunities
> where we should use it to get ahead.
>
> Finally make a **very clean PDF with visuals**: every number or statistic that can be
> visualised is visualised; what reads best as text stays text. Sections like a report the
> team can read and share.

**Never add duplication.** Nothing appears twice — no heading, section title, chart, table,
caption, callout or point is repeated if it is already in the report. Before rendering, scan
for repeated headings, the same caveat sentence above and below a chart, and tables that
restate a chart without adding columns; keep one.

## Process

1. **Research in parallel.** If a deep-research skill is installed (e.g. Anthropic's
   `deep-research`), invoke it and act as its coordinator; otherwise spawn subagents
   directly, or run the five passes in sequence. Five researchers:
   - **Products & philosophy** — verify exact names, companies, launch dates, prices. Users
     often dictate names wrong; find the real ones and record them for a "name check"
     callout. Include precursors and peers, dated.
   - **Architecture** — how it is built, with numbers (latencies, limits, costs), the
     security model, published reference architectures.
   - **Providers A** and **Providers B** — split the list. Per provider: offer, limits,
     pricing with a worked monthly cost for one reference unit, region/residency and
     compliance, SDK fit for your stack, maturity. A comparison table ready for charts.
   - **Your codebase** — read-only: what exists today (file paths), pain points the paradigm
     solves, ranked opportunities with value / effort / risk, exact numbers from code. Never
     modify the repo, stash, or touch production.

   Give every researcher today's date, the current-state constraint, and the instruction to
   **write its notes file incrementally** so an interrupted session loses nothing.
2. **Write the report.** Executive summary; then three sections — the paradigm, architecture
   and providers (ending in a recommendation for you), opportunities in your product (with
   risks and a phased roadmap); appendix of caveats and sources. Every chartable number goes
   in a clean markdown table. Claims sourced; estimates and vendor claims labelled. Plain
   language.
3. **Render the PDF with the [`pdf-report`](../pdf-report/) skill** — it owns the HTML →
   headless Chrome pipeline, print CSS and inline SVG. Every chart uses numbers from the
   report's tables, never invented ones. Charts worth having for this kind of report:
   - launch timeline of the products and peers
   - cost per provider (grouped bars: always-running vs typical usage)
   - limits / timeouts per provider; latency on a log scale, vendor claim vs your measurement
   - provider fit matrix with rating chips
   - an architecture diagram and a lifecycle/state diagram
   - opportunity value-vs-effort scatter; a gantt roadmap

   Axis units and a source / "estimate" footnote under every chart. A cover, a contents page
   with page numbers, and an executive summary with 3–5 stat callouts.
4. **Verify by looking**, then fix. See [verify.md](verify.md) for the page-by-page check
   and the traps specific to long, chart-heavy reports.
5. **Deliver** the PDF with a short summary: page count, what each section shows, and which
   numbers are estimates or unverified. Never delete user files; temp files go to a scratch
   directory.
