import reflex as rx


def stat_card(stat: str, text: str, class_name: str = "") -> rx.Component:
    return rx.box(
        rx.text(stat, class_name="font-x-large text-slate-12"),
        rx.text(text, class_name="font-base text-slate-9"),
        class_name="flex flex-col gap-2 w-full p-10 items-center lg:items-start",
    )


def stats_grid() -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(
                "With Reflex you can start with an mvp and scale up to a full fledged production application",
                class_name="font-base text-slate-9 max-w-[12.875rem] text-center lg:text-left",
            ),
            class_name="p-10 lg:border-l border-slate-3 flex justify-center lg:justify-start",
        ),
        stat_card(stat="500+", text="Teams using Reflex in a production environment"),
        stat_card(
            stat="10,000+", text="New applications built with Reflex every month"
        ),
        class_name="grid grid-cols-1 lg:grid-cols-3 gap-0 grid-rows-1 w-full divide-slate-3 lg:divide-x !border-t-0 lg:border-b border-slate-3 lg:border-r divide-y lg:divide-y-0 [&>:last-child]:!border-b lg:[&>:last-child]:!border-b-0",
    )


def stats() -> rx.Component:
    return rx.el.section(
        stats_grid(),
        class_name="flex flex-row max-w-[64.19rem] justify-center w-full",
    )
