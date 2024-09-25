import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.h1(
            """Meet the teams
who chose Reflex""",
            class_name="max-w-full inline-block bg-clip-text bg-gradient-to-r from-slate-12 to-slate-11 w-full font-xx-large text-center text-transparent text-balance whitespace-pre mx-auto break-words",
        ),
        rx.el.h2(
            """Companies of all sizes trust Reflex to build internal tools and customer-facing apps""",
            class_name="max-w-full w-full font-md-smbold text-center text-slate-9 whitespace-pre mx-auto text-balance word-wrap break-words",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[2.5rem] pt-24 lg:pt-48",
    )
