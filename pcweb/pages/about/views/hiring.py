import reflex as rx

from pcweb.components.marketing_button import button
from pcweb.constants import JOBS_BOARD_URL


def hiring() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "We're Hiring",
                    class_name="text-sm font-[525] text-primary-10 max-lg:text-center",
                ),
                rx.el.div(
                    rx.el.h1(
                        "Join the team behind the platform trusted by the next generation",
                        class_name="text-secondary-12 lg:text-4xl text-3xl font-[575]",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Reflex is growing and we're looking for people who care deeply about developer experience, clean abstractions, and shipping things that matter.",
                            class_name="text-base text-secondary-11 font-[475]",
                        ),
                        rx.el.a(
                            button(
                                "See Open Positions",
                                variant="primary",
                                size="lg",
                                class_name="w-fit",
                            ),
                            to=JOBS_BOARD_URL,
                            target="_blank",
                        ),
                        class_name="flex flex-col gap-6 lg:pr-12 pt-2",
                    ),
                    class_name="flex lg:flex-row flex-col gap-8 lg:gap-36",
                ),
                rx.el.div(
                    class_name="absolute right-0 top-0 w-px h-full bg-gradient-to-b from-transparent to-current text-secondary-4 from-[-20%] to-100%"
                ),
                class_name="relative flex flex-col gap-6 lg:py-24 py-16",
            ),
            rx.el.div(
                class_name="absolute -bottom-px right-0 w-24 h-px bg-gradient-to-l from-transparent to-current text-secondary-4"
            ),
            rx.el.div(
                class_name="absolute -bottom-px left-0 w-24 h-px bg-gradient-to-r from-transparent to-current text-secondary-4"
            ),
            class_name="flex max-w-(--layout-max-width) mx-auto lg:px-24 px-6 max-lg:text-center relative",
        ),
        class_name="bg-gradient-to-b from-white-1 to-secondary-1 w-full",
    )
