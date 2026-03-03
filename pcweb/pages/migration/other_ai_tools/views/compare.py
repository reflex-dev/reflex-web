from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

COMPARISON_ITEMS: list[ComparisonItem] = [
    {
        "title": "Full control without the ceiling.",
        "icon": "CodesandboxIcon",
        "description": "AI app builders (ChatGPT, Claude, Replit, Lovable) get you to v1 fast, but you hit walls — custom logic, integrations beyond what the AI knows, or anything the platform didn't anticipate. What you get is what they generate. With Reflex, you're writing Python, so there's no ceiling. You can do anything a full-stack app can do.",
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
        "description": "AI app builders create output that lives on their infrastructure, in their proprietary format. Your app is tied to their platform — you can't export it, version it properly, or deploy it yourself. With Reflex, it's your Python code — you can deploy it anywhere, version control it, and you're never hostage to a platform's pricing changes or shutdown.",
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
        "description": "Data scientists, ML engineers, and backend devs already live in Python. Reflex lets them build internal tools or customer-facing apps using libraries they already know (pandas, scikit-learn, whatever) without being constrained by an AI's pre-built integrations or learning JavaScript. AI tools are limited to what the model knows how to integrate.",
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
        "description": "AI app builders work great for simple demos, but once you need auth flows, real-time features, complex state management, custom APIs, or production-grade performance, you hit a wall. The generated output isn't designed for that. Reflex handles that complexity natively because it's just code.",
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
        "description": "AI app builders get you a prototype, but when it's time to hand it to IT or take it to production, you hit a wall. None of these tools support native version control, git integration, code review, or CI/CD pipelines. With Reflex, your app is built on real code from the start. It fits into the workflows your engineering team already uses — Git, PRs, automated testing, staging environments — so there's no painful \"rewrite it properly\" phase. What you demo is what you ship.",
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
