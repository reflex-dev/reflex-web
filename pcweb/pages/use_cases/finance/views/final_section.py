import reflex as rx

from pcweb.pages.use_cases.common.final_section import left_content, right_content


def final_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            left_content(
                "Make Your Toughest Internal Tool Real With Reflex",
                "Have a spreadsheet-driven workflow, a fragile Streamlit app, or a dashboard that never quite got to production? We’ll show you what it looks like as a Reflex app in pure Python.",
            ),
            right_content(
                "Spin Up Your First Finance App",
                "Connect your data source, and ship a working internal tool in an afternoon—no JavaScript required.",
            ),
            class_name="flex xl:flex-row flex-col w-full rounded-2xl border border-m-slate-4 dark:border-m-slate-12 bg-white-1 dark:bg-m-slate-14 z-5 xl:divide-x divide-slate-3 max-xl:divide-y",
        ),
        class_name="mx-auto w-full max-w-[71.125rem] relative rounded-4xl border border-slate-4 backdrop-blur-[6px] bg-slate-2/48 p-4 flex z-1 max-lg:mb-6 -mb-px",
    )
