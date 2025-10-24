import reflex as rx

from pcweb.components.numbers_pattern import numbers_pattern


def hero() -> rx.Component:
    return rx.el.section(
        numbers_pattern(
            side="left",
            class_name="lg:top-[65px] top-[45px] lg:h-[calc(100%-65px)] h-[calc(100%-45px)]",
        ),
        numbers_pattern(
            side="right",
            class_name="lg:top-[65px] top-[45px] lg:h-[calc(100%-65px)] h-[calc(100%-45px)]",
        ),
        rx.el.h1(
            "Reflex x Databricks",
            class_name="text-slate-12 lg:text-4xl text-3xl font-semibold text-center lg:max-w-[576px] text-balance",
        ),
        rx.el.h2(
            "The most powerful App Builder for Databricks.",
            class_name="text-slate-10 text-xl font-medium text-center lg:max-w-[576px] text-balance",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[3rem] pt-28 lg:pt-[8rem] relative lg:overflow-hidden overflow-hidden z-[1] bg-transparent lg:bg-slate-1 lg:px-4",
    )
