# App data contract — `app/data/*.json` and `course.json`

Phase 5 (2-3 agents in parallel) writes the JSON; `app/build.py` inlines it into
`app/template.html` at `/*__DATA__*/` and reads `course.json` for every domain string.
`scripts/validate.py` must pass before the app is built. All text is plain strings; light
markdown (**bold**, *italic*, `- ` bullets, line breaks) is rendered. Tags per SPEC (E/H/V or
E/C/O); the `tags` map in `course.json` supplies the labels.

---

## course.json (manifest; one per run, repo root)

| Field | Type | Example (run 1) | Used for |
|---|---|---|---|
| `slug` | string | `founding-school` | localStorage key prefix, output filename |
| `title` | string | `Founding School` | `<title>`, rail brand, header label |
| `subtitle` | string | `Learning science to school design to institution building` | gallery/description |
| `description` | string | one sentence | `<meta description>`, artifact description |
| `tagline` | string | `Learn what 13 books know about learning, then design a school with it.` | home `<h1>` |
| `lede` | string | the levels-in-order paragraph | home lede |
| `artifact_name` | string | `Design brief` | rail entry, tile, module step 6, artifact view heading |
| `artifact_items` | string | `decisions` | "N decisions recorded" |
| `artifact_lede` | string | `One document that grows with every module.` | artifact view lede |
| `artifact_critique_prompt` | string | "Critique this school-design brief. Check: (1) tagging ... (4) the single most important missing decision." | mentor critique of the artifact |
| `case_noun` | string | `founder dilemmas` | casebook heading count |
| `case_singular` | string | `founder dilemma` | mentor case-evaluation prompt |
| `case_lede` | string | `Realistic situations a founder hits in the first three years.` | casebook lede |
| `levels` | string[] | `["Minds","Design","Institutions"]` | rail count, home level grouping, model header arrows; must match `modules[].level` values (plus `Start`/`Integration`) |
| `laws_noun` | string | `laws of this school` | model view laws heading |
| `model_lede` | string | "Read it like a building: ..." | model view lede |
| `mentor_voice` | string | "You are a demanding but supportive mentor (high standards, high support) coaching a learner who is {{GOAL}}. They have a {{LEARNER}} background. Be specific and concise (under 250 words). Use markdown bullets. Tag claims as [E]/[H]/[V] where useful." | prefix on every mentor call |
| `source_count` | int | `14` | home label |
| `repo_path` | string | `school-design-course` | "full breakdowns live in the repository under ..." |
| `tags` | object | `{"E":"supported by evidence","H":"hypothesis to test","V":"value commitment"}` | tag chips and legends; keys must match the tags used in data |

Rules: every string is domain-specific and written by the orchestrator from SPEC; no field may
still read "school"/"founder" in a non-school run. The template falls back to generic strings
for any missing field, so a missing field is a validation *warning*, an ungeneralized one an
*error*. Use exactly these names: `build.py` does no aliasing.

---

## app/data/modules.json (may be split into modules-a.json / modules-b.json; build.py merges and sorts by id)

```json
{ "modules": [ {
  "id": "m1", "num": 1, "title": "...", "level": "{{LEVEL_1}}|{{LEVEL_2}}|{{LEVEL_3}}|Integration|Start",
  "minutes": 90, "sources": ["01-slug", "..."],
  "hook": "a short opening question or puzzle whose answer is the module target",
  "attempt": { "prompt": "cold attempt the learner tries BEFORE the content", "minutes": 10 },
  "objectives": ["the learner can ...", "...", "..."],
  "ideas": [ { "title": "load-bearing idea", "body": "300-600 words of distilled teaching, markdown", "tag": "E" } ],
  "worked_example": { "title": "...", "steps": ["step with reasoning", "..."] },
  "hinge": [ { "q": "...", "options": ["A","B","C","D"], "answer": 1,
               "diagnoses": ["misconception revealed by choosing A", "correct - why", "...", "..."] } ],
  "brief_prompt": "what to add/change in the {{ARTIFACT_NAME}} after this module",
  "deeper": ["books/NN-slug.md#section"]
} ] }
```
- m0 = diagnostic + cold challenge (`level: "Start"`, `sources: []`, `attempt.minutes` ≈ 40).
- 3-5 ideas per module (m0: 2); 3-5 hinge per module; `diagnoses.length === options.length`;
  `answer` is a 0-based index; every non-answer diagnosis is a misconception, not "wrong".
- `level` values must be in `course.json.levels` or `Start`/`Integration`.

## app/data/diagnostic.json
```json
{ "items": [ { "id": "d1", "statement": "...", "correct": true, "folk_theory": "...", "explanation": "...", "module": "m2" } ] }
```
16 items; learner answers true/false + confidence 1-5; ~half true; `module` must exist.

## app/data/flashcards.json
```json
{ "cards": [ { "id": "c001", "module": "m1", "type": "recall|explain|apply|discriminate",
               "front": "...", "back": "...", "source": "01-slug" } ] }
```
~15 per module (12-24 acceptable), atomic (one fact/decision per card), ~180-220 total; mix of
types per module (recall 4-5, explain 3-4, apply 3-4, discriminate 2-3); unlock on module
completion; cap 20 new/day; `source` is a SPEC slug.

## app/data/cases.json
```json
{ "cases": [ { "id": "k01", "title": "...", "scenario": "...", "tension": "t03",
               "question": "What do you do?", "considerations": ["..."], "model_answer": "...",
               "sources": ["..."] } ] }
```
`tension` = primary tension id, must exist in tensions.json.

## app/data/tensions.json
```json
{ "tensions": [ { "id": "t01", "name": "X vs Y", "pole_a": "...", "pole_b": "...",
                  "rule": "IF ... THEN ...; IF ... THEN ...", "switch_signal": "...",
                  "evidence": "...", "sources": ["..."] } ] }
```
Order = synthesis/tensions.md order (canonical).

## app/data/brief.json
```json
{ "sections": [ { "id": "s1", "title": "...", "guidance": "...", "default_tag": "V", "prompts": ["..."] } ] }
```

## app/data/model.json
```json
{ "bands": [ { "id": "{{level-slug}}", "title": "...", "certainty": "...",
               "nodes": [ { "id": "M1", "label": "...", "summary": "...", "tag": "E",
                            "links": ["D1"], "sources": ["slug"] } ] } ],
  "chain": ["causal-chain sentence 1", "..."],
  "laws": ["law 1", "..."],
  "loop": "improvement loop description" }
```
Band order = levels order; `links` must resolve to node ids; `laws` non-empty.

---

## validate.py checks (fail the run on any error)

- JSON parses; top-level keys as above; ids match regex (`m\d+`, `t\d{2}`, `k\d{2}`, `d\d+`,
  `c\d{3}`, `s\d+`) and are unique and contiguous.
- Cross-refs: `cases[].tension` → tensions; `diagnostic[].module`, `cards[].module` → modules;
  `cards[].source`, `modules[].sources`, `*[].sources` → SPEC slugs; `model.nodes[].links` → nodes.
- Modules: m0 present; each has hook, attempt, ≥3 objectives, ≥2 ideas, worked_example, ≥3
  hinge; each hinge has 4 options, `answer` in range, `diagnoses` same length, no empty diagnosis.
- Counts: 16 diagnostic items; 12-24 cards per module (m0 may be 0); ≥10 tensions; ≥18 cases;
  ≥8 brief sections; ≥3 bands.
- Tags: every `tag` value is a key of `course.json.tags`.
- course.json: all fields present (warning) and none contain a placeholder or a string from a
  different run's manifest (error).

---

## Agent prompt — Phase 5 (split: A = modules + diagnostic; B = flashcards; C = cases + tensions + brief + model, or as the synthesis agents already produced them)

```
Read SPEC.md, synthesis/claims-ledger.md (section 5 binding), and the synthesis files assigned
to you ({{list}}). Produce {{files}} per references/data-spec.md exactly.
- Ids are fixed by SPEC and the synthesis files; never renumber. `answer` is 0-based.
- Expand each module's 1-2 load-bearing ideas into 3-5 idea cards of 300-600 words, written from
  the book files (not from the module summary), each tagged.
- Every hinge distractor's diagnosis names a misconception; copy them from learning-design.md,
  do not paraphrase them into "incorrect".
- Cards: ~15 per module, atomic, four types, `source` slug on each; fronts are questions or
  scenarios, backs ≤60 words; no card duplicates a hinge question verbatim.
- Run `python3 scripts/validate.py` before handing back; fix every error; report warnings.
- Report back: counts per file, validator output, and any place the synthesis file and the book
  file disagreed (you used the book file).
```
