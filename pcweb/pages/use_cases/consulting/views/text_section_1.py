import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_1() -> rx.Component:
    return text_section(
        header="Consulting Firms Build their Client Apps with Reflex",
        description="Consulting teams use Reflex to create reusable, client-ready applications with AI.",
    )
