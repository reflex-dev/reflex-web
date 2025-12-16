import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_1() -> rx.Component:
    return text_section(
        header="What You Can Build with Reflex",
        description="Healthcare organizations use Reflex to create fully custom applications using AI including:",
    )
