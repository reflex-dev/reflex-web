import reflex as rx


def logo(path: str, height: str) -> rx.Component:
    return rx.fragment(
        rx.color_mode_cond(
            rx.image(
                src=f"/companies/light/{path}.svg",
                alt=f"{path} logo",
                loading="lazy",
                height=height,
                class_name="shrink-0",
            ),
            rx.image(
                src=f"/companies/dark/{path}.svg",
                alt=f"{path} logo",
                height=height,
                loading="lazy",
                class_name="shrink-0",
            ),
        ),
    )


def companies() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.box(
                class_name="bg-gradient-to-r from-slate-2 to-85% to-slate-4 w-[12.5rem] h-[0.125rem]"
            ),
            rx.el.span(
                "Trusted by industry leading teams",
                class_name="px-2 py-0.5 font-small text-center text-slate-9",
            ),
            rx.box(
                class_name="bg-gradient-to-r from-15% from-slate-4 to-slate-2 w-[12.5rem] h-[0.125rem]"
            ),
            class_name="flex flex-row justify-center items-center w-full",
        ),
        rx.box(
            logo("amazon", "42px"),
            logo("nasa", "29px"),
            logo("dell", "44px"),
            logo("samsung", "34px"),
            logo("ibm", "29px"),
            logo("accenture", "29px"),
            logo("rappi", "29px"),
            logo("nike", "27px"),
            class_name="flex flex-row flex-wrap justify-center items-center gap-10 h-8",
        ),
        class_name="flex flex-col justify-center gap-6 pt-4 w-full h-auto",
    )
