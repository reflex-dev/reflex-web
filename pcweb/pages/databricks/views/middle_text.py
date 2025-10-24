import reflex as rx

from pcweb.components.numbers_pattern import numbers_pattern


def content() -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            "TODO: Placeholder text",
            class_name="text-slate-12 lg:text-4xl text-3xl font-semibold text-center",
        ),
        class_name="flex flex-col items-center mx-auto w-full justify-center max-w-[42rem]",
    )


def middle_text() -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", reverse=True, class_name="left-0 top-0"),
        numbers_pattern(side="right", reverse=True, class_name="right-0 top-0"),
        content(),
        class_name="flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x relative overflow-hidden py-20 border-b border-slate-3 max-lg:border-t",
    )
