import reflex as rx

from pcweb.meta.meta import create_meta_tags, faq_jsonld
from pcweb.pages.about.views.divider import divider
from pcweb.pages.migration.other_ai_tools.views import compare, explore, hero, quotes
from pcweb.templates.marketing_page import marketing_page

OTHER_AI_TOOLS_FAQ_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "What are the main limitations of Replit and Lovable for enterprise use?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Replit and Lovable generate code that is often fragile, hard for developers to take over, and not production-ready without significant manual finishing work. They're SaaS-only with no on-prem option, lock you into a specific stack, and have no way to integrate with existing codebases or internal services. They also have no audit logging, centralized access control, or organization-wide governance.",
            },
        },
        {
            "@type": "Question",
            "name": "How does Reflex differ from AI coding assistants like Claude Code and Cursor?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Claude Code and Cursor are built exclusively for developers and help you write code faster — but they don't provide a framework, deployment, hosting, or app management. Non-technical team members are completely cut out. Reflex is a complete platform: non-technical users build with natural language, developers refine the same codebase, and the AI builder, open-source framework, and hosting are all unified.",
            },
        },
        {
            "@type": "Question",
            "name": "Can non-technical users build apps with Reflex?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. Non-technical users can describe what they need in natural language and get a working app — no coding knowledge, Git, terminal commands, or software architecture required. Developers can then refine the exact same codebase when needed, with no handoff gap between prototype and production.",
            },
        },
        {
            "@type": "Question",
            "name": "Does Reflex support on-premises deployment for enterprise security requirements?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Yes. The Reflex AI App Builder deploys on-prem, in your private cloud, or in an air-gapped environment so your apps run wherever your infrastructure already lives and your code and data never leave your environment. Replit and Lovable are SaaS-only with no self-hosted option.",
            },
        },
        {
            "@type": "Question",
            "name": "What enterprise security and governance features does Reflex include?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Reflex includes prompt security, sandboxed code generation, SSO enforcement on every application, RBAC controls across integrations and users, and full audit logging to your SIEM. Your data is never used for training. It provides a unified governance layer across every app your organization builds — something neither AI app builders like Lovable nor coding assistants like Cursor offer.",
            },
        },
    ],
}


@marketing_page(
    path="/migration/other-ai-tools",
    title="Switch from Replit, Lovable & Cursor to Reflex | Enterprise AI App Builder",
    meta=create_meta_tags(
        title="Switch from Replit, Lovable & Cursor to Reflex | Enterprise AI App Builder",
        description="AI tools like Replit, Lovable, and Cursor hit production walls fast. Reflex gives your whole team — technical and non-technical — a governed, on-prem-ready Python platform to build and ship.",
        image="/previews/index_preview.webp",
    ),
)
def other_ai_tools_migration_page() -> rx.Component:
    return rx.el.div(
        faq_jsonld(OTHER_AI_TOOLS_FAQ_SCHEMA),
        rx.el.div(
            hero(),
            quotes(),
            divider(),
            compare(),
            divider(),
            explore(),
            class_name="flex flex-col relative justify-center items-center w-full",
        ),
        class_name="flex flex-col w-full relative h-full justify-center items-center",
    )
