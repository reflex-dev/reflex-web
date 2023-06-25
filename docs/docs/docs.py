import pynecone as pc
from pynecone import el

from .utils import add_pages


class State(pc.State):
    """The app state."""

    ...


def page(markup) -> pc.Component:
    """Create a page."""
    return el.div(
        *markup,
        class_name="container max-w-screen-md mx-auto py-12 flex flex-col gap-4",
    )


# Add state and page to the app.
app = pc.App(state=State)
add_pages(app, component=page)
app.compile()
