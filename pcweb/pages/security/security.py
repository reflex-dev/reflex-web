"""Main security page implementation."""

import reflex as rx
from pcweb.templates.mainpage import mainpage
from .views import security_title, security_grid, features_table_section


@mainpage(path="/security", title="Security - Reflex")
def security():
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
