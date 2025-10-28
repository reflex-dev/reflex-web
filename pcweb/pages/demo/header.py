import reflex as rx
import reflex_ui as ui
from reflex_ui.blocks.demo_form import demo_form_dialog

from pcweb.components.hosting_banner import HostingBannerState
from pcweb.pages.framework.views.companies import pricing_page_companies


def custom_quote_form() -> rx.Component:
    """Custom quote form component with clean, maintainable structure."""
    return rx.box(
        rx.box(
            rx.el.h2(
                "Book a Demo",
                class_name="text-slate-12 text-4xl font-bold",
            ),
            rx.el.p(
                "Enterprise-ready solutions designed for scale, compliance, and support. Contact us for a tailored quote based on your infrastructure and team size.",
                class_name="text-slate-11 text-md leading-relaxed font-medium text-center max-w-xl mx-auto",
            ),
            demo_form_dialog(
                rx.el.div(
                    ui.button(
                        "Contact Sales",
                        class_name="font-semibold",
                        size="lg",
                    ),
                    class_name="p-3 border border-slate-3 rounded-[1.375rem] border-solid mt-2",
                ),
            ),
            rx.box(
                rx.el.span(
                    "Trusted by",
                    class_name="text-slate-10 text-sm leading-relaxed font-medium text-center max-w-lg mx-auto mt-2",
                ),
                pricing_page_companies(),
                class_name="flex flex-col items-center justify-center gap-4",
            ),
            class_name="flex flex-col items-center justify-center gap-6",
        ),
        id="demo-form",
        class_name="pb-12 sm:pb-20 px-4 sm:px-8 scroll-m-20 text-center",
    )


def header() -> rx.Component:
    return rx.box(
        custom_quote_form(),
        class_name="flex flex-col gap-2 justify-center items-center max-w-[64.19rem] xl:border-x border-slate-4 w-full -mb-10 pb-16 "
        + rx.cond(
            HostingBannerState.show_banner,
            "pt-[8rem] lg:pt-[11rem]",
            "pt-[8rem] lg:pt-[12rem]",
        ),
    )
