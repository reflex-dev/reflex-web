"""Search bar component for the navbar."""

import reflex as rx

from .inkeep import inkeep


@rx.memo
def search_bar(custom_style: str = "") -> rx.Component:
    return inkeep(custom_style=custom_style)
