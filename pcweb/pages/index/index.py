import reflex as rx
from pcweb.templates import webpage

from .views.hero import hero
from .views.companies import companies
from pcweb.pages.index.components.stat import stat
from .views.deploy import deploy
from .views.open_source import open_source


@webpage(path="/", title="Reflex · Web apps in Pure Python")
def index() -> rx.Component:
    """Get the main Reflex landing page."""
    return rx.box(
        hero(),
        companies(),
        stat(stat="100K+", text="apps built with Reflex"),
        # Wrap reacts components here
        stat(stat="3,700+", text="community members"),
        # Backend preview here
        stat(stat="5,000+", text="projects created monthly"),
        deploy(),
        open_source(),
        class_name="flex flex-col gap-32 w-full max-w-[67rem] justify-center items-center mx-auto px-4 lg:px-5",
    )
