import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_3() -> rx.Component:
    return text_section(
        header="The most powerful tool for Consulting Firms",
        description="Build full-stack applications from a prompt. Reflex AI generates Python backend logic, data pipelines, and UI components which are all editable, extensible, and ready for real client delivery.",
        class_name="border-t-0",
    )
