"""Search bar component for the navbar."""

import reflex as rx
from .inkeep import inkeep

def search_bar() -> rx.Component:
    return inkeep(width="100%", border_radius="8px")
