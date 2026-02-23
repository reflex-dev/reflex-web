import reflex as rx
import reflex_ui as ui
from reflex_ui.blocks.demo_form import demo_form_dialog

from pcweb.components.marketing_button import button


def floating_logo(src: str, alt: str, class_name: str = "") -> rx.Component:
    return rx.el.div(
        rx.image(
            src=src,
            alt=alt,
            loading="eager",
            custom_attrs={"fetchPriority": "high"},
        ),
        class_name=ui.cn(
            class_name,
            "absolute left-1/2 -translate-x-1/2 -translate-y-1/2 z-[-1] pointer-events-none size-16 rounded-[1rem] bg-m-slate-1 dark:bg-m-slate-12 [box-shadow:0_1px_0_0_#FFF_inset,_0_0_0_1px_rgba(0,_0,_0,_0.12),_0_8px_16px_0_rgba(0,_0,_0,_0.06),_0_1px_1px_0_rgba(0,_0,_0,_0.01),_0_4px_8px_0_rgba(0,_0,_0,_0.02)] dark:shadow-none dark:border dark:border-m-slate-9 flex items-center justify-center",
        ),
    )


def gradient_logo() -> rx.Component:
    return rx.el.div(
        rx.image(
            src=f"/logos/{rx.color_mode_cond('light', 'dark')}/gradient_r.svg",
            alt="Gradient Reflex Logo",
            loading="eager",
            custom_attrs={"fetchPriority": "high"},
        ),
        class_name="size-24 rounded-[1rem] bg-gradient-to-b from-m-slate-2 to-white-1 dark:from-m-slate-11 dark:to-m-slate-12 [box-shadow:0_1px_0_0_#FFF_inset,_0_0_0_1px_rgba(0,_0,_0,_0.12),_0_8px_16px_0_rgba(0,_0,_0,_0.06),_0_1px_1px_0_rgba(0,_0,_0,_0.01),_0_4px_8px_0_rgba(0,_0,_0,_0.02)] dark:shadow-none dark:border dark:border-m-slate-9 flex items-center justify-center absolute left-1/2 -translate-x-1/2 -translate-y-1/2 z-[1] pointer-events-none top-[13.5rem]",
    )


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"/common/{rx.color_mode_cond('light', 'dark')}/grid.svg",
                    alt="Grid",
                    loading="eager",
                    custom_attrs={"fetchPriority": "high"},
                    class_name=ui.cn(
                        "absolute left-1/2 -translate-x-1/2 z-[-1] pointer-events-none top-[2.815rem]",
                    ),
                ),
                floating_logo(
                    src=f"/migration/{rx.color_mode_cond('light', 'dark')}/plotly.svg",
                    alt="Plotly Logo",
                    class_name="top-[9.5rem] -ml-[10.5rem]",
                ),
                floating_logo(
                    src=f"/migration/{rx.color_mode_cond('light', 'dark')}/powerbi.svg",
                    alt="Power BI Logo",
                    class_name="top-[15rem] ml-[16.5rem]",
                ),
                floating_logo(
                    src=f"/migration/{rx.color_mode_cond('light', 'dark')}/retool.svg",
                    alt="Retool Logo",
                    class_name="top-[9.5rem] ml-[10.5rem]",
                ),
                floating_logo(
                    src=f"/migration/{rx.color_mode_cond('light', 'dark')}/streamlit.svg",
                    alt="Streamlit Logo",
                    class_name="top-[15rem] -ml-[16.5rem]",
                ),
                gradient_logo(),
                class_name="max-lg:hidden",
            ),
            rx.el.p(
                "Move From Low Code to Reflex",
                class_name="text-sm font-[525] text-primary-10 dark:text-m-slate-6",
            ),
            rx.el.h1(
                "The Next-Gen Platform Built for Modern Enterprises",
                class_name="text-m-slate-12 dark:text-m-slate-3 lg:text-5xl text-3xl font-[575]",
            ),
            rx.el.h2(
                "Escape low-code constraints without sacrificing speed. Build production-grade apps in pure Python with complete control over your stack.",
                class_name="text-m-slate-7 dark:text-m-slate-6 text-base font-[475]",
            ),
            demo_form_dialog(
                trigger=button(
                    "Book a Demo",
                    variant="primary",
                    size="lg",
                    native_button=False,
                ),
            ),
            rx.el.div(
                class_name="absolute -bottom-px -right-24 w-24 h-px bg-gradient-to-l from-transparent to-current text-m-slate-4 dark:text-m-slate-10"
            ),
            rx.el.div(
                class_name="absolute -bottom-px -left-24 w-24 h-px bg-gradient-to-r from-transparent to-current text-m-slate-4 dark:text-m-slate-10"
            ),
            class_name=ui.cn(
                "flex flex-col gap-6 items-center justify-center text-center max-w-[45rem] pb-16 border-b border-m-slate-4 dark:border-m-slate-10 relative isolate lg:pt-[21.75rem] pt-[10.5rem]",
            ),
        ),
        class_name=ui.cn(
            "flex lg:flex-row flex-col max-w-(--layout-max-width) mx-auto lg:px-24 px-6 overflow-hidden",
        ),
    )
