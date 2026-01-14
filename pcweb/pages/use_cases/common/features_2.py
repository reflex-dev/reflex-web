import reflex as rx
import reflex_ui as ui


def feature_card(
    icon: str,
    stat: str,
    title: str,
    description: str,
    items: list[str] | None = None,
    class_name: str = "",
) -> rx.Component:
    return rx.el.div(
        ui.icon(
            icon, class_name="text-m-violet-9 dark:text-m-violet-10 shrink-0 size-5"
        ),
        rx.el.span(
            stat,
            class_name="font-semibold text-m-violet-9 dark:text-m-violet-10 text-sm mt-4",
        ),
        rx.el.span(title, class_name="font-semibold text-slate-12 text-lg mt-4"),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium mt-2",
        ),
        rx.el.ul(
            *[
                rx.el.li(
                    item,
                    class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium mt-1",
                )
                for item in items
            ],
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium list-disc list-inside mt-2",
        )
        if items
        else None,
        class_name=ui.cn("flex flex-col items-start p-10", class_name),
    )
