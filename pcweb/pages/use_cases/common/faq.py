import reflex as rx
import reflex_ui as ui

from pcweb.components.numbers_pattern import numbers_pattern
from pcweb.pages.pricing.faq import accordion, accordion_text


def content(header: str, description: str | None = None) -> rx.Component:
    return rx.el.div(
        rx.el.h2(
            header,
            class_name="max-w-full w-full lg:text-3xl text-2xl text-center text-slate-12 font-semibold",
        ),
        rx.el.p(
            description,
            class_name="text-m-slate-11 dark:text-slate-9 text-sm font-medium text-center",
        )
        if description
        else None,
        class_name="flex flex-col gap-4 items-center mx-auto w-full relative overflow-hidden max-w-[26.5rem] text-center",
    )


def faq_section(faq_items: list[tuple[str, str]], class_name: str = "") -> rx.Component:
    return rx.el.section(
        numbers_pattern(side="left", reverse=True, class_name="left-0 top-0"),
        numbers_pattern(side="right", reverse=True, class_name="right-0 top-0"),
        content("Frequently Asked Questions"),
        rx.el.div(
            *[
                accordion(title, accordion_text(content))
                for title, content in faq_items
            ],
            class_name="max-w-[35rem] flex justify-center items-center flex-col mx-auto w-full gap-2 mt-[2rem]",
        ),
        class_name=ui.cn(
            "flex flex-col items-center mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 relative overflow-hidden py-20 max-lg:px-4",
            class_name,
        ),
    )
