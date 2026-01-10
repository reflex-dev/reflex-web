import reflex as rx

from pcweb.pages.use_cases.common.features_2 import feature_card


def features_2() -> rx.Component:
    return rx.el.section(
        feature_card(
            "ArtificialIntelligence04Icon",
            "AI App Builder for Healthcare",
            "Build complete healthcare applications from a prompt",
            "Reflex AI generates Python code, UI components, and data connections — all editable and production-ready. Hear from Matt, CEO of Playspace: 'I just built an app and beyond impressed by the output. I asked claude to create a PRD from a URL/app that i wanted to copy. I uploaded the PDF to reflex and just said build this and it did, including some advanced capabilities like image and video generation within the app.'",
        ),
        feature_card(
            "ShieldKeyIcon",
            "HIPAA-Compliant by Design",
            "Self-host on your infrastructure with full control",
            "Self-host Reflex apps on your own infrastructure, VPC, or air-gapped environment with fully encrypted data and no external internet required. Perfect for PHI, clinical workflows, and sensitive analytics. Built for enterprise IT & compliance teams with full auditability, identity control and role-based access.",
        ),
        feature_card(
            "ZapIcon",
            "10x Faster Than Traditional Development",
            "Move from idea to deployed app in days, not months",
            "Reflex handles frontend, backend, state management, and deployment so your team can focus on patient outcomes and operational efficiency. Build production-grade healthcare apps without leaving Python or waiting on front-end teams.",
        ),
        feature_card(
            "PlugSocketIcon",
            "Designed for Data-Intensive Healthcare Workflows",
            "Native Python environment for all your integrations",
            "Integrate EMR data, HL7 & FHIR APIs, claims & billing systems, research databases, Snowflake, Postgres, Databricks, BigQuery, and clinical analytics & ML models — all in pure Python without switching contexts or languages.",
        ),
        class_name="grid lg:grid-cols-4 grid-cols-1 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t lg:divide-x divide-slate-3 max-lg:divide-y",
    )
