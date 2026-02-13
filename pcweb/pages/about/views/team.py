import reflex as rx


def team() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.image(
                src="/about/team_1.avif",
                alt="Team 1",
                loading="lazy",
                class_name="col-span-1 row-span-2 pointer-events-none",
            ),
            rx.image(
                src="/about/team_2.avif",
                alt="Team 2",
                loading="lazy",
                class_name="pointer-events-none",
            ),
            rx.image(
                src="/about/team_3.avif",
                alt="Team 3",
                loading="lazy",
                class_name="pointer-events-none",
            ),
            class_name="grid lg:grid-cols-2 grid-cols-1 grid-rows-2 gap-2 lg:p-2 lg:border border-m-slate-4 dark:border-m-slate-10",
        ),
        rx.el.div(
            class_name="absolute bottom-0 right-0 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10"
        ),
        rx.el.div(
            class_name="absolute bottom-0 left-0 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10"
        ),
        class_name="lg:px-24 px-6 max-w-(--layout-max-width) mx-auto relative",
    )
