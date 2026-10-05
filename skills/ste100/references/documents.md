# Document types, intent, and trajectory

STE controls the sentences. This file controls the document: which type it is,
what order the sections go in, and how strict the STE is. Read it before you
write any document longer than one screen: a report, paper, memo, PRD, design
doc, postmortem, guide, or a PDF of any of these.

## Step 1: Find the intent

Before you write, answer these four questions. Write the answers in one line
each, for yourself. Do not put them in the document.

1. **Reader.** Who reads it? What do they know already?
2. **Action.** What must the reader do, decide, or know after they read it?
3. **Type.** Which document type below matches that action?
4. **Trajectory.** What is the reader's path from the first page to the action?

If the request names a type ("write a PRD"), use that type. If it does not, use
the signals below. If two types match, pick the one whose **action** matches.

| Signals in the request | Reader's action | Type |
|---|---|---|
| "should we", "decide", "approve", "recommend" | Decide | Decision memo / proposal |
| "FYI", "update", "status", "this week" | Know the state | Status report / update memo |
| "what happened", "outage", "incident" | Learn, prevent again | Postmortem |
| "build", "feature", "requirements", "spec for product" | Agree on what to build | PRD |
| "how should we build", "architecture", "RFC" | Agree on how to build | Design doc / RFC |
| "we chose", "record the decision" | Remember why | ADR |
| "how do I", "steps", "runbook", "on-call" | Do a task | Procedure / runbook |
| "explain", "teach", "onboard", "README" | Understand and use | Guide / explainer |
| "research", "compare vendors", "landscape" | Choose from options | Research or evaluation report |
| "paper", "study", "experiment", "results" | Trust a finding | Research paper / technical report |
| "one-pager", "for the CEO", "brief" | Decide fast | Executive brief |
| "release notes", "changelog", "what's new" | Know what changed | Release notes |

## Step 2: Follow the trajectory

The **trajectory** is the order in which the reader needs the information to
get to the action. Each section moves the reader one step. If a section does
not move the reader toward the action, remove it or put it in an appendix.

Three rules for every type:
- **The answer comes first** (BLUF: "bottom line up front", from US Army
  correspondence practice, AR 25-50). The first paragraph gives the conclusion,
  the decision needed, or the result. The reader can stop after it.
- **Known → new.** Start each section from what the reader knows (STE rule 6.1).
- **Detail goes down, not up.** Summary → main body → appendix. Evidence
  supports a claim that the reader already saw.

The intent can change the trajectory inside one type. A memo that asks for a
decision ends with the options and the ask. A memo that informs ends with the
next steps and owners.

## Step 3: Use the type's shape

Each type below has: the trajectory (the section order), the STE level, and the
diagrams that help most. Section names are defaults. Rename them to fit the
topic, but keep the order.

### Decision memo / proposal
- **Trajectory:** Decision needed (1–2 sentences, with the deadline) → Recommendation → Why (3 reasons max) → Options compared (table) → Cost and risk → What happens next if approved.
- **STE level:** standard. **Length:** 1–2 pages.
- **Diagrams:** an options table. A simple before/after diagram if the change is structural.

### Status report / update memo
- **Trajectory:** Overall state in one line (on track / at risk / blocked) → What changed since the last report → Risks and blockers, with an owner for each → Next steps with dates.
- **STE level:** standard. Use status colors from IEC 60073 (red / amber / green) together with a text label.
- **Diagrams:** a timeline or a milestone table.

### Postmortem (incident report)
- **Trajectory:** Summary (what broke, for how long, the impact in numbers) → Timeline (UTC, ISO 8601 time stamps) → Root cause → Contributing factors → What went well → Action items (owner, due date, ticket).
- **STE level:** standard. Write the timeline in the simple past tense. Blameless: name systems and roles, not people (STE GR-7 also asks for neutral language).
- **Diagrams:** the failure path on the architecture diagram (IEC 61082 flow left→right), and a timeline.

### PRD (product requirements document)
- **Trajectory:** Problem (who has it, the evidence) → Users and their goals → Goals and non-goals → Requirements (numbered, each one testable, with priority) → User flows → Success metrics → Scope and release plan → Open questions.
- **STE level:** standard. Requirements use "must" for a requirement and "can" for an option. Number each requirement (R1, R2…) so that tickets and tests can refer to it. Make each requirement one sentence that a tester can check.
- **Diagrams:** user flow (ISO 5807 flowchart or BPMN swimlanes), a scope table (in / out).

### Design doc / RFC
- **Trajectory:** Summary (what we will build, in 3 sentences) → Context and problem → Goals and non-goals → Proposed design → Alternatives considered (and why not) → Risks, security, cost → Rollout and rollback plan → Open questions.
- **STE level:** standard for the body, light for the discussion of alternatives.
- **Diagrams:** C4 context and container diagrams, a sequence diagram for the main path, a state chart for lifecycles (GRAFCET style). Callout numbers that the text refers to.

### ADR (architecture decision record)
- **Trajectory:** Title (the decision as a statement) → Status → Context → Decision → Consequences (good and bad). (Format from Michael Nygard, 2011.)
- **STE level:** standard. **Length:** less than 1 page.

### Procedure / runbook / SOP
- **Trajectory:** Purpose (one sentence) → When to use it → Before you start (access, tools, conditions) → Steps → How to make sure that it worked → Rollback → Who to contact.
- **STE level:** **strict.** Run the checker with `--mode procedure`. Safety instructions before the step (STE section 7).
- **Standard:** IEC/IEEE 82079-1 (information for use): give the reader the safety information, the conditions, and the result of each task. Put each task in its own section.
- **Diagrams:** a flowchart for decision points. Callout illustrations for screens or hardware (S1000D practice).

### Guide / explainer / README
- **Trajectory:** What it is and why it matters (one paragraph) → Quick start (shortest path to a result) → Concepts (one per section, known → new) → Tasks → Reference → Troubleshooting.
- **STE level:** standard. Concepts are descriptive writing (25 words max). Tasks are procedural writing (20 words max).
- **Standard:** ISO/IEC/IEEE 26514 (user documentation) separates concept, task, and reference information. Do not mix them in one section.
- **Diagrams:** one overview diagram near the top (IDEF0 A-0 or C4 context), then one diagram for each hard concept.

### Research or evaluation report
- **Trajectory:** Executive summary (the answer, with 3–5 key numbers) → Question and method → Findings (one section per finding) → Comparison of options → Recommendation for us → Risks and unknowns → Sources.
- **STE level:** standard. Mark each estimate as an estimate. Mark each vendor claim as a vendor claim.
- **Diagrams:** comparison tables and charts. A fit matrix. For the full visual PDF workflow, use the `research-report` skill together with this skill.

### Research paper / technical report
- **Trajectory (IMRaD):** Abstract (problem, method, main result, meaning) → Introduction (gap, contribution) → Method → Results → Discussion (meaning, limits) → Conclusion → References.
- **Standard:** ANSI/NISO Z39.18 (scientific and technical reports) for the report parts and their order.
- **STE level:** light to standard. Papers need hedges. STE gives you "can", "possibly", and "approximately". Use these, not "might", "arguably", "it seems". Citations, titles, and quoted text count as one word (rule 8.6).
- **Diagrams:** a method diagram (IDEF0 is good for pipelines), result charts with units and error bars.

### Executive brief / one-pager
- **Trajectory:** The ask or the conclusion → 3 supporting points, each with a number → Risk → Next step.
- **STE level:** standard. **Length:** 1 page. No section has more than 3 sentences.
- **Diagrams:** one, or none. A single chart that proves the main point.

### Release notes
- **Trajectory:** Most important change first → New → Changed → Fixed → Removed or deprecated → Action that the user must do (if any).
- **STE level:** standard. Each item: one sentence, starts with the user-visible result.

## Step 4: Make it a PDF or a printed report

Use these rules when the output is a PDF, a printed report, or any page-based document.

**Structure**
- Cover or title block: title, date (ISO 8601: 2026-10-05), author, version, status (draft / final).
- Contents with page numbers when the document has more than 6 pages.
- Running header or footer with the title and page number ("Page 3 of 12").
- Each figure and table has a number and a caption: "Figure 2: Request path through the gateway". The text refers to the figure before the figure appears.
- Appendices for the detail that does not move the reader toward the action.

**Layout**
- One column for most reports. Body text 10–11 pt. Line length 60–80 characters.
- Do not break a figure, a table row, a callout, or a warning across two pages (CSS `break-inside: avoid`).
- Do not leave a heading alone at the bottom of a page (`break-after: avoid` on headings).
- Safety and caution boxes come before the step on the same page.
- Units: SI units with a space ("20 ms", "4 GB"), ISO 80000. Same number format everywhere.

**Rendering**
- Write the document in Markdown or HTML first. Then render HTML with print CSS to PDF with headless Chrome (`--print-to-pdf`), or use the `anthropic-skills:pdf` skill.
- For a long visual research PDF, use the `research-report` skill's build kit.
- After rendering, look at every page (`pdftoppm -r 50` to PNG, then read the images). Fix clipped text, orphan headings, and broken tables before delivery.

**STE check**
- Run `ste_check.py` on the body text only. Code, quoted text, citations, and tables are not checked.
- Use `--mode procedure` for step sections and `--mode descriptive` for the rest.

## Step 5: Final check for the document

- [ ] Can the reader do the action after the first paragraph alone?
- [ ] Does each section move the reader one step along the trajectory?
- [ ] Is each term the same in the text, the diagrams, and the tables?
- [ ] Does each figure and table have a number and a caption, and does the text refer to it?
- [ ] Is each number sourced, or marked as an estimate?
- [ ] Does each action item have an owner and a date?
