import reflex as rx
from .style import button_style


def color() -> rx.Component:
    return rx.flex(
            rx.color_mode.icon(
                light_component=rx.icon("sun", color=rx.color("mauve", 9)),
                dark_component=rx.icon("moon", color=rx.color("mauve", 9)),
            ),
            padding="7px",
            style=button_style,
            border_radius="8px",
        )
