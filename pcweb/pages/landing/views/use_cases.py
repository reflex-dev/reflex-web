import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern
from reflex.experimental.client_state import ClientStateVar

selected_industry = ClientStateVar.create(var_name="selected_industry", default="analytics")

def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("BrowserIcon", class_name="shrink-0"),
            rx.el.span("Use Cases", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-violet-9",
        ),
        rx.el.h2(
            "Use Cases by Industry",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "See what’s built with Reflex.",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def use_cases_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            numbers_pattern(side="left", class_name="left-0 top-0"),
            numbers_pattern(side="right", class_name="right-0 top-0"),
            header(),
            class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20",
        ),
        class_name="flex flex-col items-center mx-auto w-full max-w-[84.5rem]",
    )
