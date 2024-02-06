import reflex as rx
from .style import button_style



def discord() -> rx.Component:
    return rx.flex(
        rx.image(
            src="/companies/light/discord.svg",
        ),
        padding="7px",
        style=button_style,
        border_radius="8px",
    )