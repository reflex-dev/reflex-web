"""The base application state."""

import reflex as rx


class State(rx.State):
    """The base state."""

    @rx.var
    def current_page(self) -> str:
        """The current page."""
        page = self.router_data.get("headers", {}).get("origin", "") + self.get_current_page()
        print(page)
        return page