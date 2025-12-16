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
                "The Future Of Finance Is",
                " Python, Data, and AI",
                "Give quants, risk teams, and operations the power to build production-grade dashboards and AI tools in pure Python—without waiting on front-end teams.",
                "Talk to a solutions engineer",
                "Book a financial services demo",
            ),
            right_content(
                [
                    ("ShieldEnergyIcon", "Build secure internal tools and data apps"),
                    ("DashboardSpeed01Icon", "Develop up to 10x faster in pure Python"),
                    ("PythonIcon", "Go in Python from prototype to production"),
                    (
                        "BrowserIcon",
                        "From risk dashboards and model validation portals to AI-powered RAG chatbots",
                    ),
                ],
            ),
            class_name="flex lg:flex-row flex-col lg:gap-20 gap-10 max-lg:items-center max-lg:justify-center max-lg:text-center",
        ),
        class_name="flex flex-col justify-center items-center gap-4 mx-auto w-full max-w-[64.19rem] lg:border-x border-slate-3 pb-[3rem] pt-32 lg:pt-[11.5rem] lg:pb-[7.5rem] relative lg:overflow-hidden overflow-hidden z-[1] lg:px-10",
    )
