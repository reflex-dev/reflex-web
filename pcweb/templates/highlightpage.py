import reflex as rx

from reflex.event import EventType
from typing import Callable, Any
from pcweb.components.docpage.navbar import navbar
from pcweb.pages.customers.views.footer import footer_customer
from pcweb.views.bottom_section.bottom_section import bottom_section
from pcweb.pages.framework.index_colors import index_colors

def highlight_page(
    route: str | None = None,
    title: str | None = None,
    image: str | None = None,
    description: str | None = None,
    meta: list[Any] | None = None,
    script_tags: list[Any] | None = None,
    on_load: EventType[()] | None = None,
) -> Callable[[Callable[[], rx.Component]], Callable[[], rx.Component]]:
    """Decorator that wraps a page's main content in a consistent layout and registers it with rx.page."""

    def decorator(page_func: Callable[[], rx.Component]) -> Callable[[], rx.Component]:
        @rx.page(
            route=route,
            title=title,
            image=image,
            description=description,
            meta=meta,
            script_tags=script_tags,
            on_load=on_load,
        )
        def wrapped_page() -> rx.Component:
            content = page_func()
            return rx.box(
                rx.box(
                    index_colors(),
                    navbar(),
                    rx.el.main(
                        content,
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

        return wrapped_page

    return decorator
