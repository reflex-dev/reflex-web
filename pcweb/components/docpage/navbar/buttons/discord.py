import reflex as rx
from .style import button_style, new_button_style
from pcweb.components.icons.icons import get_icon
from pcweb.styles.colors import c_color
from pcweb.constants import DISCORD_URL


def discord() -> rx.Component:
    return rx.link(
        rx.flex(
            rx.image(
                src="/companies/light/discord.svg",
            ),
            padding="7px",
            style=button_style,
            border_radius="8px",
        ),
        href="https://discord.gg/T5WSbC2YtQ",
    )


def new_discord() -> rx.Component:
    return rx.link(
        rx.box(
            get_icon("discord", color=c_color("slate", 9)),
            height="32px",
            width="32px",
            style=new_button_style,
            _hover={
                "background-color": c_color("slate", 3),
            },
        ),
        underline="none",
        href=DISCORD_URL,
    )
