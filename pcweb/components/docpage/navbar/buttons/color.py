import reflex as rx
from reflex.style import toggle_color_mode

from pcweb.components.icons import get_icon


def color() -> rx.Component:
    return rx.el.button(
        rx.color_mode.icon(
            light_component=get_icon("sun", class_name="shrink-0 !text-slate-9"),
            dark_component=get_icon("moon", class_name="shrink-0 !text-slate-9"),
        ),
        on_click=toggle_color_mode,
        custom_attrs={"aria-label": "Toggle color mode"},
        class_name="hover:bg-slate-3 size-8 text-slate-9 flex justify-center items-center rounded-[10px] border border-slate-5 bg-slate-1 transition-bg cursor-pointer shadow-large py-0.5 px-3",
    )
