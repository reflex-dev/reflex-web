import reflex as rx
import reflex_ui as ui

from pcweb.constants import GITHUB_STARS


def stat(icon: str, value: str, label: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(
            value,
            class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-3xl text-2xl font-[575] tracking-tight",
        ),
        rx.el.div(
            ui.icon(
                icon,
                class_name="text-m-slate-7 dark:text-m-slate-6 size-4 shrink-0 transition-all duration-300 ease-out group-hover:scale-125 group-hover:rotate-[-8deg] group-hover:text-primary-10",
                stroke_width=1.5,
            ),
            rx.el.p(
                label,
                class_name="text-sm font-[475] text-m-slate-7 dark:text-m-slate-6",
            ),
            class_name="flex flex-row items-center gap-2 justify-center",
        ),
        class_name="group flex flex-col items-center gap-1.5 px-6",
    )


def stats() -> rx.Component:
    return rx.el.section(
        stat("StarIcon", f"{GITHUB_STARS // 1000}K+", "GitHub Stars"),
        stat("BrowserIcon", "1M+", "Apps Built"),
        stat("Building03Icon", "30%", "of Fortune 500"),
        stat("UserGroupIcon", "180+", "Contributors"),
        class_name="flex flex-row flex-wrap justify-center items-center lg:gap-16 gap-x-8 gap-y-8 max-w-[69rem] mx-auto lg:pt-24 pt-16 max-lg:px-6",
    )
