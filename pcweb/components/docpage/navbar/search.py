"""Search bar component for the navbar."""

import reflex as rx
from .typesense import typesense_search


@rx.memo
def search_bar() -> rx.Component:
    return typesense_search()
