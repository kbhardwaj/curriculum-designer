# Source breakdown — per-source file template + agent prompt

Phase 2 (catabolic). One agent per source, all in parallel, default model. Output:
`books/NN-slug.md`. These files are **authoritative for everything downstream**: every synthesis
agent must cite them by slug and log any departure.

---

## (a) File template (`books/NN-slug.md`)

```markdown
# <Title> — <Author(s)> (<edition/year>)
Level: {{LEVEL_1}} | {{LEVEL_2}} | {{LEVEL_3}}  ·  Priority: Core | Extension | Selections
Est. reading time saved: ~Nh  ·  Your time with this file: ~N min

> Role in the course: one sentence on what this source is the reference *for* and which other
> sources build on or argue with it.

## The book in one sentence
## The book in one paragraph
(author background, structure, arc, stance, what edition changed)

## Why it's in this curriculum (the question to read it with)
(one bolded question the learner should hold while reading; plus one skeptical second question:
where does this source's frame stop applying?)

## Table of contents
State at top: "TOC verified against <source>" | "TOC partially verified" | "TOC reconstructed —
not verified". Parts → chapters, as a table: # | chapter title | anchoring study/model | status
(v = verbatim in a search snippet; bk = background knowledge, with confidence). Never invent
chapter titles silently. For Selections sources: full TOC, then mark which chapters this file
covers and why.

## Chapter-by-chapter: the salient knowledge
### Part / Ch N — <title>
- Core claim(s) — 2-5 bullets, own words
- Key study / model / example (researchers + year when known; for formal sources, state the
  setup and result in plain words, with one small worked example where it helps)
- So-what for {{someone pursuing GOAL}}
(Group minor chapters; spend words where the ideas are load-bearing.)

## The 5-10 ideas you must carry out of this book
(numbered, each 1-3 sentences, ranked by importance)

## Mental models & vocabulary
(term — crisp definition — where it bites in practice)

## Evidence strength & limits
- Robust (replicated, meta-analytic)
- Solid but with inflated headline numbers
- Contested
- Arguing vs. showing (what the author asserts beyond the data)
- Known critiques of the source
- Mapping caveat for this file (which chapter anchors are reconstructed)

## {{Design | Practical}} implications for {{GOAL}}
(bulleted decisions, each tagged [E]/[H]/[V] — or [E]/[C]/[O]; split compound claims:
mechanism [E], parameter [H])

## Connections
(agrees with / tensions with other curriculum sources — use slugs; one line each)

## Retrieval practice
10 questions, mixed: recall, explain-why, apply-to-a-scenario, spot-the-misconception.
Put answers in a <details> block after each question.

## Common misreadings of this book
(3-6 bullets: the plausible wrong takeaways)
```

---

## (b) Agent prompt — Phase 2 (one per source)

```
Read {{REPO}}/SPEC.md in full. You are writing {{REPO}}/books/{{NN-slug}}.md for
"{{Title}}" by {{Author}} ({{year/edition}}), level {{LEVEL}}, priority {{PRIORITY}}
{{, selections: chapters ...}}.

Follow the per-source template in SPEC.md exactly (headings, order). Rules:
- Own words. No quotes over ~12 words. Never reproduce passages. Chapter titles are fine.
- Verify the TOC, edition and key studies with WebSearch. WebFetch may be blocked by the proxy;
  if a fetch fails, do not retry more than once — rely on search-result snippets (publisher page,
  retailer listings, reviews, library records). Label the TOC section "verified" / "partially
  verified" / "reconstructed — not verified", and mark each chapter row (v) or (bk, confidence).
- Never fabricate studies, numbers, effect sizes or chapter titles. When a number is from memory,
  say "about" and mark it background. When you cannot confirm, say so in the file.
- Flag where popular claims outrun the evidence: replication failures, effect sizes that shrank in
  later meta-analyses, findings the author states more strongly than the data supports. Put these
  in "Evidence strength & limits"; downstream agents rely on that section.
- Tag every implication [E]/[H]/[V] (per SPEC). Split compound claims.
- Connections must use the SPEC slugs; name at least one tension with another source.
- Target {{WORDS}} words. Dense and skimmable. Markdown only. No emojis.
- Do not touch any other file. When done, report: word count, TOC verification status, the three
  least-certain claims in the file, and any source you believe is misattributed in SPEC.
```

---

## (c) Quality bar

- [ ] TOC status stated at the top of the section; every row marked (v) or (bk + confidence).
- [ ] Every chapter group has claim / evidence / so-what; load-bearing chapters get the words.
- [ ] 5-10 keep-ideas, ranked; each usable as a flashcard back.
- [ ] Evidence section separates robust / inflated / contested / arguing-vs-showing; names critics.
- [ ] Implications tagged; no untagged decision; mechanism and parameter tagged separately.
- [ ] Connections cite ≥3 other slugs, including at least one disagreement.
- [ ] 10 retrieval questions across all four types with <details> answers.
- [ ] "Common misreadings" present (feeds diagnostic distractors and hinge diagnoses).
- [ ] No quote >12 words; no invented study, number or chapter title; "about" on remembered figures.
- [ ] Word count within budget; hand-back names the three least-certain claims.
