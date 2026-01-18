import reflex as rx

from pcweb.components.numbers_pattern import numbers_pattern
from pcweb.pages.use_cases.common.hero import left_content, right_content


def hero() -> rx.Component:
    return rx.el.section(
        numbers_pattern(
            side="right",
            class_name="lg:top-[65px] top-[45px] lg:h-[calc(100%-65px)] h-[calc(100%-45px)] max-lg:hidden",
        ),
        rx.el.div(
            left_content(
                "Build Client-Ready Enterprise Apps —",
                " 10x Faster with Reflex AI",
                "The fastest way for consulting firms to prototype and build secure, production-grade internal tools and client-facing applications using only Python. Go from idea to deployed app in days, not quarters, without front-end teams or rebuild cycles.",
                "Book a Demo",
                "Get Started Free",
            ),
            right_content(
                [
                    (
                        "ZapIcon",
                        "Turn slideware into live applications in days, not quarters",
                    ),
                    (
                        "RepeatIcon",
                        "Prototype fast, then deploy to production without rewrites",
                    ),
                    (
                        "PythonIcon",
                        "Stay in Python—no React, no frontend teams required",
                    ),
                    (
                        "ShieldKeyIcon",
                        "Deploy inside client VPCs and on-prem for enterprise security",
                    ),
                ],
            ),
            class_name="flex lg:flex-row flex-col lg:gap-20 gap-10 max-lg:items-center max-lg:justify-center max-lg:text-center",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[3rem] pt-32 lg:pt-[11.5rem] lg:pb-[7.5rem] relative lg:overflow-hidden overflow-hidden z-[1] lg:px-10",
    )
