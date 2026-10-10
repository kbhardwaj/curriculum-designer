# Working artifact template — the evolving {{ARTIFACT_NAME}}

Phase 4, parallel agent. Output: `synthesis/artifact-template.md` (+ `app/data/brief.json`).
The versioned document the learner writes from m0 (v0, one cold page) to the capstone (v5,
3,000-4,000 words). Domain instances: design brief (school), investment policy (fund), clinical
protocol (medicine), study plan (language), cooperation design brief (groups). ~5,500 words for
10-12 sections.

---

## (a) File structure

```markdown
# {{ARTIFACT_NAME}}: template and guide
Intro: versioned from v0 to v5; what each section gives (purpose, expected tags, prompts,
example entry, common failures); the worked example context (a named hypothetical {{project}}
with concrete parameters); examples illustrate form and tagging, not a recommended design.

## Rules that apply to the whole {{ARTIFACT_NAME}}
- Tag every declarative sentence in the mechanism sections (s3-s9); untagged fails rubric 8.
- [E] needs a source slug and, where contested, a caveat in the same sentence.
- Split compound claims (mechanism [E], parameter [H]).
- Values are not weaker than evidence; never upgrade [V]→[E] because a source agrees.
- Later sections cite the model-of-{{foundation}} commitments by number (L1-L5).
- Every [H] appears in the hypotheses register; every [V] in the values register.
- Length: v0 one page; v5 3,000-4,000 words.

## Header and changelog format
# <Name> - {{ARTIFACT_NAME}} v<N> / Date / Previous version / Changelog lines:
"- [sN] Reversed|Added|Re-tagged|Removed: <what>. Motivated by M<n> (<author>). Tag <old>→<new>.
New H-nn/V-nn."

## Version plan
Table: Version | After | What changes (v0 m0 cold; v1 after m1-2; v2 after m3-5 + full re-tag
checkpoint; v3 after m6-7; v4 after m8-9 + registers; v5 after integration + capstone).

## sN. <Section title> (<expected tag mix>)
**Guidance.** What the section is for; the tension it governs; the most common founding mistake.
**Expected tags.** Which tags dominate and why; where [H] hides inside an [E].
**Prompts.** 4-6 questions to draft from.
**Example entry (<hypothetical>).** 150-300 words, every claim tagged, slugs on [E], register
ids on [H]/[V].
**Common failures.** 3 bullets.

## Section set (default; rename per domain, keep the roles)
s1 Purpose and {{stakeholders}} (mostly [V]; the open-vs-closed layers rule)
s2 The concrete day / the median case, narrated minute by minute at three points (inline tags)
s3 Model of the {{foundation level}}: five numbered commitments L1-L5 + rejected folk theories
s4 {{Content/scope}} decisions ([E] mechanisms, [V] choices)
s5 {{Core practice}} defaults and exceptions with conditions ([E] defaults, [H] parameters)
s6 {{Feedback/measurement}} ([E] mechanisms, [H] cadence)
s7 {{People}}: selection vs development ([E]/[H])
s8 {{Structure}} ([H]; every departure names the need behind it)
s9 Improvement system ([E] method, [V] aim)
s10 Open hypotheses register ([H]) — table: Id | Hypothesis | Section | Why H not E | Test |
    Prediction | Practical measure | Balancing measure | Decision rule | Review date | Status
s11 Value commitments register ([V]) — table: Id | Commitment ("We choose X over Y") | Section |
    Who reasonably disagrees + best argument | Cost | Evidence that informs it | Conflicts with |
    Owner and review

## Self-check before saving a new version
6 questions (traceability to L1-L5; untagged sentences; contested findings without caveat;
registers complete; median case not showcase; changelog attributes module + author).
```

---

## (b) brief.json mapping

- One object per section: `id` (s1..), `title`, `guidance` (guidance + expected tags + example
  entry, markdown), `default_tag` (E/H/V), `prompts[]`.
- Registers (s10, s11) are sections too; their `guidance` carries the table format.

---

## (c) Agent prompt

```
Read SPEC.md, synthesis/claims-ledger.md (section 5 binding), synthesis/learning-design.md
(section 4c skeleton, module ids, the m0 cold-challenge prompt), synthesis/tensions.md (ids),
and the "Implications" sections of books/*.md. Write synthesis/artifact-template.md per
references/artifact-template.md (a).
- 10-12 sections s1..sNN in the SPEC order; keep the roles in the default set, rename per
  domain. s3 must be the five L1-L5 commitments + rejected folk theories (from the diagnostic's
  folk theories and the ledger's corrections). The last two sections are the registers.
- Every section: guidance (naming the tension it governs), expected tags, 4-6 prompts, a fully
  tagged example entry for one consistent hypothetical {{project}} with concrete parameters,
  common failures.
- Example entries must cite slugs on every [E], register ids on every [H]/[V], and must not
  contradict the ledger.
- Include the whole-document rules, header/changelog format, version plan keyed to module ids,
  and the self-check.
- Write app/data/brief.json per references/data-spec.md.
- Append a reconciliation log. Report back: section list with default tags, the hypothetical's
  parameters, and any section whose example you could not source from the book files.
```

---

## (d) Quality bar

- [ ] 10-12 sections; ids contiguous; roles from the default set present; registers last.
- [ ] Every example sentence tagged; every [E] has a slug; every [H]/[V] has a register id.
- [ ] s2 narrates the median case at three points, minute by minute, inline-tagged.
- [ ] s3 has exactly five (±1) commitments and a rejected-folk-theory list.
- [ ] Register tables have every column; example rows have predictions and dissenters.
- [ ] Version plan keyed to module ids; changelog format shown; self-check present.
- [ ] brief.json validates; reconciliation log present.
