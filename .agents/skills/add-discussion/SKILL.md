---
name: add-discussion
description: Use when adding a new philosophy discussion page to the Sophist archive, changing the site theme, or building/previewing/deploying the site. Covers the content Markdown schema, the build step, and how theme consistency is guaranteed.
---

# Adding a discussion to Sophist

Sophist is a static archive: each philosophy discussion is one Markdown file in
`content/`, and `build.py` renders the whole folder into a themed site. The
whole point is that **a new page requires no HTML/CSS** — it inherits the theme.

## Add one discussion

1. `cp content/_example.md content/<slug>.md` — the slug becomes the URL
   (`<slug>.html`). Use a short kebab-case name, e.g. `free-will.md`.
   (Files whose names start with `_` are treated as templates and never published.)
2. Fill the frontmatter — only `title` is strictly required:

   | field | meaning |
   |---|---|
   | `title` | discussion title |
   | `source_ai` | which AI it came from (ChatGPT / Claude / Gemini / …) |
   | `date_discussed` | approx date, or `unknown` |
   | `themes` | list — powers index filter chips and aggregation |
   | `thinkers` | list of philosophers/schools referenced (`[]` if none) |
   | `abstract` | one or two sentences |
   | `status` | `settled` or `open` (renders as 已结 / 未决 pill) |

3. Write the body as plain Markdown. Recommended section headings (they render
   as styled uppercase `##` kickers): 缘起 / 核心问题, 关键概念, 论证脉络,
   高光片段, 暂时的结论, 悬而未决, 延伸. Use `>` blockquotes for highlight quotes.
4. Preview: `uv run python build.py --serve` → open http://localhost:8000
5. Commit + push to `main`. The GitHub Action rebuilds and redeploys to Pages.

These files pair with the user's **export prompt** (run inside other AIs) which
already emits exactly this frontmatter + section structure — paste its output
straight into a new `content/*.md`.

## Build commands

- `uv run python build.py` — build into `_site/`
- `uv run python build.py --serve` — build, then serve `_site/` on :8000
- Dependencies are declared in `pyproject.toml` (`markdown`, `python-frontmatter`, `jinja2`).

## Changing the theme (keep all pages consistent)

Do **not** add per-page styles. Edit:

- `theme/theme.css` — palette + typography are CSS variables at the top
  (`--ink`, `--paper`, `--brass`, `--display`, `--body`…). Change once, the
  whole archive follows.
- `templates/base.html` — masthead/footer/`<head>` shared by every page.
- `templates/index.html` — the 目录 (landing) page + theme filter chips.
- `templates/discussion.html` — the per-discussion layout + `.prose` styling
  for rendered Markdown.

Keep the temperament: dark background, classical serif display (Fraunces) +
literary body (Newsreader), one warm-brass accent, generous space, restrained
motion — an intellectual / 哲思 feel.
