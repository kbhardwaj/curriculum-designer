# Learning design — modules, hinge questions, schedule

Phase 4, step 1. One agent (Fable). Output: `synthesis/learning-design.md`. Written after the
claims ledger, before the other synthesis agents (they take module ids and the "draws on" map from
it). Book files outrank this file; the reconciliation log at the end records every departure.

---

## (a) File structure

```markdown
# Learning design for the anabolic phase
Status line: what this was designed against; that book files win disagreements; pointer to the
reconciliation log. Learner profile and total time budget (e.g. 15-18 h over three weeks vs ~150 h
of reading).

## 1. Design principles (each tied to the source that justifies it)
8-11 numbered principles. Each: bold statement + (slug, author) + 2-3 sentences of how it shapes
the course. Required set:
  1. Attempt before instruction, where the learner has priors to activate (productive failure).
  2. Worked examples first, faded problems second, novel problems last; scaffolding fades across modules.
  3. One or two load-bearing ideas per module; everything else is "reference, not memory".
  4. Confront the intuitive/folk theory, do not just supply the correct one; hinge distractors are
     built from folk theories so a wrong answer says which is still active.
  5. Retrieve, space, interleave; every third day is a retrieval day.
  6. Hinge questions gate the next step; a wrong answer routes to a specific 5-minute repair.
  7. Mentor tone: high standards, high support, wise feedback; no cheerleading.
  8. The {{ARTIFACT_NAME}} improves through versioned diffs, each with a prediction.
  9. Curiosity hooks sit on the module's target, never beside it.
 10. Every claim carries a tag; the capstone penalizes mis-tags.
 11. Design for the median case, not the showcase.

## 2. Course architecture
### Levels, one spine — order bottom-up (each level constrains the next); opening top-down (cold
attempt at the goal before any content).
### Module list — table: # | module | level | minutes | draws on (slugs). m0 + m1..mN (+ capstone
+ retrieval sessions). Standard depth: 10-12 modules of 90-100 min; light: 6.
### Rationale for the order — one bullet per ordering decision, citing the source.
### Pre-course diagnostic (m0 part A, 20 min) — 16 true/false statements + confidence 1-5, each
diagnosing one named folk theory, keyed to a module and slug; plus one free-response baseline.
### Opening cold challenge (m0 part B, 40 min) — the verbatim prompt: attempt {{GOAL}} in one
page, no research, "the point is to generate, not to be right". Becomes {{ARTIFACT_NAME}} v0.
Then: list indefensible assumptions; tag every decision as best they can.

## 3. Module specifications (one block per module, identical shape)
**Draws on:** slugs + which sections.
**Learning objectives.** 3, as "the learner can (a)... (b)... (c)...".
**Load-bearing ideas.** 1-2 (app expands to 3-5 idea cards of 300-600 words each).
**Curiosity hook.** A question the learner cannot yet answer; its answer is the module target.
**Attempt (cold, before content).** A concrete task with numbers; state what the learner will
predictably get wrong and what the reading then explains. Skip only where there are no priors.
**Worked example.** One decision fully reasoned step by step, ending in a policy, tagged.
**Hinge questions.** 3-5. See rules below.
**Repair paths.** Wrong on Qn → specific book-file section.
**{{ARTIFACT_NAME}} deliverable.** A diff to the artifact, tagged, with a prediction.

## 4. Cross-cutting artifacts (pointers + seeds)
4a unified model sketch · 4b tensions seed list · 4c artifact template skeleton · 4d casebook seed
list (18-24 one-liners with tension + source) · 4e deck plan · 4f capstone outline.
The dedicated synthesis files are authoritative; this section seeds them.

## 5. Spaced schedule (21 days)
## 6. Gaps: what the reading list omits that {{GOAL}} needs
## Reconciliation log
```

---

## (b) Hinge question rules

- 4 options, one correct; question is a scenario, not a definition.
- **Every distractor diagnoses a named misconception** — written as "*Diagnoses: ...*" — drawn
  from the book files' "Common misreadings", the claims ledger corrections, or the diagnostic's
  folk theories. A distractor with no diagnosis is invalid.
- The correct option gets a one-line "why".
- Answerable in under a minute; the decision it gates is stated (move on vs. repair path).
- Distractors are plausible to someone who has read a summary; at least one is "partly right,
  wrong level".
- Across a module the 3-5 questions cover different ideas; no two diagnose the same misconception.
- **Not guessable without reading**: all options in the same register and within ~25% of each
  other's length; the correct option is not the only one with a mechanism/"because" clause; correct
  positions spread across a-d over the module and the course (validate.py fails on >50% longest-is-
  correct or >45% on one index).
- The answer is derivable from the module's ideas; do not rely on a study only the diagnosis cites.
- Change the surface (numbers, setting) from the idea and worked example it tests.

## (c) Diagnostic rules (16 items)

- True/false statement + confidence 1-5; roughly half true, half false; both written as
  scenario statements of similar length with no absolute-word tells ("always", "solves", "on its own"
  only in false items is a giveaway); each item names its
  `folk_theory`, gives an `explanation` citing the source, and keys to one module.
- Retaken on day 21; report accuracy and confidence-calibration delta.
- Item 16 (or a separate free response) is the baseline "what makes a world-class {{X}}?"

## (d) 21-day schedule pattern

- Day 1: m0 (diagnostic 20 + cold challenge 40). Artifact v0.
- Modules >60 min split over two days: day one = hook + attempt + reading map; day two = worked
  example + hinge + artifact diff (a night between generation and consolidation is spacing).
- Every third day is a retrieval day (R1..R6, 40-50 min): deck reviews (1, 3, 7, 14-day
  intervals), 1-3 casebook cases, one free-recall task (re-attempt an earlier attempt; draw the
  model from memory), periodic artifact re-tag checkpoint.
- Cards for module N are introduced the day after N completes; retrieval sessions pull from ≥3
  modules (interleaving).
- Day 20: integration module. Day 21: retake diagnostic + capstone prep. Days 22-24: capstone.
- Table columns: Day | Session | Content | Min. Total ≈ 21 h; floor ≈ 17 h.
- Post-course: deck to the learner's own SRS at 1-3 month spacing; unused cases one per week.

## (e) Gaps section

- 4-8 areas the reading list omits that {{GOAL}} requires, each labeled Critical / Important /
  Useful, with a 1-3 hour recommendation and honest note "this is not in the sources".
- Seeds `gaps-primer.md`; do not write the primer here.

## (f) Reconciliation log (required)

- Bulleted: item → what the draft said → what the book file / ledger says → change made.
- Ends with "Checked, no change needed" list and "Still open" list.
- Book files and the claims ledger win every disagreement; the log proves the check was done.

---

## (g) Agent prompt — Phase 4 step 1

```
Read {{REPO}}/SPEC.md, {{REPO}}/synthesis/claims-ledger.md (section 5 is binding), and every
file in {{REPO}}/books/ (at minimum: one-sentence, one-paragraph, 5-10 ideas, evidence strength,
implications, connections, common misreadings). Write {{REPO}}/synthesis/learning-design.md
following references/learning-design.md sections (a)-(f) exactly.

Constraints:
- Goal: {{GOAL}}. Learner: {{LEARNER}}. Depth: {{DEPTH}} → {{N}} modules of {{MIN}} min.
- Module ids m0..m{{N}} per SPEC; do not renumber later. Every module lists its "draws on" slugs.
- Every module: hook, cold attempt, 1-2 load-bearing ideas, worked example, 3-5 hinge questions
  with a diagnosed misconception per distractor, repair paths, {{ARTIFACT_NAME}} deliverable.
- Diagnostic: 16 items with folk_theory, explanation, module; plus free-response baseline.
- Cold challenge prompt verbatim, no research, one page, becomes {{ARTIFACT_NAME}} v0.
- 21-day schedule table with retrieval days every third day and split modules.
- Seed lists for tensions (10-14), cases (18-24, each with tension + slug), deck plan
  (~15 atomic cards per module by type), capstone outline, artifact skeleton (s1..sNN).
- Gaps section: what {{GOAL}} needs that the sources omit.
- Every number you cite must appear in the claims ledger section 4; otherwise use words.
- End with the reconciliation log: check every factual claim in the modules and hinge questions
  against the book files' evidence sections; record every change; list "checked, no change".
- Report back: module count, hinge count, any book file you could not use, and the three claims
  you are least sure survive a fact check.
```

---

## (h) Quality bar

- [ ] Principles each cite a slug; the required eleven are present.
- [ ] Levels ordered bottom-up with a stated constraint rationale; m0 is top-down and cold.
- [ ] Every module block has all eight parts; attempts have concrete numbers and predicted errors.
- [ ] Every hinge distractor has "Diagnoses: ..."; no module reuses a misconception across questions.
- [ ] Repair paths point to a book-file section, never "re-read the module".
- [ ] Diagnostic has 16 keyed items + confidence; retake on day 21 is scheduled.
- [ ] Schedule: retrieval every third day, cards introduced day-after, ≥3 modules per session.
- [ ] Seeds exist for all six downstream files; case seeds carry tension + source.
- [ ] Reconciliation log present with at least one "checked, no change" line.
- [ ] No number without a ledger row.
