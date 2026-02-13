import reflex as rx

from pcweb.meta.meta import create_meta_tags
from pcweb.pages.about.views import (
    cards,
    companies,
    divider,
    hero,
    hiring,
    news,
    square_logo,
    team,
)
from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.views.marketing_navbar import marketing_navbar


@rx.page(
    route="/about",
    title="Reflex · About",
    meta=create_meta_tags(
        title="Reflex · About",
        description="About Reflex - The platform to build and scale enterprise apps",
        image="/previews/index_preview.webp",
    ),
)
def about() -> rx.Component:
    return rx.el.div(
        marketing_navbar(),
        rx.el.main(
            rx.el.div(
                hero(),
                companies(),
                square_logo(),
                cards(),
                divider(),
                hiring(),
                team(),
                news(),
                divider(),
                footer_index(),
                class_name="flex flex-col relative justify-center items-center w-full",
            ),
            class_name="flex flex-col w-full relative h-full justify-center items-center",
        ),
        class_name="flex flex-col w-full justify-center items-center relative dark:bg-m-slate-12 bg-m-slate-1",
    )
