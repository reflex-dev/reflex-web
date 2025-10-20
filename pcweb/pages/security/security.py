"""Main security page implementation."""

import reflex as rx

from pcweb.templates.mainpage import mainpage

from .views import features_table_section, security_grid, security_title


@mainpage(path="/security", title="Security - Reflex")
def security_page() -> rx.Component:
    """Main security page with modular sections."""
    return rx.box(
        rx.box(
            security_title(),
            security_grid(),
            features_table_section(),
            class_name="flex flex-col relative justify-center items-center w-full",
        ),
        class_name="flex flex-col w-full",
    )
