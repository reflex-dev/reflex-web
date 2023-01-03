"""Manage routing for the application."""

import inspect
from typing import Callable

import pynecone as pc
from pynecone.base import Base


class Route(Base):
    """A page route."""

    # The path of the route.
    path: str

    # The page title.
    title: str | None = None

    # The component to render for the route.
    component: pc.Component | Callable[[], pc.Component]


def get_path(component_fn: Callable):
    """Get the path for a page based on the file location.

    Args:
        component_fn: The component function for the page.
    """
    module = inspect.getmodule(component_fn)

    # Create a path based on the module name.
    return module.__name__.replace(".", "/").replace("_", "-").split("pcweb/pages")[1]
