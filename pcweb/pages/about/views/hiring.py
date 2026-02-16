import reflex as rx

from pcweb.components.marketing_button import button
from pcweb.constants import JOBS_BOARD_URL


def hiring() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "We're Hiring",
                    class_name="text-sm font-[525] text-primary-10 max-lg:text-center dark:text-m-slate-6",
                ),
                rx.el.div(
                    rx.el.h1(
                        "Join the team behind the platform trusted by the next generation",
                        class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-4xl text-3xl font-[575]",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Our founding team consists of open source maintainers, top-ranked competitive programmers/IOI medalists, and founding team members from dev tool unicorns.",
                            class_name="text-base text-m-slate-7 dark:text-m-slate-6 font-[475]",
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
                    class_name="absolute right-0 top-0 w-px h-full bg-gradient-to-b from-transparent to-current text-m-slate-4 dark:text-m-slate-10 from-[-20%] to-100%"
                ),
                class_name="relative flex flex-col gap-6 lg:py-24 py-16",
            ),
            rx.el.div(
                class_name="absolute -bottom-px right-0 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10"
            ),
            rx.el.div(
                class_name="absolute -bottom-px left-0 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10"
            ),
            class_name="flex max-w-(--layout-max-width) mx-auto lg:px-24 px-6 max-lg:text-center relative",
        ),
        class_name="bg-gradient-to-b from-white-1 to-m-slate-1 dark:from-m-slate-11 dark:to-m-slate-12 w-full",
    )
