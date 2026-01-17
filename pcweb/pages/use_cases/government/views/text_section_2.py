import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_2() -> rx.Component:
    return text_section(
        header="What Governments Build with Reflex",
        description="Public sector organizations use Reflex to create secure, purpose-built applications with AI.",
        class_name="border-t-0",
    )
