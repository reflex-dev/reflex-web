import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_1() -> rx.Component:
    return text_section(
        header="Why Government Teams Choose Reflex",
        description="Reflex powers mission-critical internal applications used by public servants, analysts, and researchers. Government organizations choose Reflex to modernize systems faster — without compromising security or control.",
        class_name="border-t-0",
    )
