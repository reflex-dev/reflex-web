from typing import Callable

import reflex as rx
from pcweb.route import Route
from pcweb.meta.meta import meta_tags

DEFAULT_TITLE = "Web Apps in Pure Python"

def mainpage(
    path: str,
    title: str = DEFAULT_TITLE,
    description: str = None,
    image: str = None,
    meta: list[dict[str, str]] = meta_tags,
    props=None,
    add_as_page=True,
) -> Callable:
    """A template that most pages on the reflex.dev site should use.

    This template wraps the webpage with the navbar and footer.

    Args:
        path: The path of the page.
        title: The title of the page.
        props: Props to apply to the template.
        add_as_page: whether to add the route to the app pages.

    Returns:
        A wrapper function that returns the full webpage.
    """
    props = props or {}

    def mainpage(contents: Callable[[], Route]) -> Route:
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
            from pcweb.components.docpage.navbar import navbar
            from pcweb.pages.index.views.footer_index import footer_index
            from pcweb.pages.index.views.get_started import get_started
            from pcweb.pages.index.index_colors import index_colors

            # Wrap the component in the template.
            return rx.box(
                index_colors(),
                navbar(),
                rx.el.main(
                    contents(*children, **props),
                    get_started(),
                    class_name="flex flex-col w-full justify-center items-center",
                ),
                footer_index(),
                class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
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

    return mainpage
