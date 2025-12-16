import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_3() -> rx.Component:
    return text_section(
        header="Why Healthcare Teams Choose Reflex",
        description="Reflex offers the speed of no-code with the power of full-code, ideal for healthcare. Healthcare organizations use Reflex to create fully custom applications using AI including:",
        class_name="border-t-0",
    )
