# Sophist · 思辨对话录

A themed static archive of philosophy / 思辨 discussions held with various AIs,
collected into one browseable site. Each discussion is a single Markdown file;
a small generator renders the whole collection with a consistent look.

- **Add a discussion:** drop a `content/<slug>.md` (see `content/_example.md`), push.
- **Preview locally:** `uv run python build.py --serve` → http://localhost:8000
- **Theme:** all visual consistency lives in `theme/theme.css` + `templates/`.

Full guidance for agents and contributors is in **[AGENTS.md](./AGENTS.md)**.

Deployment is automatic: pushing to `main` builds and publishes to GitHub Pages
via `.github/workflows/deploy.yml`.
