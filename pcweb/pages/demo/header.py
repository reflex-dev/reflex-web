import reflex as rx

from reflex_ui.blocks.demo_form import demo_form
from pcweb.components.hosting_banner import HostingBannerState
from pcweb.pages.framework.views.companies import pricing_page_companies


def custom_quote_form() -> rx.Component:
    """Custom quote form component with clean, maintainable structure."""
    return rx.box(
        rx.box(
            # Left column - Content
            rx.box(
                rx.el.h2(
                    "Book a Demo",
                    class_name="text-slate-12 text-4xl font-bold mb-8",
                ),
                rx.el.p(
                    "Enterprise-ready solutions designed for scale, compliance, and support. Contact us for a tailored quote based on your infrastructure and team size.",
                    class_name="text-slate-11 text-md leading-relaxed mb-12 max-w-lg",
                ),
                rx.box(
                    pricing_page_companies(),
                    class_name="flex flex-col",
                ),
                class_name="mb-8 lg:mb-0 text-center sm:text-left",
            ),
            # Right column - Form
            demo_form(
                class_name="relative bg-slate-1 p-6 sm:p-8 rounded-2xl border-2 border-violet-9 shadow-lg w-full max-w-md mx-auto lg:max-w-none lg:mx-0"
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 max-w-7xl mx-auto items-start",
        ),
        id="demo-form",
        class_name="py-12 sm:py-20 px-4 sm:px-8 scroll-m-20",
    )


def header() -> rx.Component:
    return rx.box(
        custom_quote_form(),
        class_name="flex flex-col gap-2 justify-center items-center max-w-[64.19rem] 2xl:border-x border-slate-4 w-full -mb-10 pb-16 "
        + rx.cond(
            HostingBannerState.show_banner,
            "pt-[8rem] lg:pt-[11rem]",
            "pt-[8rem] lg:pt-[12rem]",
        ),
    )
