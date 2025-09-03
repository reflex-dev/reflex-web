import reflex as rx
from pcweb.pages.framework.index_colors import index_colors
from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.meta.meta import meta_tags
from pcweb.pages.demo.header import header
from pcweb.templates.mainpage import mainpage
from pcweb.components.icons.patterns import default_patterns


@mainpage(path="/demo", title="Reflex · Book Demo", meta=meta_tags)
def book_demo() -> rx.Component:
    """Get the Book Demo landing page."""

    return rx.el.main(
        rx.el.section(
            *default_patterns(),
            header(),
            class_name="overflow-hidden w-full relative mx-auto flex flex-col justify-center items-center max-w-[64.19rem]",
        ),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )
