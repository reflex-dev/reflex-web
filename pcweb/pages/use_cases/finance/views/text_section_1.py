import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_1() -> rx.Component:
    return text_section(
        header="Balance Resilience and Innovation",
        description="Financial organizations are under pressure from every side: volatile markets, new regulations, GenAI, and rising expectations. Most internal tools haven't kept up.",
        class_name="border-t-0",
    )
