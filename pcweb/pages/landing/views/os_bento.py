import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern
from pcweb.pages.framework.views.frontend_features import frontend_grid


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("Layers01Icon", class_name="shrink-0"),
            rx.el.span(
                "Open Source",
                class_name="text-sm font-semibold",
            ),
            class_name="flex flex-row gap-2 items-center text-primary-9",
        ),
        rx.el.h2(
            "Built on our Open Source Python Framework",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "Reflex is the only solution that gives you full flexibility while staying in the language your team knows - Python.",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def os_bento() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            numbers_pattern(side="left", reversed=True, class_name="left-0 top-0"),
            numbers_pattern(side="right", reversed=True, class_name="right-0 top-0"),
            header(),
            class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20",
        ),
        frontend_grid(),
        class_name="flex flex-col items-center mx-auto w-full",
    )
