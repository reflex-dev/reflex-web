import reflex as rx
from pcweb.templates import webpage

from .components.hero import hero_section
from .components.stats import stats
from .components.news_letter import news_letter_section
from .demos.demos import demos

@webpage(path="/", title="Reflex · Web apps in Pure Python")
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
        rx.tablet_and_desktop(
            rx.container(
                news_letter_section(),
                padding_x="3em",
                padding_y="10em",
            ),
        ),
        rx.container(
            stats(),
            padding_x="1em",
            padding_y="3em",
        ),
        width="100%",
        direction="column",
    )
