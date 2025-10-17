import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern


def header() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon("Layers01Icon", class_name="shrink-0"),
            rx.el.span("Features", class_name="text-sm font-semibold"),
            class_name="flex flex-row gap-2 items-center text-primary-9",
        ),
        rx.el.h2(
            "Generate your app with AI",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold text-balance word-wrap break-words md:whitespace-pre",
        ),
        rx.el.p(
            "Build production-ready web apps in seconds with AI-powered code generation.",
            class_name="text-slate-9 text-sm font-medium text-center text-balance word-wrap break-words md:whitespace-pre",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden",
    )


def frontend_card(
    title: str,
    description: str,
    image: str,
    height: str = "auto",
    cols: str = "1",
) -> rx.Component:
    return rx.box(
        rx.el.div(
            rx.box(
                rx.el.h2(
                    title, class_name="text-2xl font-semibold text-slate-12 z-[1]"
                ),
                rx.el.p(
                    description,
                    class_name="text-base font-medium text-slate-9 z-[1] text-pretty",
                ),
                class_name="flex flex-col gap-2 px-10 pt-10",
            ),
            rx.image(
                src=f"/landing/ai_bento/light/{image}",
                class_name="dark:hidden w-full shrink-0",
                height=height,
                loading="lazy",
                alt=title + " image",
            ),
            rx.image(
                src=f"/landing/ai_bento/dark/{image}",
                class_name="dark:block hidden w-full shrink-0",
                height=height,
                loading="lazy",
                alt=title + " image",
            ),
            class_name="flex flex-col gap-8",
        ),
        class_name=f"lg:col-span-{cols} col-span-1 h-96 rounded-[1.125rem] bg-white-1 border border-slate-4 overflow-hidden relative lg:shadow-small max-h-full pointer-events-none",
    )


def bento_cards() -> rx.Component:
    return rx.el.div(
        frontend_card(
            title="Work With UI and Backend in 100% Python",
            description=(
                "Generate and refine UI and backend in 100% Python.\n"
                "No JavaScript or frontend frameworks required"
            ),
            image="bento1.webp",
            cols="2",
        ),
        frontend_card(
            title="Integrate With Tools",
            description="Over 15 integrations are available.",
            image="bento2.webp",
        ),
        frontend_card(
            title="Research Web",
            description="Reflex AI finds the best way to implement new features and fix your code.",
            image="bento3.webp",
        ),
        frontend_card(
            title="Build with Visual References",
            description="Pass it screenshots, and even video, Figma design",
            image="bento4.webp",
            cols="2",
        ),
        frontend_card(
            title="Test Any App",
            description=(
                "Reflex simulates real users interaction and debugs the app for you."
            ),
            image="bento5.webp",
            cols="2",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-4 gap-4 grid-rows-2 max-w-[84.5rem]",
    )


def ai_bento() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            numbers_pattern(side="left", reversed=True, class_name="left-0 top-0"),
            numbers_pattern(side="right", reversed=True, class_name="right-0 top-0"),
            header(),
            class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20",
        ),
        bento_cards(),
        class_name="flex flex-col items-center mx-auto w-full",
    )
