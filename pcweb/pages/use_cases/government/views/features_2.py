import reflex as rx

from pcweb.pages.use_cases.common.features_2 import feature_card


def features_2() -> rx.Component:
    return rx.el.section(
        feature_card(
            "WebDesign01Icon",
            "Internal Government Dashboards",
            "Track & Monitor Programs",
            "Build program performance dashboards, budgeting and spend oversight tools, policy impact analysis, and operations and service delivery tracking.",
        ),
        feature_card(
            "ArtificialIntelligence04Icon",
            "AI Assistants for Public Servants",
            "Empower Your Teams",
            "Create RAG chatbots over legislation and regulations, internal knowledge assistants, caseworker and analyst copilots, and research and document analysis tools.",
        ),
        feature_card(
            "FlowConnectionIcon",
            "Case, Permit & Workflow Systems",
            "Streamline Operations",
            "Develop case management tools, review and approval workflows, compliance and inspection apps, and grant and funding administration systems.",
        ),
        feature_card(
            "TestTube02Icon",
            "Research & National Lab Applications",
            "Support Scientific Work",
            "Build scientific data visualization, experiment tracking and analysis, secure model exploration tools, and internal research portals.",
        ),
        class_name="grid lg:grid-cols-4 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t lg:divide-x divide-slate-3 max-lg:divide-y lg:border-b",
    )
