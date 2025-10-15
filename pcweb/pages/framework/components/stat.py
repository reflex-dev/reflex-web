import reflex as rx

from pcweb.components.icons.icons import get_icon


@rx.memo
def stat(stat: str, text: str) -> rx.Component:
    return rx.el.section(
        get_icon("feather"),
        rx.box(
            rx.text(
                stat,
                class_name="font-x-large inline-block bg-clip-text bg-gradient-to-r from-slate-8 via-slate-9 to-slate-8 w-full text-balance text-center text-transparent",
            ),
            rx.text(text, class_name="font-small text-slate-9"),
            class_name="flex flex-col justify-center items-center text-center text-nowrap",
        ),
        get_icon("feather", class_name="scale-x-[-1]"),
        class_name="flex flex-row items-center gap-4 justify-center",
    )
