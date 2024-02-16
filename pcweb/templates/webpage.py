from typing import Callable

import reflex as rx
from pcweb import styles
from pcweb.route import Route

DEFAULT_TITLE = "Web Apps in Pure Python"


def webpage(path: str, title: str = DEFAULT_TITLE, props=None) -> Callable:
    """A template that most pages on the reflex.dev site should use.

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
            from pcweb.components.sidebar import sb

            # Wrap the component in the template.
            return rx.chakra.box(
                navbar(sidebar=sb),
                contents(*children, **props),
                footer(),
                **props,
            )

        return Route(
            path=path,
            title=title,
            component=wrapper,
        )

    return webpage
