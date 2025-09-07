"""Search bar component for the navbar."""

import reflex as rx
from .search_component import reflex_fuzzy_search

@rx.memo
def search_bar():
    return reflex_fuzzy_search()
