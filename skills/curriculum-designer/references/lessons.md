# Lessons from run 1 — what went wrong and the rule that prevents it

Each rule is binding on the orchestrator (SKILL.md) or on the agent prompt that cites it.

## Structure and IDs
- **Fix every ID scheme in SPEC before any synthesis agent starts.** Run 1: the casebook agent
  used a different tension order than tensions.json and every case needed a remap. Rule: SPEC
  lists m/t/k/d/c/s/node schemes; tensions.md's published order is canonical; casebook and
  capstone agents receive the id list in their prompt; validate.py checks cross-refs.
- **Book files outrank synthesis.** learning-design.md was drafted before the breakdowns landed
  and carried ten factual errors (an invented example, inflated figures, a misattributed number).
  Rule: every synthesis agent reads the book files, cites slugs, and appends a reconciliation log
  naming each departure; the claims ledger (Phase 3) is a gate, not an afterthought.
- **Every number lives in the ledger.** Rule: a synthesis file may quote a figure only if the
  ledger's key-numbers table has it with status and caveat; otherwise use words.

## Process
- **Commit and push after every agent hand-back.** Long runs lose work otherwise. Rule: the
  orchestrator commits with a one-line message per agent; a stop hook does the same; never batch
  three agents' output into one commit.
- **Agents run in parallel per source.** Breakdowns are independent; launch all Phase 2 agents
  at once (default model). Phase 4's five synthesis agents also run in parallel after
  learning-design.md lands.
- **Fable for planning and synthesis; default model for breakdowns and data.** Discovery, SPEC,
  ledger, learning-design and the QA cold-learner use Fable; per-source breakdowns and JSON
  expansion do not need it.
- **Hand-backs report the least-certain items.** Every agent ends with "three claims I am least
  sure of"; the README names them under "Honesty notes".

## Verification
- **Assume WebFetch may be blocked by the proxy.** Rule: verify via search snippets (publisher,
  retailer, library, review pages); retry a fetch at most once; label every TOC "verified /
  partially verified / reconstructed"; mark each chapter row (v) or (bk + confidence); mark each
  number "verified" or "background".
- **Flag claims that outrun the evidence.** Run 1 corrections: curiosity's memory boost is for
  the target, not incidental material; productive failure shows no procedural advantage
  (g ≈ -0.03); 1998 formative-assessment effect sizes are far above later estimates;
  reconsolidation is contested in humans. Rule: breakdown prompts require an "arguing vs.
  showing" line; the ledger's corrections list is pasted into every downstream prompt.
- **Never fabricate.** No invented studies, numbers, chapter titles or examples. When memory
  supplies a figure, write "about" and mark it background; when an example is hypothetical,
  say so in the text.

## Learning design
- **Cold challenge first.** m0 = diagnostic + one-page attempt at the goal before any content;
  it becomes artifact v0 and the capstone's delta baseline. Skip an attempt only where the
  learner has no priors to activate.
- **Hinge distractors each diagnose a misconception.** A distractor whose diagnosis is
  "incorrect" is invalid; diagnoses come from "Common misreadings", the ledger corrections, or
  the diagnostic's folk theories. Wrong answers route to a specific book-file section.
- **Diagnostic captures confidence.** 16 true/false items with confidence 1-5, retaken on day
  21; report accuracy and calibration deltas; the capstone's criterion 10 reads them.
- **Hooks sit on the target.** An exciting unrelated opener is extraneous load, not a primer.
- **Design the median case.** Every deliverable asks what the ordinary Tuesday looks like, not
  the showcase.

## Cards and app
- **Cards unlock on module completion; ~15 atomic cards per module; cap 20 new per day.**
  Run 1 shipped 212 cards for 10 modules (19-24 each); that is the upper bound. Four types
  (recall / explain / apply / discriminate); introduced the day after the module; reviewed at
  1, 3, 7, 14 days; interleaved across ≥3 modules per session.
- **All domain strings come from course.json.** No "school", "founder", "design brief" or level
  names in template.html; validate.py errors on a manifest string copied from another run.
- **Playwright uses `executablePath: /opt/pw-browsers/chromium`.** Do not run `playwright
  install` (no network for browser downloads). smoke.js checks: every view renders, hinge
  diagnosis appears, card grading works, artifact entry saves, case reveal, model panel, 390 px
  width without horizontal overflow.
- **Split large JSON.** modules.json over ~300 KB was split into modules-a/-b; build.py merges
  and sorts by id. Keep the built page under 16 MB; run 1 was ~600 KB.
- **Publish private with `db`, `user`, `sample` capabilities** so mentor feedback and progress
  work on claude.ai; state in the app when mentor feedback is unavailable.

## QA
- **Fact spot-check:** sample 30 claims across files, search-verify, target ≥90% confirmed;
  every miss becomes a ledger correction and a file edit.
- **Cold-learner check:** an agent takes the diagnostic and m0 cold, reads m1-m3, retakes; the
  questions must discriminate and the sequence must show a gain, or the modules are rewritten.

## Added after run 2 (games-and-norms), from the cold-learner QA
- **Hinge questions were guessable without reading**: the correct option was the longest in 46/48
  questions and sat at index 1 in 30/48; distractors were one-line slogans while the correct option
  carried a mechanism clause. Run 1 had the same flaw (49/53, 35/53). Rule: all four options in the
  same register and within ~25% of each other's length; correct positions shuffled roughly evenly;
  no option is the only one with a "because" clause. `validate.py` now fails on either pattern.
- **Diagnostic items had tells**: false items were short absolutes ("always", "solves", "on its
  own"); true items were long, hedged, course-voice. Rule: write both as scenario statements of
  similar length; put some absolutes in true items and some hedges in false ones. `validate.py` warns.
- **Hinges and cases lifted verbatim from the module's own ideas/worked example** test recall, not
  transfer. Rule: change the surface (numbers, setting, actors) between idea, hinge and case; key at
  least a third of cases to a module other than the one that teaches the idea.
- **A hinge's answer must be derivable from the module text**: if the diagnosis cites a study the
  ideas never mention, add it to the ideas or drop the question.
- **QA agents must not see answer keys**: print statements only (`python3 -c` filtering to id +
  statement) before answering; the run-2 agent accidentally printed diagnoses alongside m1/m2 hinges.

## Added after publishing (2026-10)
- **Internal ids leaked into learner text**: tension ids (t14), case ids (k03), brief sections (s4),
  module ids (m8), claims-ledger refs ("ledger C37", "rule 2") and book file ids (`07`) showed up in
  lessons, quizzes and cases, and readers could not decode them. Rule: ids are for the files and the
  data contract only. Learner-visible strings name things: the tension's name, the case title,
  "Module 8", the author and chapter. The ledger is not shipped, so never cite it in learner text.
  `validate.py` now fails on any of these patterns in learner-facing fields.
