import reflex as rx

from pcweb.pages.use_cases.common.features_2 import feature_card


def features_2() -> rx.Component:
    return rx.el.section(
        feature_card(
            "ZapIcon",
            "Create initial prototypes easily",
            "Build without engineering resources",
            "Create initial prototype/gather requirements very quickly without engineering resources. Build full-stack applications from a prompt. Reflex AI generates Python backend logic, data pipelines, and UI components which are all editable, extensible, and ready for real client delivery. Use Reflex to:",
            items=[
                "Turn slideware into live applications",
                "Prototype fast, then deploy to production without rewrites",
                "Package IP into reusable, deployable tools",
            ],
            class_name="lg:border-b",
        ),
        feature_card(
            "RepeatIcon",
            "From Prototype to Production",
            "No rebuilds required",
            "Most consulting tools die as demos. Reflex apps are production-grade by default, meaning what you build for a pilot can be handed off, deployed, and operated long-term. Perfect for:",
            items=[
                "Proofs of concept",
                "MVPs for client programs",
                "Long-lived internal platforms",
                "Commercialized advisory products",
            ],
            class_name="lg:border-b",
        ),
        feature_card(
            "DashboardSpeed01Icon",
            "10x Faster Delivery",
            "No front-end teams needed",
            "Reflex handles frontend, backend, state, and deployment automatically. Your teams stay in Python and focus on business logic, analytics, and outcomes — not React, infra glue, or UI frameworks.",
            items=[
                "Frontend, backend, state, and deployment automation",
                "Python focus for business logic and analytics",
                "No React, infra glue, or UI frameworks",
            ],
        ),
        feature_card(
            "DatabaseIcon",
            "Built for Data-Heavy Work",
            "Integrate with client systems",
            "Reflex lets consulting teams seamlessly and securely integrate directly with a wide variety of client and third-party data sources, including:",
            items=[
                "Snowflake, Databricks, BigQuery",
                "Postgres, SQL Server, Oracle",
                "ERP, CRM, and operational systems",
                "ML models, forecasting pipelines, optimization engines",
                "APIs, flat files, and secure data rooms",
            ],
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t lg:divide-x divide-slate-3 max-lg:divide-y",
    )
