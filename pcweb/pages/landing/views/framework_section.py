import reflex as rx
from pcweb.components.icons.hugeicons import hi
from pcweb.pages.framework.demos.demos import demo_section


def header() -> rx.Component:
    return rx.box(
        rx.image(
            src="/landing/patterns/light/pattern_framework.webp",
            class_name="absolute top-0 left-0 w-full h-full object-cover pointer-events-none",
        ),
        rx.box(
            hi("source-code-circle", class_name="shrink-0"),
            rx.el.span("Reflex Framework", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-jade-10",
        ),
        rx.el.h2(
            """Write full-stack apps in pure Python. 
No JavaScript, no limits""",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            """Write, test, and refine your full-stack app using just Python—no need to manage 
complex frameworks or switch between languages.""",
            class_name="text-slate-11 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 p-10 justify-center items-center relative overflow-hidden h-[22.75rem]",
    )


def framework_section() -> rx.Component:
    return rx.el.section(
        header(),
        demo_section(color="jade"),
        class_name="flex flex-col mx-auto w-full max-w-[84.19rem] justify-center items-center",
    )
