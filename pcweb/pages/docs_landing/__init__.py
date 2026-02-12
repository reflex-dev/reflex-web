import reflex as rx

from pcweb.meta.meta import create_meta_tags
from pcweb.pages.docs_landing.views import (
    ai_builder_section,
    divider,
    enterprise_section,
    framework,
    hero,
    hosting_section,
    other_section,
    self_hosting_section,
)
from pcweb.views.docs_navbar import docs_navbar


@rx.page(
    route="/docs",
    title="Reflex · Docs",
    meta=create_meta_tags(
        title="Reflex · Docs",
        description="Docs for Reflex - The platform to build and scale enterprise apps",
        image="/previews/index_preview.webp",
    ),
)
def docs_landing() -> rx.Component:
    return rx.el.div(
        docs_navbar(),
        rx.el.main(
            rx.el.div(
                hero(),
                divider(),
                ai_builder_section(),
                framework(),
                enterprise_section(),
                hosting_section(),
                self_hosting_section(),
                other_section(),
                class_name="flex flex-col relative justify-center items-center w-full",
            ),
            class_name="flex flex-col w-full relative h-full justify-center items-center",
        ),
        class_name="flex flex-col w-full justify-center items-center relative",
    )
