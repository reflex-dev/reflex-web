from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

COMPARISON_ITEMS: list[ComparisonItem] = [
    {
        "title": "One language, one codebase",
        "icon": "PythonIcon",
        "pros": [
            "Build your entire app — frontend and backend — in pure Python with no context switching between languages",
            "One codebase to maintain, version control, test, and deploy instead of two separate projects",
            "No need to hire or rely on separate JavaScript and Python developers",
        ],
        "cons": [
            "Traditional stacks require maintaining two codebases in two languages — Python for the backend and JavaScript/TypeScript for the frontend where every new feature touches both codebases",
            "Connecting the two halves requires writing and maintaining REST or GraphQL API glue code, data serialization, and state synchronization",
            "The full stack quickly expands to include React, TypeScript, Node, a bundler, a package manager, a CSS framework, and separate deployment orchestration",
        ],
    },
    {
        "title": "Built-in features vs. assembly required",
        "icon": "Settings01Icon",
        "pros": [
            "Authentication, ORM, database migrations, real-time sync, background jobs, and file uploads all come out of the box",
            "No need to evaluate, install, configure, and maintain a dozen separate libraries just to get production essentials",
        ],
        "cons": [
            "FastAPI and Flask give you almost nothing out of the box — no auth, no admin panel, no ORM, no templating",
            "Django includes more built-in features but its HTML templating is not suited for modern interactive interfaces",
        ],
    },
    {
        "title": "Development speed",
        "icon": "ZapIcon",
        "pros": [
            "Building with Reflex is roughly 5x faster than assembling the same app from a traditional Python + React stack",
            "No time spent wiring API endpoints, configuring CORS, setting up build pipelines, or debugging mismatches between frontend and backend",
        ],
        "cons": [
            "Traditional stacks require significant boilerplate just to get a frontend talking to a backend before any real feature work begins",
            "Every new feature touches both codebases — a backend endpoint, a frontend component, and the API contract between them",
        ],
    },
    {
        "title": "Modern frontend without JavaScript",
        "icon": "WebDesign01Icon",
        "pros": [
            "Reflex compiles your Python code into a React frontend automatically — you get a modern, interactive UI without writing any JavaScript",
            "Wrap any existing React component directly from Python when you need something custom",
        ],
        "cons": [
            "Django's built-in templating and Flask's Jinja templating produce static HTML that looks poor out of the box and building anything interactive means bringing in the full JavaScript toolchain",
            "FastAPI has no frontend or templating at all so you're starting from zero on the UI side",
        ],
    },
    {
        "title": "Performance and real-time capabilities",
        "icon": "SquareArrowExpand02Icon",
        "pros": [
            "Reflex runs on an async web server with WebSocket sync — real-time updates, live data feeds, and high-concurrency traffic are handled natively",
            "Compiles down under the hood to a FastAPI backend with a React frontend — the same production architecture, without the assembly cost",
        ],
        "cons": [
            "Flask is synchronous by default and Django's monolithic architecture makes scaling more challenging — neither is natively built for high-concurrency or real-time use cases",
            "None of the traditional frameworks include built-in real-time capabilities — adding WebSocket support requires additional libraries and infrastructure",
        ],
    },
    {
        "title": "Scaling and maintainability",
        "icon": "SourceCodeSquareIcon",
        "pros": [
            "Python class-based state model keeps code organized as apps grow in complexity — no scattered API endpoints and disconnected frontend components",
            "Adding new features means working in one place, not coordinating changes across two separate projects",
        ],
        "cons": [
            "Traditional stacks become harder to maintain as they grow — every change requires coordinating updates across backend endpoints, frontend components, and the API layer between them",
            "FastAPI's lack of built-in structure means teams must design their own patterns for organizing large applications",
        ],
    },
]


def compare():
    return common_compare(
        kicker="Compare",
        heading_lines=[
            "How You Benefit ",
            "With Reflex vs. ",
            "React, Django, FastAPI",
        ],
        description="React, Django, and FastAPI each solve part of the stack. Reflex lets you finish. Here's how Reflex compares to the leading Python and JavaScript frameworks.",
        top_left_title="Reflex",
        top_right_title="React, Django, FastAPI",
        comparison_items=COMPARISON_ITEMS,
    )


__all__ = ["compare"]
