import reflex as rx
import reflex_ui as ui

from pcweb.components.icons import get_icon
from pcweb.constants import CONTRIBUTORS, DISCORD_USERS, GITHUB_STARS


def stat_card(
    stat: str, text: str, icon: str, class_name: str = "", color: str = "!text-slate-9"
) -> rx.Component:
    return rx.box(
        rx.box(
            get_icon(icon, class_name=color),
            rx.text(text, class_name="font-base text-slate-9"),
            class_name="flex flex-row gap-2 items-center",
        ),
        rx.text(stat, class_name="font-x-large text-slate-12"),
        class_name=ui.cn(
            "flex flex-col gap-2 w-full p-10 items-center",
            class_name,
        ),
    )


def stats_grid() -> rx.Component:
    return rx.box(
        stat_card(
            stat=f"{GITHUB_STARS:,}+",
            text="Stars",
            icon="star",
        ),
        stat_card(
            stat=f"{CONTRIBUTORS:,}+",
            text="Contributors",
            icon="fork",
        ),
        stat_card(
            stat=f"{DISCORD_USERS:,}+",
            text="Discord",
            icon="discord_navbar",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-1 w-full divide-slate-3 lg:divide-x max-lg:divide-y",
    )


def os_stats() -> rx.Component:
    return rx.el.section(
        rx.box(
            stats_grid(),
            class_name="flex flex-row max-w-[64.19rem] justify-center w-full lg:border-x border-slate-3",
        ),
        class_name="flex flex-col justify-center items-center w-full",
    )
