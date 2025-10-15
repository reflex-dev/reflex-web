import reflex as rx

from pcweb.components.icons.icons import get_icon
from pcweb.constants import DISCORD_URL


def discord() -> rx.Component:
    return rx.link(
        get_icon(icon="discord_navbar", class_name="shrink-0 !text-slate-9"),
        custom_attrs={"aria-label": "Discord link"},
        class_name="hover:bg-slate-3 size-8 text-slate-9 flex justify-center items-center rounded-[10px] border border-solid border-slate-5 bg-slate-1 transition-bg cursor-pointer py-0.5 px-3 hover:!text-slate-9",
        underline="none",
        href=DISCORD_URL,
    )
