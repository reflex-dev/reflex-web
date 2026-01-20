import reflex as rx

from pcweb.pages.use_cases.common.faq import faq_section


def faq() -> rx.Component:
    return faq_section(
        faq_items=[
            (
                "Is Reflex suitable for client delivery?",
                "Yes. Reflex is used to deliver real, long-lived applications inside enterprise client environments — not just demos.",
            ),
            (
                "Do consultants need frontend or DevOps skills?",
                "No. Reflex abstracts frontend and deployment so teams can focus on Python, analytics, and business logic.",
            ),
            (
                "Can we reuse apps across multiple clients?",
                "Absolutely. Many firms build reusable templates and accelerators on Reflex and customize them per engagement.",
            ),
            (
                "Can Reflex support AI, analytics, and ML workloads?",
                "Yes. Reflex runs in Python and integrates directly with models, data pipelines, and AI services.",
            ),
            (
                "Can we deploy inside client infrastructure?",
                "Yes. Reflex supports VPC, on-prem, and air-gapped deployments to meet strict client requirements.",
            ),
        ],
    )
