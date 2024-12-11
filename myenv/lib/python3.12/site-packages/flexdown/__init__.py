import reflex as rx

from .flexdown import Flexdown
from .document import Document


# The default Flexdown instance.
flexdown = Flexdown()


def parse(source) -> Document:
    """Parse a Flexdown document.

    Args:
        source: The source code of the Flexdown document.

    Returns:
        The parsed Flexdown document.
    """
    return Document.from_source(source)


def parse_file(path: str) -> Document:
    """Parse a Flexdown file.

    Args:
        path: The path to the Flexdown file.

    Returns:
        The parsed Flexdown document.
    """
    return Document.from_file(path)


def render(source: str, **kwargs) -> rx.Component:
    """Render Flexdown source code into a Reflex component.

    Args:
        source: The source code of the Flexdown file.
        **kwargs: The keyword arguments to pass to the Flexdown constructor.

    Returns:
        The Reflex component representing the Flexdown file.
    """
    return Flexdown(**kwargs).render(source)


def render_file(path: str, **kwargs) -> rx.Component:
    """Render a Flexdown file into a Reflex component.

    Args:
        path: The path to the Flexdown file.
        **kwargs: The keyword arguments to pass to the Flexdown constructor.

    Returns:
        The Reflex component representing the Flexdown file.
    """
    return Flexdown(**kwargs).render_file(path)


def app(path: str, **kwargs) -> rx.App:
    """Create a Reflex app from a directory of Flexdown files.

    Args:
        path: The path to the directory of Flexdown files.
        **kwargs: The keyword arguments to pass to the Flexdown constructor.

    Returns:
        The Reflex app representing the directory of Flexdown files.
    """

    class State(rx.State):
        pass

    return Flexdown(**kwargs).create_app(path)
