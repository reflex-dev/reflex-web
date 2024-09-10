import reflex as rx
from pcweb.templates import webpage

from .views.hero import hero
from .views.companies import companies
from .demos.demos import demo_section
from pcweb.pages.index.components.stat import stat
from .views.deploy import deploy
from .views.open_source import open_source
from .views.frontend_features import frontend_features
from pcweb.components.icons.patterns import new_patterns


@webpage(path="/", title="Reflex · Web apps in Pure Python")
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.box(
        *new_patterns(),
        hero(),
        demo_section(),
        companies(),
        frontend_features(),
        # stat(stat="100K+", text="apps built with Reflex"),
        # Wrap reacts components here
        rx.box(
            rx.box(
                stat(stat="3,700+", text="Community members"),
                stat(stat="5,000+", text="Projects created monthly"),
                class_name="flex flex-col lg:flex-row gap-32 w-full justify-center",
            ),
            deploy(),
            open_source(),
            class_name="flex flex-col gap-24 mt-32 w-full max-w-[67.25rem]",
        ),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5",
    )
