"""Search bar component for the navbar."""

import reflex as rx
from .typesense import typesense_search_with_styles


@rx.memo
def search_bar() -> rx.Component:
    return typesense_search_with_styles()
