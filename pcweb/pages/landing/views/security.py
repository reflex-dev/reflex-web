import reflex as rx


def security_badges() -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(src="/soc2.webp", class_name="h-24 w-auto"),
            rx.image(src="/databricks-partner.svg", class_name="h-24 w-auto"),
            class_name="flex flex-row gap-10 items-center justify-center",
        ),
        class_name="p-10 flex items-center justify-center",
    )


def security():
    return rx.el.section(
        rx.box(
            rx.box(
                rx.el.h2(
                    "Secure by default",
                    class_name="text-slate-12 text-xl lg:text-3xl font-semibold text-start",
                ),
                rx.el.h3(
                    "SOC 2 compliant with enterprise-grade security and flexible deployment options.",
                    class_name="text-slate-9 text-lg lg:text-2xl font-semibold text-start",
                ),
                class_name="flex flex-col gap-2 lg:col-span-2 p-10 max-lg:border-b border-slate-3",
            ),
            security_badges(),
            class_name="grid grid-cols-1 lg:grid-cols-3 lg:divide-x divide-slate-4 w-full",
        ),
        class_name="flex flex-col gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 justify-center items-center relative overflow-hidden border-t border-slate-3",
    )
