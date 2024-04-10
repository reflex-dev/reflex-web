"""chatapp.py"""

import reflex as rx
from .components import chat, navbar


def chatapp() -> rx.Component:
    """The main app."""
    return rx.chakra.vstack(
        navbar(),
        chat.chat(),
        chat.action_bar(),
        background_color=rx.color("mauve", 1),
        color=rx.color("mauve", 12),
        align_items="stretch",
        spacing="0",
        height="100%",
        width="100%",
        theme=rx.theme(
            appearance="dark",
            accent_color="violet",
        )
    )

