import reflex as rx
import reflex_ui as ui

from pcweb.pages.use_cases.common.logos_carousel import logos_carousel

LOGOS = [
    "dana_farber",
    "united_health_group",
    "ggdzl",
    "mercy",
    "drager",
    "wvu_medicine",
    "roche",
    "thermofisher",
]


def first_card(title: str) -> rx.Component:
    return rx.el.div(
        ui.icon(
            "CheckmarkBadge02Icon",
            class_name="text-m-slate-11 dark:text-m-slate-9 shrink-0",
        ),
        rx.el.span(
            title,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium text-wrap",
        ),
        class_name="flex flex-row gap-2.5 items-center max-lg:justify-center lg:col-span-2 px-10 h-full max-lg:h-[10.75rem] max-lg:w-full w-full lg:border-r",
    )


def social_proof() -> rx.Component:
    return rx.el.div(
        first_card(
            "Reflex powers mission-critical internal apps used by thousands of employees worldwide."
        ),
        logos_carousel(LOGOS),
        class_name="flex lg:flex-row flex-col justify-center items-center mx-auto w-full max-w-[64.19rem] lg:border border-slate-3 h-[10.75rem] z-1",
    )
