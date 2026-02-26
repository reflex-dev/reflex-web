from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

COMPARISON_ITEMS: list[ComparisonItem] = [
    {
        "title": "Full Control Without the Ceiling",
        "icon": "CodesandboxIcon",
        "pros": [
            "Write real Python — no ceiling on what you can build",
            "Handle custom logic, complex data flows, and performance optimization natively",
            "Build anything a full-stack app can do",
        ],
        "cons": [
            "Get you to v1 fast, then you hit walls",
            "Custom logic and complex data flows require ugly workarounds",
            "Platform limitations dictate what's possible, not your requirements",
        ],
    },
    {
        "title": "You Own Your Code",
        "icon": "SourceCodeSquareIcon",
        "pros": [
            "It's your Python code — deploy it anywhere",
            "Full version control with Git",
            "Never hostage to a platform's pricing or shutdown",
        ],
        "cons": [
            "Your app lives on their infrastructure in their proprietary format",
            "Vendor lock-in makes migration painful or impossible",
            "Pricing changes or platform shutdowns put your app at risk",
        ],
    },
    {
        "title": "Python Ecosystem Access",
        "icon": "PythonIcon",
        "pros": [
            "Use libraries you already know — pandas, scikit-learn, whatever",
            "Build internal tools or customer-facing apps in one language",
            "Leverage the entire Python ecosystem with no restrictions",
        ],
        "cons": [
            "Limited to the platform's pre-built integrations",
            "Can't tap into Python's ML, data science, or backend libraries",
            "Forces non-JS developers to learn new tools or work around limitations",
        ],
    },
    {
        "title": "Scales With Complexity",
        "icon": "SquareArrowExpand02Icon",
        "pros": [
            "Auth flows, real-time features, complex state management — all native",
            "Handles growing complexity because it's just code",
            "No artificial boundaries on what you can build",
        ],
        "cons": [
            "Great for simple CRUD apps and dashboards, then it breaks down",
            "Once you need real complexity, you're fighting the tool instead of building",
            "Workarounds pile up and become unmaintainable",
        ],
    },
    {
        "title": "Team Collaboration & Engineering Practices",
        "icon": "UserSwitchIcon",
        "pros": [
            "Fits into normal engineering workflows — Git, PRs, CI/CD",
            "Code review and automated testing work out of the box",
            "Your whole team can collaborate using standard dev practices",
        ],
        "cons": [
            "Version control is difficult or impossible",
            "Code review and testing are afterthoughts at best",
            "Engineering best practices don't apply to proprietary drag-and-drop formats",
        ],
    },
]


def compare():
    return common_compare(
        kicker="Compare",
        heading_lines=["How You Benefit ", "With Reflex vs. ", "Other Approaches"],
        description="No-code tools get you started fast, but Reflex lets you finish. Here's how Reflex compares to platforms like Retool, Streamlit, Plotly Dash, and Power BI.",
        top_left_title="Reflex",
        top_right_title="Retool, Streamlit, Plotly Dash, Power BI",
        comparison_items=COMPARISON_ITEMS,
    )


__all__ = ["compare"]
