from typing import Callable
from pcweb import styles

import reflex as rx

from pcweb.route import Route

DEFAULT_TITLE = "Reflex: The easiest way to build web apps."


def webpage(path: str, title: str = DEFAULT_TITLE, props=None) -> Callable:
    """A template that most pages on the pynecone.io site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        path: The path of the page.
        title: The title of the page.
        props: Props to apply to the template.

    Returns:
        A wrapper function that returns the full webpage.
    """
    props = props or {}

    def webpage(contents: Callable[[], Route]) -> Route:
        """Wrapper to create a templated route.

        Args:
            contents: The function to create the page route.

        Returns:
            The templated route.
        """

        def wrapper(*children, **props) -> rx.Component:
            """The template component.

            Args:
                children: The children components.
                props: The props to apply to the component.

            Returns:
                The component with the template applied.
            """
            # Import here to avoid circular imports.
            from pcweb.components.footer import footer
            from pcweb.components.navbar import navbar

            # Wrap the component in the template.
            return rx.box(
                navbar(),
                contents(*children, **props),
                footer(),
                font_family=styles.SANS,
                **props
            )

        return Route(
            path=path,
            title=title,
            component=wrapper,
        )

    return webpage
