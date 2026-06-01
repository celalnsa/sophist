# AGENTS.md

Guidance for agents (and humans) working in this repository. This file is the
**single source of truth**. `CLAUDE.md` only points here; `.claude/skills` is a
symlink to `.agents/skills`. We follow the broad, cross-tool standard
(`AGENTS.md` + `.agents/`) deliberately — don't fork instructions into
tool-specific files.

## What this is

**Sophist** (思辨对话录) is a themed static archive of philosophy / 思辨
discussions the user has held with various AIs (ChatGPT, Claude, Gemini, …),
collected into one browseable site. Each discussion is one Markdown file; the
generator turns the whole `content/` folder into a cohesive site.

The cardinal rule: **adding a discussion must stay effortless and on-theme.**
Never hand-author page HTML or per-page CSS. All visual consistency lives in
`theme/theme.css` and `templates/`. A new page is just content.

## Layout

```
content/        one .md per discussion (the only thing you usually touch)
                files starting with "_" are templates, not published (_example.md)
templates/      base.html · index.html (目录) · discussion.html — Jinja2
theme/theme.css the design system: palette, type, components. Edit once → all pages follow.
build.py        the generator: content/*.md → _site/
_site/          build output (git-ignored; produced by build.py / CI)
.github/workflows/deploy.yml   builds on push and deploys to GitHub Pages
```

## Adding a discussion (the common task)

1. Copy `content/_example.md` to `content/<slug>.md` (slug = url, e.g. `free-will.md`).
2. Fill the frontmatter. Schema (only `title` is required):

   ```yaml
   ---
   title: 标题
   source_ai: ChatGPT        # which AI it came from
   date_discussed: 2026-01-01 # or "unknown"
   themes: [自由意志, 决定论]   # drives index filtering + aggregation
   thinkers: [康德, 萨特]       # philosophers referenced; [] if none
   abstract: 一两句话概括。
   status: open               # settled | open
   ---
   ```
3. Write the body in plain Markdown. The export prompt's section headings
   (缘起/核心问题, 关键概念, 论证脉络, 高光片段, 暂时的结论, 悬而未决, 延伸)
   render as styled `##` headers; use `>` blockquotes for 高光片段.
4. Build & preview locally: `uv run python build.py --serve` → http://localhost:8000
5. Commit and push. CI rebuilds and deploys automatically.

That's it — no HTML, no CSS. The page inherits the theme.

## Changing the look

Edit `theme/theme.css` (palette/type are CSS variables at the top) and/or the
`templates/`. Every page re-renders from these, so one edit restyles the whole
archive. Keep the temperament: dark, classical serif (Fraunces/Newsreader),
single warm-brass accent, restrained — a 哲思 feel. See `.agents/skills/add-discussion`.

## Build & deploy

- Local: `uv run python build.py` (output in `_site/`), add `--serve` to preview.
- Deps: `markdown`, `python-frontmatter`, `jinja2` (see `pyproject.toml`).
- CI: pushing to `main` triggers `.github/workflows/deploy.yml`, which builds and
  publishes `_site/` to GitHub Pages. Pages source = GitHub Actions.

## Conventions

- Content language is the user's — Chinese by default; keep English for code,
  identifiers, quoted English sources.
- Be faithful to the source discussion; don't invent positions. If a piece adds
  outside background, it should say so (the export prompt enforces «（补充背景）»).
- `_`-prefixed files in `content/` are never published.
