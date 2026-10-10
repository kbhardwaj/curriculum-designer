# Unified model — nodes by band, causal chain, laws, certainty

Phase 4, parallel agent. Output: `synthesis/unified-model.md` (+ feeds `app/data/model.json`).
The one page the learner rereads before any big decision. ~4,000-5,000 words.

---

## (a) File structure

```markdown
# The unified model: {{LEVEL_1}}, {{LEVEL_2}}, {{LEVEL_3}}, and the loop that connects them
Intro: what it compresses (N sources → ~30 nodes in {{N}} bands + links + {{N}} laws); tags per
SPEC; "certainty is high at the bottom and thin at the top"; book files' evidence sections are
the authority for any single-source claim.

## 1. The core causal chain in plain words
10-12 numbered sentences. Bottom-level mechanisms first ("A learner can only..."), then
"Therefore {{practice}}...", then "None of this happens reliably by itself, so {{system}}...".
Each sentence must be defensible from a book file.

## 2. The nodes
### Band 1: {{LEVEL_1}} ({{what it covers}})
**M1. <Label as a claim.>** [tag] `slug`, `slug`
2-3 sentences: the mechanism, the key study, why it matters for the bands above.
(9-11 nodes per band; ids M1.., D1.., I1.. — letters fixed in SPEC.)
### Band 2: {{LEVEL_2}}
### Band 3: {{LEVEL_3}}

## 3. The key links: why a {{band-1}} fact implies a {{band-2}} rule implies a {{band-3}} structure
8-12 bullets of the form **M1 + M2 → D1 → I3, I4.** "Because A, then B, so the system must C,
because D."

## 4. The improvement loop
One paragraph: how the system learns (aim → theory → small test with prediction → practical
measure → study → revise); the two ways the loop breaks. Same loop at three scales.

## 5. Where certainty degrades
Table: Band | What is solid | What is thin | Honest tag mix. Two rules follow: a higher-band claim
is never more certain than the mechanism it rests on; the right response to uncertainty changes by
band (adopt / adopt and tune / commit as [V] or test as [H]).

## 6. The {{N}} laws of this {{ARTIFACT_SUBJECT}}
10-12 numbered, bolded one-liners + one sentence each. Each law traces to nodes; each is
phrased so a violation is observable.

## 7. Diagram
Mermaid `flowchart BT`, one subgraph per band, nodes labeled "M1 Short label [E]", upward
edges "constrains", downward "enables", a loop edge on the right.

## 8. One worked path through the model
A single top-level policy traced down through the bands to mechanism and back up through the loop,
naming the practical measure, prediction and balancing measure.
```

---

## (b) Agent prompt

```
Read SPEC.md, synthesis/claims-ledger.md (section 5 binding), synthesis/learning-design.md
(section 4a is the seed; module ids fixed), and every books/*.md ("5-10 ideas", "Mental models",
"Evidence strength", "Implications", "Connections"). Write synthesis/unified-model.md per
references/unified-model.md (a).
- {{N}} bands = the SPEC levels, in order. 9-11 nodes per band, ids {{M/D/I}}N, each with tag,
  slugs, 2-3 sentences. A node is a claim, not a topic.
- Every node's tag must match the book files' evidence sections and the ledger; contested items
  get the caveat in the node text.
- Links section: each bullet names node ids and reads "because / then / so / because".
- Certainty table must be honest: band 3 is [H]/[V]-heavy in most domains; say what is thin.
- Laws: 10-12, observable, each traceable to nodes; no law that is only a value without saying so.
- Mermaid diagram must parse (no special characters in ids; labels in quotes with <br/>).
- Also output app/data/model.json per references/data-spec.md: bands[].nodes[] with id, label,
  summary, tag, links (node ids), sources; plus chain[], laws[], loop.
- Append a reconciliation log: any place you departed from learning-design 4a, and why (book
  file or ledger citation).
- Report back: node count per band, tag distribution per band, the three nodes with the thinnest
  evidence.
```

---

## (c) Quality bar

- [ ] Node count 27-33; ids fixed; every node has tag + ≥1 slug.
- [ ] Causal chain reads bottom-up and each "therefore" is licensed by a node.
- [ ] Links use node ids and the because/then/so form; ≥8 links, ≥1 crossing all bands.
- [ ] Certainty table names specific thin items per band, not generic "more research needed".
- [ ] Laws are observable (a visitor could check for a violation).
- [ ] Mermaid renders; diagram matches node list.
- [ ] Worked path names a practical measure, a prediction and a balancing measure.
- [ ] model.json validates (ids unique, links resolve, laws present); reconciliation log present.
