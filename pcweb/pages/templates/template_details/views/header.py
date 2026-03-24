import reflex as rx
import reflex_ui as ui

from pcweb.components.marketing_button import button as marketing_button
from pcweb.constants import SCREENSHOT_BUCKET
from pcweb.pages.templates.templates_state import TemplatesState


def app_top_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("BrowserIcon"),
            rx.el.span(
                "Preview",
                class_name="text-sm text-secondary-12 font-semibold",
            ),
            class_name="flex flex-row gap-2.5 items-center h-full border-b border-primary-9",
        ),
        rx.el.div(
            ui.icon("SourceCodeIcon"),
            rx.el.span(
                "Code",
                class_name="text-sm font-medium",
            ),
            class_name="flex flex-row gap-2.5 items-center h-full text-secondary-11",
        ),
        rx.el.div(
            rx.el.div(
                ui.icon("Refresh04Icon"),
                class_name="size-9 flex items-center justify-center bg-secondary-1 text-secondary-10",
            ),
            rx.el.div(
                ui.icon("ArrowDown01Icon", class_name="text-secondary-10"),
                "/index",
                class_name="flex items-center gap-2.5 h-full text-secondary-12 px-2.5 bg-white-1 w-[12.5rem] text-sm font-medium",
            ),
            rx.el.div(
                ui.icon("LinkSquare02Icon"),
                class_name="size-9 flex items-center justify-center bg-secondary-1 text-secondary-10",
            ),
            class_name="flex flex-row items-center rounded-[0.625rem] border border-secondary-5 h-9 overflow-hidden divide-x divide-secondary-5",
        ),
        rx.el.div(
            ui.icon("CpuIcon"),
            rx.el.span(
                "Workspace is ready",
                class_name="text-sm font-medium",
            ),
            class_name="flex flex-row gap-2.5 items-center rounded-[0.625rem] px-2.5 border border-jade-7 bg-jade-2 h-9 text-jade-11",
        ),
        class_name="flex flex-row gap-8 items-center bg-secondary-1 pr-16 min-h-[3.25rem] w-full border-y border-secondary-4 max-xl:hidden",
    )


def app_image() -> rx.Component:
    return rx.el.div(
        ui.avatar.root(
            ui.avatar.image(
                src=f"{SCREENSHOT_BUCKET.strip('/')}/{TemplatesState.active_template.id}",
                loading="lazy",
            ),
            unstyled=True,
            class_name="size-full object-cover object-top",
        ),
        class_name="w-full h-full max-h-[47.75rem] overflow-hidden p-4 bg-white-1",
    )


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                marketing_button(
                    ui.icon("ArrowLeft01Icon"),
                    "Back to Templates",
                    variant="ghost",
                    native_button=False,
                    class_name="px-0",
                ),
                to="/templates",
                class_name="-mb-2",
            ),
            rx.el.h1(
                TemplatesState.active_template.name,
                class_name="text-3xl text-secondary-12 font-[575]",
            ),
            rx.el.div(
                rx.cond(
                    TemplatesState.active_template.last_modified,
                    rx.el.div(
                        ui.icon("Clock01Icon", class_name="size-3.5"),
                        rx.el.span("Updated "),
                        rx.moment(
                            TemplatesState.active_template.last_modified,
                            from_now=True,
                        ),
                        class_name="flex flex-row gap-2 items-center text-secondary-12 text-sm font-[525]",
                    ),
                ),
                rx.foreach(
                    TemplatesState.active_template.tags,
                    lambda tag: rx.el.span(
                        f"#{tag}",
                        class_name="text-secondary-10 text-sm font-[525] capitalize",
                    ),
                ),
                class_name="flex flex-row gap-x-8 gap-y-2 items-center flex-wrap",
            ),
            rx.el.p(
                TemplatesState.active_template.description,
                class_name="text-sm text-secondary-11 font-[475] max-w-[48rem]",
            ),
            class_name="flex flex-col gap-6 xl:pr-16 xl:pb-16",
        ),
        app_top_bar(),
        app_image(),
        class_name="flex flex-col pt-12 w-full",
    )
