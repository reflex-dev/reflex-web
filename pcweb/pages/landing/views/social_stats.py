import reflex as rx

from pcweb.components.icons.icons import get_icon
from pcweb.components.numbers_pattern import numbers_pattern
from pcweb.constants import GITHUB_STARS


def stat(icon: str, text: str) -> rx.Component:
    return rx.el.section(
        get_icon(icon, class_name="text-primary-9 [&_svg]:!size-5"),
        rx.el.span(text, class_name="font-medium text-lg text-slate-12"),
        class_name="flex flex-row items-center gap-2",
    )


def social_stats():
    return rx.el.section(
        numbers_pattern(side="left", reversed=True, class_name="left-0 top-0"),
        numbers_pattern(side="right", reversed=True, class_name="right-0 top-0"),
        stat("browser", "1M+ Apps Built"),
        stat("checkmark", "Used by 25% of Fortune 500"),
        stat("github_navbar", f"{GITHUB_STARS // 1000}K GitHub Stars"),
        class_name="flex flex-col justify-center items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden border-t gap-4 lg:py-[5rem] py-[3.5rem] max-lg:border-b",
    )
