import reflex as rx


def divider() -> rx.Component:
    return rx.el.hr(
        class_name="h-[1px] w-full bg-m-slate-4 dark:bg-m-slate-10",
    )
