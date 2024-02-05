import reflex as rx
from typing import Any, Optional, Set
import reflex.components.radix.themes as rdxt
from .style import button_style



def discord() -> rx.Component:
    return rdxt.flex(
        rx.image(
            src="/companies/light/discord.svg",
        ),
        padding="7px",
        style=button_style,
        border_radius="8px",
    )