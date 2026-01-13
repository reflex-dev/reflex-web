import reflex as rx

from pcweb.pages.use_cases.common.faq import faq_section


def faq() -> rx.Component:
    return faq_section(
        [
            (
                "Is Reflex suitable for government use?",
                "Yes. Reflex is already used by government agencies, public institutions, and national labs for real production systems.",
            ),
            (
                "Can Reflex run in restricted or air-gapped environments?",
                "Yes. Reflex supports fully isolated deployments with no external internet access.",
            ),
            (
                "Do teams need frontend or cloud expertise?",
                "No. Reflex abstracts frontend and deployment so teams can focus on Python and mission logic.",
            ),
            (
                "Can Reflex integrate with existing government systems?",
                "Yes. Reflex runs in Python, making integration with internal databases, APIs, and legacy systems straightforward.",
            ),
            (
                "Can Reflex be used for AI and analytics?",
                "Absolutely. Reflex supports AI assistants, analytics dashboards, and ML-powered tools — fully inside government infrastructure.",
            ),
        ]
    )
