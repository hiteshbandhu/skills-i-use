# Document Craft — Structure, Tone, Evidence

The layout can be perfect and the document still fail, because a client document is
judged on whether it is *trustworthy* and *actionable*, not whether it is tidy.

---

## The spine that works

Almost every client report is the same three questions:

1. **What we know** — how work actually happens, and how we found out
2. **What is wrong** — what we measured, with numbers
3. **What we propose** — the fix, sequenced, with what each part solves

Everything else is packaging. If a section does not serve one of those three, cut it.

### For a 5-page brief

| Page | Job |
|---|---|
| 1 | The thesis as a headline, four numbers, one decisive diagram |
| 2 | How work happens today, and where it breaks |
| 3 | What we found — findings plus one scannable measurement table |
| 4 | The proposed setup — a diagram and the changes in build order |
| 5 | Their stated problems answered, the build approach, what you need from them |

### For a 15–20 page reference

Add a contents page with one line of description per section, a glossary if the reader is
non-technical, a worked example ("the same job, today versus after"), and a sources
appendix. Keep the 5-page spine underneath it.

---

## Opening

The first page decides whether the rest is read.

- **Lead with the conclusion**, not the methodology. *"Your Zoho isn't broken. It's
  unfinished and disconnected"* beats *"Introduction and scope."*
- **Four numbers, no more.** Each one the punchline of a section.
- **One diagram that makes the argument** before anyone reads a sentence.
- Method, dates and sample sizes go in a footnote on that page — present, not prominent.

---

## Writing for a non-technical reader

- **Define every term of art the first time.** A short glossary near the front (5–6 terms)
  costs a third of a page and removes the barrier.
- **Name things as the reader experiences them.** "The list of stages a deal passes
  through", not "the pipeline layout metadata".
- **Numbers need a consequence.** `12.5% of leads have a phone number` means nothing.
  *"Sales runs on WhatsApp, which needs a number. Seven in eight leads have none."* means
  something. Put the consequence in its own column.
- **Use the reader's units.** Crore and lakh for an Indian company. Their financial year.
  Their currency.
- **Short sentences.** If you need a semicolon, you probably need a full stop.

---

## The evidence rules

**Separate the three kinds of statement.** What people told you, what you concluded, and
what you measured are different epistemic objects. A reader who cannot tell them apart
discounts all three. Give them visually distinct treatment — a sources block, a quote
style, a measurements table.

**State limits explicitly.** Sample sizes, what you could not access, where a match is
probable rather than confirmed. This *increases* credibility: a document with no stated
limits reads as either naive or evasive.

**Verify anything cheaply checkable before asserting it.** If one API call settles whether
their licence tier includes the feature you are proposing, make the call. Getting a
checkable fact wrong costs the reader's trust in everything else.

**Ask whether a finding has a boring explanation.** A striking pattern usually does. One
user account owning thousands of records is almost always an integration authenticating as
that user — not a person doing extraordinary volume. Check the boring explanation first;
publishing the exciting one and being corrected is expensive.

**Attribute to roles and systems, never to named individuals.** *"Records are assigned to a
closed account"* not *"X left without reassigning their leads."* A named person in a client
document turns a systems review into a performance review, and the client's internal
politics will eat the document.

**Do not overstate consensus.** "Six people described the same problem" is a finding.
"Six people proposed the same solution" usually is not — the solution is typically yours.
Say which is which.

---

## Tone

- **Diagnostic, not damning.** *"Unfinished and disconnected"* lands; *"a mess"* makes
  someone defensive and the recommendations get resisted.
- **Credit what exists.** If they half-built the right thing, say so. It is true, it is
  useful, and it makes finishing it feel achievable rather than admitting failure.
- **Reframe rather than contradict.** When their stated problem is not the real one, show
  the measurement and let it reframe. *"You asked for three mandatory fields. There is
  currently one — nothing forces anyone to fill anything in. The obstacle is 70 fields
  on the form."*
- **No hedging where you have evidence.** If you measured it, state it flatly.

---

## Sequencing recommendations

Order by **dependency**, not by impact, and say why:

- What must happen first because everything else depends on it
- What is cheap and proves the approach
- What needs a decision from them
- What is cleanup, explicitly last

State the dependency where it is not obvious. *"Merge duplicates last — do it before the
matching rule exists and they simply regrow."* That one sentence stops a client
reordering the plan into failure.

For each recommendation give four things:
**what it solves · which process it touches · what happens today · what changes**.
The "what happens today" line in a warning colour is what makes the change feel necessary.

---

## Closing

Two things:

1. **What you need from them** — decisions, access, confirmations. Concrete and short.
2. **Pre-answered objections** — the risks they will raise, already checked. *"Your plan
   already includes the sandbox. No new software. No migration."*

If the document asks the reader to confirm your understanding, put those questions
**early** (in the "what we know" section) and repeat them in the close. Everything
downstream depends on them, and framing it as *"correct us"* rather than *"we conclude"*
makes it far more likely they engage.

---

## Final checks

- [ ] Every number traceable to a source, and sources stated
- [ ] Limits and sample sizes stated somewhere
- [ ] No individual named as a problem
- [ ] Jargon defined at first use
- [ ] Each recommendation says what it solves and what happens today
- [ ] Sequencing explained where it is not obvious
- [ ] The ask is explicit and near the end
- [ ] Objections pre-answered with evidence
- [ ] Readable printed in greyscale
