#!/usr/bin/env python3
"""Validate a course's app/data/*.json + course.json against the data contract.

Usage: validate.py <course-dir>   (exit 1 on any error)
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

errors, warns = [], []
err = errors.append
warn = warns.append


def load(path, key=None):
    if not path.exists():
        err(f"missing file {path.name}")
        return []
    try:
        d = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        err(f"{path.name}: invalid JSON: {e}")
        return []
    return d[key] if key else d


def need(obj, fields, where):
    for f in fields:
        if f not in obj or obj[f] in ("", None, []):
            err(f"{where}: missing '{f}'")


def main(course_dir: Path):
    data = course_dir / "app" / "data"
    course = load(course_dir / "course.json")
    need(course, ["slug", "title", "tagline", "lede", "levels", "artifact_name", "case_noun", "mentor_voice"], "course.json")

    modules = []
    for f in sorted(data.glob("modules*.json")):
        modules += load(f, "modules")
    cards = load(data / "flashcards.json", "cards")
    cases = load(data / "cases.json", "cases")
    tensions = load(data / "tensions.json", "tensions")
    brief = load(data / "brief.json", "sections")
    diag = load(data / "diagnostic.json", "items")
    model = load(data / "model.json")

    # --- modules
    mids = [m.get("id") for m in modules]
    if not mids:
        err("no modules")
    for i, m in enumerate(sorted(modules, key=lambda m: int(str(m.get("id", "m0")).lstrip("m") or 0))):
        if m.get("id") != f"m{i}":
            err(f"module ids must be contiguous m0..mN; found {m.get('id')} at position {i}")
    for m in modules:
        w = f"module {m.get('id')}"
        need(m, ["id", "title", "level", "minutes", "hook", "objectives", "ideas"], w)
        if m.get("level") not in set(course.get("levels", [])) | {"Start", "Integration"}:
            warn(f"{w}: level '{m.get('level')}' not in course.levels")
        if m.get("id") != "m0" and not m.get("attempt", {}).get("prompt"):
            err(f"{w}: no cold attempt prompt (productive-failure opener)")
        for j, h in enumerate(m.get("hinge", [])):
            hw = f"{w} hinge {j+1}"
            need(h, ["q", "options", "diagnoses"], hw)
            opts, diags = h.get("options", []), h.get("diagnoses", [])
            if len(opts) < 3:
                err(f"{hw}: fewer than 3 options")
            if len(diags) != len(opts):
                err(f"{hw}: {len(diags)} diagnoses for {len(opts)} options (need one per option)")
            if not isinstance(h.get("answer"), int) or not (0 <= h.get("answer", -1) < len(opts)):
                err(f"{hw}: answer index out of range")
            if any(len(d.strip()) < 20 for d in diags):
                warn(f"{hw}: a diagnosis is under 20 chars; each distractor should diagnose a misconception")
        if m.get("id") != "m0" and len(m.get("hinge", [])) < 2:
            warn(f"{w}: fewer than 2 hinge questions")
        for idea in m.get("ideas", []):
            if idea.get("tag") not in (None, "E", "H", "V"):
                err(f"{w}: idea tag '{idea.get('tag')}' not E/H/V")
            if len(idea.get("body", "").split()) < 120:
                warn(f"{w}: idea '{idea.get('title','')[:40]}' body under 120 words")

    # --- guessability (found by the cold-learner QA in run 2): correct option must not be
    # identifiable by position or length, and diagnostic items must not carry absolute-word tells.
    longest_hits, total_h, pos = 0, 0, Counter()
    for m in modules:
        for h in m.get("hinge", []):
            opts = h.get("options", [])
            a = h.get("answer")
            if not opts or not isinstance(a, int) or not (0 <= a < len(opts)):
                continue
            total_h += 1
            pos[a] += 1
            if len(opts[a]) == max(len(o) for o in opts):
                longest_hits += 1
    if total_h:
        if longest_hits / total_h > 0.5:
            err(f"hinge guessability: longest option is the correct one in {longest_hits}/{total_h} questions (max 50%); equalise option length")
        top = pos.most_common(1)[0]
        if total_h >= 8 and top[1] / total_h > 0.45:
            err(f"hinge guessability: answer index {top[0]} is correct in {top[1]}/{total_h} questions; shuffle positions")
    tells = re.compile(r"\b(always|never|solves|mainly|whatever|on its own|guarantees|all|only|nothing)\b", re.I)
    false_tells = [d.get("id") for d in diag if d.get("correct") is False and tells.search(d.get("statement", ""))]
    if diag and len(false_tells) > len(diag) / 4:
        warn(f"diagnostic tells: {len(false_tells)} false items use absolute words ({', '.join(false_tells)}); rewrite as scenario statements")
    if diag:
        t_len = [len(d["statement"]) for d in diag if d.get("correct") is True]
        f_len = [len(d["statement"]) for d in diag if d.get("correct") is False]
        if t_len and f_len and sum(t_len) / len(t_len) > 1.5 * sum(f_len) / len(f_len):
            warn("diagnostic tells: true statements are much longer than false ones on average; balance lengths")

    # --- cards
    cid = Counter(c.get("id") for c in cards)
    for k, n in cid.items():
        if n > 1:
            err(f"duplicate card id {k}")
    for c in cards:
        need(c, ["id", "module", "front", "back"], f"card {c.get('id')}")
        if c.get("module") not in mids:
            err(f"card {c.get('id')} references unknown module {c.get('module')}")
        if c.get("type") not in (None, "recall", "explain", "apply", "discriminate"):
            warn(f"card {c.get('id')}: unknown type {c.get('type')}")
    per_mod = Counter(c.get("module") for c in cards)
    for mid in mids:
        if mid != "m0" and per_mod.get(mid, 0) < 8:
            warn(f"module {mid} has only {per_mod.get(mid, 0)} cards (aim ~15)")

    # --- tensions / cases
    tids = [t.get("id") for t in tensions]
    for i, t in enumerate(tensions):
        if t.get("id") != f"t{i+1:02d}":
            err(f"tension ids must be t01..tNN in order; found {t.get('id')} at {i}")
        need(t, ["id", "name", "pole_a", "pole_b", "rule", "switch_signal", "evidence"], f"tension {t.get('id')}")
        if not re.search(r"\bIF\b", t.get("rule", ""), re.I):
            warn(f"tension {t.get('id')}: rule is not an IF/THEN rule")
    for i, k in enumerate(cases):
        if k.get("id") != f"k{i+1:02d}":
            err(f"case ids must be k01..kNN in order; found {k.get('id')} at {i}")
        need(k, ["id", "title", "scenario", "question", "considerations", "model_answer"], f"case {k.get('id')}")
        if k.get("tension") and k.get("tension") not in tids:
            err(f"case {k.get('id')} references unknown tension {k.get('tension')}")
        if k.get("module") and k.get("module") not in mids:
            err(f"case {k.get('id')} references unknown module {k.get('module')}")

    # --- diagnostic / brief / model
    for i, d in enumerate(diag):
        if d.get("id") != f"d{i+1}":
            err(f"diagnostic ids must be d1..dN in order; found {d.get('id')} at {i}")
        need(d, ["id", "statement", "explanation", "module"], f"diag {d.get('id')}")
        if not isinstance(d.get("correct"), bool):
            err(f"diag {d.get('id')}: 'correct' must be boolean")
        if d.get("module") not in mids:
            err(f"diag {d.get('id')} references unknown module {d.get('module')}")
    if diag and len(diag) < 12:
        warn(f"only {len(diag)} diagnostic items (aim 16)")
    for i, s in enumerate(brief):
        if s.get("id") != f"s{i+1}":
            err(f"brief section ids must be s1..sN in order; found {s.get('id')} at {i}")
        need(s, ["id", "title", "guidance", "prompts"], f"brief {s.get('id')}")
    node_ids = set()
    for b in model.get("bands", []) if isinstance(model, dict) else []:
        need(b, ["id", "title", "nodes"], f"band {b.get('id')}")
        for n in b.get("nodes", []):
            need(n, ["id", "label", "summary"], f"node {n.get('id')}")
            node_ids.add(n.get("id"))
    for b in model.get("bands", []) if isinstance(model, dict) else []:
        for n in b.get("nodes", []):
            for l in n.get("links", []):
                if l not in node_ids:
                    err(f"node {n.get('id')} links to unknown node {l}")
    if isinstance(model, dict) and not model.get("bands"):
        err("model.json has no bands")

    # Learner-visible text must never show internal ids or ledger references (see lessons.md).
    CODE = re.compile(r"`(?:\d{2}(?:-[a-z0-9-]+)?|primer|unified-model|claims-ledger|tensions|casebook|learning-design|four-layers)[^`\n]{0,20}`|\b[tkmdcs]\d{1,3}\b|\b(?:ledger|rule)\s+[A-Z]?\d+|\b[CX]\d{1,3}\b|§\s?\d+")
    SKIP = {"id", "ids", "module", "modules", "tension", "tensions_ref", "source", "sources", "deeper", "links",
            "tag", "default_tag", "type", "answer", "correct", "level", "slug", "repo_path"}
    def scan(obj, where):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k not in SKIP:
                    scan(v, f"{where}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                scan(v, f"{where}[{i}]")
        elif isinstance(obj, str):
            for m in CODE.finditer(obj):
                err(f"{where}: internal id in learner text: {m.group(0)!r} (use a name instead)")
    for name, obj in [("modules", modules), ("cards", cards), ("cases", cases), ("tensions", tensions),
                      ("diagnostic", diag), ("brief", brief), ("model", model)]:
        scan(obj, name)

    for w in warns:
        print("warn:", w)
    for e in errors:
        print("ERROR:", e)
    print(f"\n{len(modules)} modules, {len(cards)} cards, {len(cases)} cases, {len(tensions)} tensions, "
          f"{len(diag)} diagnostic items, {len(brief)} brief sections, {len(node_ids)} model nodes")
    print(f"{len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main(Path(sys.argv[1]).resolve())
