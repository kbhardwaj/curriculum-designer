# SPEC template — the run's shared contract

The orchestrator (Phase 1 agent, Fable) writes `SPEC.md` at the root of the course repo before any
breakdown agent starts. Every later agent gets this file verbatim. It fixes: the goal, the levels,
the tag scheme, the per-source template, the rules, the source slugs, and every ID scheme.

Placeholders: `{{SUBJECT}}` (domain), `{{GOAL}}` (capability the learner wants at the end),
`{{ARTIFACT_NAME}}` (the evolving working document, e.g. "design brief", "investment policy",
"clinical protocol", "study plan"), `{{LEVELS}}` (ordered level names), `{{LEARNER}}` (profile).

---

## (a) Template

```markdown
# Course build spec (shared by all agents) — {{SUBJECT}}

Goal: the learner ({{LEARNER}}; time-poor) must understand this entire reading list well enough
to **{{GOAL}}** — without reading the books. The learner keeps an evolving "{{ARTIFACT_NAME}}"
for a {{context of their choosing}}. Two phases:

- **Catabolic** — break each source into parts → TOC → most salient knowledge per chapter/section.
- **Anabolic** — synthesize across sources into models, tensions, decisions, practice and a capstone.

{{N}} levels organize everything:
1. **{{LEVEL_1}}** — {{one-line question this level answers}} ({{sources}})
2. **{{LEVEL_2}}** — {{question}} ({{sources}})
3. **{{LEVEL_3}}** — {{question}} ({{sources}})
[4. **Synthesis under critique** — {{the critic/unifier source}} and its problems]  (optional)

Every {{design|knowledge}} claim is tagged:
  EHV scheme: **[E]** supported by evidence · **[H]** hypothesis to test · **[V]** value commitment
  ECO scheme: **[E]** established · **[C]** contested · **[O]** open question

## Per-source file template (`books/NN-slug.md`)
{{paste the template from references/source-breakdown.md, with {{SUBJECT}}-specific "So-what"
line and implications heading filled in}}

## Rules
- Write in your own words. No quotations longer than ~12 words; no reproducing passages.
  Chapter titles are fine.
- Use WebSearch (WebFetch may be blocked by the proxy — if so, rely on search snippets) to verify
  TOCs, editions, key studies. Say plainly when something is from background knowledge vs.
  verified. Do not fabricate studies, numbers, or chapter titles.
- Where popular claims outrun the evidence (replication failures, contested interpretations,
  inflated headline effect sizes), say so explicitly.
- Dense, skimmable, high-signal. Target {{3,500-6,000}} words per source (light: ~3,000;
  more for anthologies/collections — cover every study they discuss).
- Markdown only. No emojis.

## Source slugs (fixed — use exactly these)
- 00-{{slug}} — {{Author, Title (year/edition)}} · {{Level}} · {{Core | Extension | Selections: ch N, M}}
- 01-{{slug}} — ...
- NN-{{slug}} — ...

## ID schemes (fixed for every downstream file — do not renumber)
- modules: m0 (diagnostic + cold challenge), m1..mN in synthesis/learning-design.md
- tensions: t01..tNN in synthesis/tensions.md (that file's order is canonical)
- cases: k01..kNN in synthesis/casebook.md
- diagnostic items: d1..d16
- flashcards: c001..cNNN
- {{ARTIFACT_NAME}} sections: s1..sNN in synthesis/artifact-template.md
- model nodes: {{band-letter}}N (e.g. M1, D1, I1) in synthesis/unified-model.md
```

---

## (b) Filling rules

- **Goal** is a capability, phrased as a verb: "design and found X", "diagnose Y and design Z",
  "run W". It drives the capstone and the artifact. If the user gave none, propose one and confirm.
- **Levels** default to the ladder *foundations (mechanisms) → practice (methods/design) →
  systems (institutions/markets/organizations)*. Rename per domain (e.g. Minds/Design/Institutions;
  Origins/Mechanisms/Order). Add a 4th "synthesis under critique" level only when a source
  attempts a grand unification. Every source gets exactly one primary level.
- **Tag scheme:** EHV for design-oriented goals (learner will make decisions); ECO for
  knowledge-oriented goals (learner wants to understand a field). Fix it here; every file uses it.
- **Slugs:** `NN-kebab-title`, two-digit, in level order then reading order. `00` is reserved for a
  "learner's own papers" or "foundational papers" bundle if one exists; otherwise start at 01.
  For "selections" sources, list which chapters are covered and why.
- **Priority:** Core (full treatment) · Extension (shorter, ~60% budget) · Selections (named chapters).
- **IDs:** fix every scheme above now. Downstream agents may append (add t15) but never renumber.
  The tensions file's order is canonical for `tNN`; the casebook cites those ids.
- Add domain-specific "So-what" phrasing to the per-source template (e.g. "So-what for someone
  designing cooperation in a real group").

---

## (c) Agent prompt — Phase 1 (structure + SPEC)

```
You are writing SPEC.md for a self-paced course on {{SUBJECT}}. Read
references/spec-template.md and references/source-breakdown.md. Inputs: the confirmed reading
list (title, author, year, edition, one-line rationale, verification status per source), the
goal "{{GOAL}}", the learner profile "{{LEARNER}}", depth={{light|standard|deep}},
claim-tags={{EHV|ECO}}.

Produce {{REPO}}/SPEC.md following the template exactly:
1. Goal paragraph naming the capability and the {{ARTIFACT_NAME}} the learner will keep.
2. Level structure ({{3-4}} levels), one question per level, every source assigned to exactly one.
   Justify the level order in two sentences (each level should constrain the next).
3. Tag scheme with definitions.
4. Per-source file template with the domain-specific "So-what" line and the implications heading.
5. Rules (own words, ≤12-word quotes, verify via search, WebFetch fallback, flag claims that
   outrun evidence, word budget for this depth, markdown only, no emojis).
6. Source slugs 00/01..NN, fixed, with author/title/year/level/priority, and for Selections the
   chapters covered.
7. ID schemes for m, t, k, d, c, s and model nodes.
Do not write any breakdown or synthesis content. Do not invent sources. Output only the file.
```

---

## (d) Checklist before Phase 2 starts

- [ ] Goal is a capability, not a topic; artifact name is concrete.
- [ ] Every source has exactly one level, one slug, one priority; slugs are two-digit and unique.
- [ ] At least one source is a critic/contrarian (tensions need it) and one is adjacent-field.
- [ ] Tag scheme chosen and defined; per-source template uses it.
- [ ] All six ID schemes written; "do not renumber" line present.
- [ ] Word budget matches depth; anthology sources get the larger budget.
- [ ] WebFetch fallback and verification-status rule are in the Rules section.
- [ ] Committed and pushed before any breakdown agent launches.
