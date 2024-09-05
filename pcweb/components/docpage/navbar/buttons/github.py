import reflex as rx
from .style import new_button_style
from pcweb.styles.fonts import small
from pcweb.constants import GITHUB_STARS, GITHUB_URL
from pcweb.components.icons.icons import get_icon
from pcweb.styles.colors import c_color


def github() -> rx.Component:
    return rx.link(
        rx.flex(
            get_icon(icon="github"),
            rx.text(
                f"{GITHUB_STARS/1000:.1f}K",
                class_name="font-small",
            ),
            class_name="text-slate-9 flex-row gap-2 hover:bg-slate-3 flex justify-center rounded-[10px] border border-slate-5 bg-slate-1 transition-bg cursor-pointer shadow-large py-0.5 px-3 items-center h-8",
        ),
        href=GITHUB_URL,
        underline="none",
    )
