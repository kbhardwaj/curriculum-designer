# Casebook — dilemmas keyed to modules and tensions

Phase 4, parallel agent (runs after tensions.md publishes its id order, or is handed that order).
Output: `synthesis/casebook.md` (+ `app/data/cases.json`). 20-24 cases, ~600-700 words each
(~16,000 words total). Each case is a realistic decision someone pursuing {{GOAL}} will face.

---

## (a) File structure

```markdown
# {{Role}}'s casebook: {{N}} {{CASE_NOUN}} for the {{SUBJECT}} course
Intro: practice layer; each case gives concrete numbers and people, names the tension, and has a
model answer citing slugs with tags. How the seed list (learning-design 4d) was kept, merged or
sharpened.

## How to use a case
1. Read scenario + question only. 10-minute timer.
2. Write 150-250 words that: name the tension (id + name), apply its rule, state the switch
   signal, tag each decision.
3. Read considerations; note what you missed.
4. Read model answer + novice error. Self-score 0-2 on: tension named, rule applied, switch
   signal, tagging, concrete next step. ≥8/10 strong.
5. Below 6: open the implications section of the first two sources; redo in two days.
Model answers are defensible, not uniquely correct.

## Tension mapping
Table: Id | Tension | Primary in (cases) | Also exercised in. Ids from tensions.md (canonical).

## Case index
Table: Id | Case | Tension(s).

## kNN. <Title (concrete, memorable)>
**Tension:** tNN <name>   **Module:** mN
**Sources:** `slug`, `slug`, `slug`
### Scenario
150-250 words. Named people, real numbers, a deadline, a plausible voice pushing the wrong way.
Set at the learner's own {{context}}, not in a lab.
### Question
One or two sentences ending in a decision ("What do you do, and which two authors are arguing in
your head?").
### Considerations
4-6 bullets, as questions, that point at the evidence without giving the answer.
### Model answer
250-400 words. Opens with the decision. Names the tension, applies the rule, cites slugs with
tags on each decision, states the switch signal, gives a concrete next step, and speaks to the
person pushing the wrong way. Logs any [H] as a register entry.
### What a novice would do wrong
2-4 sentences: the plausible wrong move and why it is tempting.
```

---

## (b) Agent prompt

```
Read SPEC.md, synthesis/claims-ledger.md (section 5 binding), synthesis/tensions.md (its id
order is canonical — do not reorder or rename tensions), synthesis/learning-design.md (module
ids; section 4d seed cases), and the "Implications" and "5-10 ideas" sections of every
books/*.md. Write synthesis/casebook.md per references/casebook.md (a).
- 20-24 cases. Keep, merge or sharpen the seeds; add cases so every tension is primary in ≥1
  case and every module ≥1 case. Cover both the "classroom"-scale and the "institution"-scale
  tensions.
- Each case: scenario with named people, numbers, a deadline and a dissenting voice; question;
  4-6 considerations as questions; model answer that names the tension, applies its rule, tags
  each decision, cites slugs, states the switch signal and a next step; novice error.
- Numbers only from the ledger. No case may rest on a claim the ledger corrects.
- Write app/data/cases.json per references/data-spec.md (id, title, scenario, tension = primary
  id, question, considerations[], model_answer, sources[]).
- Append a reconciliation log (departures from seeds; any case whose model answer had to change
  because of the ledger).
- Report back: case count, tension coverage table, module coverage, and any tension you could
  not build a realistic case for.
```

---

## (c) Quality bar

- [ ] 20-24 cases; ids k01.. contiguous; every tension primary in ≥1 case; every module covered.
- [ ] Scenarios have people, numbers, a deadline and a wrong-way voice; none is abstract.
- [ ] Model answers open with the decision and hit all five scoring moves.
- [ ] Every [H] in a model answer says how it would be tested; every [V] names the dissenter.
- [ ] Novice error present for every case.
- [ ] Tension ids and names match tensions.md exactly; cases.json `tension` is the primary id.
- [ ] No number outside the ledger; reconciliation log present.
