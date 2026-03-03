from pcweb.pages.migration.common.explore import Feature
from pcweb.pages.migration.common.explore import explore as common_explore

FEATURES: list[Feature] = [
    {
        "title": "One Language End to End",
        "description": "Python for frontend and backend. No JavaScript required. Data scientists and backend devs build UIs without learning React.",
        "icon": "PythonIcon",
    },
    {
        "title": "Architecture That Scales",
        "description": "Declarative state, event-driven updates, and reactive re-renders. Only affected components update — no callback spaghetti.",
        "icon": "SquareArrowExpand02Icon",
    },
    {
        "title": "Real-Time Out of the Box",
        "description": "WebSocket sync means server changes show up instantly in the browser. Live dashboards and collaborative features work natively.",
        "icon": "ZapIcon",
    },
    {
        "title": "Clean, Maintainable Code",
        "description": "Python class-based state keeps logic organized. Single codebase for frontend and backend.",
        "icon": "SourceCodeSquareIcon",
    },
    {
        "title": "Production-Ready Built-Ins",
        "description": "Auth, ORM, database migrations, background jobs, and file uploads — everything you need to ship without stitching together libraries.",
        "icon": "Settings01Icon",
    },
    {
        "title": "What You Build Is What You Ship",
        "description": "Compiles to FastAPI + React. Fits Git, CI/CD, and container deployment from day one. One build, one deploy.",
        "icon": "UserSwitchIcon",
    },
]


def explore():
    return common_explore(
        kicker="Explore",
        title_prefix="Why Reflex Over ",
        title_suffix="React, Django, FastAPI",
        description="React, Django, and FastAPI each solve part of the stack. Reflex lets you finish. One language, full-stack, production-ready from day one.",
        features=FEATURES,
    )


__all__ = ["explore"]
