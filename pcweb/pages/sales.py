import reflex as rx
from reflex_ui.blocks.demo_form import demo_form

from pcweb.templates.webpage import webpage


@webpage(
    path="/sales",
    title="Contact Sales - Enterprise Pricing | Reflex",
    description="Get a custom quote for Reflex Enterprise. On-prem deployment, dedicated support, and enterprise features.",
)
def sales():
    return rx.el.section(
        rx.box(
            rx.el.h1(
                "Contact Sales - Enterprise Pricing",
                class_name="text-4xl font-[575] text-m-slate-12 dark:text-m-slate-3 text-center mb-8",
            ),
            rx.box(
                demo_form(),
                class_name="mt-12 w-full",
            ),
            class_name="flex flex-col justify-center items-center w-full max-w-[84.5rem]",
        ),
        id="pricing",
        class_name="section-content",
    )
