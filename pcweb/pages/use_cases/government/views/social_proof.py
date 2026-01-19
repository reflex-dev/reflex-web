import reflex as rx
import reflex_ui as ui

from pcweb.pages.use_cases.common.logos_carousel import logos_carousel

LOGOS = [
    "scc",
    "forem",
    "saccounty",
    "unglobalcompact",
    "llnl",
    "norfolk",
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
            "Government agencies use Reflex to modernize mission-critical systems faster—without compromising security or control."
        ),
        logos_carousel(LOGOS),
        class_name="flex lg:flex-row flex-col justify-center items-center mx-auto w-full max-w-[64.19rem] lg:border border-slate-3 h-[10.75rem] z-1",
    )
