import reflex as rx


def stat_card(stat: str, text: str, class_name: str = "") -> rx.Component:
    return rx.box(
        rx.text(stat, class_name="font-x-large text-slate-12"),
        rx.text(text, class_name="font-base text-slate-9"),
        class_name="flex flex-col gap-2 w-full p-10",
    )


def stats_grid() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "Teams that switch to Reflex create more issues and close them faster",
                class_name="font-base text-slate-9 max-w-[12.875rem]",
            ),
            class_name="p-10 lg:border-l border-slate-3",
        ),
        stat_card(stat="98.5%", text="Increase in filed issues"),
        stat_card(
            stat="24x",
            text="Faster to close issues",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-1 w-full divide-slate-3 lg:divide-x !border-t-0 lg:border-b border-slate-3 lg:border-r",
    )


def stats() -> rx.Component:
    return rx.el.section(
        stats_grid(),
        class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
    )
