from pcweb.pages.migration.common.explore import Feature
from pcweb.pages.migration.common.explore import explore as common_explore

FEATURES: list[Feature] = [
    {
        "title": "Full Control Without the Ceiling",
        "description": "Pure Python with no ceiling — custom logic, complex data flows, and performance optimization are all possible out of the box. You own every line of code.",
        "icon": "CodesandboxIcon",
    },
    {
        "title": "You Own Your Code",
        "description": "Deploy anywhere, on any infrastructure. Full version control. Never hostage to a platform's pricing changes or shutdown.",
        "icon": "SourceCodeSquareIcon",
    },
    {
        "title": "Python Ecosystem Access",
        "description": "Build with pandas, scikit-learn, or any pip package. No JavaScript. Data scientists and ML engineers can ship directly.",
        "icon": "PythonIcon",
    },
    {
        "title": "Scales With Complexity",
        "description": "CRUD, auth flows, real-time features, complex state management, and custom APIs — all native. Real-time by default.",
        "icon": "SquareArrowExpand02Icon",
    },
    {
        "title": "Production-Ready From Day One",
        "description": "Git, PRs, automated testing, staging environments from the start. What you demo is what you ship.",
        "icon": "UserSwitchIcon",
    },
    {
        "title": "Data Stack Integrations",
        "description": "Connect databases, APIs, and internal services without platform workarounds. No lock-in to what the AI knows.",
        "icon": "DatabaseIcon",
    },
]


def explore():
    return common_explore(
        kicker="Explore",
        title_prefix="Why Reflex Over ",
        title_suffix="ChatGPT, Claude, Replit, Lovable",
        description="AI app builders get you prototyping fast, but Reflex lets you finish. Pure Python, no ceiling, you own your code.",
        features=FEATURES,
    )


__all__ = ["explore"]
