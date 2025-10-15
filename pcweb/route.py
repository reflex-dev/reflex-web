"""Manage routing for the application."""

import inspect
from typing import Callable

import reflex as rx
from reflex.base import Base


class Route(Base):
    """A page route."""

    # The path of the route.
    path: str

    # The page title.
    title: str | None = None

    # The page description.
    description: str | None = None

    # The page image.
    image: str | None = None

    # The page extra meta data.
    meta: list[dict[str, str]] | None = None

    # Background color for the page.
    background_color: str | None = None

    # The component to render for the route.
    component: Callable[[], rx.Component]

    # whether to add the route to the app's pages. This is typically used
    # to delay adding the 404 page(which is explicitly added in pcweb.py).
    # https://github.com/reflex-dev/reflex-web/pull/659#pullrequestreview-2021171902
    add_as_page: bool = True

    def __hash__(self):
        """Hash the route based on the path and title."""
        return hash(f"{self.path}-{self.title}")


def get_path(component_fn: Callable):
    """Get the path for a page based on the file location.

    Args:
        component_fn: The component function for the page.
    """
    module = inspect.getmodule(component_fn)

    # Create a path based on the module name.
    return (
        module.__name__.replace(".", "/").replace("_", "-").split("pcweb/pages")[1]
        + "/"
    )
