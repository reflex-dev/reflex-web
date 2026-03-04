from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

COMPARISON_ITEMS: list[ComparisonItem] = [
    {
        "title": "Full control without the ceiling.",
        "icon": "CodesandboxIcon",
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
