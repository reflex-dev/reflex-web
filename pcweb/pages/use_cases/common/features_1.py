import reflex as rx
import reflex_ui as ui


def feature_card(
    icon: str, title: str, description: str = "", items: list[str] | None = None
) -> rx.Component:
    return rx.el.div(
        ui.icon(
            icon, class_name="text-m-violet-9 dark:text-m-violet-10 shrink-0 size-7"
        ),
        rx.el.span(title, class_name="font-semibold text-slate-12 text-lg mt-2"),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium",
        )
        if description
        else None,
        rx.el.ul(
            *[
                rx.el.li(
                    item,
                    class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium mt-1",
                )
                for item in items
            ],
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium list-disc list-inside",
        )
        if items
        else None,
        class_name="flex flex-col items-start gap-2 p-10 lg:border-r border-b border-slate-3",
    )
