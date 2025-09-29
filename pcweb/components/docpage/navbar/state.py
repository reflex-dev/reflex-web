"""The state for the navbar component."""

import reflex as rx


class NavbarState(rx.State):
    """The state for the navbar component."""

    # Whether the sidebar is open.
    sidebar_open: bool = False

    search_input: str = ""

    enter: bool = False

    banner: bool = True

    ai_chat: bool = True

    current_category = "All"

    @rx.event
    def set_sidebar_open(self, value: bool):
        self.sidebar_open = value

    @rx.event
    def toggle_banner(self):
        self.banner = not self.banner

    @rx.event
    def toggle_sidebar(self):
        self.sidebar_open = not self.sidebar_open

    @rx.event
    def toggle_ai_chat(self):
        self.ai_chat = not self.ai_chat

    @rx.event
    def update_category(self, tag):
        self.current_category = tag
