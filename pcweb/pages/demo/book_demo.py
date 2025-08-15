import reflex as rx
from pcweb.pages.framework.index_colors import index_colors
from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.meta.meta import hosting_meta_tags
from pcweb.pages.demo.header import header

@rx.page(route="/demo", title="Reflex · Book Demo", meta=hosting_meta_tags)
def book_demo() -> rx.Component:
    """Get the Book Demo landing page."""
    from pcweb.components.docpage.navbar import navbar

    return rx.box(
        index_colors(),
        navbar(),
        rx.el.main(
            rx.box(
                header(),
                class_name="flex flex-col relative justify-center items-center w-full",
            ),
            class_name="flex flex-col w-full relative h-full justify-center items-center",
        ),
        footer_index(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )
