from pcweb.pages.migration.common.explore import Feature
from pcweb.pages.migration.common.explore import explore as common_explore

FEATURES: list[Feature] = [
    {
        "title": "AI-Assisted App Development",
        "description": "Generate UI and app logic faster with AI while keeping full code control.",
        "icon": "ArtificialIntelligence04Icon",
    },
    {
        "title": "Real Python, Not Drag-and-Drop",
        "description": "Write maintainable Python code that fits your existing engineering standards.",
        "icon": "SourceCodeSquareIcon",
    },
    {
        "title": "Data Stack Integrations",
        "description": "Connect databases, APIs, and internal services without low-code workarounds.",
        "icon": "DatabaseIcon",
    },
    {
        "title": "Security-First by Design",
        "description": "Deploy with full control over infrastructure, access, and compliance boundaries.",
        "icon": "ShieldEnergyIcon",
    },
    {
        "title": "Production-Grade Performance",
        "description": "Scale from internal tools to enterprise apps with robust backend capabilities.",
        "icon": "DashboardSpeed01Icon",
    },
    {
        "title": "Team-Friendly Workflows",
        "description": "Use Git, PR reviews, and CI/CD workflows your team already trusts.",
        "icon": "UserSwitchIcon",
    },
]


def explore():
    return common_explore(
        kicker="Explore",
        title_prefix="Build Your App With the Speed of ",
        title_suffix="AI and Precision of Python",
        description="Reflex is growing—and we're looking for people who care deeply about developer experience, clean abstractions.",
        features=FEATURES,
    )


__all__ = ["explore"]
