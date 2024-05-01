import reflex as rx
from pcweb.templates import webpage

from .components.hero import hero_section
from .components.stats import stats
from .demos.demos import demos

@webpage(path="/testapp", title="Reflex · Web apps in Pure Python")
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.flex(
        rx.container(
            hero_section(),
            padding_top="3em",
            padding_bottom="3em",
        ),
        rx.container(
            demos(),
            padding_x="1em",
        ),
        rx.container(
            stats(),
            padding_x="1em",
        ),
        width="100%",
        direction="column",
    )
