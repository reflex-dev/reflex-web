import reflex as rx
from reflex import el

from .utils import add_pages


class State(rx.State):
    """The app state."""

    ...


def page(markup) -> rx.Component:
    """Create a page."""
    return el.div(
        *markup,
        class_name="container max-w-screen-md mx-auto py-12 flex flex-col gap-4",
    )


# Add state and page to the app.
app = rx.App(state=State)
add_pages(app, component=page)
app.compile()
