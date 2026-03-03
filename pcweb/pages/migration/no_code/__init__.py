import reflex as rx
import reflex_ui as ui

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.meta.meta import create_meta_tags
from pcweb.pages.about.views.divider import divider
from pcweb.pages.framework.views.footer_index import footer_index
from pcweb.pages.migration.no_code.views import compare, explore, hero, quotes
from pcweb.views.marketing_navbar import marketing_navbar


@rx.page(
    route="/migration/no-code",
    title="Switch from No Code to Reflex",
    meta=create_meta_tags(
        title="Switch from No Code to Reflex",
        description="Switch from No Code to Reflex - The platform to build and scale enterprise apps",
        image="/previews/index_preview.webp",
    ),
)
def no_code_migration_page() -> rx.Component:
    return rx.el.div(
        marketing_navbar(),
        rx.el.main(
            rx.el.div(
                hero(),
                quotes(),
                divider(),
                compare(),
                divider(),
                explore(),
                divider(),
                footer_index(),
                class_name="flex flex-col relative justify-center items-center w-full",
            ),
            class_name="flex flex-col w-full relative h-full justify-center items-center",
        ),
        class_name=ui.cn(
            "flex flex-col w-full justify-center items-center relative dark:bg-m-slate-12 bg-m-slate-1",
            rx.cond(
                HostingBannerState.is_banner_visible,
                "lg:pt-[7rem] pt-[3.5rem]",
                "lg:pt-[4.5rem] pt-[3.5rem]",
            ),
        ),
    )
