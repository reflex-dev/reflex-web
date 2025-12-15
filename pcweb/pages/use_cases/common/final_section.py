import reflex as rx
import reflex_ui as ui
from reflex_ui.blocks.calcom import get_cal_attrs

from pcweb.constants import REFLEX_BUILD_URL
from pcweb.pages.pricing.plan_cards import radial_circle


def right_content(h1: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            h1,
            class_name="text-slate-12 text-2xl font-semibold",
        ),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium mt-2",
        ),
        ui.link(
            render_=ui.button(
                "Go to the builder",
                size="lg",
                variant="outline",
                class_name="w-fit font-semibold lg:mt-auto mt-8 text-m-slate-11 dark:text-m-slate-9 border-m-slate-5 dark:border-m-slate-12",
            ),
            to=REFLEX_BUILD_URL,
            target="_blank",
        ),
        class_name="flex flex-col lg:p-20 p-8 h-full",
    )


def left_content(h1: str, description: str) -> rx.Component:
    return rx.el.div(
        radial_circle(class_name="dark:opacity-50"),
        rx.el.h2(
            h1,
            class_name="text-slate-12 lg:text-3xl text-2xl font-semibold",
        ),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-m-slate-9 text-sm font-medium",
        ),
        ui.button(
            ui.icon("Calendar04Icon"),
            "Schedule a demo",
            size="lg",
            custom_attrs=get_cal_attrs(),
            class_name="w-fit font-semibold mt-4",
        ),
        class_name="flex flex-col gap-4 items-start justify-center lg:py-20 py-8 lg:pl-20 pl-8 lg:pr-[7.5rem] pr-8 relative overflow-hidden min-h-fit",
    )
