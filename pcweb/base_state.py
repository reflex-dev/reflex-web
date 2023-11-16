"""The base application state."""

import reflex as rx


class State(rx.State):
    """The base state."""

    @rx.var
    def current_page(self) -> str:
        """The current page."""
        return self.router.page.full_path
