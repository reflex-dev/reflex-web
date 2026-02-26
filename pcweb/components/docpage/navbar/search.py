"""Search bar component for the navbar."""

from typing import Optional

import reflex as rx

from .inkeep import inkeep


def search_bar(
    custom_style: str = "", trigger: Optional[rx.Component] = None
) -> rx.Component:
    if trigger is None:
        return inkeep(custom_style=custom_style)

    return rx.el.div(
        trigger,
        rx.el.div(
            inkeep(custom_style=custom_style),
            class_name="absolute inset-0 z-10 opacity-0 overflow-hidden",
        ),
        class_name="relative inline-flex",
    )
