import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern
from pcweb.constants import REFLEX_BUILD_URL


def content() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Start building with Reflex.",
            class_name="text-slate-12 lg:text-4xl text-3xl font-semibold text-center",
        ),
        rx.el.h3(
            "All in one platform in Python",
            class_name="text-slate-9 lg:text-4xl text-3xl font-semibold text-center",
        ),
        ui.link(
            render_=ui.button(
                "Get Started with Reflex",
                size="lg",
                class_name="font-semibold mt-8 h-10",
            ),
            to=REFLEX_BUILD_URL,
            target="_blank",
        ),
        class_name="flex flex-col items-center mx-auto w-full justify-center",
    )


def final_cta() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", reverse=True, class_name="left-0 top-0"),
        numbers_pattern(side="right", reverse=True, class_name="right-0 top-0"),
        content(),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20",
    )
