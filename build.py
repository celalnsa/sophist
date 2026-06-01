#!/usr/bin/env python3
"""Sophist static site generator.

Reads every Markdown file in ``content/`` (each one a philosophy discussion
carrying YAML frontmatter), renders it through the shared templates, and emits
a fully static site into ``_site/``. Adding a page = drop a ``.md`` in content/
and rebuild; theme consistency is automatic because every page extends the same
base template and links the same theme.css.

Frontmatter schema (all optional except title):
    title, source_ai, date_discussed, themes[], thinkers[], abstract,
    status (settled|open)

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


def slugify(name: str) -> str:
    s = re.sub(r"[^\w一-鿿-]+", "-", name.strip().lower())
    return re.sub(r"-+", "-", s).strip("-") or "untitled"


def load_entries() -> list[dict]:
    entries: list[dict] = []
    for path in sorted(CONTENT.glob("*.md")):
        if path.name.startswith("_"):
            continue  # _example.md etc. are templates, not published
        post = frontmatter.load(path)
        meta = post.metadata
        slug = slugify(meta.get("slug") or path.stem)
        MD.reset()
        themes = meta.get("themes") or []
        status = (meta.get("status") or "").strip().lower()
        if status not in ("settled", "open"):
            status = ""
        entries.append({
            "slug": slug,
            "url": f"{slug}.html",
            "title": meta.get("title") or path.stem,
            "source_ai": meta.get("source_ai") or "",
            "date_discussed": str(meta.get("date_discussed") or ""),
            "themes": [str(t) for t in themes],
            "thinkers": [str(t) for t in (meta.get("thinkers") or [])],
            "abstract": meta.get("abstract") or "",
            "status": status,
            "body_html": MD.convert(post.content),
            "mtime": path.stat().st_mtime,
        })
    # newest first by date string, then by file mtime as tiebreaker
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
        html = page_tpl.render(e=e, body_html=e["body_html"], rel="")
        (OUT / e["url"]).write_text(html, encoding="utf-8")

    index_html = env.get_template("index.html").render(
        entries=entries, all_themes=all_themes, rel="")
    (OUT / "index.html").write_text(index_html, encoding="utf-8")

    # .nojekyll so GitHub Pages serves our files verbatim
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"✓ built {len(entries)} discussion(s) + index → {OUT.relative_to(ROOT)}/")
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
