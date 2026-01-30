import reflex as rx

from pcweb.pages.use_cases.common.features_2 import feature_card


def features_2() -> rx.Component:
    return rx.el.section(
        feature_card(
            "WebDesign01Icon",
            "Internal Government Dashboards",
            "Track & Monitor Programs",
            "Gain real-time visibility into program effectiveness, resource allocation, and service delivery with customizable dashboards.",
            items=[
                "Program performance dashboards",
                "Budgeting and spend oversight tools",
                "Policy impact analysis",
                "Operations and service delivery tracking",
            ],
            class_name="lg:border-b",
        ),
        feature_card(
            "ArtificialIntelligence04Icon",
            "AI Assistants for Public Servants",
            "Empower Your Teams",
            "Equip your workforce with AI-powered tools to navigate complex regulations and enhance decision-making.",
            items=[
                "RAG chatbots over legislation and regulations",
                "Internal knowledge assistants",
                "Caseworker and analyst copilots",
                "Research and document analysis tools",
            ],
            class_name="lg:border-b",
        ),
        feature_card(
            "FlowConnectionIcon",
            "Case, Permit & Workflow Systems",
            "Streamline Operations",
            "Modernize administrative processes with tailored applications that reduce bottlenecks and improve transparency.",
            items=[
                "Case management tools",
                "Review and approval workflows",
                "Compliance and inspection apps",
                "Grant and funding administration systems",
            ],
        ),
        feature_card(
            "TestTube02Icon",
            "Research & National Lab Applications",
            "Support Scientific Work",
            "Accelerate scientific discovery with purpose-built tools for data analysis, collaboration, and secure research environments.",
            items=[
                "Scientific data visualization",
                "Experiment tracking and analysis",
                "Secure model exploration tools",
                "Internal research portals",
            ],
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t lg:divide-x divide-slate-3 max-lg:divide-y lg:border-b",
    )
