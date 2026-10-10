# Reconciliation — the claims ledger

Phase 3. One agent (Fable), after all breakdowns land and before any synthesis agent starts.
Output: `synthesis/claims-ledger.md`. Every Phase 4-5 agent receives it and must respect its
"corrections" list. In run 1 this step was ad hoc (a reconciliation log bolted onto
learning-design.md after the fact) and caught ten factual errors; promote it to a gate.

---

## (a) File template (`synthesis/claims-ledger.md`)

```markdown
# Claims ledger — {{SUBJECT}}

Built from every file in `books/`. Where two book files disagree, this ledger records both and
states which reading downstream files must use. Tags per SPEC.

## 1. Contradictions between sources
| # | Claim | Source A says (slug) | Source B says (slug) | Resolution for this course | Tag |
|---|-------|----------------------|----------------------|----------------------------|-----|
| X1 | ... | ... | ... | "conditional: IF ... THEN A, else B" / "A is better supported" / "open" | E/H/V |
(Aim for 8-15 rows. Each row should feed a tension in tensions.md; note the likely tNN.)

## 2. Corrections: where evidence overturned a popular claim
| # | Popular claim (where it appears) | What the evidence shows | Source(s) | Downstream rule |
|---|----------------------------------|-------------------------|-----------|-----------------|
| C1 | ... | ... | slug(s) | "Do not state X as [E]; say Y with caveat Z" |
(Pull from every "Evidence strength & limits" and "Common misreadings" section. Include:
replication failures, effect sizes that shrank, mechanism-vs-parameter conflations, claims the
author argues but does not show.)

## 3. Shared glossary
| Term | Definition (one sentence, own words) | Canonical source | Also used by | Note on divergent usage |
(20-40 terms. Where sources use the same word differently, say which meaning the course uses.)

## 4. Key numbers and effect sizes
| Quantity | Value | Unit / metric | Source (study, year) | Slug | Status | Caveat |
|----------|-------|---------------|----------------------|------|--------|--------|
| ... | g ≈ 0.36 | Hedges g on concepts+transfer | Sinha & Kapur 2021 meta-analysis | 04 | verified / background | proponent-run studies; upper estimate |
(Every number any downstream file may cite lives here. If it is not here, it may not be quoted
as a number; say "small"/"moderate" instead.)

## 5. Corrections downstream agents must respect
Numbered, imperative, one line each. Examples of the form:
1. Do not describe {{finding}} as general; the effect is {{scope}} (C3).
2. Quote {{figure}} as "about N", from {{study}}, with the caveat "{{...}}" (row 4.7).
3. Treat {{tension}} as conditional, not as a winner; the rule is in X4.
4. {{Term}} means {{definition}} in this course; do not use {{other sense}}.
5. {{Claim}} is [H] in this course, never [E]; the only evidence is {{...}}.

## 6. Open questions the sources cannot settle
(bullets; these become [O]/[H] items and gaps-primer candidates)

## 7. Verification summary
| Slug | TOC status | Least-certain claims (from the agent hand-back) |
(copied from each breakdown; the README names the least-certain items across the course)
```

---

## (b) Agent prompt — Phase 3

```
Read {{REPO}}/SPEC.md, then every file in {{REPO}}/books/ in full. Write
{{REPO}}/synthesis/claims-ledger.md following references/reconciliation.md exactly.

Method:
- For each book file, extract: every claim in "Evidence strength & limits", every item in
  "Common misreadings", every number with a study attached, every "Connections" line that names
  a disagreement, and every term in "Mental models & vocabulary".
- Section 1: pair up disagreements across files. State each pole in one line with its slug.
  Resolve as conditional where the evidence supports conditions; otherwise say which reading is
  better supported, or mark open. Note the likely tension id (t01..) for each.
- Section 2: list every place a popular or headline claim is stronger than the evidence. The
  test: would a learner who only read the book's blurb state it as settled? Then it belongs here.
- Section 3: glossary. One definition per term; flag divergent usage between sources.
- Section 4: every number. Mark "verified" only if a book file says it was search-verified;
  otherwise "background". Add the caveat from the book file.
- Section 5: rewrite sections 1-4 as imperative rules. This is the list synthesis agents will be
  handed; make each line self-contained.
- Do not add claims not present in the book files. Do not resolve a contradiction by preference;
  cite the evidence line from the book file that decides it, or mark it open.
- Report back: row counts per section, the five corrections you consider most likely to be
  violated by a synthesis writer, and any book file whose evidence section was too thin to use.
```

---

## (c) Quality bar

- [ ] Every book file is cited at least once in sections 1-4.
- [ ] Every contradiction row has both slugs and a resolution or an explicit "open".
- [ ] Corrections section includes every "Common misreadings" item that a synthesis agent could
      plausibly repeat as fact.
- [ ] Every number that later files quote appears in section 4 with status and caveat.
- [ ] Section 5 rules are imperative, one line, self-contained, numbered (agents cite "ledger #7").
- [ ] Glossary resolves every term two sources use differently.
- [ ] No new claims introduced; no contradiction resolved without a cited evidence line.
- [ ] Committed and pushed before Phase 4 launches; the orchestrator pastes section 5 into every
      Phase 4-5 prompt.
