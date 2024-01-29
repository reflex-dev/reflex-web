import reflex as rx
from typing import Any, Optional, Set
import reflex.components.radix.themes as rdxt
from .style import button_style


def shorten_to_k(number):
    if number >= 1000:
        return "{:.0f}k+".format(number / 1000)
    else:
        return str(number)
    
def github() -> rx.Component:
    return rdxt.flex(
        rx.image(
            src="/icons/github/light.svg",
        ),
        rdxt.text(
            "Github",
            color=rx.color("mauve", 12),
        ),
        rdxt.text(
            "14k",
            color=rx.color("violet", 9),
            background=rx.color("violet", 4),
            border_radius="5px",
            padding="0px 3px",
        ),
        gap="2",
        style=button_style
    )