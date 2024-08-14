import reflex as rx
from .style import new_button_style
from pcweb.styles.fonts import small
from pcweb.constants import GITHUB_STARS, GITHUB_URL
from pcweb.components.icons.icons import get_icon
from pcweb.styles.colors import c_color


def github_mobile() -> rx.Component:
    return rx.link(
        rx.flex(
            get_icon("github", color=c_color("slate", 9)),
            rx.text(
                f"{GITHUB_STARS/1000:.1f}K",
                color=c_color("slate", 9),
                style=small,
            ),
            gap="8px",
            style=new_button_style,
        ),
        href=GITHUB_URL,
        underline="none",
    )


def github() -> rx.Component:
    return rx.fragment(github_mobile())
