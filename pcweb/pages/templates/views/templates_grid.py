import reflex as rx
import reflex_ui as ui

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.components.marketing_button import button as marketing_button
from pcweb.constants import SCREENSHOT_BUCKET
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
        class_name="flex flex-row items-center gap-2 bg-white-1 px-2.5 border rounded-[0.625rem] relative [box-shadow:0_-1px_0_0_rgba(0,_0,_0,_0.08)_inset,_0_0_0_1px_rgba(0,_0,_0,_0.08)_inset,_0_1px_2px_0_rgba(0,_0,_0,_0.02),_0_1px_4px_0_rgba(0,_0,_0,_0.02)] text-sm placeholder:text-m-slate-7 dark:placeholder:text-m-slate-6 font-[475] focus:outline-none outline-none dark:border dark:border-m-slate-8 dark:bg-m-slate-9 h-9",
    )


def checkbox_item(item: TagWithCount) -> rx.Component:
    label = item["label"]
    count = item["count"]
    return ui.checkbox.root(
        rx.el.div(
            ui.checkbox.indicator(class_name="text-m-slate-12 dark:text-m-slate-3"),
            class_name="flex size-5 items-center justify-center rounded-sm bg-white dark:bg-m-slate-9 hover:bg-secondary-3 border border-m-slate-4 dark:border-m-slate-8",
        ),
        rx.el.span(
            label,
            class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[525] min-w-0 truncate group-hover:text-m-slate-12 dark:group-hover:text-m-slate-3",
        ),
        rx.el.span(
            count,
            class_name="text-m-slate-7 dark:text-m-slate-6 text-xs font-mono tabular-nums font-[415] ml-auto",
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
            class_name="text-m-slate-12 dark:text-m-slate-3 text-xs font-[525] font-mono py-1",
        ),
        rx.el.div(
            rx.foreach(TemplatesState.tags, checkbox_item),
            class_name="flex flex-col gap-1",
        ),
        class_name="flex flex-col gap-4",
    )


@rx.memo
def template_card(template: Template) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                f"{SCREENSHOT_BUCKET.strip('/')}/{template.id}",
                alt=template.title,
                loading="lazy",
                class_name="size-full object-cover rounded-sm object-top",
            ),
            class_name="px-2 pt-2 overflow-hidden max-h-[12.25rem] h-full",
        ),
        rx.el.div(
            rx.el.span(
                template.title,
                class_name="text-m-slate-12 dark:text-m-slate-3 text-base font-[525] mb-2",
            ),
            rx.el.span(
                template.difficulty,
                class_name=ui.cn(
                    "text-xs text-[0.75rem] font-[525] mb-2 capitalize",
                    rx.match(
                        template.difficulty.lower(),
                        ("beginner", "text-jade-10"),
                        ("intermediate", "text-amber-10"),
                        ("advanced", "text-primary-11"),
                        "text-primary-11",
                    ),
                ),
            ),
            rx.el.span(
                template.description,
                class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-medium mb-4",
            ),
            rx.el.div(
                rx.foreach(
                    template.tags,
                    lambda tag: rx.el.span(
                        f"#{tag}",
                        class_name="text-m-slate-7 dark:text-m-slate-6 text-xs font-[525] capitalize",
                    ),
                ),
                class_name="flex flex-wrap gap-4 empty:hidden mb-4",
            ),
            marketing_button(
                "Use Template",
                variant="outline",
                native_button=False,
                on_click=TemplatesState.redirect_to_template(template.id),
            ),
            class_name="p-6 flex flex-col",
        ),
        rx.el.a(
            href=f"/templates/{template.id}",
            target="_blank",
            class_name="absolute inset-0",
        ),
        key=template.id,
        class_name="flex flex-col bg-white dark:bg-m-slate-11 dark:border-m-slate-9 dark:border shadow-[0_1px_0_0_rgba(0,_0,_0,_0.04),0_1px_1px_0_rgba(0,_0,_0,_0.01),0_4px_8px_0_rgba(0,_0,_0,_0.03)] rounded-xl border border-slate-4 overflow-hidden isolate relative cursor-pointer",
    )


def templates_sidebar() -> rx.Component:
    return rx.box(
        rx.el.div(
            search_bar(),
            categories_checkboxes(),
            class_name=ui.cn(
                "flex flex-col gap-8 pr-6 py-8 overflow-y-auto overscroll-contain sticky",
                rx.cond(
                    HostingBannerState.is_banner_visible,
                    "top-[113px] h-[calc(100vh-113px)]",
                    "top-[77px] h-[calc(100vh-77px)]",
                ),
            ),
        ),
        class_name=(
            "w-[16.5rem] shrink-0 hidden lg:block z-10 border-r border-m-slate-4 dark:border-m-slate-10 relative "
            "before:content-[''] before:absolute before:top-0 before:bottom-0 before:right-0 before:w-[100vw] before:bg-white-1 dark:before:bg-m-slate-11 before:-z-10"
        ),
    )


def templates_grid() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "Templates",
                class_name="text-4xl font-[575] text-m-slate-12 dark:text-m-slate-3",
            ),
            rx.el.p(
                "Start building faster with production-ready Reflex templates.",
                class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-medium",
            ),
            class_name="flex flex-col gap-4",
        ),
        rx.el.div(
            rx.el.span(
                "No templates found for the current filters.",
                class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-medium only:block hidden",
            ),
            rx.foreach(
                TemplatesState.filtered_templates,
                lambda t: template_card(template=t),
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-4 gap-y-5",
        ),
        class_name="flex flex-col gap-12 flex-1 min-w-0 px-14 py-16",
    )
