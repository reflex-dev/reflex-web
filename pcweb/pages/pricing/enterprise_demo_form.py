import reflex as rx
from reflex_ui.blocks.demo_form import demo_form

from pcweb.pages.framework.views.companies import pricing_page_companies


def book_a_demo_form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                # Left column - Content
                rx.el.div(
                    rx.el.h2(
                        "Book a Demo",
                        class_name="text-slate-12 text-4xl font-bold mb-8",
                    ),
                    rx.el.div(
                        "Enterprise-ready solutions designed for scale, compliance, and support. Contact us for a tailored quote based on your infrastructure and team size.",
                        class_name="text-slate-11 text-md leading-relaxed mb-12 max-w-lg font-medium",
                    ),
                    rx.el.div(
                        pricing_page_companies(),
                        class_name="flex flex-col",
                    ),
                    class_name="mb-8 lg:mb-0 text-center sm:text-left",
                ),
                # Right column - Form
                rx.box(
                    demo_form(),
                    class_name="relative bg-slate-1 rounded-2xl border-2 border-violet-9 shadow-lg w-full max-w-md mx-auto lg:max-w-none lg:mx-0 overflow-hidden",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 lg:gap-2 max-w-7xl mx-auto items-start",
            ),
            class_name="lg:pt-[4.5rem] pt-[2.5rem] pb-[3.5rem] px-4",
        ),
        class_name="flex items-center justify-center 2xl:border-x border-slate-4 max-w-[64.19rem] mx-auto w-full gap-1 2xl:border-b",
    )
