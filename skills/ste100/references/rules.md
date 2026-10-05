# ASD-STE100 Issue 9 — all writing rules

Paraphrased summary of Part 1 of ASD-STE100 Issue 9 (2025-01-15). 53 rules in 9
sections, plus 8 general recommendations. Rule numbers match the spec so you can
look them up. Examples are software examples written for this skill, not quotes
from the spec. Read the spec for the full text: https://www.asd-ste100.org

---

## Section 1 — Words

| Rule | Rule (short form) |
|---|---|
| 1.1 | Use only: (a) approved dictionary words, (b) technical nouns, (c) technical verbs. |
| 1.2 | Use an approved word only as its listed part of speech. "TEST" is approved as a noun, so "Do a test of the endpoint", not "Test the endpoint" — unless your field makes *test* a technical verb. |
| 1.3 | Use an approved word only with its approved meaning. Each word has one meaning. "FALL" = to move down by gravity, not "to decrease". |
| 1.4 | Use only the listed forms of verbs and adjectives. Comparatives ("-er", "-est") only when listed. |
| 1.5 | A technical noun is permitted when it fits one of 22 categories (below). |
| 1.6 | A word that is not in the dictionary is permitted only when it is a technical noun or part of one. |
| 1.7 | Do not use technical nouns as verbs. "Cache the token" → "Keep the token in the cache". |
| 1.8 | Use the technical nouns approved by your company, industry or field. |
| 1.9 | When you choose a technical noun, choose the short, easy one. |
| 1.10 | No regional words, slang or jargon as technical nouns. "Spin up" / "nuke" / "the prod box" are not permitted. |
| 1.11 | One item = one technical noun. Do not use "server", "host", "node", "box" for the same thing. |
| 1.12 | A technical verb is permitted when it fits one of 4 categories (below). |
| 1.13 | Do not use technical verbs as nouns. "Do the install" → "Install the package". |
| 1.14 | American English spelling, unless your directives say different. |

**The 22 technical-noun categories (rule 1.5):**
1 official parts information · 2 vehicles/machines and locations on them · 3 tools and support equipment · 4 materials, consumables, unwanted material · 5 facilities, infrastructure, logistics · 6 systems, components, circuits, functions, configurations · 7 mathematical, scientific, engineering terms and formulas · 8 navigation and geography · 9 numbers, units, time · 10 quoted text · 11 roles, people, groups, organizations, geopolitical entities · 12 body parts · 13 personal effects, food, drink · 14 medical terms · 15 documents, standards, guidelines · 16 environmental and operational conditions · 17 colors · 18 damage terms · 19 **computer science and ICT** · 20 civil and military operations · 21 law and regulations · 22 animals, plants, life forms.

**The 4 technical-verb categories (rule 1.12):**
1. Manufacturing processes (remove, add, attach material; change properties, finish, shape — for example drill, grind, solder).
2. **Computer processes and applications** — the spec lists, for example: input/output (*click, enter, press, print, swipe, tap, type*); UI and application (*clear, close, copy, delete, disable, drag and drop, enable, encrypt, filter, navigate, open, paste, save, scroll, sort, validate, zoom in*); system operations (*abort, boot, debug, download, format, install, load, process, reboot, update, upgrade, upload*).
3. Subject-field verbs (engineering, medical, civil/military, navigation, automotive/rail, energy).
4. Law and regulations.

For software text this means: *deploy, commit, merge, compile, query, cache* can be technical verbs if your team uses them as defined terms. Write them in your term list once and use them the same way each time.

---

## Section 2 — Multi-word nouns

| Rule | Rule |
|---|---|
| 2.1 | A multi-word noun (noun cluster) has max 3 words. |
| 2.2 | When a technical noun has more than 3 words, write it in full once. Then use a short form, or use hyphens to show which words go together. |

Break a long cluster with prepositions: "user session token refresh endpoint" → "the endpoint that refreshes the session token of the user". Or define it once: "the token-refresh endpoint (TRE)".

---

## Section 3 — Verbs

| Rule | Rule |
|---|---|
| 3.1 | Use only the verb forms in the dictionary. |
| 3.2 | Permitted forms: infinitive, imperative (command), simple present, simple past, simple future, past participle as an adjective. |
| 3.3 | Use the past participle only as an adjective: "the *connected* client", "the file is *deleted*" (state). |
| 3.4 | No complex constructions with auxiliaries: no perfect tenses ("has failed" → "failed"), no "is to be", "must be adjusted", "can be configured". Name who does it: "You can configure the limit." |
| 3.5 | The "-ing" form only as part of a technical noun ("load balancing", "logging level"). Not "When restarting, …" → "When you restart the service, …". |
| 3.6 | Active voice. In descriptions, passive is permitted only when the agent is unknown. Procedures: always active. |
| 3.7 | Use a verb for an action, not a noun. "Do a restart of" / "perform validation" → "restart" / "validate". |

---

## Section 4 — Sentences

| Rule | Rule |
|---|---|
| 4.1 | Short, clear sentences. In procedures, speak to the reader with commands. |
| 4.2 | Do not omit words or use contractions to make a sentence shorter. Keep articles, "that", "you". Not "Check config, restart" → "Examine the configuration file. Then restart the service." |
| 4.3 | Use a vertical list for complex text (many conditions, items or steps). |
| 4.4 | Connect related sentences with connecting words: *then, but, also, thus, if, when, after, before, because, as a result, for example*. |
| 4.5 | Use an article (*the, a, an*) or a demonstrative (*this, these*) before a noun when applicable. |

Vertical list pattern: lead-in sentence that ends with a colon, then items in the same grammatical form.

---

## Section 5 — Procedural writing

| Rule | Rule |
|---|---|
| 5.1 | Max **20 words** in each sentence (also warnings and cautions). |
| 5.2 | One instruction per sentence, unless two actions occur at the same time ("Hold the key and press Enter"). |
| 5.3 | Instructions use the imperative (command) form. |
| 5.4 | If the reader must know a condition first, start with it, then a comma, then the command: "If the build fails, examine the log." |
| 5.5 | Notes give information only. Never put a command in a note. |

---

## Section 6 — Descriptive writing

| Rule | Rule |
|---|---|
| 6.1 | Give information gradually. One subject per sentence. Known → new. |
| 6.2 | Use key words and key phrases (headings, topic sentences, consistent labels) to give the text a logical structure. |
| 6.3 | Max **25 words** in each sentence. |
| 6.4 | Use paragraphs to group related information. |
| 6.5 | One topic in each paragraph. |
| 6.6 | Max **6 sentences** in each paragraph. |

Descriptive text gives information, not instructions, so no imperative verbs in it. Notes are descriptive text.

---

## Section 7 — Safety instructions

Definitions: a **WARNING** = risk of injury or death. A **CAUTION** = risk of damage to objects (for software: data loss, outage, corrupted state). Other domains can use *DANGER / NOTICE* (ANSI Z535, ISO 3864), but the content still obeys 7.1–7.3.

| Rule | Rule |
|---|---|
| 7.1 | Use a signal word that shows the level of risk. |
| 7.2 | Start with a clear command or condition. |
| 7.3 | Then give the risk or the possible result. |

Pattern (the spec shows safety text in capitals):

```
CAUTION: DO NOT RUN THE MIGRATION ON THE PRIMARY DATABASE DURING PEAK HOURS.
THE TABLE LOCK CAN STOP ALL WRITES FOR MANY MINUTES.
```

Put the safety instruction immediately **before** the step it applies to. Not after.

---

## Section 8 — Punctuation and word count

| Rule | Rule |
|---|---|
| 8.1 | All standard punctuation is permitted, except the semicolon. |
| 8.2 | Use hyphens to join words that are directly related ("pre-flight check", "read-only replica"). |
| 8.3 | Parentheses are permitted for: references to illustrations or text; item numbers on an illustration; work step identifiers; abbreviations; singular/plural ("the server(s)"); short explanations; alternatives. |
| 8.4 | In a vertical list, a colon ends a sentence for word count. |
| 8.5 | Text in parentheses counts as one word. |
| 8.6 | Each of these counts as one word: numbers, number + unit, abbreviations, alphanumeric identifiers, quoted text, titles/headings/labels, proper nouns. |
| 8.7 | A hyphenated word counts as one word. |

So `Set "max_connections" to 200 in postgresql.conf (the main configuration file).` = 7 words.

---

## Section 9 — Writing practices

| Rule | Rule |
|---|---|
| 9.1 | When a word-for-word swap does not work, rewrite the sentence with a different structure. |
| 9.2 | Use each approved word correctly (meaning, part of speech, context). |
| 9.3 | No phrasal verbs, even when both words are approved. *set up → configure / install; carry out → do; find out → find; turn on → start / energize; shut down → stop; back up → make a copy; roll back → return to the previous version; give off → release*. |
| 9.4 | Use a consistent style: the same term, the same sentence pattern, the same format for the same type of information. |

### General recommendations (GR)

- **GR-1 "that"** — Do not drop "that" after *make sure, show, recommend, tell*. "Make sure *that* the port is open."
- **GR-2 "with"** — "with" can mean *has*, *together with*, or *by means of*. If the sentence can be read two ways, rewrite it.
- **GR-3 Pronouns** — If "it/they/them" can refer to two nouns, repeat the noun.
- **GR-4 "this"** — Make sure that the reader knows what "this" refers to. Prefer "this error", "this step".
- **GR-5 False friends** — Non-native writers: check that the English word has the meaning you intend.
- **GR-6 Latin abbreviations** — Do not use *e.g., i.e., etc., vs., via*. Write *for example, that is, and other, compared to, through*.
- **GR-7 Inclusive language** — Gender-neutral only. No *he/she*. Use *you*, *the user*, *the operator*.
- **GR-8 Possessive** — Permitted, but if you are not sure, use "of": "the configuration of the server".

---

## Quick self-check before you send

- [ ] Each sentence ≤ 20 words (steps) / ≤ 25 words (description)?
- [ ] Each step = one command?
- [ ] Active voice? No "has been", "can be done", "is to be"?
- [ ] No phrasal verbs, contractions, semicolons, Latin abbreviations?
- [ ] Noun clusters ≤ 3 words?
- [ ] One name for each thing, the same in text and diagram?
- [ ] Warnings and cautions before the step, command first, then risk?
- [ ] Notes contain no commands?
- [ ] Paragraphs: one topic, ≤ 6 sentences?
