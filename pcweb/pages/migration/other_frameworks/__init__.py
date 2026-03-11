import reflex as rx

from pcweb.meta.meta import create_meta_tags
from pcweb.pages.about.views.divider import divider
from pcweb.pages.migration.other_frameworks.views import compare, explore, hero, quotes
from pcweb.templates.marketing_page import marketing_page


@marketing_page(
    path="/migration/other-frameworks",
    title="Switch from Other Frameworks to Reflex",
    meta=create_meta_tags(
        title="Switch from Other Frameworks to Reflex",
        description="Switch from Other Frameworks to Reflex - The platform to build and scale enterprise apps",
        image="/previews/low_code_migration_preview.webp",
    ),
)
def other_frameworks_migration_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            hero(),
            quotes(),
            divider(),
            compare(),
            divider(),
            explore(),
            class_name="flex flex-col relative justify-center items-center w-full",
        ),
        class_name="flex flex-col w-full relative h-full justify-center items-center",
    )
