import reflex as rx

from pcweb.pages.use_cases.common.features_1 import feature_card


def features_1() -> rx.Component:
    return rx.el.section(
        feature_card(
            "Hospital02Icon",
            "Electronic Medical Record (EMR) & Patient Tools",
            items=[
                "Internal EMR viewers",
                "Patient intake dashboards",
                "Referral and triage portals",
                "Physician scheduling tools",
            ],
        ),
        feature_card(
            "TestTube02Icon",
            "Lab, Research & Clinical Ops Tools",
            items=[
                "Lab workflow management",
                "Clinical trials data dashboards",
                "Sample tracking and chain of custody",
                "Adverse event reporting systems",
            ],
        ),
        feature_card(
            "Analytics01Icon",
            "Healthcare Analytics & BI Dashboards",
            items=[
                "Outcomes tracking",
                "Operational KPIs",
                "Financial & claims analytics",
                "Provider performance dashboards",
            ],
        ),
        feature_card(
            "ArtificialIntelligence04Icon",
            "AI-Driven Assistants and RAG Chatbots",
            items=[
                "PHI-safe medical documentation assistants",
                "Staff support tools",
                "AI routing and triage helpers",
                "Knowledge base Q&A over internal documents",
            ],
        ),
        feature_card(
            "ShieldUserIcon",
            "Administrative & Compliance Automation",
            items=[
                "HIPAA training dashboards",
                "Staff credentialing systems",
                "Equipment & inventory management",
                "Audit reporting automation",
            ],
        ),
        feature_card(
            "UserMultipleIcon",
            "Patient & Staff Portals",
            items=[
                "Secure messaging",
                "Case management",
                "Payment flows",
                "Appointment scheduling",
            ],
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-l border-slate-3 relative overflow-hidden border-t",
    )
