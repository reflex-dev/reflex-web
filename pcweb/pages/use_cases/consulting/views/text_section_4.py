import reflex as rx

from pcweb.pages.use_cases.common.text_section import text_section


def text_section_4() -> rx.Component:
    return text_section(
        header="Designed for Enterprise Clients",
        description="Reflex apps run entirely in client-approved environments, making them suitable for the most demanding enterprises. Reflex never sees client data. Ideal for consulting firms working with sensitive, regulated, or mission-critical systems.",
        class_name="border-t-0",
    )
