import reflex as rx
from pcweb.components.icons.icons import get_icon
from pcweb.constants import GITHUB_STARS, CONTRIBUTION_URL, BUGS_URL


def stat(icon: str, stat: str, text: str) -> rx.Component:
    return rx.box(
        get_icon(icon),
        rx.box(
            rx.text(
                stat,
                class_name="font-semibold text-[2.5rem] text-slate-9 leading-[3rem] tracking-[-0.0375rem]",
            ),
            rx.text(text, class_name="font-small text-slate-9"),
            class_name="flex flex-col text-center",
        ),
        class_name="flex flex-col justify-center items-center gap-4",
    )


def stats() -> rx.Component:
    return rx.box(
        stat("star", f"{GITHUB_STARS:,}+", "stars"),
        stat("fork", "1,200+", "forks"),
        stat("contributors", "180+", "contributors"),
        class_name="justify-center gap-10 grid grid-cols-1 md:grid-cols-3 lg:grid-cols-3",
    )


def open_source() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "Join our open source community",
                class_name="font-x-large gradient-heading",
            ),
            rx.text(
                "Get help and contribute on GitHub.",
                class_name="font-base text-slate-9",
            ),
            class_name="flex flex-col gap-4 text-center",
        ),
        # Stats
        stats(),
        class_name="flex flex-col gap-10 w-full",
    )
