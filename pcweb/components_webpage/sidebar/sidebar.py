"""Logic for the sidebar component."""

from __future__ import annotations

import reflex as rx


def sidebar(url=None, width: str = "100%") -> rx.Component:
    """Render the sidebar."""


    return rx.flex(
        
        width="100%",
        height="100%",
        justify="end",
    )


sb = sidebar(width="100%")
