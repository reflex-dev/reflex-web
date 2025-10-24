import reflex as rx
import reflex_ui as ui
from reflex_ui.blocks.lemcal import lemcal_dialog

from pcweb.components.numbers_pattern import numbers_pattern


def content() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Get a personalized walkthrough of Reflex for Databricks for your company",
            class_name="text-slate-12 lg:text-4xl text-3xl font-semibold text-center",
        ),
        lemcal_dialog(
            ui.button(
                "Get Personalized Walkthrough",
                size="lg",
                class_name="font-semibold mt-8 h-10",
            )
        ),
        class_name="flex flex-col items-center mx-auto w-full justify-center max-w-[42rem]",
    )


def final_cta() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", reverse=False, class_name="left-0 top-0"),
        numbers_pattern(side="right", reverse=False, class_name="right-0 top-0"),
        content(),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20",
    )
