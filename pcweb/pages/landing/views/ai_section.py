import reflex as rx

from pcweb.components.icons.hugeicons import hi


def header() -> rx.Component:
    return rx.box(
        rx.image(
            src="/landing/patterns/light/pattern_ai.webp",
            class_name="absolute top-0 left-0 w-full h-full object-cover pointer-events-none",
        ),
        rx.box(
            hi("magic-wand-01", class_name="shrink-0"),
            rx.el.span("AI Builder", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-violet-9",
        ),
        rx.el.h2(
            """Instantly turn your ideas into real apps. 
Try AI-powered generation""",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            """Describe what you want to build, and AI will generate a working Python app instantly 
—complete with a backend, frontend, and database integration.""",
            class_name="text-slate-11 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 p-10 justify-center items-center relative overflow-hidden h-[22.75rem]",
    )


def gallery_item() -> rx.Component:
    return rx.box(
        # rx.image(
        #     src="",
        #     class_name="absolute top-0 left-0 w-full h-full object-cover",
        # ),
        rx.text("Gallery Item", class_name="text-slate-6 text-base font-medium"),
        class_name="relative overflow-hidden border-slate-3 border rounded-[1.125rem] h-[14rem] bg-slate-2 flex justify-center items-center w-full shadow-small",
    )


def gallery() -> rx.Component:
    return rx.box(
        *[gallery_item() for _ in range(12)],
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4",
    )


def ai_section() -> rx.Component:
    return rx.el.section(
        header(),
        gallery(),
        class_name="flex flex-col mx-auto w-full max-w-[84.19rem]",
    )
