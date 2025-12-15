import reflex as rx


def stat_card(stat: str, title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.span(
            stat,
            class_name="font-semibold text-m-violet-9 dark:text-m-violet-10 text-3xl",
        ),
        rx.el.span(title, class_name="font-semibold text-slate-12 text-sm"),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium",
        ),
        class_name="flex flex-col items-start p-10 gap-2",
    )
