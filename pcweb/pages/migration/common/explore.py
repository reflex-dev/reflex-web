from typing import TypedDict

import reflex as rx
import reflex_ui as ui


class Feature(TypedDict):
    title: str
    description: str
    icon: str


def feature_card(feature: Feature) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            ui.icon(
                feature["icon"], class_name="text-primary-10 dark:text-primary-9 size-5"
            ),
            rx.el.span(
                feature["title"],
                class_name="text-m-slate-12 dark:text-m-slate-3 text-sm font-[525]",
            ),
            class_name="flex flex-row gap-2.5 items-center",
        ),
        rx.el.p(
            feature["description"],
            class_name="text-m-slate-7 dark:text-m-slate-6 text-sm font-[475] text-start",
        ),
        class_name="flex flex-col gap-2 justify-start",
    )


def feature_grid(features: list[Feature]) -> rx.Component:
    return rx.el.div(
        *[feature_card(feature) for feature in features],
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-x-12 gap-y-16",
    )


def explore(
    *,
    kicker: str,
    title_prefix: str,
    title_suffix: str,
    description: str,
    features: list[Feature],
) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    kicker,
                    class_name="text-sm font-[525] text-primary-10 max-lg:text-center dark:text-m-slate-6",
                ),
                rx.el.div(
                    rx.el.h1(
                        title_prefix,
                        rx.el.br(),
                        title_suffix,
                        class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-4xl text-3xl font-[575] shrink-0",
                    ),
                    rx.el.p(
                        description,
                        class_name="text-base text-m-slate-7 dark:text-m-slate-6 font-[475]",
                    ),
                    class_name="flex lg:flex-row flex-col gap-8 lg:gap-36",
                ),
                class_name="relative flex flex-col gap-6 lg:py-24 py-16",
            ),
            feature_grid(features),
            class_name="flex flex-col gap-16 max-w-(--layout-max-width) mx-auto lg:px-24 px-6 max-lg:text-center relative lg:pb-24 pb-16",
        ),
        class_name="bg-gradient-to-b from-white-1 to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12 w-full",
    )
