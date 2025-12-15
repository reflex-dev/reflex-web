import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_3() -> rx.Component:
    return text_section(
        header="Why Financial Organizations Choose Reflex",
        description="From global banks to agile fintechs, see how teams are transforming their internal tools with Reflex.",
        class_name="border-t-0",
    )
