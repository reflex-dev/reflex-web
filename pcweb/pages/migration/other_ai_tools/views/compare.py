import reflex as rx

from pcweb.pages.migration.common.compare import ComparisonItem
from pcweb.pages.migration.common.compare import compare as common_compare

AI_APP_BUILDERS_ITEMS: list[ComparisonItem] = [
    {
        "title": "Built on a real Python framework, not a black box.",
        "icon": "PythonIcon",
        "pros": [
            "The AI writes to an open-source Python framework with shared abstractions, so generated code follows consistent, structured patterns that developers can fully inspect and modify",
            "Non-technical users can start apps with natural language and developers refine the exact same codebase. No handoff gap and no throwaway prototype",
            "Built-in abstractions for auth, real-time streaming, and shared state mean the AI generates reliable code rather than stitching together workarounds",
        ],
        "cons": [
            "Replit and Lovable generate code that is often fragile, hard to understand, and difficult for developers to take over and maintain",
            "Debugging is unpredictable and expensive. Users report burning through significant tokens and spending hundreds of dollars just fixing bugs the AI introduced",
            "The output often looks great as a demo but can't actually be launched without significant technical help to finish and configure external services",
        ],
    },
    {
        "title": "Works with your existing infrastructure.",
        "icon": "CloudServerIcon",
        "pros": [
            "The AI App Builder deploys on-prem, in your private cloud, or air-gapped so your apps run wherever your infrastructure already lives",
            "Connects to any data source: REST or GraphQL APIs, any Python library or SDK, databases like PostgreSQL, MySQL, and MongoDB, and file formats like CSV, Excel, PDF, and images",
            "Integrates natively with your existing Python codebase and auth systems rather than being a separate island",
        ],
        "cons": [
            "Replit and Lovable are SaaS-only with no self-hosted on-prem option. Your code and data flow through their servers",
            "These platforms lock you into a specific stack — a particular database, cloud, or frontend framework — that may not match what your organization has standardized on",
            "Enterprise projects are rarely greenfield, but these platforms have no way to integrate with existing codebases, data stacks, or internal services",
        ],
    },
    {
        "title": "Enterprise guardrails and governance.",
        "icon": "Layers01Icon",
        "pros": [
            "Prompt security blocks malicious threats, code generation runs in sandboxed environments, and your data is never used for training",
            "SSO enforced on every application, with RBAC controls across integrations, apps, and users",
            "Every action is audit-logged and sent to your SIEM for full visibility, with a unified platform to view, manage, and govern all apps across the organization",
        ],
        "cons": [
            "Replit and Lovable are built for individual users, not organizations. There's no shared view of what's been built, no consistent security policies, and no governance layer",
            "Non-technical users building apps on these platforms commonly misconfigure databases and security policies, with Lovable having had a critical vulnerability where AI-generated code was exposed to malicious prompt injection",
            "No audit logging, no centralized access control, and no way to enforce security standards across teams",
        ],
    },
    {
        "title": "Deploy anywhere, scale without limits.",
        "icon": "SquareArrowExpand02Icon",
        "pros": [
            "One-click deployment to any infrastructure including on-premise, with a unified platform to manage, monitor, and govern all apps",
            "The platform owns the full stack — the AI builder, underlying framework, and hosting — so the same app scales from prototype to production without switching tools",
            "No manual finishing, no external service configuration, and no rebuilding required to get to production",
        ],
        "cons": [
            "Replit and Lovable typically offer one deployment option: their own cloud. If you need AWS, Azure, GCP, or on-premise, you're out of luck",
            "These platforms create great prototypes but are often fragile under more complex enterprise requirements, requiring significant manual work to get anywhere near production-ready",
            "Scaling beyond a demo means configuring external services, debugging platform limitations, and often rebuilding parts of the app outside the platform entirely",
        ],
    },
]

AI_CODING_ASSISTANTS_ITEMS: list[ComparisonItem] = [
    {
        "title": "Accessible to your whole team, not just engineers.",
        "icon": "UserGroupIcon",
        "pros": [
            "Non-technical users describe what they need in natural language and get a working app. No coding knowledge required",
            "Developers can refine the exact same codebase when needed, with no handoff gap between prototype and production",
            "The person with the idea can take it all the way to deployment without needing to know Git, terminal commands, or software architecture",
        ],
        "cons": [
            "Claude Code and Cursor are built exclusively for developers who already understand code, Git workflows, terminal commands, and software architecture",
            "Non-technical team members like PMs, analysts, operations, and business stakeholders are completely cut out of the development process",
            "Only 17% of developers say AI coding tools have improved team collaboration, meaning they remain individual productivity tools, not organization-wide solutions",
        ],
    },
    {
        "title": "A complete platform, not just a coding tool.",
        "icon": "CodesandboxIcon",
        "pros": [
            "Includes the AI builder, the underlying open-source framework, and deployment and hosting as a unified platform for the entire app lifecycle from idea to production",
            "Built-in integrations, auth, real-time features, and database management mean you're not assembling separate tools for each piece",
            "Organization-level features like shared integrations, governance, and a centralized app management dashboard come out of the box",
        ],
        "cons": [
            "Claude Code and Cursor help you write code faster but don't provide a framework, deployment, hosting, or app management",
            "You still need to choose and assemble your own stack (framework, database, auth, hosting, CI/CD) and the AI just helps you type faster within that stack",
            "Every new project starts from scratch with no shared patterns, no reusable integrations, and no consistency across what different teams build",
        ],
    },
    {
        "title": "Structured, maintainable output.",
        "icon": "SourceCodeSquareIcon",
        "pros": [
            "The AI writes to a specific framework with shared abstractions, so generated code follows consistent patterns that are easy to understand and modify",
            "Common operations like authentication, real-time streaming, and shared state are handled by the framework itself, reducing boilerplate and increasing reliability",
            "The framework acts as guardrails, keeping codebases consistent across teams and projects",
        ],
        "cons": [
            "Claude Code and Cursor can generate code in any style, any framework, and any architecture, leading to inconsistent patterns across projects and teams",
            "Without framework-level guardrails, AI-generated code can be harder to review, maintain, and scale because there's no shared standard for how things are built",
            "Large refactors across many files can still go wrong, and the AI has no awareness of your organization's conventions unless you manually configure it each time",
        ],
    },
    {
        "title": "Enterprise security and data privacy.",
        "icon": "DatabaseIcon",
        "pros": [
            "Deploys entirely on your own infrastructure (on-prem, private cloud, or air-gapped) so your code and data never leave your environment",
            "Prompt security, code sandboxing, SSO on every application, RBAC controls, and full audit logging to your SIEM",
            "Your data is never used for training, with a unified governance layer across the entire platform",
        ],
        "cons": [
            "Claude Code and Cursor offer privacy options like bring-your-own-key and Privacy Mode, but they remain individual developer tools with no centralized way to enforce consistent security policies across all developers",
            "No unified governance layer across all the apps being built, no built-in deployment to your own infrastructure, and no organization-wide RBAC or audit logging to a SIEM",
            "They solve the 'write code faster' problem but not the 'manage, govern, and deploy apps across an organization' problem",
        ],
    },
]


def compare():
    return rx.el.div(
        common_compare(
            kicker="AI App Builder Platforms",
            heading_lines=[
                "How You Benefit ",
                "With Reflex vs. ",
                "Replit & Lovable",
            ],
            description="AI app builders get you prototyping fast but hit a wall in production. Here's how Reflex compares to Replit and Lovable.",
            top_left_title="Reflex",
            top_right_title="Replit & Lovable",
            comparison_items=AI_APP_BUILDERS_ITEMS,
        ),
        common_compare(
            kicker="AI Coding Assistants",
            heading_lines=[
                "How You Benefit ",
                "With Reflex vs. ",
                "Claude Code & Cursor",
            ],
            description="AI coding assistants boost developer speed but leave the rest of your organization behind. Here's how Reflex compares to Claude Code and Cursor.",
            top_left_title="Reflex",
            top_right_title="Claude Code & Cursor",
            comparison_items=AI_CODING_ASSISTANTS_ITEMS,
        ),
        class_name="flex flex-col w-full",
    )


__all__ = ["compare"]
