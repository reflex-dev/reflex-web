from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

COMPARISON_ITEMS: list[ComparisonItem] = [
    {
        "title": "Full control without the ceiling.",
        "icon": "CodesandboxIcon",
        "description": "No-code tools (PowerBI, Tableau, Retool) get you to v1 fast, but you hit walls — custom logic, complex data flows, performance optimization, or anything the platform didn't anticipate. Despite being \"no-code,\" there is a significant learning curve for advanced features. With Reflex, you're writing Python, so there's no ceiling. You can do anything a full-stack app can do.",
        "pros": [
            "Pure Python with no ceiling — if Python can do it, Reflex can do it",
            "Custom logic, complex data flows, and performance optimization are all possible out of the box",
            "One language to learn, no platform-specific syntax",
        ],
        "cons": [
            "No-code tools hit walls on custom logic, complex data flows, and performance optimization",
            "Anything the platform didn't anticipate requires workarounds or is impossible",
            'Despite the "no-code" label, there is a significant learning curve for advanced features',
        ],
    },
    {
        "title": "You own your code.",
        "icon": "SourceCodeSquareIcon",
        "description": "No-code platforms create vendor lock-in. Your app lives on their infrastructure, in their proprietary format. With Reflex, it's your Python code — you can deploy it anywhere, version control it, and you're never hostage to a platform's pricing changes or shutdown.",
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
        "description": "Data scientists, ML engineers, and backend devs already live in Python. Reflex lets them build internal tools or customer-facing apps using libraries they already know (pandas, scikit-learn, whatever) without learning JavaScript or being constrained by a drag-and-drop builder's integrations.",
        "pros": [
            "Build with Python libraries your team already knows — pandas, scikit-learn, or any pip package",
            "No need to learn JavaScript or be constrained by a drag-and-drop builder's integrations",
            "Data scientists, ML engineers, and backend devs can build internal tools or customer-facing apps directly",
        ],
        "cons": [
            "No-code tools constrain you to a drag-and-drop builder's integrations",
            "Requires learning JavaScript or platform-specific languages for anything custom",
            "Data scientists and ML engineers can't use the Python libraries they already know",
        ],
    },
    {
        "title": "Scales with complexity.",
        "icon": "SquareArrowExpand02Icon",
        "description": "No-code works great for simple dashboards, but even basic interactivity is a problem. Tools like Tableau and Power BI don't natively support CRUD operations at all. Once you need users to create, edit, or delete data, plus auth flows, real-time features, complex state management, or custom APIs, you're fighting the tool instead of building. Tools also struggle with performance at scale — whether it's dataset size limits, reliance on scheduled refreshes instead of real-time data, or apps slowing down as complexity grows. Reflex handles that complexity natively because it's just code.",
        "pros": [
            "CRUD, auth flows, real-time features, complex state management, and custom APIs are all native",
            "No dataset size limits, no scheduled refreshes — real-time by default",
            "Handles complexity natively because it's just code",
        ],
        "cons": [
            "Even basic interactivity is a problem and tools like Tableau and Power BI don't natively support CRUD operations at all",
            "Performance degrades at scale — dataset size limits, scheduled refreshes instead of real-time data, and apps slowing under complexity",
            "Once you need users to create, edit, or delete data, you're fighting the tool instead of building",
        ],
    },
    {
        "title": "Production-ready from day one.",
        "icon": "UserSwitchIcon",
        "description": "No-code tools get you a prototype, but when it's time to hand it to IT or take it to production, you hit a wall. None of these tools support native version control, git integration, code review, or CI/CD pipelines. With Reflex, your app is built on real code from the start. It fits into the workflows your engineering team already uses — Git, PRs, automated testing, staging environments — so there's no painful \"rewrite it properly\" phase. What you demo is what you ship.",
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
        heading_lines=["How You Benefit ", "With Reflex vs. ", "Other Approaches"],
        description="No-code tools get you started fast, but Reflex lets you finish. Here's how Reflex compares to platforms like Power BI, Tableau, Retool, and similar no-code tools.",
        top_left_title="Reflex",
        top_right_title="Power BI, Tableau, Retool",
        comparison_items=COMPARISON_ITEMS,
    )


__all__ = ["compare"]
