from pcweb.pages.migration.common.explore import Feature
from pcweb.pages.migration.common.explore import explore as common_explore

FEATURES: list[Feature] = [
    {
        "title": "Full Control Without the Ceiling",
        "description": "Pure Python with no ceiling — custom logic, complex data flows, and performance optimization are all possible out of the box. You own every line of code.",
        "icon": "CodesandboxIcon",
    },
    {
        "title": "Accessible to Your Whole Team",
        "description": "Non-technical users build with natural language, developers refine the same codebase. No handoff gap, no throwaway prototype, no one left out.",
        "icon": "UserGroupIcon",
    },
    {
        "title": "A Complete Platform, Not Just a Tool",
        "description": "The AI builder, open-source framework, and hosting in one place. No assembling a stack, no starting from scratch on every project.",
        "icon": "Layers01Icon",
    },
    {
        "title": "Works With Your Existing Infrastructure",
        "description": "Deploy on-prem, in your private cloud, or air-gapped. Connect any database, API, or Python library your organization already uses.",
        "icon": "CloudServerIcon",
    },
    {
        "title": "Enterprise Guardrails and Governance",
        "description": "SSO, RBAC, audit logging to your SIEM, and sandboxed code generation. A unified governance layer across every app your organization builds.",
        "icon": "DatabaseIcon",
    },
    {
        "title": "Python Ecosystem Access",
        "description": "Build with pandas, scikit-learn, or any pip package. Data scientists and ML engineers can ship directly without learning a new stack.",
        "icon": "PythonIcon",
    },
]


def explore():
    return common_explore(
        kicker="Explore",
        title_prefix="Why Reflex Over ",
        title_suffix="Replit, Lovable, Claude Code & Cursor",
        description="Whether you're escaping fragile AI-generated code or looking beyond a developer-only tool, Reflex gives your whole organization a production-grade platform.",
        features=FEATURES,
    )


__all__ = ["explore"]
