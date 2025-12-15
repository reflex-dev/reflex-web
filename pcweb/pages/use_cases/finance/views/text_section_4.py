import reflex as rx

from pcweb.components.numbers_pattern import numbers_pattern


def header() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "Reflex as a Strategic Platform for Finance Teams",
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold",
        ),
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden max-w-[26.5rem] text-center",
    )


def text_section_4() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", reverse=True, class_name="left-0 top-0"),
        numbers_pattern(side="right", reverse=True, class_name="right-0 top-0"),
        header(),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20",
    )
