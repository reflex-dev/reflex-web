import reflex as rx

from pcweb.components.new_button import button
from pcweb.pages.pricing.plan_cards import plan_cards


def pricing_cards() -> rx.Component:
    return rx.el.section(
        rx.box(
            rx.el.h2(
                "Start for free and scale as you grow.",
                class_name="lg:text-3xl text-xl font-semibold text-slate-12 text-balance",
            ),
            rx.el.span(
                "Flexible pricing",
                class_name="lg:text-3xl text-xl font-semibold text-slate-9 z-[1] text-balance",
            ),
            class_name="flex flex-col text-center pb-[3.5rem] max-w-[64.19rem] lg:border-x border-slate-3 border-t pt-[5rem] w-full mx-auto",
        ),
        plan_cards(),
        rx.box(
            rx.link(
                button(
                    "Compare plans",
                    size="md",
                    icon=rx.icon("chevron-right", size=16),
                    variant="transparent",
                    class_name="mt-[3.5rem] flex-row-reverse mb-[5rem]",
                ),
                href="/pricing",
            ),
            class_name="flex flex-col text-center max-w-[64.19rem] lg:border-x border-slate-3 w-full mx-auto",
        ),
        class_name="flex flex-col justify-center items-center w-full relative",
    )
