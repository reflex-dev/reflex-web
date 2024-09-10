import reflex as rx
from .style import new_button_style
from pcweb.styles.colors import c_color
from pcweb.components.icons import get_icon


from reflex.style import toggle_color_mode


def color() -> rx.Component:
    return rx.el.button(
        rx.color_mode.icon(
            # light_component=rx.icon(
            #     "sun", size=16, stroke_width="2.25px", class_name="shrink-0"
            # ),
            # dark_component=rx.icon(
            #     "moon", size=16, stroke_width="2.25px", class_name="shrink-0"
            # ),
            light_component=get_icon("sun", class_name="shrink-0 !text-slate-9"),
            dark_component=get_icon("moon", class_name="shrink-0 !text-slate-9"),
        ),
        on_click=toggle_color_mode,
        class_name="hover:bg-slate-3 size-8 text-slate-9 flex justify-center items-center rounded-[10px] border border-slate-5 bg-slate-1 transition-bg cursor-pointer shadow-large py-0.5 px-3",
    )
