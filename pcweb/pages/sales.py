import reflex as rx
from reflex_ui.blocks.demo_form import demo_form

from pcweb.templates.webpage import webpage


@webpage(path="/sales", title="Pricing · Reflex")
def sales():
    return rx.el.section(
        rx.box(
            rx.box(
                demo_form(),
                class_name="mt-12 w-full",
            ),
            class_name="flex flex-col justify-center items-center w-full max-w-[84.5rem]",
        ),
        id="pricing",
        class_name="section-content",
    )
