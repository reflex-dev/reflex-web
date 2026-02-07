# Reflex Website - Claude AI Context

## Project Overview

**Project:** reflex-web - The official website and documentation for Reflex
**Repository:** https://github.com/reflex-dev/reflex-web
**Purpose:** Marketing, documentation, and showcase website for Reflex, a Python framework for building full-stack web applications

The website is built using Reflex itself, demonstrating the framework's capabilities while providing comprehensive documentation, tutorials, blog posts, and templates.

## Tech Stack

### Core Technologies
- **Reflex** (Python framework) - Full-stack web framework with Python backend and React frontend
- **Python 3.11+** - Primary language
- **FastAPI** - Backend API framework (integrated with Reflex)
- **React** - Frontend (abstracted through Reflex components)
- **Tailwind CSS v4** - Styling with custom plugins
- **Radix UI** - Accessible UI component library

### Database & ORM
- **PostgreSQL** - Primary database (production)
- **SQLite** - Local development (`reflex.db`)
- **SQLAlchemy** - ORM layer
- **Alembic** - Database migrations

### Development Tools
- **uv** (>=0.7.0) - Python package manager
- **Ruff** - Python linter and formatter (targets Python 3.11)
- **Pytest** - Unit testing
- **Playwright** - E2E testing
- **Pre-commit** - Git hooks for code quality

### External Services
- **OpenAI API** - AI features
- **Typesense** - Search functionality
- **Loops.so** - Email marketing
- **Replicate** - ML model serving
- **Google Translate API** - Internationalization
- **Zapier Webhooks** - Form integrations

## Project Structure

```
reflex-web/
├── pcweb/                    # Main Reflex application
│   ├── pages/                # Page components (landing, docs, blog, pricing, etc.)
│   ├── components/           # Reusable UI components (22 subdirectories)
│   ├── templates/            # Layout templates (mainpage, webpage, docpage, etc.)
│   ├── styles/               # Global styles (colors, fonts, shadows)
│   ├── views/                # Page view sections
│   ├── meta/                 # SEO metadata
│   ├── telemetry/            # Analytics
│   ├── constants.py          # URLs and configuration constants
│   ├── models.py             # Database models
│   ├── route.py              # Route definitions
│   ├── flexdown.py           # Custom markdown processor
│   └── pcweb.py              # Main app configuration
│
├── docs/                     # Documentation markdown files
│   ├── getting_started/      # Getting started guides
│   ├── ui/                   # UI component docs
│   ├── database/             # Database docs
│   ├── library/              # Component library docs
│   ├── enterprise/           # Enterprise features (AG Grid, Mantine, React Flow)
│   └── api-reference/        # API documentation
│
├── blog/                     # Blog posts (29+ markdown files)
├── reflex_build_templates/   # Pre-built templates (18 dashboards & apps)
├── case-studies/             # Customer case studies
├── integrations-docs/        # Integration documentation
├── tests/                    # Test suite (pytest, Playwright)
├── assets/                   # Static assets (66 subdirectories)
├── alembic/                  # Database migrations
│
├── rxconfig.py               # Reflex app configuration
├── tailwind_config.py        # Tailwind CSS theme
├── pyproject.toml            # Python dependencies
├── uv.lock                   # Locked dependency versions
└── README.md                 # Project README
```

## Key Files

### Configuration
- `rxconfig.py:1` - Main Reflex config (port 3000, plugins, environment)
- `tailwind_config.py:1` - Tailwind theme customization
- `tailwind_radix_map.py:1` - Tailwind-Radix color mapping
- `pyproject.toml:1` - Python project metadata and dependencies

### Core Application
- `pcweb/pcweb.py:1` - Main app setup with routes, redirects, styling (166 lines)
- `pcweb/route.py:1` - Route definition dataclass
- `pcweb/constants.py:1` - External URLs and API endpoints
- `pcweb/flexdown.py:1` - Custom markdown processor for docs

### Styling System
- `pcweb/styles/styles.py:1` - Base style configuration
- `pcweb/styles/colors.py:1` - Color constants (Radix palette)
- `pcweb/styles/fonts.py:1` - Font definitions (Instrument Sans, JetBrains Mono)
- `pcweb/styles/shadows.py:1` - Shadow definitions

### Database
- `pcweb/models.py:1` - Database models (Customer model)
- `alembic/env.py:1` - Migration environment configuration

## Development Workflow

### Setup
```bash
# Install dependencies
uv sync

# Run development server
reflex run

# Open browser at http://localhost:3000
```

### Testing
```bash
# Run unit tests
pytest

# Run integration tests (requires Playwright)
pytest tests/test_*.py

# Pre-commit checks
pre-commit run --all-files
```

### Code Quality
- **Linting:** Ruff (configured in pyproject.toml)
- **Formatting:** Ruff format
- **Type checking:** Basic type hints (not enforced with mypy)
- **Spell checking:** Codespell via pre-commit hooks
- **Docstrings:** Google-style convention

### CI/CD Pipeline
- **Integration tests** - On push to main and PRs
- **Unit tests** - On pull requests
- **Deploy workflows** - Separate pipelines for dev, staging, production
- **Search index updates** - Typesense index updates on content changes

## Database Models

### Customer Model (`pcweb/models.py:1`)
- `name` - Customer name
- `email` - Email address
- `phone` - Phone number
- `address` - Physical address

Managed through SQLAlchemy ORM with Alembic migrations in `alembic/versions/`.

## Styling Architecture

### Tailwind CSS v4
- Custom theme in `tailwind_config.py:1`
- Radix UI color palette integration via `tailwind_radix_map.py:1`
- Dark/light mode support
- Responsive design utilities

### Component Styling
- ~262 Python files across pcweb directory
- Extensive use of Tailwind utility classes
- Component library organized in 22 subdirectories
- Custom components inherit from Reflex base classes

### Typography
- **Instrument Sans** - Body text
- **JetBrains Mono** - Code blocks

## Documentation Structure

The site includes comprehensive documentation in `/docs`:

1. **Getting Started** - 11 guides for beginners
2. **UI/Components** - Component usage and API
3. **Database** - Database integration guides
4. **Events** - Event handling documentation
5. **State Management** - State handling patterns
6. **Hosting** - Self-hosted and cloud deployment
7. **Enterprise** - AG Grid, Mantine, React Flow integration
8. **API Reference** - Complete API documentation

Blog posts (29+) cover technical topics and framework updates.

## Common Tasks

### Adding a New Page
1. Create component in `pcweb/pages/[section]/[pagename].py`
2. Define route in `pcweb/route.py:1`
3. Register route in `pcweb/pcweb.py:1`
4. Add to navigation if needed

### Adding Documentation
1. Create markdown file in `docs/[category]/[doc-name].md`
2. Update doc index/navigation in relevant page component
3. Rebuild search index (runs automatically in CI)

### Adding a Blog Post
1. Create markdown file in `blog/[YYYY-MM-DD-title].md`
2. Include frontmatter (title, author, date, description)
3. Post automatically appears in blog index

### Styling Changes
- Global styles: `pcweb/styles/styles.py:1`
- Colors: `pcweb/styles/colors.py:1`
- Tailwind config: `tailwind_config.py:1`

### Database Migrations
```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Environment Variables

Check `rxconfig.py:1` and `.env` for required environment variables:
- Database connection strings
- API keys (OpenAI, Typesense, Loops.so, etc.)
- Deployment configuration

## Build & Deploy

### Local Build
```bash
reflex export
```

### Production Deploy
Automated via GitHub Actions workflows:
- `.github/workflows/deploy-dev.yml:1` - Dev environment
- `.github/workflows/deploy-stg.yml:1` - Staging environment
- `.github/workflows/deploy-prd.yml:1` - Production environment

Cloud configuration in `cloud-prod.yml:1`.

## Key Dependencies

**Core:** reflex, reflex-enterprise (rxe), fastapi, uvicorn
**Database:** sqlalchemy, alembic, psycopg
**Frontend:** tailwindcss, radix-ui (via Reflex)
**APIs:** openai, httpx, aiohttp
**Dev Tools:** pytest, playwright, ruff, pre-commit
**Total:** 31 main dependencies (see `pyproject.toml:1`)

## Architecture Notes

### Reflex Framework
- Python-only full-stack framework
- Compiles to React on frontend
- State management through Python classes
- Event handlers are Python functions
- No JavaScript required for development

### Page Rendering
- Server-side rendering (SSR) support
- Static generation for docs and blog
- Dynamic routes with path parameters
- SEO optimization through meta tags

### Component System
- Reusable components in `pcweb/components/`
- Template system in `pcweb/templates/`
- Style inheritance through Reflex component classes
- Props passed as Python function arguments

## Testing Strategy

### Unit Tests (`tests/`)
- Component rendering tests
- URL routing tests
- Event handler tests
- State management tests

### Integration Tests
- End-to-end with Playwright
- Full user flows (signup, navigation, search)
- Cross-browser testing

### Test Configuration
- `tests/conftest.py:1` - Pytest fixtures
- Test files: `tests/test_*.py`
- Run via `pytest` command

## Getting Help

- **Documentation:** https://reflex.dev/docs
- **Discord:** Community support
- **GitHub Issues:** https://github.com/reflex-dev/reflex-web/issues
- **Main Reflex Repo:** https://github.com/reflex-dev/reflex

## Branch Information

Current branch: `focused-euler`
Main branch: `main`
This is a git worktree (check git status for current location and main repository path)

---

*Last Updated: 2026-02-06*
