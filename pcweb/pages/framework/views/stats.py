import reflex as rx
from pcweb.components.icons import get_icon
from pcweb.github import GithubStarState
from pcweb.constants import DISCORD_USERS, CONTRIBUTORS


def stat_card(stat: str, text: str, icon: str, class_name: str = "") -> rx.Component:
    return rx.box(
        rx.box(
            get_icon(icon, class_name="!text-slate-9"),
            rx.text(text, class_name="font-base text-slate-9"),
            class_name="flex flex-row gap-2 items-center",
        ),
        rx.text(stat, class_name="font-x-large text-slate-12"),
        class_name="flex flex-col gap-2 w-full p-10 items-center lg:items-start"
        + " "
        + class_name,
    )


def stats_grid() -> rx.Component:
    return rx.box(
        stat_card(
            stat=f"{GithubStarState.stars:,}",
            text="Stars",
            icon="star",
            class_name="lg:!border-l !border-slate-3",
        ),
        stat_card(
            stat=f"{CONTRIBUTORS:,}+",
            text="Contributors",
            icon="fork",
            class_name="lg:!border-l !border-slate-3",
        ),
        stat_card(
            stat=f"{DISCORD_USERS:,}+",
            text="Discord",
            icon="discord_navbar",
            class_name="lg:!border-r !border-slate-3",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-1 w-full divide-slate-3 lg:divide-x !border-t-0 divide-y lg:divide-y-0 lg:border-b border-slate-3",
    )


def stats() -> rx.Component:
    return rx.el.section(
        rx.box(
            stats_grid(),
            class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
        ),
        class_name="flex flex-col justify-center items-center w-full",
    )
