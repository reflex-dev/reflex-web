import reflex as rx

from pcweb.components.icons import get_icon


def feature_card(icon: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        get_icon(icon, class_name="text-m-violet-9 dark:text-m-violet-10 shrink-0"),
        rx.el.span(title, class_name="font-semibold text-slate-12 text-lg mt-2"),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium",
        ),
        class_name="flex flex-col items-start gap-2 p-10 lg:border-r border-b border-slate-3",
    )
