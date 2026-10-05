---
name: ste100
description: Write explanations, documents and diagrams in ASD-STE100 Simplified Technical English (the aerospace controlled language, Issue 9, 2025), shaped to the document type and the reader's intent, and draw diagrams to engineering standards (IDEF0, ISO 5807, IEC 61082, S1000D-style callouts) in Hairline or Blueprint-minimalism style. Covers reports, PDFs, research papers, technical reports, internal memos, decision memos, status updates, PRDs, design docs/RFCs, ADRs, postmortems, runbooks/SOPs, guides/READMEs, executive briefs and release notes. Use when the user says "STE", "ASD-STE100", "simplified technical English", "80% STE", "plain technical English", "explain it like a maintenance manual", asks for a clearer or more readable explanation, or asks for any of those documents or a technical diagram that must be easy to follow — also together with the pdf or research-report skills when they produce the final file.
---

# ASD-STE100 Simplified Technical English

STE is a controlled language from aerospace maintenance. It has 53 writing rules
and a dictionary of approved words. Each approved word has one meaning and one
part of speech. The result is text that a tired, non-native reader can follow
with no misunderstanding.

Source: ASD-STE100 Issue 9 (2025-01-15), free from
https://www.asd-ste100.org. The full rules with examples are in
[references/rules.md](references/rules.md). Document types, intent and
structure are in [references/documents.md](references/documents.md). Diagram
standards are in [references/diagrams.md](references/diagrams.md). Visual
styles (Hairline and Blueprint minimalism) are in
[references/styles.md](references/styles.md).

## Pick a level

The full spec is strict. Pick the level from the request. When the request does
not say, use **standard**.

| Level | When | What applies |
|---|---|---|
| **strict** | "pure STE", safety text, text for translation | All rules. Only dictionary words plus technical nouns and verbs. Run the checker. |
| **standard** ("80% STE") | Default. Explanations, runbooks, docs | All sentence, verb, procedure and structure rules. Prefer approved words, but use a normal word when the approved swap makes the text worse. |
| **light** | Chat answers, quick notes | Short sentences, active voice, one idea per sentence, commands for steps, no idioms. |

## The core rules (memorize these)

These rules give most of the value. They apply at every level.

1. **One idea in each sentence.** Procedures: max **20 words**. Descriptions: max **25 words**.
2. **One instruction in each step.** Two actions go in one step only when they occur at the same time.
3. **Steps use the command form.** "Restart the worker." Not "The worker should be restarted."
4. **Active voice.** Say who does the action: "The scheduler sends the job." Passive only in descriptions, and only when the agent is unknown.
5. **Simple tenses only.** Present, past, future, and commands. No "has been", "is being", "would have".
6. **A verb for the action, not a noun.** "Examine the logs." Not "Perform an examination of the logs."
7. **One word, one meaning. One thing, one name.** If you call it a "job", do not call it a "task" later.
8. **No phrasal verbs.** "set up" → "configure", "find out" → "find", "carry out" → "do".
9. **No contractions, no semicolons, no Latin** ("e.g." → "for example", "i.e." → "that is", "etc." → "and other").
10. **Do not drop small words.** Keep articles and "that": "Make sure that the port is open."
11. **Max 3 words in a noun cluster.** "Cache invalidation retry policy timeout" → "the timeout of the retry policy for cache invalidation".
12. **Paragraphs: one topic, max 6 sentences.** Give information gradually. Put the key point first.
13. **Lists for complex text.** When a sentence has three or more parallel items or steps, use a vertical list.
14. **Notes give information, not commands.** A command never hides in a note.
15. **Warnings first.** A WARNING (risk to people) or CAUTION (risk to equipment or data) comes *before* the step. It starts with a command or condition, then gives the risk.

## Words

- Approved words have one meaning only. Example: "fall" means "move down by gravity", not "decrease". "Close" is a verb, not "near".
- **Technical nouns and verbs are permitted** when they are terms in your subject field (rules 1.5, 1.12). In software this includes: *database, endpoint, cache, commit, container, deploy, debug, install, reboot, download, upload, encrypt, scroll, click*. Use the term your team uses, and use it consistently.
- Do not use a technical noun as a verb ("to cache the value" → "to keep the value in the cache") unless the verb is also a standard technical verb.
- Use American English spelling.

Common swaps (from the STE dictionary):

| Do not use | Use |
|---|---|
| ensure, verify, check (that) | make sure (that) |
| check (look at) | examine |
| utilize | use |
| perform, accomplish | do |
| require | necessary, must |
| should | must (a rule), or rewrite as a command |
| may | can, possibly |
| about (as "approximately") | approximately |
| prior to / subsequent to | before / after |
| due to | because of |
| acceptable | permitted, satisfactory |
| obtain, acquire | get |
| locate | find |
| indicate | show |
| commence, initiate | start |
| terminate | stop |
| enough | sufficient |
| allow, enable (as "let") | let |
| facilitate | help |
| additional | more |
| via | through |
| whether | if |
| such as | for example |
| simultaneously | at the same time |
| run (a test) | do (or a technical verb your team defines) |
| fail | failure (noun): "a failure occurs" |
| old | expired, used, remaining |

For any other word, check `dictionary/unapproved.txt` (after you build it, see below).

## Workflow

0. **For a document (report, PDF, paper, memo, PRD, design doc, postmortem, guide), read [references/documents.md](references/documents.md) first.** Find the reader, the action they must take, the document type, and the trajectory (the section order that gets the reader to the action). The type also sets the STE level: procedures strict, papers light to standard, most others standard. The answer always comes first.
1. **Find the text type.** Procedure (steps the reader does) or description (how something is or works). Most explanations are description plus a short procedure.
2. **Decide the terms.** Write a short term list first. One name for each thing. Keep it for the full answer.
3. **Draft by the rules.** Description: say what the thing is, then what it does, then how. Procedure: numbered steps, one command each, warnings before the step.
4. **Add a diagram when the text has more than three parts that connect.** Follow [references/diagrams.md](references/diagrams.md) for the structure and [references/styles.md](references/styles.md) for the look (Hairline for one idea, Blueprint for parts and numbers). Draw only when a picture carries more than the text. Text refers to diagram items by number in parentheses, for example "the queue (3)".
5. **Check.** For strict and standard level, run the checker on the draft and fix every error:
   ```bash
   python3 ~/.claude/skills/ste100/scripts/ste_check.py draft.md --mode descriptive --level standard
   ```
   Use `--mode procedure` for step lists. Word flags (`info`) are hints only. A flagged word can be a valid technical noun.
6. **Read it once as the reader.** If a sentence can have two meanings, rewrite it.

## Output shapes

**Explanation of a system** (descriptive):

```
## <Thing>
<Thing> is a <category> that <main function>.        ← one sentence, the key point

### Parts
- <Part A> (1): <function, one sentence>.
- <Part B> (2): <function, one sentence>.

### How it operates
1-6 short paragraphs. Each paragraph has one topic. Use the same names as the parts list.

[diagram with callouts (1), (2) …]
```

**Procedure / runbook:**

```
## <Task as a verb phrase: "Rotate the API keys">
Before you start: <conditions, tools, access>.

CAUTION: DO NOT ROTATE THE KEYS DURING A DEPLOY. THE SERVICE CAN STOP.

1. Open the secrets console.
2. Select the production project.
3. If the key expires in less than 30 days, click "Rotate".
   NOTE: The previous key stays active for 24 hours.
4. Make sure that the health check shows "OK".
```

## Examples

**Non-STE:** "Once the cache has been warmed up, requests should be routed through the edge, which drastically reduces latency; however, stale entries may need to be purged manually."

**STE (standard):** "First, fill the cache. Then send the requests through the edge servers. This decreases the latency by a large quantity. The cache can keep expired entries. Remove these entries manually."

**Non-STE:** "To deploy, you'll want to make sure the tests pass and then tag the release, after which CI will pick it up."

**STE procedure:**
1. Start the test suite.
2. Make sure that no test failure occurs.
3. Tag the release.
   NOTE: The CI system starts the deploy when it finds the new tag.

## Dictionary setup (once)

The STE dictionary is copyrighted by ASD. It is free to download, but this
skill does not include a copy. Build the local word lists from the official PDF:

```bash
python3 ~/.claude/skills/ste100/scripts/build_dictionary.py
```

This downloads Issue 9 and writes `dictionary/approved.txt` (about 730 headwords
with verb forms) and `dictionary/unapproved.txt` (about 1,200 words with their
approved alternatives). Do not redistribute these files. Grep them when you are
not sure about a word:

```bash
grep -i "^ensure " ~/.claude/skills/ste100/dictionary/unapproved.txt
```
