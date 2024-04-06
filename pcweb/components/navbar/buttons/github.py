import reflex as rx
from .style import button_style


def github_mobile() -> rx.Component:
    return rx.link(
        rx.flex(
            rx.icon(
                "github",
                color=rx.color("mauve", 9),
            ),
            padding="7px",
            style=button_style,
            border_radius="8px",
        ),
        href="https://github.com/reflex-dev/reflex",
    )


def github() -> rx.Component:
    return rx.fragment(
        github_mobile()
    )                             