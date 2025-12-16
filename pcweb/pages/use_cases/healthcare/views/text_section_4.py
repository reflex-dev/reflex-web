import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_4() -> rx.Component:
    return text_section(
        header="HIPAA Compliance & Security",
        description="Reflex is purpose-built for regulated industries. Reflex does not transmit, store, or access PHI. Perfect for organizations needing complete security and observability.",
        class_name="border-t-0",
    )
