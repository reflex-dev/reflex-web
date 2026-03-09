from pcweb.pages.migration.common.explore import Feature
from pcweb.pages.migration.common.explore import explore as common_explore

FEATURES: list[Feature] = [
    {
        "title": "Architecture That Scales",
        "description": "Declarative state, event-driven updates, and reactive re-renders. Only affected components update — no full script reruns or callback spaghetti.",
        "icon": "SquareArrowExpand02Icon",
    },
    {
        "title": "Real-Time Out of the Box",
        "description": "WebSocket sync means server changes show up instantly in the browser. Live dashboards and collaborative features work natively.",
        "icon": "ZapIcon",
    },
    {
        "title": "Clean, Maintainable Code",
        "description": "Python class-based state keeps logic organized. Real projects use roughly half the code compared to equivalent Dash apps.",
        "icon": "SourceCodeSquareIcon",
    },
    {
        "title": "Full Customization",
        "description": "Wrap any React component from Python. Complete design flexibility without leaving the Python ecosystem.",
        "icon": "WebDesign01Icon",
    },
    {
        "title": "Production-Ready Built-Ins",
        "description": "Auth, ORM, database migrations, background jobs, and file uploads — everything you need to ship without stitching together libraries.",
        "icon": "Settings01Icon",
    },
    {
        "title": "What You Build Is What You Ship",
        "description": "Compiles to FastAPI + React. Fits Git, CI/CD, and container deployment from day one. No prototype-to-production rewrite.",
        "icon": "UserSwitchIcon",
    },
]


def explore():
    return common_explore(
        kicker="Explore",
        title_prefix="Why Reflex Over ",
        title_suffix="Streamlit, Dash, Gradio",
        description="Low-code Python frameworks get you prototyping fast. Reflex lets you finish. Declarative state, real-time updates, production-ready output from day one.",
        features=FEATURES,
    )


__all__ = ["explore"]
