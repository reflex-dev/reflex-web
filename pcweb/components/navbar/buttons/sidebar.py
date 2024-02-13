import reflex as rx
from .style import button_style
from ...sidebar import sb



def sidebar_drawer(trigger):
    return rx.drawer.root(
        rx.drawer.trigger(trigger, as_child=True),
        #rx.drawer.overlay(),
        rx.drawer.portal(
            rx.drawer.content(
                rx.center(
                    rx.drawer.close(
                        rx.box(
                            height="1.5em",
                            width="6em",
                            border_radius="8px",
                            background_color = rx.color("mauve", 4),
                            margin_y="1em"
                        ),
                        as_child=True,
                    ),
                    sb,
                    flex_direction="column",
                    align_items="center",
                    justify_content = "center",
                    width="100%"
                ),
                top="80px",
                height="100%",
                width="100%",
                flex_direction="column",
                background_color="#FFF"
            ),
        )
    )


def sidebar_button() -> rx.Component:
    return rx.flex(
        sidebar_drawer(rx.icon("menu", color=rx.color("mauve", 9),)),
        padding="7px",
        style=button_style,
        border_radius="8px",
    )