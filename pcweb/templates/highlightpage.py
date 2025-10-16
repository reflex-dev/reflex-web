import functools
from typing import Callable

import reflex as rx

from pcweb.route import Route


def highlight_page(
    path: str,
    title: str = "",
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
            from pcweb.pages.customers.views.footer import footer_customer
            from pcweb.pages.framework.index_colors import index_colors
            from pcweb.views.bottom_section.bottom_section import bottom_section

            # Wrap the component in the template.
            return rx.box(
                rx.box(
                    index_colors(),
                    navbar(),
                    rx.el.main(
                        contents(*children, **props),
                        rx.box(class_name="flex-grow"),
                        class_name="w-full z-[1] relative flex flex-col justify-center mx-auto max-w-[640px] lg:px-0 px-4 pb-20",
                    ),
                    rx.box(class_name="h-[1px] bg-slate-3 w-full"),
                    bottom_section(),
                    footer_customer(),
                    class_name="relative flex flex-col justify-start items-center w-full h-full min-h-screen font-instrument-sans gap-4 mx-auto max-w-[64.19rem] lg:border-x border-slate-3 pt-24 lg:pt-48",
                ),
                class_name="relative overflow-hidden",
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
