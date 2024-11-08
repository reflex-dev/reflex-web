"""Search bar component for the navbar."""

import reflex as rx
from .inkeep import inkeep

@rx.memo
def search_bar() -> rx.Component:
    return rx.box(inkeep(), class_name="w-full h-full min-w-0 max-w-[256px] max-h-[32px]")