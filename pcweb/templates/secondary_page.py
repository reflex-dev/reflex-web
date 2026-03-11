import functools
from typing import Callable

import reflex as rx
import reflex_ui as ui
from reflex.event import EventType

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.route import Route

DEFAULT_TITLE = "The platform to build and scale enterprise apps"
DEFAULT_DESCRIPTION = "Build secure internal apps with AI. Deploy on prem or cloud with governance. Technical and nontechnical teams ship together."


def secondary_page(
    path: str,
    title: str = DEFAULT_TITLE,
    description: str | None = DEFAULT_DESCRIPTION,
    image: str | None = None,
    meta: list[dict[str, str]] | None = None,
    props=None,
    add_as_page=True,
    on_load: EventType[()] | None = None,
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
        on_load: The function to call when the page is loaded.

    Returns:
        A wrapper function that returns the full webpage.
    """
    props = props or {}

    def secondary_page(contents: Callable[[], Route]) -> Route:
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
            from pcweb.views.docs_navbar import docs_navbar

            # Wrap the component in the template.
            return rx.el.div(
                docs_navbar(),
                rx.el.main(
                    rx.el.div(
                        contents(*children, **props),
                        class_name="flex flex-col relative justify-center items-center w-full",
                    ),
                    class_name=ui.cn(
                        "flex flex-col w-full relative h-full justify-center items-center",
                        rx.cond(
                            HostingBannerState.is_banner_visible,
                            "mt-28",
                            "mt-16",
                        ),
                    ),
                ),
                class_name="flex flex-col w-full justify-center items-center relative dark:bg-m-slate-12 bg-m-slate-1",
            )

        return Route(
            path=path,
            title=title,
            description=description,
            image=image,
            meta=meta,
            component=wrapper,
            add_as_page=add_as_page,
            on_load=on_load,
        )

    return secondary_page
