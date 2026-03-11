from pcweb.pages.migration.common.explore import Feature
from pcweb.pages.migration.common.explore import explore as common_explore

FEATURES: list[Feature] = [
    {
        "title": "One language, one codebase",
        "description": "Build your entire app in pure Python with no context switching. One codebase to maintain, version control, test, and deploy instead of two separate projects.",
        "icon": "PythonIcon",
    },
    {
        "title": "Built-in features vs. assembly required",
        "description": "Authentication, ORM, database migrations, real-time sync, background jobs, and file uploads all come out of the box — no need to stitch together a dozen separate libraries.",
        "icon": "Settings01Icon",
    },
    {
        "title": "Development speed",
        "description": "Roughly 5x faster than assembling a traditional Python + React stack. No time spent wiring API endpoints, configuring CORS, or debugging frontend-backend mismatches.",
        "icon": "ZapIcon",
    },
    {
        "title": "Modern frontend without JavaScript",
        "description": "Reflex compiles your Python into a React frontend automatically. Wrap any existing React component from Python when you need something custom.",
        "icon": "WebDesign01Icon",
    },
    {
        "title": "Performance and real-time capabilities",
        "description": "Async web server with WebSocket sync. Real-time updates, live data feeds, and high-concurrency traffic handled natively.",
        "icon": "SquareArrowExpand02Icon",
    },
    {
        "title": "Scaling and maintainability",
        "description": "Python class-based state keeps code organized as apps grow. Add new features in one place, not across two separate projects.",
        "icon": "SourceCodeSquareIcon",
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
