import reflex as rx

from pcweb.pages.use_cases.common.faq import faq_section


def faq() -> rx.Component:
    return faq_section(
        faq_items=[
            (
                "Is Reflex HIPAA-compliant?",
                "Yes, both the Reflex Builder and the Reflex apps can be deployed in fully self-hosted, HIPAA-compliant environments with PHI remaining entirely under your control.",
            ),
            (
                "Do I need frontend experience?",
                "No. Reflex handles frontend automatically. You type Prompts or write Python; Reflex generates the UI and the backend together.",
            ),
            (
                "Can non-developers use the AI builder?",
                "Yes, the AI builder allows clinicians, analysts, and operations teams to generate apps from natural-language prompts.",
            ),
            (
                "Can Reflex replace spreadsheets?",
                "Absolutely, many healthcare teams use Reflex to create secure, auditable, workflow-specific replacements.",
            ),
            (
                "Can I integrate with (Epic / Cerner / Athena / HL7 / FHIR)?",
                "Yes, Reflex runs in Python, so integrations are straightforward using Premium built-in integrations or using available SDKs or APIs.",
            ),
        ],
    )
