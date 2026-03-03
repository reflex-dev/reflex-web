from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

COMPARISON_ITEMS: list[ComparisonItem] = [
    {
        "title": "One language for frontend and backend.",
        "icon": "PythonIcon",
        "description": "React and JavaScript require a split stack — you maintain frontend in JS/TypeScript and backend in Python, Go, or Node. Django is full-stack Python but server-rendered, with a different paradigm for modern SPAs. FastAPI is backend only — you still need React or Vue for the UI. Reflex gives you both in Python: declarative UI components and backend logic in one codebase.",
        "pros": [
            "One language end to end — no context switching between JavaScript and Python",
            "Data scientists, ML engineers, and backend devs build UIs without learning React",
            "Single codebase for frontend and backend — simpler architecture, easier to maintain",
        ],
        "cons": [
            "React requires JavaScript or TypeScript for the frontend — a separate stack to learn and maintain",
            "Django is server-rendered — building modern SPAs with real-time updates requires additional tooling",
            "FastAPI is backend only — you still need a separate frontend framework and two deployments",
        ],
    },
    {
        "title": "Architecture and state management.",
        "icon": "SquareArrowExpand02Icon",
        "description": "React uses a component-based model with hooks and external state libraries. Django uses server-side request/response. FastAPI has no built-in frontend. Reflex takes a declarative, state-driven approach where you define state classes and UI components in Python, and changes propagate reactively via WebSockets. Only affected components re-render.",
        "pros": [
            "Declarative state and event-driven updates — only affected components re-render",
            "User sessions remember where they are — multi-step workflows and real-time updates work without extra effort",
            "The event-driven model keeps your code clean and organized as your app grows",
        ],
        "cons": [
            "React's ecosystem of state libraries (Redux, Zustand, etc.) adds complexity — you choose and maintain the stack",
            "Django's request/response model doesn't natively support real-time or reactive updates",
            "FastAPI has no frontend — real-time state sync requires building it yourself",
        ],
    },
    {
        "title": "Real-time and interactivity.",
        "icon": "ZapIcon",
        "description": "React can do real-time but requires manual WebSocket setup or third-party services. Django has no native server-push. FastAPI supports WebSockets but you build the frontend integration yourself. Reflex uses automatic WebSocket sync where state changes on the server instantly propagate to the browser.",
        "pros": [
            "Changes on the server show up instantly in the browser — no refresh needed, no extra setup",
            "Live dashboards, real-time data feeds, and collaborative features just work out of the box",
            "Fully event-based — your app reacts to user actions as they happen",
        ],
        "cons": [
            "React has no built-in server push — real-time needs manual WebSocket setup or services like Pusher",
            "Django has no native real-time — you add Channels and more infrastructure",
            "FastAPI has WebSockets but no integrated frontend — you wire it up yourself",
        ],
    },
    {
        "title": "Code structure and maintainability.",
        "icon": "SourceCodeSquareIcon",
        "description": "React apps split logic across components, hooks, and often a separate API layer. Django keeps things in one place but with a different mental model for SPAs. FastAPI + React means two codebases, two test suites. Reflex's Python class-based state model keeps frontend and backend logic organized in one place.",
        "pros": [
            "Clean Python class structure keeps your code organized, even as apps grow to multiple pages and features",
            "Frontend and backend logic live together — no API contract drift, no separate deployments to coordinate",
            "One test suite, one deployment — simpler CI/CD and developer experience",
        ],
        "cons": [
            "React + backend means two codebases, two languages, API contracts to maintain",
            "Django's templates and views are a different paradigm from modern component-based UIs",
            "FastAPI + React requires coordinating two deployments and keeping frontend and backend in sync",
        ],
    },
    {
        "title": "Built-in functionality.",
        "icon": "Settings01Icon",
        "description": "React is a UI library — no auth, database, or background jobs. Django has these but with a server-rendered focus. FastAPI is minimal by design. Reflex ships with ORM, database migrations, background jobs, file uploads, and role-based auth out of the box — all integrated with your Python UI code.",
        "pros": [
            "Authentication, database management, background jobs, file uploads, and role-based access all come built in",
            "Everything you need to go from prototype to production without stitching together a patchwork of libraries",
            "SSO and user management are included — no third-party auth services required",
        ],
        "cons": [
            "React is UI only — auth, database, and backend logic each need separate libraries and services",
            "Django has built-ins but they're built for server-rendered apps — adapting for SPAs takes work",
            "FastAPI is minimal — you add each piece (auth, ORM, etc.) yourself",
        ],
    },
    {
        "title": "Deployment and production readiness.",
        "icon": "UserSwitchIcon",
        "description": "React apps need a separate backend deployment. Django and FastAPI need proper WSGI/ASGI setup and often separate static hosting. Reflex compiles to a FastAPI backend with a React frontend — production-ready and container-friendly from day one. One build, one deploy.",
        "pros": [
            "Compiles to a FastAPI backend with a React frontend on an async web server — production-ready from the start",
            "Fits into Git, pull requests, automated testing, and CI/CD from day one",
            "What you build is what you ship — one deployment, no separate frontend and backend to orchestrate",
        ],
        "cons": [
            "React requires a separate backend and often a CDN for static assets — two deployments to manage",
            "Django and FastAPI need manual configuration for production — WSGI, ASGI, static files, CORS",
            "Split stack means more moving parts when it's time to deploy and scale",
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
