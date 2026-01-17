import reflex as rx

from pcweb.pages.use_cases.common.features_1 import feature_card


def features_1() -> rx.Component:
    return rx.el.section(
        feature_card(
            "ArtificialIntelligence04Icon",
            "AI App Builder for the Public Sector",
            description="Build complete government applications from a prompt. Reflex AI generates Python logic, UIs, and secure data integrations — all fully editable and suitable for production use in public sector environments.",
            items=[
                "Modernize legacy workflows without full rewrites",
                "Turn policy ideas into real software fast",
                "Support analysts, operators, and researchers with AI tools",
            ],
        ),
        feature_card(
            "ShieldEnergyIcon",
            "Built for Secure, Controlled Environments",
            description="Reflex is designed to run entirely inside government infrastructure, including VPCs, on-prem data centers, and air-gapped networks. Perfect for:",
            items=[
                "Sensitive citizen data",
                "Regulatory and compliance workflows",
                "National security and research environments",
                "Restricted or offline deployments",
            ],
        ),
        feature_card(
            "DashboardSpeed01Icon",
            "10x Faster Than Traditional Government IT Projects",
            description="Move from requirements → deployed app in weeks instead of years. Reflex removes frontend and infrastructure bottlenecks so small teams can ship meaningful systems quickly.",
            items=[
                "No React",
                "No fragile prototypes",
                "No rebuilds after pilots",
            ],
        ),
        feature_card(
            "DatabaseIcon",
            "Designed for Data-Heavy Government Work",
            description="Reflex being in Pure Python makes it easy to integrate with existing public sector systems:",
            items=[
                "Internal databases and data warehouses",
                "Case management and registry systems",
                "Geospatial and census datasets",
                "Research, modeling, and simulation pipelines",
                "Secure APIs and document repositories",
            ],
        ),
        class_name="grid lg:grid-cols-2 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-l border-slate-3 relative overflow-hidden border-t",
    )
