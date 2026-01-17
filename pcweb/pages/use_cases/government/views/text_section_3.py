import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_3() -> rx.Component:
    return text_section(
        header="Built for Government Security & Compliance",
        description="Reflex is purpose-built for regulated, high-assurance environments. Reflex does not access, transmit, or store government data. Agencies maintain full ownership and control at all times.",
        class_name="border-t-0",
    )
