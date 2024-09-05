import reflex as rx
from .style import button_style, new_button_style
from pcweb.components.icons.icons import get_icon
from pcweb.styles.colors import c_color
from pcweb.constants import DISCORD_URL


def discord() -> rx.Component:
    return rx.link(
        rx.flex(
            rx.image(
                src="/companies/light/discord.svg",
            ),
            padding="7px",
            style=button_style,
            border_radius="8px",
        ),
        href="https://discord.gg/T5WSbC2YtQ",
    )


def new_discord() -> rx.Component:
    return rx.link(
        get_icon(icon="discord"),
        # style=new_button_style,
        class_name="hover:bg-slate-3 size-8 text-slate-9 flex justify-center items-center rounded-[10px] border border-solid border-slate-5 bg-slate-1 transition-bg cursor-pointer shadow-large py-0.5 px-3 hover:!text-slate-9",
        underline="none",
        href=DISCORD_URL,
    )
