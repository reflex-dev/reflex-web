import reflex as rx
from pcweb.components.icons import get_icon
from pcweb.constants import GITHUB_STARS

def stat_card(stat: str, text: str, icon: str, class_name: str = "") -> rx.Component:
    return rx.box(
        rx.box(
            get_icon(icon, class_name="!text-slate-9"),
            rx.text(text, class_name="font-base text-slate-9"),
            class_name="flex flex-row gap-2 items-center",
        ),
        rx.text(stat, class_name="font-x-large text-slate-12"),
        class_name="flex flex-col gap-2 w-full p-10" + " " + class_name,
    )


def stats_grid() -> rx.Component:
    return rx.box(
        stat_card(stat=f"{GITHUB_STARS:,}+", text="Stars", icon="star", class_name="lg:!border-t lg:!border-l !border-slate-3"),
        stat_card(stat="150+", text="Contributors", icon="fork"),       
        stat_card(stat="5,500+", text="Discord", icon="discord_navbar", class_name="lg:!border-r !border-slate-3"),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-1 w-full lg:divide-y divide-slate-3 lg:divide-x",
    )


def stats() -> rx.Component:
    return rx.box(
        rx.box(
            stats_grid(),
            class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
        ),
        class_name="flex flex-col justify-center items-center w-full",
    )
