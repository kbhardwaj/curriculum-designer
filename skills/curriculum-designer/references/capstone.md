# Capstone — deliverables and the 10-criterion rubric

Phase 4, parallel agent. Output: `synthesis/capstone.md`. The final performance that proves the
learner can {{GOAL}}: the finished {{ARTIFACT_NAME}}, a defense under attack, and a first-90-days
(or equivalent first-action) plan. ~5,000 words.

---

## (a) File structure

```markdown
# Capstone: the {{ARTIFACT_NAME}}, the defense, the first 90 days
Intro: the one question the capstone asks ("could you {{GOAL}} on this, defend it under
pressure, and run its first {{period}} as a learning system?"). Table: # | Deliverable | Length |
Time | Main criteria. Schedule (days 22-24, one deliverable per sitting; order: artifact, defense,
plan). Prerequisites (artifact v4 with registers started; day-21 diagnostic retake; ≥8 cases done).

## Deliverable 1: {{ARTIFACT_NAME}} v5
Use synthesis/artifact-template.md. Minimum contents list, one line per section (s1..sNN):
what must be present; a missing item caps the matching criterion at 2. 3,000-4,000 words.

## Deliverable 2: The defense
Six challenges; ≥2 attack the learner's own [V] commitments. 200-300 words each or a 20-minute
talk. Every answer makes five moves: (1) name the tension (id + name); (2) apply the rule to the
case *and the artifact*, citing the section; (3) state the switch signal (a number or
observation); (4) say what you don't know, tagged; (5) say what changes in the artifact, or why
nothing does — at least one answer must change it (logged as v5.1).
Value challenges: steelman the dissenter, name the cost, then hold or revise. Citing evidence as
if it settled a value is a mis-tag.
### Challenge-selection procedure
Step 1 attack map (each [V] paired with a case + dissenter). Step 2 draw four cases at random
with constraints: ≥2 unseen during the course; ≥1 {{practice-scale}} and ≥1 {{system-scale}}
tension; no two share a primary tension. Step 3 draw two value attacks (co-planner writes them if
available). Step 4 transplant each case into the learner's own context. Step 5 seal the six
before answering; 45-minute timebox. Include a worked example of a draw.
### What the defense is not
"My artifact doesn't address this, here is what I'd add and what would show me wrong" can earn a
4; reciting a model answer about someone else's context cannot.

## Deliverable 3: The first 90 days
One page + driver diagram. Must contain: (1) year-one aim (what, how much, by when, for whom;
[V] choice, [H] size); (2) driver diagram with a measure at each level and [E]/[H] on change
ideas; (3) first three small tests, each with change, owner, written prediction with a number,
practical measure and return time, balancing measure, dates, adopt/adapt/abandon rule; ≥1 tests
an [H] from the register; (4) the launch of the {{development/learning routine}}; (5) three
mechanisms the learner will personally observe weekly, with "good" in one sentence and the
two-week no-show action; (6) days 30/60/90: what must be true and what if not.

## Rubric
Each criterion 1-4. **Pass:** 32/40, no criterion below 2. **World-class:** 36/40 with a 4 on the
four criteria that separate "built on how {{domain}} works" from "built on how {{things}} usually
look" (name them).
Levels: 4 = an expert practitioner would sign it; 3 = sound, gaps a colleague catches in one read;
2 = the right words without the working parts; 1 = absent, wrong, or contradicted elsewhere.
### 1..7 — domain criteria (one per load-bearing section of the artifact, in level order)
### 8. Tagging discipline
### 9. Defense quality
### 10. Delta from v0
Each criterion: *Where to look:* sections. Then 4/3/2/1 descriptors, each concrete (counts,
named items, "caps at 1 if X appears untagged").
### Scoring procedure
Self-score at once with evidence; re-score cold at 48 h; co-planner scores independently, lower
score wins unless evidence is quoted; repair map (criterion → modules + book-file sections);
one resubmission.

## Worked exemplar: what a 4 looks like
Excerpts from a hypothetical learner's v5 for two or three criteria, annotated: why it earns 4
and what would drop it to 3.

## Appendix: scoring sheet
Table: # | Criterion | Self (day 0) | Self (day 2) | Co-planner | Final | Evidence.
```

---

## (b) Rubric criterion pattern (domain criteria 1-7)

- Criterion = one load-bearing commitment of the artifact, in level order (bottom level first).
- 4 descriptor lists the working parts by name (numbers, named mechanisms, the switch signal, the
  register entry).
- 3 = all parts present but one missing or asserted without being visible elsewhere.
- 2 = the vocabulary without the mechanism ("balanced approach", "we'll iterate").
- 1 = a rejected folk theory endorsed untagged (caps at 1), or the section absent.
- Criterion 8 (tagging): every declarative sentence tagged; compound claims split; every [E] has
  a slug; contested findings (list them from the ledger) caveated; registers ≥8 [H] and ≥6 [V].
- Criterion 9 (defense): five moves in all six; switch signals specific; value attacks steelmanned.
- Criterion 10 (delta): ≥8 substantive reversals of v0 with module + author attribution; v0 free
  response revisited; diagnostic retake compared with confidence calibration; ≥1 v0 position
  explicitly kept with reason.

---

## (c) Agent prompt

```
Read SPEC.md, synthesis/claims-ledger.md (section 5 binding), synthesis/learning-design.md
(section 4f seed, module ids), synthesis/artifact-template.md (section ids s1..sNN),
synthesis/tensions.md (ids), synthesis/casebook.md (ids, primary tensions), and the
"Implications" sections of books/*.md. Write synthesis/capstone.md per references/capstone.md.
- Three deliverables as specified; the defense's five moves and selection procedure verbatim in
  structure, adapted to this course's ids and scales (which tensions count as practice-scale vs
  system-scale).
- Minimum contents list for the artifact keyed to s-ids.
- Rubric: criteria 1-7 map to the artifact's load-bearing sections in level order; 8-10 fixed.
  Every descriptor concrete. Name the four world-class criteria and why.
- Repair map: criterion → modules + specific book-file sections.
- Worked exemplar for ≥2 criteria, annotated. Scoring sheet appendix.
- Numbers only from the ledger. Append a reconciliation log.
- Report back: the criterion list, the four world-class criteria, and any artifact section with
  no rubric coverage.
```

---

## (d) Quality bar

- [ ] Three deliverables with length, time and criteria; prerequisites stated.
- [ ] Defense: five moves, ≥2 value attacks, selection procedure with constraints + worked draw.
- [ ] 90-day plan has all six parts; ≥1 test of a register [H].
- [ ] Rubric: 10 criteria × 4 levels, "where to look" on each, caps stated; pass 32 / world-class
      36 with the four named criteria.
- [ ] Repair map covers all 10; scoring procedure with 48-h re-score; exemplar; sheet.
- [ ] All ids (s, t, k, m) resolve to their files; reconciliation log present.
