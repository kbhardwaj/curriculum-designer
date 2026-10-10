# Discovery — building a reading list from a bare subject

Phase 0. One agent (Fable). Runs only when the user gave no sources, or fewer than ~6. Output:
a candidate reading list table + one confirmation question. This is the only interactive step
in the pipeline.

---

## (a) Composition rule (8-14 sources)

| Slot | Count | Why it is required |
|---|---|---|
| Canonical text(s) | 1-2 | the organizing reference every other source builds on or argues with |
| Seminal papers | 3-5 | the primary results; bundle as `00-foundational-papers` if short |
| Recent synthesis | 1 | a review, handbook chapter or recent book that states the current consensus and effect sizes |
| Critic / contrarian | ≥1 | tensions.md cannot be written without a source that disputes the canon; replication critics count |
| Adjacent-field source | 1 | the neighboring discipline that the goal needs (economics for education; psychology for finance; networks for sociology) |
| Practice / institutional source | 1-2 | how the knowledge is applied at scale; feeds the top level and the artifact |
| Extension | 0-2 | depth on the hardest mechanism; marked Extension (shorter budget) |

- Prefer sources with a verifiable TOC (books, published reviews) over blog posts.
- Prefer the latest edition; note when an earlier edition is the famous one.
- For a knowledge-oriented goal (ECO tags), weight toward reviews and critics; for a
  design-oriented goal (EHV), weight toward practice sources and the adjacent field.
- Total reading time saved should be ~100-180 hours (that is the course's promise).

## (b) Verification (per source)

- WebSearch the exact title + author. Confirm: title, author(s), year, edition, publisher, and
  that a TOC or chapter list is findable. WebFetch may be blocked; use search snippets
  (publisher, library, retailer, review).
- Status labels: **verified** (all fields confirmed) · **partially verified** (exists; edition or
  TOC unconfirmed) · **unverified** (could not confirm; do not include unless the user supplies it).
- Never invent a source. If a "famous paper" cannot be found, say so and offer the nearest
  confirmed alternative.

## (c) Output table

| # | Slot | Title | Author(s) | Year / ed. | Level (proposed) | Rationale (one line) | Verification |
|---|------|-------|-----------|------------|------------------|----------------------|--------------|

Then: proposed goal (if the user gave none), proposed levels, proposed tag scheme, estimated
reading hours saved, and the sources considered and rejected (one line each, so the user can
swap them in).

## (d) The one confirmation question

Ask exactly one AskUserQuestion. It presents: the table, the proposed goal, the levels, the tag
scheme. Options: **confirm as-is** / **swap or add sources** (free text) / **change the goal**.
Do not proceed to Phase 1 until answered. Do not ask a second question; take reasonable defaults
for everything else and record them in SPEC.md.

---

## (e) Agent prompt — Phase 0

```
Subject: "{{SUBJECT}}". Goal (may be empty): "{{GOAL}}". Sources given (may be empty):
{{SOURCES}}. Depth: {{DEPTH}}. Build the reading list per references/discovery.md.
- Fill every slot in the composition table; 8-14 sources total (light depth: 6-8). Keep any
  source the user gave unless it cannot be verified; say why if you drop one.
- Verify each with WebSearch; WebFetch may be blocked — rely on snippets. Label status per
  source. Never invent a title, author or year.
- Propose a goal (a capability, verb-first) if none was given; propose {{3-4}} levels with a
  one-line question each; propose EHV or ECO with a one-line reason.
- Output: the table, the proposals, rejected candidates, and a single AskUserQuestion with the
  three options above. Stop after asking.
```

## (f) Quality bar

- [ ] 8-14 sources; every slot filled; ≥1 critic; ≥1 adjacent-field.
- [ ] Every row has a verification status; no "unverified" row kept without user say-so.
- [ ] Every source has a proposed level and a one-line rationale tied to the goal.
- [ ] Goal is a capability; levels are ordered bottom-up; tag scheme chosen with reason.
- [ ] Exactly one question asked; nothing written to the repo before the answer.
