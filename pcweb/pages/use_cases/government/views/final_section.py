import reflex as rx

from pcweb.pages.use_cases.common.final_section import left_content, right_content


def final_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            left_content(
                "Modernize Government Software — Without Compromising Security",
                "Turn policies, programs, and research into secure, AI-powered applications with Reflex.",
            ),
            right_content(
                "Build Your First Government App",
                "Connect your data source, and ship a secure internal tool in weeks — entirely within your infrastructure, no JavaScript required.",
            ),
            class_name="flex xl:flex-row flex-col w-full rounded-2xl border border-m-slate-4 dark:border-m-slate-12 bg-white-1 dark:bg-m-slate-14 z-5 xl:divide-x divide-slate-3 max-xl:divide-y",
        ),
        class_name="mx-auto w-full max-w-[71.125rem] relative rounded-4xl border border-slate-4 backdrop-blur-[6px] bg-slate-2/48 p-4 flex z-1 max-lg:mb-6 -mb-px",
    )
