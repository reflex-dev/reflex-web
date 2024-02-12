import reflex as rx
from .style import button_style



def sidebar_button() -> rx.Component:
    return rx.flex(
        rx.icon("menu"),
        padding="7px",
        style=button_style,
        border_radius="8px",
    )