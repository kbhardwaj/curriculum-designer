# Gaps primer — what the reading list omits that the goal needs

Phase 4, parallel agent. Output: `synthesis/gaps-primer.md`. A reading list is a knowledge
curriculum, not a {{GOAL}} curriculum; this file briefs the learner on what is missing so they
can ask experts the right questions. 8-12 sections, ~8,000-9,000 words. Seeds come from
learning-design.md section 6.

---

## (a) File structure

```markdown
# {{Role}} gaps primer: what the {{N}} sources do not teach you
Intro: companion to learning-design §6; does not replace expert help; lets you ask the {{expert
roles}} the right questions and spot weak answers.
**How to use it.** Read "Why it matters" + numbered points for every section (~40 min); treat
"Read next" as a queue; which sections to do first and when.
**Tags:** course tags plus **[Jurisdictional]** / **[Context-dependent]** (depends on law,
market, institution where you operate; written from {{default vantage}} unless stated).
**Verification note.** "verified" = confirmed by web search (title, authors, venue, headline
result) on {{date}}; full texts not read if fetching was blocked; "background" = not re-checked,
a lead to confirm, not a fact to quote.

## N. <Gap area>
**Why it matters.** 1-2 sentences; ideally the failure mode this gap causes.
**Things to know.** 6-10 numbered points, each bolded lead + 2-4 sentences, each tagged, with
numbers marked verified/background and "illustrative arithmetic only" where invented.
**Questions to ask your {{expert}}.** 3-5.
**Read next.** 2-4 named resources with one-line why; verification status.
**How it connects to the course.** Which module/tension/law it touches.

## Cross-cutting: the ten questions a {{role}} should be able to answer cold
Numbered; each answerable with a number and a named source, or "reread section N".

## Verification log
How inline markers were assigned; anything searched for and not found.
```

---

## (b) Choosing the gaps

- Start from learning-design §6 and the ledger's "open questions". Add areas by asking: what
  will sink the learner's {{project}} before weak {{domain knowledge}} does? (money, law,
  people, operations, measurement, the adjacent technical field, the newest technology.)
- Label each Critical (fails without it, sources silent) / Important / Useful. Do Critical first.
- Each area is a 1-3 hour addition, never a full book; say honestly "this is management/legal/
  technical knowledge, not {{SUBJECT}}; nothing in the sources helps."

---

## (c) Agent prompt

```
Read SPEC.md, synthesis/learning-design.md section 6 (seed list), synthesis/claims-ledger.md
section 6 (open questions), and the "Implications" sections of books/*.md. Write
synthesis/gaps-primer.md per references/gaps-primer.md (a).
- 8-12 gap areas, each labeled Critical/Important/Useful, ordered Critical first.
- Each area: why it matters (the failure mode), 6-10 tagged points, questions for the expert,
  read-next with verification status, connection to the course.
- Use WebSearch to verify named studies and resources; WebFetch may be blocked — rely on
  snippets and mark "verified" vs "background" inline on every number and citation. Never present
  a background figure as a fact; say "about", or make the arithmetic explicitly illustrative.
- Add the [Jurisdictional]/[Context-dependent] tag and state the default vantage point.
- Ten cold questions at the end; verification log.
- Do not restate what the sources already cover; if a point is in a book file, link to it instead.
- Report back: area list with labels, count of verified vs background citations, and anything
  you searched for and could not find.
```

---

## (d) Quality bar

- [ ] 8-12 areas, labeled and ordered; each names the failure mode it prevents.
- [ ] Every number and citation marked verified/background; illustrative arithmetic labeled.
- [ ] Every point tagged; jurisdiction/context tag used where law or market decides.
- [ ] Each area has expert questions, read-next and a course connection.
- [ ] Ten cold questions; verification log; nothing duplicated from book files.
