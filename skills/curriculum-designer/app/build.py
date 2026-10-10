#!/usr/bin/env python3
"""Build a course app: inline <course>/app/data/*.json + course.json into template.html.

Usage: build.py <course-dir> [--template PATH] [--out PATH] [--standalone] [--mentor-endpoint URL]
Writes <course-dir>/app/<slug>.html by default (artifact form: no document skeleton, claude.ai adds it).
--standalone wraps the page in a full HTML document for hosting anywhere (progress stays in the
browser's localStorage; mentor feedback needs --mentor-endpoint pointing at scripts/mentor-proxy.mjs
or your own server).
"""
import argparse
import html
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def load(data_dir, name, key):
    path = data_dir / name
    if not path.exists():
        print(f"  missing {name}", file=sys.stderr)
        return []
    return json.loads(path.read_text())[key]


def build(course_dir: Path, template: Path, out: Path | None, standalone: bool = False, mentor_endpoint: str | None = None) -> Path:
    course = json.loads((course_dir / "course.json").read_text())
    if mentor_endpoint:
        course["mentor_endpoint"] = mentor_endpoint
    data = course_dir / "app" / "data"
    modules = []
    for f in sorted(data.glob("modules*.json")):
        modules += json.loads(f.read_text())["modules"]
    modules.sort(key=lambda m: int(str(m["id"]).lstrip("m")))
    for m in modules:
        m.setdefault("num", int(str(m["id"]).lstrip("m")))
    model_path = data / "model.json"
    bundle = {
        "course": course,
        "modules": modules,
        "cards": load(data, "flashcards.json", "cards"),
        "cases": load(data, "cases.json", "cases"),
        "tensions": load(data, "tensions.json", "tensions"),
        "brief": load(data, "brief.json", "sections"),
        "diagnostic": load(data, "diagnostic.json", "items"),
        "model": json.loads(model_path.read_text()) if model_path.exists() else {"bands": []},
    }
    payload = json.dumps(bundle, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = (template.read_text()
            .replace("{{TITLE}}", html.escape(course.get("title", "Course")))
            .replace("{{DESCRIPTION}}", html.escape(course.get("description", "")))
            .replace("/*__DATA__*/", payload))
    if standalone:
        # The artifact form starts with <title>/<meta>/<link>/<style>; move that head part into <head>.
        cut = page.index('<div class="mtop"')
        page = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
                + page[:cut] + "</head>\n<body>\n" + page[cut:] + "\n</body>\n</html>\n")
    out = out or course_dir / "app" / (f"{course.get('slug', 'course')}{'-standalone' if standalone else ''}.html")
    out.write_text(page)
    counts = ", ".join(f"{k}={len(v) if isinstance(v, list) else len(v.get('bands', []))}"
                       for k, v in bundle.items() if k != "course")
    print(f"wrote {out} ({len(page) // 1024} KB): {counts}")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("course_dir", type=Path)
    ap.add_argument("--template", type=Path, default=HERE / "template.html")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--standalone", action="store_true")
    ap.add_argument("--mentor-endpoint")
    a = ap.parse_args()
    build(a.course_dir.resolve(), a.template, a.out, a.standalone, a.mentor_endpoint)
