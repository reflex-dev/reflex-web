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
            rx.el.span(
                "Trusted by industry leading teams",
                class_name="px-2 py-0.5 font-small text-center text-slate-9",
            ),
            class_name="flex flex-row justify-center items-center w-full",
        ),
        rx.box(
            logo("amazon", "34px"),
            logo("nasa", "21px"),
            logo("dell", "36px"),
            logo("samsung", "26px"),
            logo("ibm", "21px"),
            logo("accenture", "21px"),
            logo("rappi", "21px"),
            logo("nike", "19px"),
            class_name="flex flex-row flex-wrap justify-center items-center gap-8 h-auto",
        ),
        class_name="flex flex-col justify-center gap-4 w-full h-auto max-w-[64.19rem] lg:border-x border-slate-3 lg:px-[8.5rem] lg:py-16 py-12 border-b lg:border-b-0",
    )


def pricing_page_companies() -> rx.Component:
    return rx.el.section(
        rx.box(
            logo("amazon", "34px"),
            logo("nasa", "21px"),
            logo("dell", "36px"),
            logo("samsung", "26px"),
            logo("ibm", "21px"),
            logo("accenture", "21px"),
            logo("rappi", "21px"),
            logo("nike", "19px"),
            class_name="flex flex-row flex-wrap justify-center md:justify-start items-center gap-8 h-auto",
        ),
        class_name="flex flex-col justify-center gap-4 w-full h-auto",
    )
