# Tensions — where the sources disagree and how to decide

Phase 4, parallel agent. Output: `synthesis/tensions.md` (+ `app/data/tensions.json`).
**This file's order is canonical for `tNN`.** The casebook, capstone and cards cite these ids;
never renumber after publishing. Needs the critic/contrarian source from discovery. ~6,000 words
for 12-14 tensions.

---

## (a) File structure

```markdown
# The tensions: where the authors disagree, what the evidence says, and how to decide
Intro: debates are settled by conditions, not winners (for whom, for what goal, at what point,
at what cost). Both poles steelmanned from the book files. Tags per SPEC. Book files win.
Numbered list of all tensions (this list = tNN order).

## T1. <Pole A> vs <Pole B>
**Pole A: <stance>.** Authors + slugs; the strongest version of the argument; the key study.
**Pole B: <stance>.** Same.
**What the evidence says.** 1-2 paragraphs: where they actually agree; the narrow real
disagreement; the conditions under which each wins; effect sizes from the ledger with caveats;
who ran the studies. Ends with the tag mix "[E for ..., H for ..., V for ...]".
**Rule.** IF <conditions> THEN <A-leaning action>. IF <conditions> THEN <B-leaning action>.
IF <edge case> THEN <lighter form>. Never <the failure mode>.
**Switch signal.** The specific observations or numbers that should make you reverse; and the
opposite signal that argues for the other pole.
**Common mistake.** The error made most often, and its mirror.

## How to use this file
Before a contested decision: find the tension, state the lean, apply the rule, write the switch
signal into the {{ARTIFACT_NAME}} next to the decision as its [H] test. A decision that fits no
tension is a pure [V] (name the dissenter) or a pure [E] (cite the mechanism); if neither, it is
not yet a decision.
```

---

## (b) Agent prompt

```
Read SPEC.md, synthesis/claims-ledger.md (sections 1, 2, 5 binding), synthesis/learning-design.md
section 4b (seed list), and every books/*.md ("Evidence strength", "Connections", "Common
misreadings", "Implications"). Write synthesis/tensions.md per references/tensions.md (a).
- 12-14 tensions. Start from the ledger's contradictions and the seed list; merge duplicates;
  add any disagreement two book files name in "Connections" that the seed list missed.
- Each tension: both poles steelmanned with slugs; evidence paragraph that names where they
  agree and the narrow real disagreement; a conditional IF/THEN rule (≥2 branches); a switch
  signal (specific, observable, both directions); a common mistake (and its mirror).
- Numbers only from the ledger section 4, with caveats. Note who ran the studies.
- The order you publish is canonical: fix it, then write app/data/tensions.json per
  references/data-spec.md (id, name, pole_a, pole_b, rule, switch_signal, evidence, sources).
- Include at least: one tension from the critic source; one that is "mostly a false tension once
  X is read properly"; one about measurement/accountability; one about the learner's own values.
- Append a reconciliation log (departures from the seed list, with citations).
- Report back: the final ordered list with ids (the casebook agent needs it), and any tension
  where the book files did not give you enough to write the evidence paragraph.
```

---

## (c) Quality bar

- [ ] 12-14 tensions; ids t01.. match the intro list and tensions.json exactly.
- [ ] Both poles cite slugs and a named author; neither is a straw man.
- [ ] Evidence paragraph states the agreement, the real disagreement, and the conditions.
- [ ] Rule has ≥2 IF/THEN branches and a "never" line.
- [ ] Switch signal is observable (a count, an observation, a delayed measure), in both directions.
- [ ] Common mistake includes the mirror error.
- [ ] Every number is in the ledger; every tag mix stated.
- [ ] "How to use this file" present; reconciliation log present.
