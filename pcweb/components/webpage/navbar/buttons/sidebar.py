import reflex as rx
from .style import button_style


def sidebar_drawer(sidebar: rx.Component, trigger):
    return rx.drawer.root(
        rx.drawer.trigger(trigger, as_child=True),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.drawer.close(
                        rx.box(
                            height=".25em",
                            width="6em",
                            border_radius="8px",
                            background_color="#6f6d78",
                            margin_y="1em",
                        ),
                        as_child=True,
                    ),
                    sidebar,
                    width="100%",
                ),
                height="100%",
                width="100%",
                flex_direction="column",
                background="linear-gradient(180deg, rgba(29, 27, 33, 0.95) 0%, rgba(20, 19, 24, 0.95) 100%);",
                backdrop_filter="blur(20px)",
            ),
        ),
        direction="top", 
    )
 

def sidebar_button(sidebar) -> rx.Component:
    return rx.flex(
        sidebar_drawer(
            sidebar,
            rx.icon(
                "menu",
                color="#6f6d78",
            ),
        ),
        padding="7px",
        style=button_style,
        border_radius="8px",
    )
