import reflex as rx
import reflex_ui as ui

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.components.marketing_button import button as marketing_button
from pcweb.constants import REFLEX_ASSETS_CDN, SCREENSHOT_BUCKET
from pcweb.pages.templates.templates_state import TagWithCount, Template, TemplatesState


def search_bar() -> rx.Component:
    return rx.el.div(
        ui.icon(
            "Search01Icon",
        ),
        rx.el.input(
            placeholder="Search templates...",
            default_value=TemplatesState.query,
            type="text",
            on_change=TemplatesState.set_query,
            class_name="outline-none focus:outline-none w-full",
        ),
        class_name="flex flex-row items-center gap-2 bg-white-1 px-2.5 rounded-[0.625rem] relative [box-shadow:0_-1px_0_0_rgba(0,_0,_0,_0.08)_inset,_0_0_0_1px_rgba(0,_0,_0,_0.08)_inset,_0_1px_2px_0_rgba(0,_0,_0,_0.02),_0_1px_4px_0_rgba(0,_0,_0,_0.02)] text-sm placeholder:text-secondary-9 font-[475] focus:outline-none outline-none dark:border border-secondary-a6 h-9",
    )


def checkbox_item(item: TagWithCount) -> rx.Component:
    label = item["label"]
    count = item["count"]
    return ui.checkbox.root(
        rx.el.div(
            ui.checkbox.indicator(class_name="text-secondary-12"),
            class_name="flex size-5 items-center justify-center rounded-sm bg-white-1 dark:bg-secondary-1 hover:bg-secondary-3 border border-secondary-a4",
        ),
        rx.el.span(
            label,
            class_name="text-secondary-11 text-sm font-[525] min-w-0 truncate group-hover:text-secondary-12 capitalize",
        ),
        rx.el.span(
            count,
            class_name="text-secondary-11 text-xs font-mono tabular-nums font-[415] ml-auto",
        ),
        key=label,
        unstyled=True,
        checked=TemplatesState.checked_tags.contains(label),
        on_checked_change=lambda checked: TemplatesState.toggle_tag(label, checked),
        class_name="flex flex-row items-center gap-3 min-h-8 min-w-0 cursor-pointer group",
    )


def categories_checkboxes() -> rx.Component:
    return rx.el.div(
        rx.el.span(
            "CATEGORY",
            class_name="text-secondary-12 text-xs font-[525] font-mono py-1",
        ),
        rx.el.div(
            rx.foreach(TemplatesState.tags, checkbox_item),
            class_name="flex flex-col gap-1",
        ),
        class_name="flex flex-col gap-4",
    )


def image_text_placeholder() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=f"{REFLEX_ASSETS_CDN}/logos/{rx.color_mode_cond(light='light', dark='dark')}/reflex.svg",
                class_name="h-3.5 lg:h-5 w-auto opacity-70 dark:opacity-85 group-hover:scale-105 duration-200 ease-out",
                alt="Logo",
            ),
            class_name="flex flex-row items-center justify-center h-full w-full rounded-[12px] relative overflow-hidden p-4",
        ),
        class_name="absolute inset-0 h-full w-full bg-white-1",
    )


@rx.memo
def template_card(template: Template) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                image_text_placeholder(),
                ui.avatar.root(
                    ui.avatar.image(
                        src=f"{SCREENSHOT_BUCKET.strip('/')}/{template.id}",
                        loading="lazy",
                    ),
                    unstyled=True,
                    class_name="group-hover:scale-105 duration-200 ease-out object-top object-cover absolute inset-0 size-full transition-all",
                ),
                class_name="relative h-[12.25rem] overflow-hidden rounded-t-lg",
            ),
            class_name="flex-shrink-0 px-2 pt-2",
        ),
        rx.el.div(
            rx.el.span(
                template.name,
                class_name="text-secondary-12 text-base font-[525] mb-2",
            ),
            rx.el.span(
                template.description,
                class_name="text-secondary-10 text-sm font-medium mb-4",
            ),
            rx.el.div(
                rx.foreach(
                    template.tags,
                    lambda tag: rx.el.span(
                        f"#{tag}",
                        class_name="text-secondary-10 text-xs font-[525] capitalize",
                    ),
                ),
                class_name="flex flex-wrap gap-4 empty:hidden mb-4",
            ),
            marketing_button(
                "Use Template",
                variant="outline",
                native_button=False,
                on_click=TemplatesState.redirect_to_template(
                    template_id=template.id,
                    use_prompt=True,
                ).stop_propagation,
                class_name="relative z-10 mt-auto dark:hover:bg-secondary-2",
            ),
            class_name="p-6 flex flex-col h-full",
        ),
        rx.el.a(
            href=f"/templates/{template.slug}/{template.id}",
            class_name="absolute inset-0",
        ),
        on_mouse_enter=TemplatesState.prefetch_template(template.id),
        key=template.id,
        class_name="flex flex-col bg-white-1 dark:bg-m-slate-11 border-secondary-a4 dark:border shadow-[0_1px_0_0_rgba(0,_0,_0,_0.04),0_1px_1px_0_rgba(0,_0,_0,_0.01),0_4px_8px_0_rgba(0,_0,_0,_0.03)] rounded-xl border overflow-hidden isolate relative cursor-pointer group",
    )


def templates_sidebar() -> rx.Component:
    return rx.box(
        rx.el.div(
            search_bar(),
            categories_checkboxes(),
            class_name=ui.cn(
                "flex flex-col gap-8 pr-6 py-8 2xl:pl-0 pl-6 overflow-y-auto sticky",
                rx.cond(
                    HostingBannerState.is_banner_visible,
                    "top-[113px] h-[calc(100vh-113px)]",
                    "top-[77px] h-[calc(100vh-77px)]",
                ),
            ),
        ),
        class_name=(
            "w-[16.5rem] shrink-0 hidden lg:block z-10 border-r border-secondary-a4 relative "
            "before:content-[''] before:absolute before:top-0 before:bottom-0 before:right-0 before:w-[100vw] before:bg-white-1 dark:before:bg-secondary-1 before:-z-10 max-xl:hidden"
        ),
    )


def templates_grid() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Templates",
                class_name="text-4xl font-[575] text-secondary-12",
            ),
            rx.el.p(
                "Start building faster with production-ready Reflex templates.",
                class_name="text-secondary-11 text-sm font-medium",
            ),
            class_name="flex flex-col gap-4",
        ),
        rx.cond(
            TemplatesState.is_loading,
            rx.el.div(
                ui.spinner(),
                rx.el.span(
                    "Loading templates...",
                ),
                class_name="flex flex-row items-center gap-2 text-sm font-[525] text-secondary-11",
            ),
            rx.el.div(
                rx.cond(
                    TemplatesState.is_hydrated,
                    rx.el.span(
                        "No templates found for the current filters.",
                        class_name="text-secondary-11 text-sm font-medium only:block hidden",
                    ),
                ),
                rx.foreach(
                    TemplatesState.filtered_templates,
                    lambda t: template_card(template=t),
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4 gap-x-4 gap-y-5",
            ),
        ),
        class_name="flex flex-col gap-12 flex-1 min-w-0 lg:px-14 px-4 lg:py-16 py-10",
    )
