import reflex as rx
from .style import button_style


def discord() -> rx.Component:
    return rx.link(
        rx.flex(
            rx.image(
                src="/companies/light/discord.svg",
                alt="Discord",
            ),
            padding="7px",
            style=button_style,
            border_radius="8px",
        ),
        href="https://discord.gg/T5WSbC2YtQ",
    )
