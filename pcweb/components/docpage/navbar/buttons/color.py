import reflex as rx
from .style import new_button_style
from pcweb.styles.colors import c_color


from reflex.style import toggle_color_mode


def color() -> rx.Component:
    return rx.el.button(
        rx.color_mode.icon(
            light_component=rx.icon("sun", color=c_color("slate", 9), size=16),
            dark_component=rx.icon("moon", color=c_color("slate", 9), size=16),
        ),
        style=new_button_style,
        width="32px",
        padding="0px",
        on_click=toggle_color_mode,
    )
