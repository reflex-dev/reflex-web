import reflex as rx

from pcweb.pages.use_cases.common.features_1 import feature_card


def features_1() -> rx.Component:
    return rx.el.section(
        feature_card(
            "Chart03Icon",
            "Client Dashboards & Executive Portals",
            items=[
                "Strategy and KPI dashboards",
                "Transformation progress trackers",
                "Financial and operational performance views",
                "C-suite-ready reporting apps",
            ],
        ),
        feature_card(
            "ArtificialIntelligence04Icon",
            "AI-Powered Advisory Tools",
            items=[
                "RAG chatbots over client documents",
                "Internal research assistants",
                "Scenario analysis and decision tools",
                "AI copilots for consultants and clients",
            ],
        ),
        feature_card(
            "Layers01Icon",
            "Internal Delivery Platforms",
            items=[
                "Engagement management tools",
                "Knowledge-base portals",
                "Staffing and utilization dashboards",
                "IP libraries and accelerators",
            ],
        ),
        feature_card(
            "FlowConnectionIcon",
            "Process & Workflow Automation",
            items=[
                "Data ingestion and validation apps",
                "Audit and compliance workflows",
                "Risk assessment tools",
                "Custom approval and review systems",
            ],
        ),
        feature_card(
            "PackageIcon",
            "Productized Consulting IP",
            items=[
                "Repeatable tools packaged across clients",
                "White-labeled internal platforms",
                "Subscription-style advisory software",
                "Embedded analytics inside client orgs",
            ],
        ),
        feature_card(
            "ChartUpIcon",
            "Analytics & Performance Tools",
            items=[
                "Custom BI dashboards",
                "Predictive modeling interfaces",
                "Data quality and monitoring apps",
                "Business intelligence reporting",
            ],
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-l border-slate-3 relative overflow-hidden border-t",
    )
