#!/usr/bin/env python3
"""Sophist static site generator.

Each discussion lives in ``content/`` and may take **either** form:

* ``<slug>.md``  — Markdown + YAML frontmatter. Rendered through the shared
  ``discussion.html`` template. The body is free-form prose; it is NOT forced
  into any fixed section structure — write whatever shape the thought wants.

* ``<slug>.html`` — a hand-authored, fully bespoke page (its own layout, its
  own CSS, its own interactions). The generator copies it verbatim and only
  reads a leading metadata comment for the index card:

      <!--sophist
      title: ...
      themes: [...]
      ...
      -->
      <!DOCTYPE html> ... your page ...

Files whose names start with ``_`` are templates and are never published.

Usage:
    uv run python build.py            # build into _site/
    uv run python build.py --serve    # build, then serve locally on :8000
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

import frontmatter
import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
TEMPLATES = ROOT / "templates"
THEME = ROOT / "theme"
OUT = ROOT / "_site"

MD = markdown.Markdown(
    extensions=["extra", "sane_lists", "smarty", "attr_list"],
    output_format="html5",
)

HTML_META_RE = re.compile(r"^\s*<!--sophist\s*(.*?)-->\s*", re.DOTALL)


def slugify(name: str) -> str:
    s = re.sub(r"[^\w一-鿿-]+", "-", name.strip().lower())
    return re.sub(r"-+", "-", s).strip("-") or "untitled"


def normalize(meta: dict, path: Path, *, layout: str) -> dict:
    status = str(meta.get("status") or "").strip().lower()
    if status not in ("settled", "open"):
        status = ""
    slug = slugify(meta.get("slug") or path.stem)
    return {
        "slug": slug,
        "url": f"{slug}.html",
        "title": meta.get("title") or path.stem,
        "source_ai": meta.get("source_ai") or "",
        "date_discussed": str(meta.get("date_discussed") or ""),
        "themes": [str(t) for t in (meta.get("themes") or [])],
        "thinkers": [str(t) for t in (meta.get("thinkers") or [])],
        "abstract": meta.get("abstract") or "",
        "status": status,
        "layout": layout,
        "mtime": path.stat().st_mtime,
    }


def load_entries() -> list[dict]:
    entries: list[dict] = []
    paths = sorted(list(CONTENT.glob("*.md")) + list(CONTENT.glob("*.html")))
    for path in paths:
        if path.name.startswith("_"):
            continue
        if path.suffix == ".md":
            post = frontmatter.load(path)
            MD.reset()
            e = normalize(post.metadata, path, layout="markdown")
            e["body_html"] = MD.convert(post.content)
        else:  # bespoke .html
            text = path.read_text(encoding="utf-8")
            m = HTML_META_RE.match(text)
            meta = yaml.safe_load(m.group(1)) if m else {}
            e = normalize(meta or {}, path, layout="custom")
            e["raw_html"] = text[m.end():] if m else text
        entries.append(e)
    entries.sort(key=lambda e: (e["date_discussed"], e["mtime"]), reverse=True)
    return entries


def build() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    shutil.copytree(THEME, OUT / "theme")

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html"]),
    )
    entries = load_entries()
    all_themes = sorted({t for e in entries for t in e["themes"]})

    page_tpl = env.get_template("discussion.html")
    for e in entries:
        if e["layout"] == "custom":
            (OUT / e["url"]).write_text(e["raw_html"], encoding="utf-8")
        else:
            html = page_tpl.render(e=e, body_html=e["body_html"], rel="")
            (OUT / e["url"]).write_text(html, encoding="utf-8")

    index_html = env.get_template("index.html").render(
        entries=entries, all_themes=all_themes, rel="")
    (OUT / "index.html").write_text(index_html, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    n_custom = sum(1 for e in entries if e["layout"] == "custom")
    print(f"✓ built {len(entries)} discussion(s) ({n_custom} bespoke) + index → {OUT.relative_to(ROOT)}/")
    print(f"  themes: {', '.join(all_themes) or '(none yet)'}")
    return len(entries)


def serve() -> None:
    import functools
    import http.server
    import socketserver

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
    with socketserver.TCPServer(("", 8000), handler) as httpd:
        print("serving _site/ at http://localhost:8000  (Ctrl-C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true", help="serve _site/ locally after building")
    args = ap.parse_args()
    build()
    if args.serve:
        serve()
    sys.exit(0)
