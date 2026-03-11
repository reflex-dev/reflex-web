# CLAUDE.md

## What is this project?

The official Reflex website (reflex.dev) — built with Reflex itself. Includes docs, blog, pricing, landing pages, and customer showcases. Serves as both the public-facing site and a real-world example of a production Reflex app.

## Tech stack

- **Framework:** Reflex (Python full-stack)
- **Styling:** Tailwind CSS v4 with Radix UI color system
- **Package manager:** UV (`uv sync` to install deps)
- **Linting:** Ruff, Codespell — enforced via pre-commit

## Project layout

```
pcweb/              # Main application code
  pcweb.py          # App entry point
  whitelist.py      # Dev mode: limits which pages are compiled (faster builds)
  pages/            # All page routes (docs/, blog/, landing/, pricing/, etc.)
  components/       # Reusable UI components
  views/            # Shared view components (navbar, footer, cta)
  templates/        # Page templates (docpage, mainpage)
  meta/             # SEO meta tags
docs/               # Markdown documentation (flexdown)
blog/               # Blog posts (markdown + frontmatter)
tests/              # Pytest + Playwright tests
```

## Commands

| Task | Command |
|------|---------|
| Install deps | `uv sync` |
| Run dev server | `uv run reflex run` |
| Run prod | `uv run reflex run --env prod` |
| Compile check | `uv run reflex compile` |
| Run tests | `uv run pytest tests/` |
| Install Playwright (if tests fail) | `uv run playwright install` |
| Lint / format | `uv run pre-commit run --all-files` |

## Dev mode: page whitelist

`pcweb/whitelist.py` limits which pages are compiled in dev mode for faster builds. Empty list = build all. See `pcweb/whitelist.py` for format; paths start with `/`, no trailing slash.

## Code patterns

- **Components:** shared components for the app — see `pcweb/components/`
- **Pages:** use `@mainpage` or `@docpage` decorators — see `pcweb/pages/`, `pcweb/templates/`
- **Imports:** absolute from project root — `from pcweb.components.button import button`
- **Elements:** use `rx.el.*` with Tailwind (not `rx.box`, `rx.text`)

## Key conventions

- Docs: flexdown in `docs/`
- Blog: flexdown in `blog/`
- Before committing: `uv run reflex compile` and `uv run pre-commit run --all-files`
