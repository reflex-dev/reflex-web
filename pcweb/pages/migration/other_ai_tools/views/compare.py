from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

COMPARISON_ITEMS: list[ComparisonItem] = [
    {
        "title": "Full control without the ceiling.",
        "icon": "CodesandboxIcon",
        "pros": [
            "Pure Python with no ceiling — if Python can do it, Reflex can do it",
            "Custom logic, complex data flows, and performance optimization are all possible out of the box",
            "You own every line of code — no black-box AI output you can't modify",
        ],
        "cons": [
            "AI tools hit walls on custom logic, integrations, and anything the platform didn't anticipate",
            "What you get is what they generate — no deep customization without fighting the tool",
            "Platform limitations dictate what's possible, not your requirements",
        ],
    },
    {
        "title": "You own your code.",
        "icon": "SourceCodeSquareIcon",
        "pros": [
            "It's your Python code — deploy it anywhere, on any infrastructure",
            "Full version control so your codebase is portable and auditable",
            "Never hostage to a platform's pricing changes or shutdown",
        ],
        "cons": [
            "Your app lives on their infrastructure, in their proprietary format",
            "Vendor lock-in — no way to export or migrate your work",
            "Exposed to pricing changes you can't control",
        ],
    },
    {
        "title": "Python ecosystem access.",
        "icon": "PythonIcon",
        "pros": [
            "Build with Python libraries your team already knows — pandas, scikit-learn, or any pip package",
            "No need to learn JavaScript or be constrained by pre-built integrations",
            "Data scientists, ML engineers, and backend devs can build internal tools or customer-facing apps directly",
        ],
        "cons": [
            "AI tools constrain you to their pre-built integrations and what the model knows",
            "Requires workarounds or is impossible for custom libraries and data sources",
            "Data scientists and ML engineers can't use the Python libraries they already know",
        ],
    },
    {
        "title": "Scales with complexity.",
        "icon": "SquareArrowExpand02Icon",
        "pros": [
            "CRUD, auth flows, real-time features, complex state management, and custom APIs are all native",
            "Handles complexity natively because it's just code",
            "No artificial boundaries on what you can build",
        ],
        "cons": [
            "AI-generated apps break down once you need real complexity — auth, real-time, or production scale",
            "The output isn't designed for maintainable, extensible codebases",
            "Once you need users to do more than view a demo, you're fighting the tool instead of building",
        ],
    },
    {
        "title": "Production-ready from day one.",
        "icon": "UserSwitchIcon",
        "pros": [
            "Fits into Git, PRs, automated testing, staging environments from the start",
            'What you demo is what you ship — no "rewrite it properly" phase',
            "Your engineering team can deploy, maintain, and scale it using workflows they already use",
        ],
        "cons": [
            "No native version control, git integration, code review, or CI/CD pipelines",
            "When it's time to hand it to IT or take it to production, you hit a wall",
            "The prototype-to-production gap forces teams to either rewrite in code or accept platform limitations",
        ],
    },
]


def compare():
    return common_compare(
        kicker="Compare",
        heading_lines=[
            "How You Benefit ",
            "With Reflex vs. ",
            "ChatGPT, Claude, Replit, Lovable",
        ],
        description="AI app builders get you prototyping fast. Reflex lets you finish. Here's how Reflex compares to platforms like ChatGPT, Claude, Replit, and Lovable.",
        top_left_title="Reflex",
        top_right_title="ChatGPT, Claude, Replit, Lovable",
        comparison_items=COMPARISON_ITEMS,
    )


__all__ = ["compare"]
