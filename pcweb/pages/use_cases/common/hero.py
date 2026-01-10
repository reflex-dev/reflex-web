import reflex as rx
import reflex_ui as ui
from reflex_ui.blocks.demo_form import demo_form_dialog

from pcweb.components.numbers_pattern import numbers_pattern


def left_content(
    h1: str, h1_accent: str, h2: str, button_1: str, button_2: str
) -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            h1,
            rx.el.span(
                h1_accent,
                class_name="text-m-violet-11",
            ),
            class_name="text-slate-12 lg:text-5xl text-3xl font-semibold",
        ),
        rx.el.h2(
            h2,
            class_name="text-m-slate-11 dark:text-slate-9 text-base font-medium",
        ),
        rx.el.div(
            demo_form_dialog(
                trigger=ui.button(
                    button_1,
                    size="lg",
                    class_name="font-semibold",
                ),
            ),
            demo_form_dialog(
                trigger=ui.button(
                    button_2,
                    size="lg",
                    variant="outline",
                    class_name="font-semibold text-m-slate-11 dark:text-slate-9 border-m-slate-5 dark:border-m-slate-12",
                ),
            ),
            class_name="flex lg:flex-row flex-col items-center max-lg:justify-center gap-4 mt-2",
        ),
        class_name="flex flex-col gap-6 max-lg:items-center max-lg:justify-center max-lg:text-center",
    )


def feature_row(icon: str, title: str) -> rx.Component:
    return rx.el.div(
        ui.icon(
            icon,
            class_name="size-5 text-m-violet-11 dark:text-m-violet-10 shrink-0",
            stroke_width=1.5,
        ),
        rx.el.span(title, class_name="font-medium text-slate-12 text-sm"),
        class_name="flex flex-row items-start gap-2.5",
    )


def right_content(features: list[tuple[str, str]]) -> rx.Component:
    return rx.el.div(
        rx.el.span(
            "Why Reflex?",
            class_name="font-semibold text-slate-12 text-base",
        ),
        rx.el.div(
            *[feature_row(icon, title) for icon, title in features],
            class_name="flex flex-col gap-4",
        ),
        class_name="shadow-large rounded-xl border-m-slate-4 border p-8 bg-white-1 dark:bg-m-slate-14 dark:border-m-slate-12 flex flex-col gap-6 max-w-[24.25rem] w-full shrink-0",
    )


def hero() -> rx.Component:
    return rx.el.section(
        numbers_pattern(
            side="right",
            class_name="lg:top-[65px] top-[45px] lg:h-[calc(100%-65px)] h-[calc(100%-45px)] max-lg:hidden",
        ),
        rx.el.div(
            left_content(),
            right_content(),
            class_name="flex lg:flex-row flex-col lg:gap-20 gap-10 max-lg:items-center max-lg:justify-center max-lg:text-center",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[3rem] pt-32 lg:pt-[11.5rem] lg:pb-[7.5rem] relative lg:overflow-hidden overflow-hidden z-[1] lg:px-10",
    )
