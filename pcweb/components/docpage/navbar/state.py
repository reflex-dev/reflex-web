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

    def toggle_banner(self) -> None:
        self.banner = not self.banner

    def toggle_sidebar(self) -> None:
        self.sidebar_open = not self.sidebar_open

    def toggle_ai_chat(self) -> None:
        self.ai_chat = not self.ai_chat

    def update_category(
        self,
        tag,
    ) -> None:
        self.current_category = tag
