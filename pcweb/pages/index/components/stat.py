import reflex as rx
from pcweb.components.icons.icons import get_icon


@rx.memo
def stat(stat: str, text: str) -> rx.Component:
    return rx.el.section(
        get_icon("feather"),
        rx.box(
            rx.text(
                stat,
                class_name="font-semibold text-[3rem] text-slate-9 leading-[3.5rem] tracking-[-0.09rem]",
            ),
            rx.text(text, class_name="font-small text-slate-9"),
            class_name="flex flex-col justify-center items-center text-center",
        ),
        get_icon("feather", class_name="scale-x-[-1]"),
        class_name="flex flex-row items-center gap-6 justify-center",
    )
