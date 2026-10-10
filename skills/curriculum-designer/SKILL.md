---
name: curriculum-designer
description: Turn a subject or a reading list (books, papers) into a complete self-paced course: per-source breakdowns (catabolic), a synthesis layer (unified model, tensions, casebook, capstone, gaps), and an interactive course app with spaced repetition, diagnostics, hinge questions and mentor feedback. Use when the user wants to "learn everything in these books without reading them", "design a curriculum for X", "build me a course on X", or hands over a syllabus/reading list.
---

# Curriculum designer

Builds a course that teaches a reading list well enough that the learner can *do the thing the
list is about*. The method is the one that produced the two courses at
https://twocents.page/paths/ (Founding School and Games and Norms): catabolic breakdown of every source, then anabolic
synthesis, then an app that applies learning science to itself (cold challenge before content,
hinge questions that diagnose misconceptions, spaced retrieval, an evolving design artifact, a
capstone).

## Inputs
`/curriculum-designer "<subject>" [--sources <file or inline list>] [--goal "<capability>"] [--depth light|standard|deep] [--no-app]`

- **sources**: titles (+ authors, editions). If absent → run `references/discovery.md`.
- **goal**: the capability the learner wants. If absent, propose one from the sources and confirm.
  The goal decides the *working artifact* (design brief / investment policy / protocol / plan) and the capstone.
- **depth**: light ≈ 3k words per source, 6 modules; standard ≈ 5k/source, 10–12 modules; deep adds primary-paper deep dives.

Read `references/lessons.md` before starting. It is the list of things that went wrong before and the rule that prevents each.

## Output layout
```
<slug>-course/
  SPEC.md            run spec: goal, levels, template, rules, source slugs, fixed ID schemes
  course.json        app manifest (see references/data-spec.md)
  README.md          plan, how to use, honesty notes
  books/NN-slug.md   one per source
  synthesis/         claims-ledger, learning-design, unified-model, tensions, casebook, capstone, gaps-primer, artifact-template
  app/data/*.json    modules*.json, diagnostic, flashcards, cases, tensions, brief, model
  app/<slug>.html    built page (published as an artifact)
```

## Procedure
Orchestrator = you. Every phase below hands work to background subagents (`Agent` tool), in parallel
whenever the inputs exist. **Commit and push after each hand-back.** Use your strongest model (Fable, if you have it) for phases 1, 3 and 4a.

0. **Discovery** (only if sources missing/thin) — `references/discovery.md`. One `AskUserQuestion` to confirm list + goal. This is the only interactive step; if the user already said "just run it", pick a sensible goal and state it in the final report.
1. **Structure** — write `SPEC.md` from `references/spec-template.md`: level ladder (default: foundations → mechanisms/practice → systems, plus a critical-synthesis level if a source plays that role), one slug per source, the *fixed* ID schemes (m, t, k, d, c, s). Write `course.json`. Nothing downstream may renumber.
2. **Breakdowns** — one agent per source, all at once, prompt from `references/source-breakdown.md`. Tell each agent the SPEC path, the file to write, the level, what to emphasize, and the word budget. Book files are authoritative for everything after this.
3. **Reconciliation** — one agent, `references/reconciliation.md` → `synthesis/claims-ledger.md`. Every later agent receives this file.
4. **Synthesis**
   a. `synthesis/learning-design.md` — `references/learning-design.md` (strongest model). Must contain the module list with IDs, the cold challenge per module, hinge questions with one diagnosis per option, and a reconciliation log.
   b. In parallel after (a): unified-model, tensions, casebook, capstone, gaps-primer, artifact-template — one agent each, from the matching reference. Give each the SPEC, the ledger, learning-design and the books folder. Casebook and tensions must use the IDs from SPEC; the tensions file's order is canonical.
5. **Data** — 2–3 agents write `app/data/*.json` per `references/data-spec.md` (modules m0–m5 / m6–mN / everything else). Then run `python3 scripts/validate.py <course-dir>`; fix until 0 errors (warnings are judgement calls — read them).
6. **App** — `python3 app/build.py <course-dir>` → `app/<slug>.html`. Smoke test: `NODE_PATH=<dir with playwright> node scripts/smoke.js <built.html>` (install once with `npm i playwright` in a scratch dir; in a Claude cloud session Chromium is at `/opt/pw-browsers/chromium`). If you have the `Artifact` tool, publish with it, capabilities `{"db":{},"user":{},"sample":{}}`, icon e.g. "book". Load the `artifact-capabilities` skill first if the runtime contract has changed. Without it, open the built HTML in a browser or self-host it (below).
7. **QA** — two agents in parallel: (i) fact spot-check of ~30 claims across files via search, report confirmed/unclear/wrong; (ii) cold-learner run: take the diagnostic and M0 challenge without content, read M1–M3, retake, report whether items discriminate. Fix what they find, rebuild, republish.
8. **README + report** — README lists every file, the how-to-use sequence (diagnostic → M0 cold challenge → one module a day → daily cards → artifact updates → capstone), and the honesty notes (what was verified how; least-certain items; corrections made). Final reply: the artifact link, what was built, caveats. Do not open a PR unless asked.

## Self-hosting a course
`python3 app/build.py <course-dir> --standalone [--mentor-endpoint https://your.site/mentor]` writes a
complete HTML document that runs anywhere (progress in the browser's localStorage; no account sync).
Mentor feedback needs a server: `scripts/mentor_proxy.py` is a 90-line Python endpoint that streams
Claude API replies to the page; put it behind your own auth if the page is public. `books/` and
`synthesis/` are plain Markdown and render with any static-site generator.

## Quality bar (what "done" means)
- validate.py: 0 errors. smoke.js: ALL PASS. Every module has a cold attempt, ≥2 hinge questions with a diagnosis per option, ~15 atomic cards.
- Hinge questions are not guessable without reading (options equal in length and register, correct positions shuffled) and diagnostic items carry no absolute-word tells; validate.py enforces both. Run the cold-learner QA before calling the course done: run 1 and run 2 both shipped guessable questions until it caught them.
- Every book file states its TOC verification status. No fabricated studies or numbers; uncertain claims say so.
- Tensions have an IF/THEN rule and a switch signal. Cases cite a tension and a module. Capstone rubric has numeric pass/world-class thresholds.
- The course names where the sources disagree and where popular claims outrun the evidence.
