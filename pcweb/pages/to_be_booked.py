import reflex as rx

from pcweb.components.docpage.navbar import navbar
from pcweb.pages.framework.index_colors import index_colors
from pcweb.pages.framework.views.footer_index import footer_index
import reflex_ui as ui
from pcweb.pages.docs import getting_started


def to_be_booked_title():
    return rx.box(
        rx.heading(
            "Call Request Received!",
            class_name="gradient-heading font-x-large lg:font-xxx-large text-start text-transparent lg:text-center",
        ),
        rx.text(
            "Our team will reach out to you shortly over email to schedule your call.",
            class_name="font-md text-balance text-slate-9",
        ),
        class_name="section-header",
    )





@rx.page(
    route="/to-be-booked",
    title="Reflex",
)
def to_be_booked() -> rx.Component:
    return rx.box(
        index_colors(),
        navbar(),
        rx.el.section(
            to_be_booked_title(),
            rx.box(
                ui.button("Home", variant="primary", size="lg", on_click=rx.redirect("/")),
                ui.button("Installation", variant="secondary", size="lg", on_click=rx.redirect(getting_started.installation.path)),
                class_name="flex flex-row items-center gap-x-4 pb-14"
            ),
            id="to-be-booked",
            class_name="section-content",
        ),
        footer_index(),
        class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
    )
