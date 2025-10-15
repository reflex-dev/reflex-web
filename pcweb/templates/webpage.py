import functools
from typing import Callable

import reflex as rx

from pcweb.route import Route

DEFAULT_TITLE = "Web Apps in Pure Python"


def webpage(
    path: str,
    title: str = DEFAULT_TITLE,
    description: str | None = None,
    image: str | None = None,
    meta: list[dict[str, str]] | None = None,
    props=None,
    add_as_page=True,
) -> Callable:
    """A template that most pages on the reflex.dev site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        path: The path of the page.
        title: The title of the page.
        description: The description of the page.
        image: The image to use for social media.
        meta: Additional meta tags to add to the page.
        props: Props to apply to the template.
        add_as_page: whether to add the route to the app pages.

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

        @functools.wraps(contents)
        def wrapper(*children, **props) -> rx.Component:
            """The template component.

            Args:
                children: The children components.
                props: The props to apply to the component.

            Returns:
                The component with the template applied.
            """
            # Import here to avoid circular imports.
            from pcweb.components.docpage.navbar import navbar
            from pcweb.components.icons.patterns import default_patterns
            from pcweb.views.bottom_section.bottom_section import bottom_section
            from pcweb.views.footer import footer

            # Wrap the component in the template.
            return rx.box(
                *default_patterns(),
                navbar(),
                rx.el.main(
                    contents(*children, **props),
                    rx.box(class_name="flex-grow"),
                    class_name="w-full z-[1]",
                ),
                bottom_section(),
                footer(),
                class_name="relative flex flex-col justify-start items-center w-full h-full min-h-screen font-instrument-sans overflow-hidden",
                **props,
            )

        return Route(
            path=path,
            title=title,
            description=description,
            image=image,
            meta=meta,
            component=wrapper,
            add_as_page=add_as_page,
        )

    return webpage
